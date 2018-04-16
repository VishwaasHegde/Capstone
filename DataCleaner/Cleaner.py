import re
from os import listdir
from os.path import isfile, join
import os

class Cleaner():

    def getjudgement(self,txts):
        for txt in txts:
            t=txt.lower()
            index = t.find('judgment')
            if index<0 :
                index=t.find('j u d g m e n t')
            if index<0:
                continue
            if index+1<len(txts):
                return txts[index+1:]

    def cleanSentences(self,string):
        string = string.lower().replace("<br />", " ")
        string = string.replace('\\n', ' ')
        string=re.sub(strip_special_chars, "", string.lower())
        string=re.sub(' +', " ", string)
        return string



dir_path = os.path.dirname(os.path.realpath('Capstone'))
ind = dir_path.rfind('\\');
dir_path= dir_path[:ind]
dir_path = dir_path+'\\scrap_kanoon_data'+'\\judgements'


onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
cleaner=Cleaner()
with open(dir_path+'\\'+onlyfiles[0], 'r') as f:
    content = f.readlines()
    judgment = cleaner.getjudgement(content)
    judgment= cleaner.cleanSentences(str(judgment))
    print(judgment)




