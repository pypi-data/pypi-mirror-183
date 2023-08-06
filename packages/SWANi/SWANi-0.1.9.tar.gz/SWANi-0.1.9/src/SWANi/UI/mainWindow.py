from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QInputDialog, QLineEdit
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6 import QtCore
import os, shutil

from SWANi.UI.mainTAB import mainTAB
from SWANi.UI.preferencesWindow import preferencesWindow
import SWANi_supplement

class mainWindow(QMainWindow):
    ptDirPath=""
    tabWidget=None

    def __init__(self, SWANiGlobalConfig):

        self.SWANiGlobalConfig=SWANiGlobalConfig

        super(mainWindow,self).__init__()

        self.inizializeUI()



        while self.SWANiGlobalConfig.getPatientsFolder()=="" or not os.path.exists(self.SWANiGlobalConfig.getPatientsFolder()):
            msgBox = QMessageBox()
            msgBox.setText("Choose the main working directory before start to use this application")
            msgBox.exec()
            self.setPatientsFolder()

        os.chdir(self.SWANiGlobalConfig.getPatientsFolder())

        #controllo che eventuali shortcut salvati esistano
        if self.SWANiGlobalConfig['MAIN']['shortcutPath']!='':
            targets=self.SWANiGlobalConfig['MAIN']['shortcutPath'].split("|")
            newPath=''
            change=False
            for fil in targets:
                if "SWANi" in fil and os.path.exists(fil):
                    if newPath!='': newPath=newPath+"|"
                    newPath=newPath+fil
                else:
                    change=True
            if change:
                self.SWANiGlobalConfig['MAIN']['shortcutPath']=newPath
                self.SWANiGlobalConfig.save()

    @QtCore.Slot()
    def searchPtDir(self):
        fileDialog=QFileDialog()
        fileDialog.setDirectory(self.SWANiGlobalConfig.getPatientsFolder())
        folderPath = fileDialog.getExistingDirectory(self, 'Select a patient folder')
        if not os.path.exists(folderPath):
            return
        if not self.checkPtDir(folderPath):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("The selected folder does not contains valid patient data!")
            msgBox.exec()

            msgBox2 = QMessageBox()
            msgBox2.setInformativeText("If you are SURE you selected a patient folder, SWANi can try to update it.\nDo you want to update selected patient folder?")
            msgBox2.setIcon(QMessageBox.Warning)
            msgBox2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox2.button(QMessageBox.Yes).setText("Yes")
            msgBox2.button(QMessageBox.No).setText("No")
            msgBox2.setDefaultButton(QMessageBox.No)
            ret = msgBox2.exec()
            if ret==QMessageBox.Yes:
                self.updatePtDir(folderPath)
            else:
                return
        os.chdir(folderPath)
        self.tabWidget.loadPt()
        self.statusBar().showMessage('Current patient: '+os.path.basename(folderPath))

    def getSuggestedPatientName(self):
        import re
        regex = re.compile('^'+self.SWANiGlobalConfig.getConfig("MAIN","patientsprefix")+'\d+$')
        fileList=[]
        for thisDir in os.listdir(self.SWANiGlobalConfig.getPatientsFolder()):
            if regex.match(thisDir): fileList.append(int(thisDir.replace(self.SWANiGlobalConfig['MAIN']['patientsprefix'],"")))

        if len(fileList)==0: return self.SWANiGlobalConfig['MAIN']['patientsprefix']+"1"
        return self.SWANiGlobalConfig['MAIN']['patientsprefix']+str(max(fileList)+1)


    def choseNewPtDir(self):
        text, ok = QInputDialog.getText(self, 'New patient',
            'Write the name of the new patient:', QLineEdit.Normal, self.getSuggestedPatientName())

        if not ok: return

        ptName=str(text)

        if ptName=="":
            msgBox = QMessageBox()
            msgBox.setText("Nome non valido: "+ptName)
            msgBox.exec()
            return

        if os.path.exists(os.path.join(self.SWANiGlobalConfig.getPatientsFolder(),ptName)):
            msgBox = QMessageBox()
            msgBox.setText("Esiste già un paziente con nome: "+ptName)
            msgBox.exec()
            return

        self.createNewPtDir(ptName)


    def setPatientsFolder(self):
        folderPath = QFileDialog.getExistingDirectory(self, 'Select the main working directory')
        if not os.path.exists(folderPath):
            return
        self.SWANiGlobalConfig.setConfig("MAIN","PatientsFolder",os.path.abspath(folderPath))
        self.SWANiGlobalConfig.save()
        os.chdir(folderPath)

    def createNewPtDir(self,ptName):
        baseFolder=os.path.abspath(os.path.join(self.SWANiGlobalConfig.getPatientsFolder(),ptName))

        for folder in self.SWANiGlobalConfig["DEFAULTFOLDERS"]:
            os.makedirs(os.path.join(baseFolder,self.SWANiGlobalConfig['DEFAULTFOLDERS'][folder]),exist_ok=True)

        msgBox = QMessageBox()
        msgBox.setText("New patient created in: "+baseFolder)
        msgBox.exec()
        os.chdir(baseFolder)
        self.tabWidget.loadPt()

    def checkPtDir(self,dirPath):
        for folder in self.SWANiGlobalConfig["DEFAULTFOLDERS"]:
            if not os.path.exists(os.path.join(dirPath,self.SWANiGlobalConfig["DEFAULTFOLDERS"][folder])):
               return False

        return True

    def updatePtDir(self,dirPath):
        for folder in self.SWANiGlobalConfig["DEFAULTFOLDERS"]:
            if not os.path.exists(os.path.join(dirPath,self.SWANiGlobalConfig["DEFAULTFOLDERS"][folder])):
               os.makedirs(os.path.join(dirPath,self.SWANiGlobalConfig['DEFAULTFOLDERS'][folder]),exist_ok=True)

    def editConfig(self):
        if hasattr(self.tabWidget, "SWANi_wf_thread") and self.tabWidget.SWANi_wf_thread.isRunning():
            msgBox = QMessageBox()
            msgBox.setText("Prefecences disabled during workflow execution!")
            msgBox.exec()
            return
        self.w=preferencesWindow(self.SWANiGlobalConfig,self)
        self.w.exec()
        self.tabWidget.reset_wf()

    def toggleShortcut(self):
        if self.SWANiGlobalConfig['MAIN']['shortcutPath']=="":
            from pyshortcuts import make_shortcut,platform
            import SWANi
            if platform.startswith('darwin'):
                iconFile=SWANi_supplement.appIcns_file
            else:
                iconFile=SWANi_supplement.appIcon_file
            script=os.path.dirname(SWANi.__file__)
            scut = make_shortcut(script, name="SWANi", icon=iconFile, terminal=True)
            targets  = [os.path.join(f, scut.target) for f in (scut.desktop_dir, scut.startmenu_dir)]
            self.SWANiGlobalConfig['MAIN']['shortcutPath']="|".join(targets)
            msgBox = QMessageBox()
            msgBox.setText("Shortcut created!")
            msgBox.exec()
        else:
            targets=self.SWANiGlobalConfig['MAIN']['shortcutPath'].split("|")
            for fil in targets:
                if "SWANi" in fil and os.path.exists(fil):
                    if os.path.isdir(fil):
                        shutil.rmtree(fil,ignore_errors=True)
                    else:
                        os.remove(fil)
            self.SWANiGlobalConfig['MAIN']['shortcutPath']=""
            msgBox = QMessageBox()
            msgBox.setText("Shortcut removed!")
            msgBox.exec()
        self.SWANiGlobalConfig.save()

    def inizializeUI(self):
        self.resize(800,600)
        self.setWindowTitle('SWANi - Standardized Workflow for Advanced Neuro-imaging')


        self.statusBar().showMessage('')

        button_action = QAction(QIcon.fromTheme("document-open"),"Load existing patient", self)
        button_action.setStatusTip("Load patient data from the main working directory")
        button_action.triggered.connect(self.searchPtDir)

        button_action2 = QAction(QIcon.fromTheme("document-new"),"Create new patient", self)
        button_action2.setStatusTip("Add a new patient in the main working directory")
        button_action2.triggered.connect(self.choseNewPtDir)

        button_action3 = QAction(QIcon.fromTheme("preferences-other"),"Preferences", self)
        button_action3.setStatusTip("Edit SWANi precerences")
        button_action3.triggered.connect(self.editConfig)

        button_action4 = QAction("Shortcut", self)
        button_action4.setStatusTip("Add/Remove SWANi shortcut")
        button_action4.triggered.connect(self.toggleShortcut)

        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action)
        file_menu.addAction(button_action2)
        tool_menu = menu.addMenu("Tools")
        tool_menu.addAction(button_action3)
        tool_menu.addAction(button_action4)

        self.tabWidget=mainTAB(self.SWANiGlobalConfig,parent=self)
        self.setCentralWidget(self.tabWidget)

        self.setWindowIcon(QIcon(QPixmap(os.path.join(os.path.dirname(__file__),"icons/swan.png"))))

        self.show()

    def closeEvent(self, event):
        # evito la chiusura se il wf è in esecuzione
        if not hasattr(self,'tabWidget') or not hasattr(self.tabWidget,'SWAN_wf_thread') or not self.tabWidget.SWAN_wf_thread.isRunning():
            return super(mainWindow,self).closeEvent(event)
        else:
            self.tabWidget.start_SWAN_wf_thread()
            if not self.tabWidget.SWAN_wf_thread.isRunning():
                return super(mainWindow,self).closeEvent(event)

        event.ignore()
