import damv1airtableprojectk8salert as airtblk8salert

from enum import Enum
from .mytime7 import currentTime7 as cT7

class const_thread(Enum):
    number_1 = 1
    number_2 = 2
    number_3 = 3

aCls = airtblk8salert.sandbox()

def logger(_time=cT7(), *args, **kwargs):
    
    if not "'str'" in str(type(args)):
        args = str(args)

    print(_time,' '.join(args))

    try:
        threadNumber = const_thread.number_1.value
        if '_argThreadNumber' in kwargs:
            threadNumber = kwargs.get("_argThreadNumber") 
            if "'int'" in str(type(threadNumber)):
                idAirtable = None
                if '_argIdAirtable' in kwargs:
                    idAirtable = kwargs.get("_argIdAirtable") 
                    if str(idAirtable).strip()!='':
                        aCls.pyairtable_updateDateTime_CurrentNumberLastOfLog(threadNumber,idAirtable)
    except ValueError:
        pass