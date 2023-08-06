import os,sys,logging
from abc import ABC,abstractmethod
import yaml
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
#log_dir = "logs"
#log_filepath = os.path.join(log_dir, "running_logs.log")
#os.makedirs(log_dir, exist_ok=True)
#logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
#log_dir = "logs"
#log_filepath = os.path.join(log_dir, "running_logs.log")
#os.makedirs(log_dir, exist_ok=True)
# logging.FileHandler(log_filepath),

def read_yaml(path:str):
    with open(path) as f:
        d=yaml.safe_load(f)
    return d

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers=[
       
        logging.StreamHandler(sys.stdout),
    ])

logger = logging.getLogger("PSQ")

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        
        logging.StreamHandler(sys.stdout),
    ])

logger = logging.getLogger("PSQ")


class process:
    @abstractmethod
    def init_process(self,*args,**kwargs):
        pass
