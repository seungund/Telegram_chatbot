import datetime
import json
import re

import googletrans
import requests
import telegram
from bs4 import BeautifulSoup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

#wufQpwOk9N7wGx3WAooWB8wdRtYVMduOSAkTVMLfegxIsHrwBBscP3MznOEbTkLOp%2FAEo9iqiX1edIvrVuUSwQ%3D%3D

#시간
date = str(datetime.date.today())
whole_date = date
date = date.replace('-','')

#------------#

path = 'Weather\XYstore.json'

with open(path, 'r') as f:
    data = json.load(f)

X= data["X"]
Y= data["Y"]

code='wufQpwOk9N7wGx3WAooWB8wdRtYVMduOSAkTVMLfegxIsHrwBBscP3MznOEbTkLOp%2FAEo9iqiX1edIvrVuUSwQ%3D%3D'
url = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={}&base_time=0500&nx={}&ny={}'\
    .format(code,date,X,Y)
    

weather = requests.get(url,verify=False).json()

wer_time = int('5')
wew_time = int('5')
#시간대 0500 to 0000
#날씨
wer_li = dict()
wew_li = dict()
data = weather["response"]["body"]["items"]["item"]

for i in data:
    if(i["category"]) == "PTY" and (i["fcstDate"]) == date:
        wea = (i["fcstValue"]+'s')
       
        wer_time = wer_time+1
        wer_li[str(wer_time)] = wea
        
        
for i in data:    
    if(i["category"]) == "SKY" and (i["fcstDate"]) == date:
        wea = (i["fcstValue"])
        
        wew_time = wew_time+1
        wew_li[str(wew_time)] = wea
        

time = int('6')

for ii in range(1,19):
    if wer_li['{}'.format(time)] == "0s" :
        a = wew_li['{}'.format(time)]
        wer_li['{}'.format(time)] = '{}'.format(a+'n')
        
    time = time  + 1
    continue   

        
        

#####
# 1s : 맑음 3s : 구름 많음 4s : 흐림,, 1 : 비 2: 비/눈 3: 눈 4 : 소나기 #
#####

#온도
tmp_time = int('5')
temp_li = dict()
data = weather["response"]["body"]["items"]["item"]
for i in data:
    if(i["category"]) == "TMP" and (i["fcstDate"]) == date:
        tmp = (i["fcstValue"])
        tmp_time = tmp_time+1
        temp_li[str(tmp_time)] = tmp
        


#-----------------------------------------------------------#


final = "6시 :{} / {}℃\n7시 :{} / {}℃\n8시 :{} / {}℃\n9시 :{} / {}℃\n10시 :{} / {}℃\n11시 :{} / {}℃\n12시 :{} / {}℃\n13시 :{} / {}℃\n14시 :{} / {}℃\n15시 :{} / {}℃\n16시 :{} / {}℃\n17시 :{} / {}℃\n\
18시 :{} / {}℃\n19시 :{} / {}℃\n20시 :{} / {}℃\n21시 :{} / {}℃\n22시 :{} / {}℃\n23시 :{} / {}℃".format(wer_li['6'],temp_li['6'],wer_li['7'],temp_li['7'],wer_li['8'],temp_li['8']\
,wer_li['9'],temp_li['9'],wer_li['10'],temp_li['10'],wer_li['11'],temp_li['11'],wer_li['12'],temp_li['12'],wer_li['13'],temp_li['13']\
,wer_li['14'],temp_li['14'],wer_li['15'],temp_li['15'],wer_li['16'],temp_li['16'],wer_li['17'],temp_li['17'],wer_li['18'],temp_li['18'],wer_li['19'],temp_li['19']\
,wer_li['20'],temp_li['20'],wer_li['21'],temp_li['21'],wer_li['22'],temp_li['22'],wer_li['23'],temp_li['23'])

final = final.replace('1n','맑음')
final = final.replace('3n','구름 약간')
final = final.replace('4n','흐림')
final = final.replace('1s','비')
final = final.replace('2s','진눈깨비')
final = final.replace('3s','눈')
final = final.replace('4s','소나기')
final = '<금일({})의 날씨>\n'.format(whole_date) + final
print(final)

print(wer_li)