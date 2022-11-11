#변수 :
#사용자가 최초1회 입력한 주소를 JSON형식으로 저장한 뒤 API를 이용해 당일의 일기예보를 불러옴, 지역이름을 찾은 뒤, 지역코드 그리고 xy값을 순차적으로 불러옴
#key = wufQpwOk9N7wGx3WAooWB8wdRtYVMduOSAkTVMLfegxIsHrwBBscP3MznOEbTkLOp%2FAEo9iqiX1edIvrVuUSwQ%3D%3D
#USER-ID = 5589523389 ,TOKEN = 5759838781:AAGWmVF7tWC1C4jwDMVdYfkBZC4SVghMqSQ

import requests
from bs4 import BeautifulSoup
import json
import datetime
import re
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

#주소입력
location = str(input("주소를 입력하세요(**특별시, **광역시, **시, **군):"))
#engloc = translator. translate(location, dest='en', src='auto')
#engloc = engloc.text
#JSON에서 읽고 저장
path = 'Weather\location.json'
path_2 = 'Weather\XYstore.json'

with open(path, 'r', encoding='utf-8') as p :
    data = json.load(p)
    str_data = str(data)
    if location in str_data:
        for i in data:
            if i["B"] == location:
                X = i["X"]
                Y = i["Y"]
                
                li = dict()
                li['X'] = X
                li['Y'] = Y
                data = li
                
                with open(path_2 , 'w' , encoding='UTF-8') as of:
                    json.dump(data, of, indent=4)
                    print("성공")
                    break 
               
            
                
    else:
        print("오류")            