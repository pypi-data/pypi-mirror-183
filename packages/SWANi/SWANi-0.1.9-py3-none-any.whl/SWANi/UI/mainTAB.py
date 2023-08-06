import os, shutil
from threading import Thread
from PySide6.QtWidgets import (QTabWidget, QWidget, QGridLayout, QLabel,
                                QPushButton, QSizePolicy, QSpacerItem, QHBoxLayout,
                                QGroupBox, QVBoxLayout,QMessageBox,QListWidget,
                                QFileDialog, QTreeWidget, QErrorMessage,QFileSystemModel,
                                QTreeView,QComboBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont

from PySide6.QtSvgWidgets import QSvgWidget

from nipype import logging
import pydicom

from SWANi.UI.persistentProgressDialog import persistentProgressDialog
from SWANi.UI.customTreeWidgetItem import customTreeWidgetItem
from SWANi.UI.verticalScrollArea import verticalScrollArea

from SWANi.SWANiWorkflow.workflowThread import exec_SWANi_Signaler, gen_SWANi_wf_thread, SignalHandler,exec_SWANi_wf_thread
from SWANi.SWANiWorkflow.mainWorkflow import SWANi_wf

from SWANi.SWANiSlicer.SWANiSlicer import SWANiSlicer

from SWANi.utils.check_dependency import check_dcm2niix, check_fsl, check_freesurfer, check_graphviz, check_python_lib, check_slicer
from SWANi.utils.dicomSearch import dicomSearch
from SWANi.utils.APPLABELS import APPLABELS

import SWANi_supplement

class mainTAB(QTabWidget):

    def __init__(self, SWANiGlobalConfig, parent = None):
        super(mainTAB, self).__init__(parent)
        self.SWANiGlobalConfig=SWANiGlobalConfig

        #setup per il monitor di esecuzione
        signal_handler = SignalHandler()
        logging.getLogger("nipype.workflow").addHandler(signal_handler)
        signal_handler.emitter.log_message.connect(self.updateNodeList)

        self.okIcon_file=SWANi_supplement.okIcon_file
        self.errorIcon_file=SWANi_supplement.errorIcon_file
        self.warnIcon_file=SWANi_supplement.warnIcon_file
        self.loadingMovie_file = SWANi_supplement.loadingMovie_file
        self.voidsvg_file = SWANi_supplement.voidsvg_file

        self.okIcon=QPixmap(self.okIcon_file)
        self.errorIcon=QPixmap(self.errorIcon_file)
        self.warnIcon=QPixmap(self.warnIcon_file)

        self.homeTab = QWidget()
        self.dataTab = QWidget()
        self.wfExecTab = QWidget()
        self.slicerTab = QWidget()

        self.addTab(self.homeTab,"Home")
        self.addTab(self.dataTab,"Data load")
        self.addTab(self.wfExecTab,"Workflow execution")
        self.addTab(self.slicerTab,"Results export")


        self.homeTabUI()

        #genero il workflow di nipype in un thread secondario, è qui per i requisiti verificati nella home generate nella home
        self.start_gen_wf_thread()

        self.dataTabUI()
        self.wfExecTabUI()
        self.slicerTabUI()

        self.setTabEnabled(1, False)
        self.setTabEnabled(2, False)
        self.setTabEnabled(3, False)

    def updateNodeList(self,msg):
        split=msg.split(".")

        if split[0]=='SWAN':
            self.setTabEnabled(1, True)
            self.execButton.setText(APPLABELS.APPNAME+" Workflow executed!")
            self.execButton.setEnabled(False)
            sceneDir=os.path.join(os.getcwd(),"scene")
            if os.path.exists(sceneDir):
                self.setTabEnabled(3, True)
                self.resultsModel.setRootPath(sceneDir)
                indexRoot = self.resultsModel.index(self.resultsModel.rootPath())
                self.resultTree.setRootIndex(indexRoot)
            return

        if split[2]==exec_SWANi_Signaler.STARTED:
            icon=self.loadingMovie_file
        elif split[2]==exec_SWANi_Signaler.COMPLETED:
                icon=self.okIcon_file
        else:
            icon=self.errorIcon_file

        self.nodeList[split[0]][split[1]].setArt(icon)

        self.nodeList[split[0]]['customTreeWidgetItem'].setExpanded(True)

        if icon==self.okIcon_file:
            completed=True
            for key in self.nodeList[split[0]].keys():
                if key!='customTreeWidgetItem' and self.nodeList[split[0]][key].art!=self.okIcon_file:
                    completed=False
                    break
            if completed:
                self.nodeList[split[0]]['customTreeWidgetItem'].setArt(self.okIcon_file)
                self.nodeList[split[0]]['customTreeWidgetItem'].setExpanded(False)

    def removeRunningIcon(self):
        for key1 in self.nodeList.keys():
            for key2 in self.nodeList[key1].keys():
                if self.nodeList[key1][key2].art==self.loadingMovie_file:
                    self.nodeList[key1][key2].setArt(self.voidsvg_file)

    def start_gen_wf_thread(self):
        if not self.fsl:
            return
        gen_thread= gen_SWANi_wf_thread(parent=self)
        gen_thread.start()
        gen_thread.signal.wf.connect(self.setwf)

    def setwf(self,wf):
        self.wf=wf
        if hasattr(self, 'nodeButton'):
            self.nodeButton.setEnabled(True)
            self.wfTypeCombo.setEnabled(True)

        if hasattr(self, 'check_input') and not '' in self.check_input.values():
            self.setTabEnabled(2, True)

    def homeTabUI(self):
        layout = QGridLayout()

        boldFont=QFont()
        boldFont.setBold(True)
        titleFont=QFont()
        titleFont.setBold(True)
        titleFont.setPointSize(titleFont.pointSize()*1.5)
        x=0

        label_welcome1=QLabel("Welcome to SWANi!")
        label_welcome1.setFont(titleFont)
        label_welcome2=QLabel("SWANi (Standardized Workflow for Advanced Neuro-imaging) is a graphic tools for modular neuroimaging processing. With SWANi you can easily import and organize DICOM files from multiple sources, generate a pipeline based on available imaging modalities and export results in a multimodal scene.")
        label_welcome2.setWordWrap(True)
        label_welcome3=QLabel("SWANi does NOT implement processing software but integrates in a user-friendly interface many external applications, so make sure the check the following dependencies.")
        label_welcome3.setWordWrap(True)
        #label_welcome4=QLabel("To start, load an existing patient folder or create a new one.\n")
        label_welcome5=QLabel("SWANi is not meant for clinical use!\n\n")
        label_welcome5.setFont(boldFont)

        layout.addWidget(label_welcome1,x,0,1,2)
        x+=1
        layout.addWidget(label_welcome2,x,0,1,2)
        x+=1
        layout.addWidget(label_welcome3,x,0,1,2)
        x+=1
        #layout.addWidget(label_welcome4,x,0,1,2)
        #x+=1
        layout.addWidget(label_welcome5,x,0,1,2)
        x+=1

        label_main_dep=QLabel("External applications dependencies:")
        label_main_dep.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        label_main_dep.setFont(boldFont)
        layout.addWidget(label_main_dep,x,0,1,2)
        x+=1

        msg,self.dcm2niix=check_dcm2niix()
        x=self.add_home_entry(layout,msg,self.dcm2niix,x)

        msg,self.fsl=check_fsl()
        x=self.add_home_entry(layout,msg,self.fsl,x)

        msg,self.freesurfer=check_freesurfer()
        x=self.add_home_entry(layout,msg,self.freesurfer,x)

        msg,self.graphviz=check_graphviz()
        x=self.add_home_entry(layout,msg,self.graphviz,x)

        if self.SWANiGlobalConfig['MAIN']['slicerPath'] == '' or not os.path.exists(self.SWANiGlobalConfig['MAIN']['slicerPath']):
            self.slicerlabel_icon=QSvgWidget()
            self.slicerlabel_icon.setFixedSize(25,25)
            self.slicerlabel_icon.load(self.loadingMovie_file)
            layout.addWidget(self.slicerlabel_icon,x,0)
            self.slicerlabel=QLabel("Searching Slicer installation...")
            self.slicerlabel.setOpenExternalLinks(True)
            self.slicerlabel.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
            layout.addWidget(self.slicerlabel,x,1)
            x+=1

            self.SWANiGlobalConfig['MAIN']['slicerPath'] = ''
            slicerrun= check_slicer(x,parent=self)
            slicerrun.start()
            slicerrun.signal.slicer.connect(self.slicerrow)
        else:
            self.add_home_entry(layout,"Slicer detected",True,x)
        x+=1

        label_py_dep=QLabel("Python libraries dependencies:")
        label_py_dep.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        label_py_dep.setFont(boldFont)
        layout.addWidget(label_py_dep,x,0,1,2)
        x+=1

        requested_lib=['nipype','PySide6','pydicom','logging','configparser','psutil']

        for thislib in requested_lib:
            x=self.add_home_entry(layout,thislib,check_python_lib(thislib),x)

        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(verticalSpacer,x,0,1,2)

        self.homeTab.setLayout(layout)

    def add_home_entry(self,gridlayout,msg,icon,x):
        label_icon=QLabel()
        label_icon.setFixedSize(25,25)
        label_icon.setScaledContents(True)
        if icon: label_icon.setPixmap(self.okIcon)
        else: label_icon.setPixmap(self.errorIcon)
        gridlayout.addWidget(label_icon,x,0)
        label=QLabel(msg)
        label.setOpenExternalLinks(True)
        label.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        gridlayout.addWidget(label,x,1)
        return (x+1)

    def slicerrow(self,cmd,msg,found,x):
        if found:
            self.SWANiGlobalConfig['MAIN']['slicerPath']=cmd
            self.SWANiGlobalConfig.save()
            self.exportResultsButton.setEnabled(True)
            self.slicerlabel_icon.load(self.okIcon_file)
        else:
            self.slicerlabel_icon.load(self.errorIcon_file)

        #self.add_home_entry(self.homeTab.layout(),msg,found,x)
        self.slicerlabel.setText(msg)

    def dataTabUI(self):
        #LAYOUT ORIZZONTALE
        layout = QHBoxLayout()

        #PRIMA COLONNA: LISTA DEGLI INPUT
        scrollArea= verticalScrollArea()
        folderLayout = QGridLayout()
        scrollArea.m_scrollAreaWidgetContents.setLayout(folderLayout)
        self.inputReport={}

        boldFont=QFont()
        boldFont.setBold(True)
        x=0

        for inputName in self.SWANiGlobalConfig.INPUTLIST:

            if inputName.startswith("op_"):
                split=inputName.split("_")
                if len(split)<3: continue
                if not self.SWANiGlobalConfig.getboolean('OPTIONAL_SERIES', split[1]+"_"+split[2]): continue

            self.inputReport[inputName] = [QSvgWidget(self), QLabel(inputName.replace("op_","")), QLabel(""),QPushButton("Import"),QPushButton("Clear")]
            self.inputReport[inputName][0].load(self.errorIcon_file)
            self.inputReport[inputName][0].setFixedSize(25,25)
            self.inputReport[inputName][1].setFont(boldFont)
            self.inputReport[inputName][1].setAlignment(Qt.AlignLeft|Qt.AlignBottom)
            self.inputReport[inputName][2].setAlignment(Qt.AlignLeft|Qt.AlignTop)
            self.inputReport[inputName][2].setStyleSheet("margin-bottom: 20px")
            self.inputReport[inputName][3].setEnabled(False)
            self.inputReport[inputName][3].clicked.connect(lambda checked=None, x=inputName: self.dicomImport2Folder(x))
            self.inputReport[inputName][3].setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
            self.inputReport[inputName][4].setEnabled(False)
            self.inputReport[inputName][4].clicked.connect(lambda checked=None, x=inputName: self.clearImportFolder(x))
            self.inputReport[inputName][4].setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)

            folderLayout.addWidget(self.inputReport[inputName][0],(x*2),0,2,1)
            folderLayout.addWidget(self.inputReport[inputName][1],(x*2),1)

            folderLayout.addWidget(self.inputReport[inputName][3],(x*2),2)
            folderLayout.addWidget(self.inputReport[inputName][4],(x*2),3)

            folderLayout.addWidget(self.inputReport[inputName][2],(x*2)+1,1,1,3)
            x+=1

        #SECONDA COLONNA: LISTA SERIE DA IMPORTARE
        importGroupBox = QGroupBox()
        importLayout = QVBoxLayout()
        importGroupBox.setLayout(importLayout)

        scanDicomFolderButton = QPushButton("Scan DICOM folder")
        scanDicomFolderButton.clicked.connect(self.scanDicomFolder)

        self.importableSeriesList = QListWidget()
        importLayout.addWidget(scanDicomFolderButton)
        importLayout.addWidget(self.importableSeriesList)

        #AGGIUNGO LE COLONNE AL LAYOUT PRINCIPALE
        layout.addWidget(scrollArea,stretch=1)
        layout.addWidget(importGroupBox,stretch=1)
        self.dataTab.setLayout(layout)

    def dicomImport2Folder(self,inputName):
        if self.importableSeriesList.currentRow()==-1:
            msgBox = QMessageBox()
            msgBox.setText("No series was selected")
            msgBox.exec()
            return

        import shutil
        destPath=self.SWANiGlobalConfig['DEFAULTFOLDERS']['default_'+inputName+'_folder']
        foundMod=self.finalSeriesList[self.importableSeriesList.currentRow()][0].split("-")[1].upper()
        expedctedMod=inputName.upper().replace("op_","").split("_")[0]

        if not expedctedMod in foundMod:
            msgBox = QMessageBox()
            msgBox.setText("You selected "+foundMod+" images while "+expedctedMod+" images were expected.")
            msgBox.setInformativeText("Do you want to continue importing?")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.No)
            ret = msgBox.exec()
            if ret==QMessageBox.No: return

        copyList=self.finalSeriesList[self.importableSeriesList.currentRow()][1]

        progress = persistentProgressDialog("Copying DICOM files in patient folder...", 0, len(copyList)+1,self)
        progress.show()

        self.inputReport[inputName][0].load(self.loadingMovie_file)

        for thisFile in copyList:
            if not os.path.isfile(thisFile): continue
            shutil.copy(thisFile, destPath)
            progress.increaseValue(1)

        progress.setRange(0,0)
        progress.setLabelText("Verifying patient folder...")

        self.checkInputFolder(inputName,progress)

        self.reset_wf()

    def scanDicomFolder(self):
        folderPath = QFileDialog.getExistingDirectory(self, 'Select a folder to scan for DICOM files')
        if not os.path.exists(folderPath):
            return

        dicomsrc= dicomSearch(folderPath, parent=self)
        dicomsrc.loadDir()


        if dicomsrc.getFilesLen()>1:
            self.importableSeriesList.clear()
            self.finalSeriesList=[]
            progress = persistentProgressDialog("Scanning DICOM folder...", 0, 0)
            progress.show()
            progress.setMaximum(dicomsrc.getFilesLen())
            dicomsrc.signal.sigLoop.connect(lambda i: progress.increaseValue(i))
            dicomsrc.signal.sigFinish.connect(self.showScanResult)
            dicomsrc.start()
        else:
            msgBox = QMessageBox()
            msgBox.setText("No DICOM file in "+folderPath)
            msgBox.exec()

    def wfExecTabUI(self):
        layout = QGridLayout()

        #PRIMA COLONNA: node list
        self.wfTypeCombo = QComboBox(self)

        for index, label in enumerate(APPLABELS.WFTYPES):
            self.wfTypeCombo.insertItem(index,label)

        self.wfTypeCombo.currentIndexChanged.connect(self.onWfTypeChanged)
        layout.addWidget(self.wfTypeCombo,0,1)

        self.nodeButton=QPushButton(APPLABELS.GENBUTTONTEXT)
        self.nodeButton.clicked.connect(self.genWF)
        if not hasattr(self, 'wf'):
            self.nodeButton.setEnabled(False)

        layout.addWidget(self.nodeButton,1,1)

        self.nodeListTreeWidget = QTreeWidget()
        self.nodeListTreeWidget.setHeaderHidden(True)
        self.nodeListTreeWidget.setFixedWidth(320)

        layout.addWidget(self.nodeListTreeWidget,2,1)
        self.nodeListTreeWidget.itemClicked.connect(self.treeItemClicked)

        #SECONDA COLONNA: graph monitor
        self.execButton=QPushButton(APPLABELS.EXECBUTTONTEXT)
        self.execButton.clicked.connect(self.start_SWANi_wf_thread)
        self.execButton.setEnabled(False)

        layout.addWidget(self.execButton,1,2)
        self.execGraph = QSvgWidget()
        layout.addWidget(self.execGraph,2,2)

        self.wfExecTab.setLayout(layout)

    def onWfTypeChanged(self,index):
        self.SWANiGlobalConfig.patientConfiguration['ptConfig']['wfType']=str(index)
        self.SWANiGlobalConfig.savePatientConfig()
        self.reset_wf()

    def genWF(self):

        if not self.fsl:
            errorDialog=QErrorMessage(parent=self)
            errorDialog.showMessage("FSL is required to generate "+APPLABELS.APPNAME+" Workflow!")
            return

        if not hasattr(self,"wf") or self.wf==None:
            self.wf=SWANi_wf(name=APPLABELS.APPNAME,base_dir=os.getcwd())

        self.wf.add_input_folders(self.SWANiGlobalConfig,self.check_input,self.freesurfer)
        self.nodeList=self.wf.get_node_array()
        self.nodeListTreeWidget.clear()

        graphdir=os.path.join(os.getcwd(),"graph/")
        shutil.rmtree(graphdir,ignore_errors=True)
        os.mkdir(graphdir)

        for node in self.nodeList.keys():
            self.nodeList[node]['customTreeWidgetItem']=customTreeWidgetItem(self.nodeListTreeWidget,self.nodeListTreeWidget,node)
            if len(self.nodeList[node].keys())>1:
                if self.graphviz:
                    thread = Thread(target=self.wf.get_node(node).write_graph, kwargs={'graph2use':'colored', 'format':'svg', 'dotfilename':os.path.join(graphdir,'graph_'+node+'.dot')})
                    thread.start()
                for subnode in self.nodeList[node].keys():
                    if subnode!='customTreeWidgetItem':
                        self.nodeList[node][subnode]=customTreeWidgetItem(self.nodeList[node]['customTreeWidgetItem'],self.nodeListTreeWidget,subnode)
        self.execButton.setEnabled(True)
        self.execButton.setText(APPLABELS.EXECBUTTONTEXT)
        self.nodeButton.setEnabled(False)
        #self.wfTypeCombo.setEnabled(False)

    def treeItemClicked(self, it, col):
        if self.graphviz and it.parent()==None:
            file=os.path.join(os.getcwd(),"graph",'graph_'+it.getText()+'.svg')
            self.execGraph.load(file)
            self.execGraph.renderer().setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)

    def noCloseEvent(self, event):
        event.ignore()

    def start_SWANi_wf_thread(self):

        if not hasattr(self,"SWANi_wf_thread") or not self.SWANi_wf_thread.isRunning():

            wfdir=os.path.join(os.getcwd(),APPLABELS.APPNAME)
            if os.path.exists(wfdir):
                msgBox = QMessageBox()
                msgBox.setInformativeText("A previus execution of "+APPLABELS.APPNAME+" was detected. Do you want to resume execution or start a new one?")
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msgBox.button(QMessageBox.Yes).setText("Resume execution")
                msgBox.button(QMessageBox.No).setText("New execution")
                msgBox.setDefaultButton(QMessageBox.Yes)
                msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
                msgBox.closeEvent=self.noCloseEvent
                ret = msgBox.exec()
                if ret==QMessageBox.No:
                    shutil.rmtree(wfdir,ignore_errors=True)

            fsdir=os.path.join(os.getcwd(),"FS")
            if os.path.exists(fsdir):
                msgBox = QMessageBox()
                msgBox.setInformativeText("An existing FreeSurfer folder was detected. Do you want to keep or delete the existing folder?")
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msgBox.button(QMessageBox.Yes).setText("Keep folder")
                msgBox.button(QMessageBox.No).setText("Delete folder")
                msgBox.setDefaultButton(QMessageBox.Yes)
                msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
                msgBox.closeEvent=self.noCloseEvent
                ret = msgBox.exec()
                if ret==QMessageBox.No:
                    shutil.rmtree(fsdir,ignore_errors=True)

            self.SWANi_wf_thread=exec_SWANi_wf_thread(self.wf,parent=self)
            self.SWANi_wf_thread.start()
            self.execButton.setText(APPLABELS.EXECBUTTONTEXT_STOP)
            self.setTabEnabled(1, False)
            self.setTabEnabled(3, False)
            self.wfTypeCombo.setEnabled(False)
        else:
            msgBox = QMessageBox()
            msgBox.setInformativeText("Do you REALLY want to stop "+APPLABELS.APPNAME+" Workflow execution?")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.No)
            ret = msgBox.exec()
            if ret==QMessageBox.No: return
            self.kill_subthread()
            self.SWANi_wf_thread.terminate()
            self.removeRunningIcon()
            self.execButton.setText(APPLABELS.EXECBUTTONTEXT)
            self.setTabEnabled(1, True)
            self.reset_wf()
            sceneDir=os.path.join(os.getcwd(),"scene")
            if os.path.exists(sceneDir):
                self.setTabEnabled(3, True)

    def kill_subthread(self):
        import signal,psutil
        try:
            parent = psutil.Process(os.getpid())
        except psutil.NoSuchProcess:
            return
        children = parent.children(recursive=True)
        for process in children:
            process.send_signal(signal.SIGTERM)


    def slicerTabUI(self):
        slicerTabLayout = QGridLayout()
        self.slicerTab.setLayout(slicerTabLayout)

        self.exportResultsButton=QPushButton("Export results into Slicer scene")
        self.exportResultsButton.clicked.connect(self.SWANiSlicer_thread)
        self.exportResultsButton.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        if self.SWANiGlobalConfig['MAIN']['slicerPath'] == '' or not os.path.exists(self.SWANiGlobalConfig['MAIN']['slicerPath']):
            self.exportResultsButton.setEnabled(False)
        slicerTabLayout.addWidget(self.exportResultsButton,0,0)

        self.resultsModel=QFileSystemModel()
        self.resultTree=QTreeView(parent=self)
        self.resultTree.setModel(self.resultsModel)

        #indexRoot = self.resultsModel.index(self.resultsModel.rootPath())
        #resultTree.setRootIndex(indexRoot)
        slicerTabLayout.addWidget(self.resultTree,1,0)

        #self.sceneList=['ref.nii.gz','ref_brain.nii.gz','r-aparc_aseg.mgz','r-flair_brain.nii.gz','r-venosa_inskull.nii.gz','r-mdc_brain.nii.gz','r-pet_brain_smooth.nii.gz','pet_surf_rh.mgz','pet_surf_lh.mgz','r-pet_brain_AI.nii.gz','petAI_surf_lh.mgz','petAI_surf_rh.mgz','r-pet_brain_z.nii.gz']


    def SWANiSlicer_thread(self):

        progress = persistentProgressDialog("Exporting results into Slicer scene...\nLoading Slicer environment", 0, 0,parent=self)
        progress.show()

        slicerThread=SWANiSlicer(self.SWANiGlobalConfig['MAIN']['slicerPath'],parent=self)
        slicerThread.signal.export.connect(lambda msg: self.SWANiSlicer_thread_signal(msg,progress))
        slicerThread.start()

    def SWANiSlicer_thread_signal(self,msg,progress):
        if msg=='ENDLOADING':
                progress.done(1)
        else:
            progress.setLabelText("Exporting results into Slicer scene...\n"+msg)

    def loadPt(self):
        dicomScanners={}
        self.check_input={}
        totalFiles=0

        #importo la configurazione del tipo di workflow
        self.SWANiGlobalConfig.getPatientWfType()

        #for inputName in self.SWANiGlobalConfig.INPUTLIST:
        for inputName in self.inputReport:
            dicomScanners[inputName]=self.checkInputFolder_step1(inputName)
            totalFiles=totalFiles+dicomScanners[inputName].getFilesLen()
            self.check_input[inputName]=''

        if totalFiles>0:
            progress = persistentProgressDialog("Checking patient DICOM folders...", 0, 0,parent=self.parent())
            progress.show()
            progress.setMaximum(totalFiles)
        else: progress=None

        #for inputName in self.SWANiGlobalConfig.INPUTLIST:
        for inputName in self.inputReport:
            self.inputReport[inputName][0].load(self.loadingMovie_file)
            self.checkInputFolder_step2(inputName, dicomScanners[inputName],progress)

        self.setTabEnabled(1, True)
        self.setCurrentWidget(self.dataTab)

        #svuoto la lista delle serie importabili
        self.importableSeriesList.clear()
        #reset del workflow
        self.reset_wf()

        sceneDir=os.path.join(os.getcwd(),"scene")
        if os.path.exists(sceneDir):
            self.setTabEnabled(3, True)
            self.resultsModel.setRootPath(sceneDir)
            indexRoot = self.resultsModel.index(self.resultsModel.rootPath())
            self.resultTree.setRootIndex(indexRoot)
        else:
           self.setTabEnabled(3, False)

    def checkInputFolder_step1(self,inputName):
        srcPath=os.path.join(os.getcwd(),self.SWANiGlobalConfig['DEFAULTFOLDERS']['default_'+inputName+'_folder'])
        dicomsrc= dicomSearch(srcPath, parent=self)
        dicomsrc.loadDir()
        return dicomsrc

    def checkInputFolder_step2(self,inputName, dicomsrc, progress=None):
        dicomsrc.signal.sigFinish.connect(lambda src, name=inputName: self.checkInputFolder_step3(name,src))
        if progress!=None:
            if progress.maximum()==0: progress.setMaximum(dicomsrc.getFilesLen())
            dicomsrc.signal.sigLoop.connect(lambda i: progress.increaseValue(i))
        dicomsrc.start()

    def checkInputFolder_step3(self, inputName, dicomsrc):
        srcPath=dicomsrc.dicomPath
        ptList=dicomsrc.getPatientList()
        self.check_input[inputName]=True

        if not '' in self.check_input.values():
            self.setTabEnabled(2, True)

        if len(ptList)==0:
            self.setError(inputName,"No dicom file in "+srcPath)
            self.check_input[inputName]=False
            return

        if len(ptList)>1:
            self.setWarm(inputName,"Dicom file from more than one patient in "+srcPath)
            return
        examList=dicomsrc.getExamList(ptList[0])
        if len(examList)!=1:
            self.setWarm(inputName,"DICOM file from more than one examination in "+srcPath)
            return
        seriesList=dicomsrc.getSeriesList(ptList[0],examList[0])
        if len(seriesList)!=1:
            self.setWarm(inputName,"DICOM file from more than one series in "+srcPath)
            return

        imageList=dicomsrc.getSeriesFiles(ptList[0],examList[0],seriesList[0])
        ds = pydicom.read_file(imageList[0], force=True)
        mod=ds.Modality
        if mod=="PT": mod="PET"
        self.setOk(inputName,str(ds.PatientName)+"-"+mod+"-"+ds.SeriesDescription+": "+str(len(imageList))+" images")

    def checkInputFolder(self,inputName,progress=None):
        dicomsrc= self.checkInputFolder_step1(inputName)
        self.checkInputFolder_step2(inputName, dicomsrc,progress)


    def clearImportFolder(self,inputName):
        srcPath=os.path.join(os.getcwd(),self.SWANiGlobalConfig['DEFAULTFOLDERS']['default_'+inputName+'_folder'])

        progress = persistentProgressDialog("Clearing DICOM files in: "+srcPath, 0, 0,self)
        progress.show()

        import shutil
        shutil.rmtree(srcPath, ignore_errors=True)
        os.makedirs(srcPath,exist_ok=True)
        self.setError(inputName,"No dicom file in "+srcPath)
        self.check_input[inputName]=False

        progress.accept()
        self.reset_wf()

    def reset_wf(self):
        #SE NON CARICATO UN PAZIENTE, NON FACCIO NULLA
        if not self.isTabEnabled(1): return

        self.wf=None
        self.nodeListTreeWidget.clear()
        self.execGraph.load(self.voidsvg_file)
        self.execButton.setEnabled(False)
        self.execButton.setText(APPLABELS.EXECBUTTONTEXT)
        self.nodeButton.setEnabled(True)
        self.wfTypeCombo.setEnabled(True)

        self.wfTypeCombo.setCurrentIndex(self.SWANiGlobalConfig.patientConfiguration['ptConfig'].getint('wfType'))

    def showScanResult(self,dicomsrc):
        folderPath=dicomsrc.dicomPath
        ptList=dicomsrc.getPatientList()

        if len(ptList)==0:
            msgBox = QMessageBox()
            msgBox.setText("No DICOM file in "+folderPath)
            msgBox.exec()
            return
        if len(ptList)>1:
            msgBox = QMessageBox()
            msgBox.setText("DICOM file from more than one patient in "+folderPath)
            msgBox.exec()
            return
        examList=dicomsrc.getExamList(ptList[0])
        for exam in examList:
            seriesList=dicomsrc.getSeriesList(ptList[0],exam)
            for serie in seriesList:
                imageList=dicomsrc.getSeriesFiles(ptList[0],exam,serie)
                ds = pydicom.read_file(imageList[0], force=True)
                #non mostro le serie troppo corte (survey ecc) a meno che non siano mosaici
                if len(imageList)<10 and hasattr(ds, 'ImageType') and not "MOSAIC" in ds.ImageType: continue

                mod=ds.Modality
                if mod=="PT": mod="PET"
                self.finalSeriesList.append([str(ds.PatientName)+"-"+mod+"-"+ds.SeriesDescription+": "+str(len(imageList))+" images", imageList])
                del(imageList)

        for serie in self.finalSeriesList:
            self.importableSeriesList.addItem(serie[0])

    def setWarm(self,inputName,msg):
        self.inputReport[inputName][0].load(self.warnIcon_file)
        self.inputReport[inputName][0].setFixedSize(25,25)
        self.inputReport[inputName][0].setToolTip(msg)
        self.inputReport[inputName][3].setEnabled(False)
        self.inputReport[inputName][4].setEnabled(True)
        self.inputReport[inputName][2].setText("")

    def setError(self,inputName,msg):
        self.inputReport[inputName][0].load(self.errorIcon_file)
        self.inputReport[inputName][0].setFixedSize(25,25)
        self.inputReport[inputName][0].setToolTip(msg)
        self.inputReport[inputName][3].setEnabled(True)
        self.inputReport[inputName][4].setEnabled(False)
        self.inputReport[inputName][2].setText("")

    def setOk(self,inputName,msg):
        self.inputReport[inputName][0].load(self.okIcon_file)
        self.inputReport[inputName][0].setFixedSize(25,25)
        self.inputReport[inputName][0].setToolTip("")
        self.inputReport[inputName][3].setEnabled(False)
        self.inputReport[inputName][4].setEnabled(True)
        self.inputReport[inputName][2].setText(msg)
