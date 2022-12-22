import random
import telegram
from telegram import *
from telegram.ext import *
import time
import requests
from bs4 import BeautifulSoup
import json
import datetime
import re

#기본값
my_token = "5759838781:AAGWmVF7tWC1C4jwDMVdYfkBZC4SVghMqSQ"
bot = telegram.Bot(token=my_token)
id = 5589523389
bot.sendMessage(chat_id=id, text="나는 대화챗봇입니다.")
updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

#파일 불러오기 - 카지노
door_file_path = "./casino/door.jpg"
road_file_path = "./casino/road.jpg"
gif = "https://media.giphy.com/media/3o6MbqNPaatT8nnEmk/giphy.gif"

#변수 선언 - 카지노
result, dcasino_start, road_path, door_path, ret= range(5)
global money
money = 5000
#변수 선언 - 급식
school_meal = range(1)
#변수 선언 - n빵
Money, People, Ncal = range(3)
#변수 선언 - 시간표
school_name = range(1)
#변수 선언 - 날씨


#함수 - 카지노
def casino(update, context):
    bot.sendMessage(chat_id=id, text="배팅게임에 오신 것을 환영합니다.")
    bot.sendMessage(chat_id=id, text="한 레벨을 통과하실 때마다 배팅 금액의 2배를 상금으로 받으실 수 있습니다.")
    bot.sendMessage(chat_id=id, text="레벨 통과에 실패하시면 모든 배팅 금액을 잃게 됩니다.")
    bot.sendMessage(chat_id=id, text="배팅 금액을 입력하세요. (기본 금액 : 5000원)")
    return dcasino_start

def casino_start(update, context):
    global r_money
    r_money = update.message.text
    if money > 5000:
        bot.sendMessage(chat_id=id, text="사기를 치다니! 거래가 종료됩니다.")
        return ConversationHandler.END
    bot.sendMessage(chat_id=id, text=f"총 {r_money}원 배팅하셨습니다. ")
    time.sleep(0.1)
    bot.send_photo(chat_id=id, photo=open(road_file_path, 'rb'))
    time.sleep(0.1)
    bot.sendMessage(chat_id=id, text="3갈래의 길로 나뉘어 있습니다. ")
    bot.sendMessage(chat_id=id, text="어느 길을 선택하시겠습니까? ")
    bot.sendMessage(chat_id=id, text="(1, 2, 3 중 입력)")
    return result

def betting_road(update, context):
    global r_money
    r_money = update.message.text
    bot.sendMessage(chat_id=id, text=f"총 {r_money}원 배팅하셨습니다. ")
    time.sleep(0.1)
    bot.send_photo(chat_id=id, photo=open(road_file_path, 'rb'))
    time.sleep(0.1)
    bot.sendMessage(chat_id=id, text="3갈래의 길로 나뉘어 있습니다. ")
    bot.sendMessage(chat_id=id, text="어느 길을 선택하시겠습니까? ")
    bot.sendMessage(chat_id=id, text="(1, 2, 3 중 입력)")
    return result

def betting_door(update, context):
    global r_money
    r_money = update.message.text
    bot.sendMessage(chat_id=id, text=f"총 {r_money}원 배팅하셨습니다. ")
    time.sleep(0.1)
    bot.send_photo(chat_id=id, photo=open(door_file_path, 'rb'))
    time.sleep(0.1)
    bot.sendMessage(chat_id=id, text="3개의 문으로 나뉘어 있습니다. ")
    bot.sendMessage(chat_id=id, text="어느 문을 선택하시겠습니까? ")
    bot.sendMessage(chat_id=id, text="(1, 2, 3 중 입력)")
    return result

def judge(update, context):
    win = random.randint(1,3)
    choice = int(update.message.text)
    global r_money
    r_money = int(r_money)
    global money
    global data
    if choice == win:
        money -= r_money
        r_money *= 2
        money += r_money
        bot.sendMessage(chat_id=id, text="축하합니다! 2배 획득!!")
        bot.sendMessage(chat_id=id, text=f"당신의 돈은 {money}원 입니다.")
        bot.sendMessage(chat_id=id, text="한번 더? (예, 아니요)")
        return ret
    else:
        money -= r_money
        bot.sendMessage(chat_id=id, text="아쉽네요. 모든 배팅 금액을 잃었습니다.")
        bot.sendMessage(chat_id=id, text=f"최종 금액은 {money}원 입니다.")
        money = 5000
        return ConversationHandler.END  

