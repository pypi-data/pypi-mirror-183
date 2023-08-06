

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
