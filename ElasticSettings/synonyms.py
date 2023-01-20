import re
from pandas import isna

def synonyms_replacer(text):
    if isna(text) or type(text) == None:
        return None
    
    regex = re.compile(r"(sars(-?|\s?))?cov(id)?(-)?(\s)?(19)?(2)?|corona(virus)?", flags=re.I|re.M)
    return regex.sub("coronavirus", text)