def retry(update, context):
    retry_op = update.message.text
    num = random.randint(1,2)
    global money
    if retry_op == "예" and num == 1:
        bot.sendMessage(chat_id=id, text=f"배팅 금액을 입력하세요. (현재 금액 : {money}원)")
        return road_path
    elif retry_op == "예" and num == 2:
        bot.sendMessage(chat_id=id, text=f"배팅 금액을 입력하세요. (현재 금액 : {money}원)")
        return door_path
    else:
        bot.sendMessage(chat_id=id, text="오늘은 여기까지!")
        bot.sendMessage(chat_id=id, text=f"최종 금액은 {money}원 입니다! 축하합니다")
        money = 10000
        bot.send_animation(chat_id=id, animation=gif)
        return ConversationHandler.END

def cancel_cas(update, context):
    bot.sendMessage(chat_id=id, text="도박 종료! 안녕!!")
    return ConversationHandler.END  

#함수 - 급식
def meal(update, context):
    bot.sendMessage(chat_id=id, text="학교 이름을 입력해주세요.")
    return school_meal

def cancel_meal(update, context):
    bot.sendMessage(chat_id=id, text="급식 명령어 종료")
    return ConversationHandler.END 

def school_meal(update, context):
    name = update.message.text
    if name[-1] == "고":
        sch = "고등학교"
    elif name[-1] == "중":
        sch = "중학교"
    elif name[-1] == "초":
        sch = "초등학교" 
    elif name[-4] == "고": 
        sch = "고등학교"
    elif name[-4] == "중":
        sch = "중학교"
    elif name[-4] == "초":
        sch = "초등학교"
    else:
        bot.sendMessage(chat_id=id, text=f"ERROR, 명령어 실행이 종료됩니다.") 
        return ConversationHandler.END
    path_e = './meal/E.json' 
    path_m = './meal/M.json'
    path_h = './meal/H.json'
    pn = str(sch)
    pcode = str(name)
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
#함수 - n빵
def ncal(update, context): 
    bot.sendMessage(chat_id=id, text="금액을 입력해주세요")
    return Money

def money_ncal(update, context):
    bot.sendMessage(chat_id=id, text="몇 명인가요?") 
    context.user_data["money"] = update.message.text 
    return People

def people(update, context):
    context.user_data["people"] = update.message.text 
    cost = int(context.user_data["money"])
    people = int(context.user_data["people"])

    average = (cost // people)
    bot.sendMessage(chat_id=id, text=f"1인당 {average}원씩 지불하시면 됩니다")
    if (cost % people) != 0:
        bot.sendMessage(chat_id=id, text=f"남은 금액은 가위바위보를 통해 기분좋게 이긴사람이 {cost % people}원을 지불할시면 됩니다.")
    return ConversationHandler.END 

def cancel_ncal(update, context):
    bot.sendMessage(chat_id=id, text="명령어 종료")
    return ConversationHandler.END 
#함수 - 시간표
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
def build_button(text_list, callback_header = "") : # make button list
    button_list = []
    text_header = callback_header
    if callback_header != "" :
        text_header += ","

    for text in text_list :
        button_list.append(InlineKeyboardButton(text, callback_data=text_header + text))

    return button_list

def get_school_grade(update, context):
    show_list = []
    show_list.append(InlineKeyboardButton("1학년", callback_data="1학년")) # add on button
    show_list.append(InlineKeyboardButton("2학년", callback_data="2학년")) # add off button
    show_list.append(InlineKeyboardButton("3학년", callback_data="3학년")) # add cancel button
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list))) # make markup build_menu(리스트, 1줄에 표시할 리스트 수)
    bot.sendMessage(chat_id=id, text="학년을 선택해주세요", reply_markup = show_markup) #https://blog.psangwoo.com/coding/2018/08/20/python-telegram-bot-4.html

def get_school_elementary_grade(update, context):
    show_list = []
    show_list.append(InlineKeyboardButton("1학년", callback_data="1학년")) # add on button
    show_list.append(InlineKeyboardButton("2학년", callback_data="2학년")) # add off button
    show_list.append(InlineKeyboardButton("3학년", callback_data="3학년")) # add cancel button
    show_list.append(InlineKeyboardButton("4학년", callback_data="4학년")) # add on button
    show_list.append(InlineKeyboardButton("5학년", callback_data="5학년")) # add off button
    show_list.append(InlineKeyboardButton("6학년", callback_data="6학년")) # add cancel button
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list))) # make markup build_menu(리스트, 1줄에 표시할 리스트 수)
    bot.sendMessage(chat_id=id, text="학년을 선택해주세요", reply_markup = show_markup) #https://blog.psangwoo.com/coding/2018/08/20/python-telegram-bot-4.html


