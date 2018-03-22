# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:31:00 2018

@author: ram
"""

import requests
from bs4 import BeautifulSoup
import sys
import time

def appendDocumentList(listofURLS):
    global alldocumentIDs
    for i in listofURLS:
        try:
            documentID = str(i).split('href="/docfragment/')[1].split('/')[0]
            alldocumentIDs.append(documentID)
        except:
            print (i)
            pass


alldocumentIDs = []
FILEPATH = r'urllist.txt'
with open(FILEPATH) as urls:
    try:
        for url in urls:
            try:
                soup = BeautifulSoup(requests.get(url).content, "lxml")
            except:
                time.sleep(180)
                soup = BeautifulSoup(requests.get(url).content, "lxml")
            try:
                totalPages = int(int(str(soup.find_all(class_="results_middle")[0]).split('<div><b>')[1].split('</b>')[0].split('of')[1].strip())/10)
                appendDocumentList(soup.find_all(class_="result_title"))
                for i in range(totalPages):
                    time.sleep(5)
                    curl=((str(url)+'&pagenum='+str((i+1))).replace('\n', '').replace('\r', ''))
                    try:
                        soup = BeautifulSoup(requests.get(curl).content, "lxml")
                        appendDocumentList( soup.find_all(class_="result_title"))
                    except:
                        time.sleep(180)
                        print("Unexpected error: -> ", sys.exc_info()[0])
                        pass
            except:
                time.sleep(180)
                print("Unexpected error    :", sys.exc_info()[0])
                pass
    except:
        print("Unexpected error    :", sys.exc_info()[0])
        pass

## writing document URLS to File
file = open('allDocumentsURLS.txt','w') 
for docid in alldocumentIDs:
    file.write('https://indiankanoon.org/doc/'+str(docid)+'/')
    file.write('\n')
file.close()