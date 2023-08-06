"""
@author Victor Valenzuela M
@since 28-12-22
"""

import os
import json
from pathlib import Path
from inspect import currentframe, getframeinfo
from datetime import datetime
from enum import Enum


date_format = "%d/%m/%Y, %H:%M:%S"

class RType(Enum):
    ERR = 'error'
    WARN = 'warning'
    #INFO = 3

class Registry():
    """
    Clase Base para errores, warnings, info, etc
    """
    r_type:RType
    description:str
    timestamp:datetime
    ex:Exception

    def __init__(
            self,
            r_type:RType,
            description:str='',
            timestamp:datetime=datetime.now(),
            ex:Exception=None
            ) -> None:
        self.r_type = r_type
        self.description = description
        self.timestamp = timestamp
        self.ex = ex
    
    def get_information(self) -> dict:
        #FIXME Fix the frame f_back when its a module
        frame = currentframe().f_back.f_back.f_back
        tb = getframeinfo(frame)

        information = {}
        information['type'] = self.r_type.value
        information['description'] = self.description
        information['timestamp'] = self.timestamp.strftime(date_format)
        information['ex_name'] = self.ex.__class__.__name__
        information['ex_args'] = self.ex.args
        information['line'] = tb.lineno
        information['filename'] = tb.filename.split('\\')[-1]
        information['class'] = frame.f_code.co_qualname
        information['function'] = tb.function
        information['positions'] = tb.positions

        return information

class Priority(Enum):
    LOW = 'low'
    MID = 'mid'
    HIGH = 'high'

class Error(Registry):
    priority:Priority

    def __init__(
            self,
            description:str='',
            timestamp:datetime=datetime.now(),
            ex:Exception=None,
            priority:Priority=Priority.MID
            ) -> None:
        """
        For actions that cause problems, every time!

        Args:
            description (str, optional): A short description for the warning. Defaults to ''.
            timestamp (datetime, optional): date and time what ocurred. Defaults to datetime.now().
            ex (Exception, optional): Exception for more details. Defaults to None.
            priority (bool, optional): When we have more than one error, we need to classify that. Defaults to False.
        """
        self.priority = priority
        super(Error, self).__init__(
            r_type=RType.ERR,
            description=description,
            timestamp=timestamp,
            ex=ex
        )
    
    def get_information(self):
        information = super(Error, self).get_information()
        information['priority'] = self.priority.value
        return information
    
    def __repr__(self) -> str:
        return f"""Error(
                        description={self.description},
                        timestamp={self.timestamp},
                        ex={self.ex},
                        priority={self.priority}
                    )
                    """

class Warning(Registry):
    follow_me:bool

    def __init__(
            self,
            description:str='',
            timestamp:datetime=datetime.now(),
            ex:Exception=None,
            follow_me:bool=False
            ) -> None:
        """
        For actions that would cause problems, but work

        Args:
            description (str, optional): A short description for the warning. Defaults to ''.
            timestamp (datetime, optional): date and time what ocurred. Defaults to datetime.now().
            ex (Exception, optional): Exception for more details. Defaults to None.
            follow_me (bool, optional): If this warning needs to followed. Defaults to False.
        """
        self.follow_me = follow_me
        super(Warning, self).__init__(
            r_type=RType.WARN,
            description=description,
            timestamp=timestamp,
            ex=ex
        )
    
    def get_information(self):
        information = super(Warning, self).get_information()
        information['follow_me'] = self.follow_me
        return information
    
    def __repr__(self) -> str:
        return f"""Warning(
                        description={self.description},
                        timestamp={self.timestamp},
                        ex={self.ex},
                        follow_me={self.follow_me}
                    )
                    """

#TODO Add an Info Class to the logger

#TODO Make a file length detector to backup the file and initialize a new one
def _save_dict(obj:dict):
    
    if not os.path.isdir('logs'):
        file_path = Path('logs/log.ev')
        file_path.parent.mkdir(exist_ok=True, parents=True)
        file_path.write_text('[]')

    with open('logs/log.ev', 'r') as file:
        lista:list = json.load(file)
    
    lista.append(obj)

    with open('logs/log.ev', 'w') as file:
        file.write(json.dumps(lista))

class Logger():
    @staticmethod
    def err(error:Error, printable:bool=False) -> bool:
        error_info = error.get_information()
        return _save_dict(error_info)
    
    @staticmethod
    def warn(warn:Warning, printable:bool=False) -> bool:
        warn_info  = warn.get_information()
        return _save_dict(warn_info)