def callback_get(update, context) :
    global data_selected
    data_selected = update.callback_query.data

    if len(data_selected.split(",")) == 1 :
        button_list = build_button(["1반", "2반", "3반", "4반", "5반", "6반", "7반", "8반","9반", "10반", "11반", "12반"], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 6))
        context.bot.edit_message_text(text="반을 선택해 주세요.",
                                      chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id,
                                      reply_markup=show_markup)

    elif len(data_selected.split(",")) == 2 :
        context.bot.edit_message_text(text=f"{name}, {update.callback_query.data}이(가) 선택되었습니다",
                                      chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id,
                                      )
        send = data_selected.split(",")
        play(sch, name, send[0], send[1])
        return ConversationHandler.END

def timetable(update, context):
     bot.sendMessage(chat_id=id, text="학교 이름을 입력해주세요") 
     return school_name

def name(update, context):
    global name
    global sch
    name = update.message.text
    if name[-1] == "고":
        sch = "고등학교"
    elif name[-1] == "중":
        sch = "중학교"
        
    elif name[-1] == "초":
         
        sch = "초등학교"
        
    elif name[-4] == "고":
         
        sch = "고등학교"
        
    elif name[-3] == "중":
         
        sch = "중학교"
        
    elif name[-4] == "초":
        
        sch = "초등학교"
    else:
        bot.sendMessage(chat_id=id, text=f"ERROR, 명령어 실행이 종료됩니다.") 
        return ConversationHandler.END

    if sch == "초등학교":
        get_school_elementary_grade(update, context)
        

    else:
        get_school_grade(update, context)

def cancel_time(update, context):
    bot.sendMessage(chat_id=id, text="시간표 명령어 종료")
    return ConversationHandler.END 

def play(sch, name, grade, clss):
    sch= str(sch)
    name= str(name)
    grade= str(grade)
    clss= str(clss)
    grade = grade.replace('학년','')
    clss= clss.replace('반','')
    time = str(datetime.date.today())
    time = time.replace('-','')
    Gcodeurl = 'https://open.neis.go.kr/hub/schoolInfo?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'+'&SCHUL_NM={}'.format(name)
    Gcode = requests.get(Gcodeurl).json()
    code = Gcode['schoolInfo'][1]['row'][0]['SD_SCHUL_CODE']
    scode = Gcode['schoolInfo'][1]['row'][0]['ATPT_OFCDC_SC_CODE']

    #고등학교
    if sch == '고등학교':
        Hurl = 'https://open.neis.go.kr/hub/hisTimetable?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'\
        +'&ATPT_OFCDC_SC_CODE={}&SD_SCHUL_CODE={}&ALL_TI_YMD={}&GRADE={}&CLASS_NM={}'.format(scode,code,time,grade,clss)
        H_timetable = requests.get(Hurl).json()
        table = H_timetable['hisTimetable'][1]['row']
        tablestr = str(table)

        if "'PERIO': '6'" in tablestr and "'PERIO': '7'" not in tablestr :
            for i in range(6):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
            
        elif "'PERIO': '7'" in tablestr :
            for i in range(7):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
        else :
            bot.sendMessage(chat_id=id, text="주말 또는 공휴일입니다.")     
                


    #중학교
    if sch == '중학교':
        Murl = 'https://open.neis.go.kr/hub/misTimetable?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'\
        +'&ATPT_OFCDC_SC_CODE={}&SD_SCHUL_CODE={}&ALL_TI_YMD={}&GRADE={}&CLASS_NM={}'.format(scode,code,time,grade,clss)
        M_timetable = requests.get(Murl).json()
        table = M_timetable['misTimetable'][1]['row']
        tablestr = str(table)
        
        if "'PERIO': '7'" in tablestr :
            for i in range(7):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])     
        
        elif "'PERIO': '6'" in tablestr and "'PERIO': '7'" not in tablestr :
            for i in range(6):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
                
        elif "'PERIO': '6'" not in tablestr and "'PERIO': '7'" not in tablestr and "'PERIO': '5'" in tablestr :
            for i in range(5):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
        
        else:
            bot.sendMessage(chat_id=id, text="주말 또는 공휴일입니다.")      
                    
    elif sch == '초등학교' :
        Eurl = 'https://open.neis.go.kr/hub/elsTimetable?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'\
        +'&ATPT_OFCDC_SC_CODE={}&SD_SCHUL_CODE={}&ALL_TI_YMD={}&GRADE={}&CLASS_NM={}'.format(scode,code,time,grade,clss)
        E_timetable = requests.get(Eurl).json()
        table = E_timetable['elsTimetable'][1]['row']
        tablestr = str(table)
        
        if "'PERIO': '7'" in tablestr :
            for i in range(7):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
            return ConversationHandler.END 
                
        elif "'PERIO': '6'" in tablestr and "'PERIO': '7'" not in tablestr :
            for i in range(6):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
            return ConversationHandler.END 
                
        elif "'PERIO': '6'" not in tablestr and "'PERIO': '7'" not in tablestr and "'PERIO': '5'" in tablestr :
            for i in range(5):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
            return ConversationHandler.END 
                
        elif "'PERIO': '6'" not in tablestr and "'PERIO': '7'" not in tablestr and "'PERIO': '5'" not in tablestr and "'PERIO': '4'" in tablestr :
            for i in range(4):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
            return ConversationHandler.END 
                    
        else:
            bot.sendMessage(chat_id=id, text="주말 또는 공휴일입니다.")
            return ConversationHandler.END   
