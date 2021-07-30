#coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
from playsound import playsound

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


word=input("输入查询词汇：")
my_param['q']=word
audio_param['audio']=word

req=requests.get(main_url,params=my_param,headers=my_header)
soup =BeautifulSoup(req.text, "lxml")

baav=soup.find(class_='baav')
phonetics=baav.find_all(class_='phonetic')

cnt=1
for phs in phonetics:
    kd=""
    fname=""
    if cnt == 1:
        kd='英'
    else:
        kd='美'
    fname=str(cnt)+".mp3"
    audio_param['ytpe']=str(cnt)
    print('['+str(cnt)+']'+kd+": "+phs.string)
    req = requests.get(audio_url, params=audio_param, headers=my_header)
    with open(fname, 'wb') as f:
        f.write(req.content)
    cnt=cnt+1

choise= input("选择发音[1/2]: ")
playsound(str(choise)+'.mp3')

os.system('del 1.mp3')
os.system('del 2.mp3')
# print(soup.prettify())