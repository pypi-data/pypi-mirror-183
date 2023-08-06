"""
@author Victor Valenzuela M
@since 28-12-22
"""

import json
from pathlib import Path
from inspect import currentframe, getframeinfo
from datetime import datetime
from enum import Enum
from types import FrameType


date_format = "%d/%m/%Y, %H:%M:%S"

class Priority(Enum):
    LOW = 'low'
    MID = 'mid'
    HIGH = 'high'

class Error():
    'Para acciones que generan problema'
    description:str
    timestamp:datetime
    priority:Priority
    ex:Exception

    def __init__(
            self,
            description:str='',
            timestamp:datetime=datetime.now(),
            priority:Priority=Priority.MID,
            ex:Exception=None) -> None:
        self.description = description
        self.timestamp = timestamp
        self.priority = priority
        self.ex = ex
    
    def __repr__(self) -> str:
        return f"""Error(
                        description={self.description},
                        timestamp={self.timestamp},
                        priority={self.priority}
                        ex={self.ex}
                    )
                    """

class Warning():
    'Para acciones que podrian generar problemas, pero funcionan igual'
    description:str
    follow_me:bool
    timestamp:datetime
    ex:Exception

    def __init__(
            self,
            description:str='',
            follow_me:bool=False,
            timestamp:datetime=datetime.now(),
            ex:Exception=None) -> None:
        self.description = description
        self.follow_me = follow_me
        self.timestamp = timestamp
        self.ex = ex
    
    def __repr__(self) -> str:
        return f"""Error(
                        description={self.description},
                        follow_me={self.follow_me},
                        timestamp={self.timestamp},
                        ex={self.ex}
                    )
                    """

#TODO Add an Info Class to the logger

def _to_dict(obj:Error | Warning, frame:FrameType) -> dict:
    tb = getframeinfo(frame)
    if isinstance(obj, Error):
        return {
            'type': 'error',
            'description': obj.description,
            'timestamp': obj.timestamp.strftime(date_format),
            'priority': obj.priority.value,
            'ex_name': obj.ex.__class__.__name__,
            'ex_args': obj.ex.args,
            'line': tb.lineno,
            'filename': tb.filename.split('\\')[-1],
            'class': frame.f_code.co_qualname,
            'function': tb.function,
            'positions': tb.positions
        }
    elif isinstance(obj, Warning):
        return {
            'type': 'warning',
            'description': obj.description,
            'follow_me': obj.follow_me,
            'timestamp': obj.timestamp.strftime(date_format),
            'ex_name': obj.ex.__class__.__name__,
            'ex_args': obj.ex.args,
            'line': tb.lineno,
            'filename': tb.filename.split('\\')[-1],
            'class': frame.f_code.co_qualname,
            'function': tb.function,
            'positions': tb.positions
        }

#TODO Make a file length detector to backup the file and initialize a new one
class Logger():
    @staticmethod
    def err(error:Error, printable:bool=False) -> bool:
        frame = currentframe().f_back
        error_dict  = _to_dict(error, frame)

        file_path = Path('logs/log.ev')
        file_path.parent.mkdir(exist_ok=True, parents=True)
        file_path.write_text('[]')

        with open('logs/log.ev', 'r') as file:
            lista:list = json.load(file)
        
        lista.append(error_dict)

        with open('logs/log.ev', 'w') as file:
            file.write(json.dumps(lista))

        return True
    
    @staticmethod
    def warn(warn:Warning, printable:bool=False) -> bool:
        frame = currentframe().f_back
        warn_dict  = _to_dict(warn, frame)

        file_path = Path('logs/log.ev')
        file_path.parent.mkdir(exist_ok=True, parents=True)
        file_path.write_text('[]')

        with open('logs/log.ev', 'r') as file:
            lista:list = json.load(file)
        
        lista.append(warn_dict)

        with open('logs/log.ev', 'w') as file:
            file.write(json.dumps(lista))
        
        return True