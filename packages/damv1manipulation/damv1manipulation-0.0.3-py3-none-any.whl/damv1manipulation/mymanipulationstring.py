from enum import Enum

class general():
    def remove_newline(_str):
        oput = None
        if _str.strip()!= '':
            oput = _str.replace('\n','').strip()
        return oput


class telegram():
    def escape_strparse_markdownv1(_string):
        output=None
        if _string.strip()!='':
            output=_string\
                    .replace('{','\\{').replace('}','\\}')\
                    .replace('[','\\[').replace(']','\\]')\
                    .replace('(','\\(').replace(')','\\)')\
                    .replace('*','\\*')\
                    .replace('~','\\~')\
                    .replace('`','\\`')\
                    .replace('_','\\_')\
                    .replace('#','\\#')\
                    .replace('+','\\+')\
                    .replace('-','\\-')\
                    .replace('=','\\=')\
                    .replace('|','\\|')\
                    .replace('.','\\.')\
                    .replace('!','\\!')
        return output

class variable_type(Enum):
    str = 'str'
    int = 'int'
    bool = 'bool'
class kwargs():
    def getValueAllowed(self, kwargs, _nameOfKwargs, _typeOfKwargs, _defaultValue = None):
        value = _defaultValue; bAllowParams = False
        if str(_nameOfKwargs) in kwargs:
            if f"'{str(_typeOfKwargs)}'" in str(type(kwargs.get(str(_nameOfKwargs)))):
                value = kwargs.get(str(_nameOfKwargs)) 
                bAllowParams = True
        return value, bAllowParams    