#함수 - 날씨

def weather(update, context):
        
    #시간
    date = str(datetime.date.today())
    whole_date = date
    date = date.replace('-','')

    #------------#

    path = './weather/XYstore.json'

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
            wer_li['{}'.format(time)] = '{}'.format(a+'s')
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


    final = "6시 :{} / {}℃\n7시 :{} / {}℃\n8시 :{} / {}℃\n9시 :{} / {}℃\n10시 :{} / {}℃\n11시 :{} / {}℃\n12시 :{} / {}℃\n13시 :{} / {}℃\n14시 :{} / {}℃\n15시 :{} / {}℃\n16시 :{} / {}℃\n17시 :{} / {}℃\n18시 :{} / {}℃\n19시 :{} / {}℃\n20시 :{} / {}℃\n21시 :{} / {}℃\n22시 :{} / {}℃\n23시 :{} / {}℃".format(wer_li['6'],temp_li['6'],wer_li['7'],temp_li['7'],wer_li['8'],temp_li['8']\
    ,wer_li['9'],temp_li['9'],wer_li['10'],temp_li['10'],wer_li['11'],temp_li['11'],wer_li['12'],temp_li['12'],wer_li['13'],temp_li['13']\
    ,wer_li['14'],temp_li['14'],wer_li['15'],temp_li['15'],wer_li['16'],temp_li['16'],wer_li['17'],temp_li['17'],wer_li['18'],temp_li['18'],wer_li['19'],temp_li['19']\
    ,wer_li['20'],temp_li['20'],wer_li['21'],temp_li['21'],wer_li['22'],temp_li['22'],wer_li['23'],temp_li['23'])
    final = final.replace('1s','맑음 ☀ ')
    final = final.replace('3s','구름 약간 🌤')
    final = final.replace('4s','흐림 ☁')
    final = final.replace('1n','비 🌧')
    final = final.replace('2n','진눈깨비 🌨')
    final = final.replace('3n','눈 ❄')
    final = final.replace('4n','소나기 🌦')
    final = '<금일({})의 날씨>\n'.format(whole_date) + final
    temp_sum = 0
    for i in range(6, 24):
        temp_sum += int(temp_li[f'{i}'])
    if temp_sum / 18<= 0:
        bot.sendMessage(chat_id=id, text=final)
        bot.sendMessage(chat_id=id, text="🥶")
    elif temp_sum / 18>= 24:
        bot.sendMessage(chat_id=id, text=final)
        bot.sendMessage(chat_id=id, text="🫠")
    else:
        bot.sendMessage(chat_id=id, text=final)
        bot.sendMessage(chat_id=id, text="☺")







#텔레그램 Handler -카지노 /dop
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler("dop", casino)],
    states={
        dcasino_start : [MessageHandler(filters=~Filters.command, callback= casino_start)],
        road_path : [MessageHandler(filters=~Filters.command, callback= betting_road)],
        door_path : [MessageHandler(filters=~Filters.command, callback= betting_door)],
        result :  [MessageHandler(filters=~Filters.command, callback= judge)],
        ret : [MessageHandler(filters=~Filters.command, callback= retry)]
    },
    fallbacks=[CommandHandler("cancel", cancel_cas)]
))
#텔레그램 Handler -급식 /meal
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler("meal", meal)],
    states={
        school_meal : [MessageHandler(filters=~Filters.command, callback= school_meal)]
    },
    fallbacks=[CommandHandler("cancel", cancel_meal)]
))
#텔레그램 Handler -n빵 /ncal
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler("ncal", ncal)],
    states={
        Money : [MessageHandler(filters=~Filters.command, callback= money_ncal)],
        People : [MessageHandler(filters=~Filters.command, callback= people)],
    },
    fallbacks=[CommandHandler("cancel", cancel_ncal)]
))
#텔레그램 Handler - 시간표 /tt
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler("tt", timetable)],
    states={
        school_name : [MessageHandler(filters=~Filters.command, callback= name)]
    },
    fallbacks=[CommandHandler("cancel", cancel_time)]
))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))
#텔레그램 Handler - 날씨 /w
updater.dispatcher.add_handler(CommandHandler('w', weather))

