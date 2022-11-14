import telegram
from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CommandHandler, Updater, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup
import json
import datetime
import re

my_token = "5336689796:AAGL3VEA1xM9dDodIbDxDNvv6Fv-VirCQoA"
bot = telegram.Bot(token=my_token)
id = 5775004281
bot.sendMessage(chat_id=id, text="나는 대화챗봇입니다.")
updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

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

def get_school_clss(update, context):
    show_list = []
    show_list.append(InlineKeyboardButton("1반", callback_data="1반")) # add on button
    show_list.append(InlineKeyboardButton("2반", callback_data="2반")) # add off button
    show_list.append(InlineKeyboardButton("3반", callback_data="3반")) # add cancel button
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list))) # make markup build_menu(리스트, 1줄에 표시할 리스트 수)
    bot.sendMessage(chat_id=id, text="반을 선택해주세요", reply_markup = show_markup) #https://blog.psangwoo.com/coding/2018/08/20/python-telegram-bot-4.html


def callback_get(update, context) :
    global data_selected
    data_selected = update.callback_query.data

    if len(data_selected.split(",")) == 1 :
        button_list = build_button(["1반", "2반", "3반", "4반", "5반", "6반"], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 1))
        context.bot.edit_message_text(text="반을 선택해 주세요.",
                                      chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id,
                                      reply_markup=show_markup)

    elif len(data_selected.split(",")) == 2 :
        context.bot.edit_message_text(text="{}이(가) 선택되었습니다".format(update.callback_query.data),
                                      chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id,
                                      )
        send = data_selected.split(",")
        play(sch, name, send[0], send[1])
                                      

    

    


def timetable(update, context):
    global sch, name
    sch, name = context.args[0], context.args[1]
    

    if sch == "초등학교":
        get_school_elementary_grade(update, context)
        

    else:
        get_school_grade(update, context)





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
        
        elif "'PERIO': '6'" in tablestr and "'PERIO': '7'" not in tablestr :
            for i in range(6):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
                
        elif "'PERIO': '6'" not in tablestr and "'PERIO': '7'" not in tablestr and "'PERIO': '5'" in tablestr :
            for i in range(5):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
                
        elif "'PERIO': '6'" not in tablestr and "'PERIO': '7'" not in tablestr and "'PERIO': '5'" not in tablestr and "'PERIO': '4'" in tablestr :
            for i in range(4):
                bot.sendMessage(chat_id=id, text=table[i]['ITRT_CNTNT'])
                    
        else:
            bot.sendMessage(chat_id=id, text="주말 또는 공휴일입니다.")  
        
        


#변수은 이곳에 기록 key = b0a0e01a8df841228238bcbfc7aa7013
#Hurl=고등학교 api url, H_timetable = 고등학교 api get, name = 학교이름 code=학교코드, grade=학년, clss=반, Gcodeurl = 학교기본정보 api url, Gcode = 학교기본정보 api get



updater.dispatcher.add_handler(CommandHandler('tt', timetable))

updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))

