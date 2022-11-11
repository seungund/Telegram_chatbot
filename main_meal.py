import requests
from bs4 import BeautifulSoup
import json
import datetime
import re
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

#텔레그램
#(현재)
# /meal 학교급 학교이름

# (발전 예정)
# /meal
# 학교 급을 입력해주세요 
# : 고등학교
# 학교 이름을 입력해주세요
# _ 동대부고


my_token = "5759838781:AAGWmVF7tWC1C4jwDMVdYfkBZC4SVghMqSQ"
bot = telegram.Bot(token=my_token)
id = 5589523389
bot.sendMessage(chat_id=id, text="나는 대화챗봇입니다.")

updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def school_meal(update, context):
    school_level = context.args[0]
    school_name = context.args[1]
    
    path_e = 'Cafeteria\E.json' 
    path_m = 'Cafeteria\M.json'
    path_h = 'Cafeteria\H.json'

    pn = school_level

    pcode = school_name

    dt = str(datetime.date.today())
    dt_a = dt.replace('-','')
    d = datetime.date.today().weekday()


    ni = 2

    if pn == '고등학교':
        n = '4'
        ns = '04'
        with open(path_h, 'r', encoding='utf-8') as h:
            data_h = json.load(h)
            for a in data_h['list']:
                if a['SCHUL_NM'] == pcode:
                    code = a['SCHUL_CODE']
                    
                    break
                
            
    elif pn == '중학교':
        n = '3'
        ns = '03'  
        with open(path_m, 'r', 'utf-8') as m:
            data_m = json.load(m)
            for a in data_m['list']:
                if a['SCHUL_NM'] == pcode:
                    code = a['SCHUL_CODE']
                    
                    break
            
        
            
    elif pn == '초등학교':
        n = '2'
        ns = '02'
        with open(path_e, 'r', 'utf-8') as e:
            data_e = json.load(e)
            for a in data_e['list']:
                if a['SCHUL_NM'] == pcode:
                    code = a['SCHUL_CODE']
                    
                    break
            
    else:
        bot.sendMessage(chat_id = id, text="잘못 입력하였습니다 처음부터 다시 입력해 주세요") 
    

    coder = code.replace("S01", "B10")      
    #(임시코드)코드의 앞머리 S01의 변화에 관한 정보가 아직 없으므로 다른학교에서는 작동하지 않을 수 있음           
    url = 'https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode={}&schulCrseScCode={}&schulKndScCode={}&schMmealScCode={}&schYmd={}'.format(coder,n,ns,ni,dt_a)




    req = requests.get(url)
    result = BeautifulSoup(req.text, "html.parser")
    elem = result.find_all("td")


    #0 ~ 6 요일, 6=토, 7=일, 1=월



    if d == 1:
        dtd = 7
        elem1 = elem[int(dtd)]
    elif d == 2:
        dtd = 8
        elem1 = elem[int(dtd)] 
    elif d == 3:
        dtd = 9
        elem1 = elem[int(dtd)]
    elif d == 4:
        dtd = 10
        elem1 = elem[int(dtd)]
    elif d == 5:
        dtd= 11
        elem1 = elem[int(dtd)]
    elif d == 6 or d == 7:
        dtd = 12

        
    r = "\(.*\)|\s-\s.*" 


    if dtd == 7 or dtd== 8 or dtd == 9 or dtd == 10 or dtd == 11:
        elemf=str(elem1).replace('<br/>','\n')
        elemf=elemf.replace('<td class="textC">','')
        elemf=elemf.replace('</td>','')
        elemf=elemf.replace('*','')
        elemf=elemf.replace('.','')
        elemf=re.sub(r,'',elemf)
        elemf=re.sub('\d','',elemf)
        
        
        bot.sendMessage(chat_id = id, text =f"오늘의 급식 \n ---------- \n {elemf}")


    elif dtd == 12:
        bot.sendMessage(chat_id = id, text="오늘은 주말/공휴일 입니다.")
updater.dispatcher.add_handler(CommandHandler('meal', school_meal))