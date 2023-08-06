from PySide6.QtCore import QThread, Signal, QObject
from nipype.pipeline import plugins
from logging import Handler
from nipype import config,logging
import re
import os

from SWANi.utils.APPLABELS import APPLABELS
from SWANi.SWANiWorkflow.mainWorkflow import SWANi_wf


class exec_SWANi_Signaler(QObject):
        log_message = Signal(str)
        STARTED="started"
        COMPLETED="completed"
        ERROR="error" 

      
class SignalHandler(Handler):
    """Logging handler to emit QtSignal with log record text."""

    def __init__(self, *args, **kwargs):
        super(SignalHandler, self).__init__(*args, **kwargs)
        self.emitter = exec_SWANi_Signaler()
        setattr(plugins.base.DistributedPluginBase,"_report_crash",_report_crash)
        setattr(plugins.multiproc.MultiProcPlugin,"_submit_job",_submit_job)
        setattr(plugins.multiproc.MultiProcPlugin,"_postrun_check",_postrun_check)


    def emit(self, logRecord):
        msg = self.format(logRecord).replace(APPLABELS.APPNAME+".","")
        
        reg_loop=[['Completed \((.*?)\)',exec_SWANi_Signaler.COMPLETED],
                    ['Cached \((.*?)\)',exec_SWANi_Signaler.COMPLETED],
                    ['\[SWANmonitor\] Error on \"(.*?)\"',exec_SWANi_Signaler.ERROR],
                    ['\[SWANmonitor\] Running \"(.*?)\"',exec_SWANi_Signaler.STARTED]]
        
        for entry in reg_loop:
            check=re.search(entry[0],msg)
            if check:
                self.emitter.log_message.emit(check.group(1)+"."+entry[1])
                break
            

        
class exec_SWANi_wf_thread(QThread):    
    def __init__(self, wf, parent = None):
        super(exec_SWANi_wf_thread,self).__init__(parent)
        
        self.wf=wf
        
    def run(self):
    
        logdir=os.path.join(os.getcwd(),"log/")
        if not os.path.exists(logdir):
            os.mkdir(logdir)
        config.update_config({'logging': {'log_directory': logdir,
                                  'log_to_file': True}})
                                  
        #config.update_config({"execution": {"crashdump_dir":os.getcwd()}})
        self.wf.config["execution"]["crashdump_dir"] = logdir
                         
        logging.update_logging(config)
    
    
        self.wf.run(plugin='MultiProc')
        
        

class gen_SWANi_Signaler(QObject):
        wf = Signal(object)        
        
class gen_SWANi_wf_thread(QThread):    
    
    def __init__(self, parent = None):
        super(gen_SWANi_wf_thread,self).__init__(parent)
        self.signal=gen_SWANi_Signaler()
        
    def run(self):
        self.wf=SWANi_wf(name=APPLABELS.APPNAME,base_dir="./")
        self.signal.wf.emit(self.wf)
        
    def terminate(self):
        return
   
orig_report=plugins.base.DistributedPluginBase._report_crash
def _report_crash(self, node, result=None):
    logger = logging.getLogger("nipype.workflow")
    logger.warning('[SWANmonitor] Error on "%s"', node.fullname)
    return orig_report(self, node, result)
    
orig_postrun_check=plugins.base.DistributedPluginBase._postrun_check 
def _postrun_check(self):
    logger = logging.getLogger("nipype.workflow")
    logger.warning('[SWANmonitor] Completed (SWAN)')
    return orig_postrun_check(self)

orig_sub=plugins.multiproc.MultiProcPlugin._submit_job
def _submit_job(self, node, updatehash=False):
    logger = logging.getLogger("nipype.workflow")
    logger.warning('[SWANmonitor] Running "%s"', node.fullname)
    return orig_sub(self, node, updatehash)
    

    