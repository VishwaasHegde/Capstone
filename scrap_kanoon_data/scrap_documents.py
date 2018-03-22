# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:09:05 2018

@author: ram
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:31:00 2018

@author: ram
"""

import requests
from bs4 import BeautifulSoup
import sys
import re
import time

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

FILEPATH = r'allDocumentsURLS.txt'
with open(FILEPATH) as urls:
    try:
        for url in urls:
                try:
                    soup = BeautifulSoup(requests.get(url).content, "lxml")
                    time.sleep(5)
                    judgement = str(soup.find_all(class_="judgments")[0])
                    docID  = str(url).replace('https://indiankanoon.org/doc/','').replace('/','').strip()
                    file = open(('judgements/'+docID+'.txt'),'w+') 
                    file.write(cleanhtml(judgement))
                    file.close()
                except:
                    time.sleep(180)
                    print("Unexpected error:", sys.exc_info()[0])
                    pass
    except:
        print("Unexpected error    :", sys.exc_info()[0])
        pass