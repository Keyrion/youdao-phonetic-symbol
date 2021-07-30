#coding:utf-8

from __future__ import print_function
import time
import requests
from bs4 import BeautifulSoup
import os
import sys
from playsound import playsound
import openpyxl
import time

main_url="https://dict.youdao.com/search"
audio_url="https://dict.youdao.com/dictvoice"
my_header ={
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Referer': ''
}
my_param= {
    'q':''
}
audio_param = {
    "audio": '',
    'type': ''
}

workbook = openpyxl.load_workbook("valc.xlsx")
sht = workbook.get_sheet_by_name("Sheet1")

words=[['' for i in range(1,4)] for i in range(1, 501)]

num=sht.max_row
for i in range(2,num+1):
    words[i-2][0]=sht['A'+str(i)].value

i=1

for now in words:
    if now[0]== '':
        break
    my_param['q']=now[0]

    req=requests.get(main_url,params=my_param,headers=my_header)
    soup =BeautifulSoup(req.text, "lxml")

    baav=soup.find(class_='baav')
    phonetics=baav.find_all(class_='phonetic')

    cnt=1
    for phs in phonetics:
        now[cnt]=phs.string
        cnt=cnt+1

    prop=(i*100)//num
    print(str(prop)+'% '+"▋" *(prop//2)+'\r', end='')

    i=i+1

for i in range(2,num+1):
    sht['B'+str(i)].value=words[i-2][1]
    sht['c' + str(i)].value = words[i-2][2]

workbook.save("valc.xlsx")
print('')