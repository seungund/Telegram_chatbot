import random
import telegram
from telegram import *
from telegram.ext import *
import time
my_token = "5336689796:AAGL3VEA1xM9dDodIbDxDNvv6Fv-VirCQoA"
bot = telegram.Bot(token=my_token)
id = 5775004281
bot.sendMessage(chat_id=id, text="나는 대화챗봇입니다.")
updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

door_file_path = "./door.jpg"
road_file_path = "./road.jpg"
gif = "https://media.giphy.com/media/3o6MbqNPaatT8nnEmk/giphy.gif"
'''
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

def deciding_next_stage(update, context):
    show_list = []
    show_list.append(InlineKeyboardButton("응!", callback_data="Yes")) # add on button
    show_list.append(InlineKeyboardButton("아니", callback_data="No")) # add off button
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list))) # make markup build_menu(리스트, 1줄에 표시할 리스트 수)
    bot.sendMessage(chat_id=id, text="한번 더?", reply_markup = show_markup) #https://blog.psangwoo.com/coding/2018/08/20/python-telegram-bot-4.html

def callback_get(update, context) :
    '''
        
                                      

    



result, dcasino_start, road_path, door_path, re= range(5)
global money
money = 10000

def casino(update, context):
    bot.sendMessage(chat_id=id, text="배팅게임에 오신 것을 환영합니다.")
    bot.sendMessage(chat_id=id, text="한 레벨을 통과하실 때마다 배팅 금액의 2배를 상금으로 받으실 수 있습니다.")
    bot.sendMessage(chat_id=id, text="레벨 통과에 실패하시면 모든 배팅 금액을 잃게 됩니다.")
    bot.sendMessage(chat_id=id, text="배팅 금액을 입력하세요. (기본 금액 : 10000원)")
    return dcasino_start



def casino_start(update, context):
    global r_money
    r_money = update.message.text
    if int(money) > 10000:
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
    win = random.randint(1,1)
    choice = int(update.message.text)
    global r_money
    r_money = int(r_money)
    global money
    global data
    if choice == win:
        r_money *= 2
        money += r_money
        bot.sendMessage(chat_id=id, text="축하합니다! 2배 획득!!")
        bot.sendMessage(chat_id=id, text=f"당신의 돈은 {money}원 입니다.")
        bot.sendMessage(chat_id=id, text="한번 더? (예, 아니요)")
        return re


    else:
        money -= r_money
        bot.sendMessage(chat_id=id, text="아쉽네요. 모든 배팅 금액을 잃었습니다.")
        bot.sendMessage(chat_id=id, text=f"최종 금액은 {money}원 입니다.")
        return ConversationHandler.END  


def retry(update, context):
    retry_op = update.message.text
    num = random.randint(1,2)
    print(num)
    if retry_op == "예" and num == 1:
        bot.sendMessage(chat_id=id, text=f"배팅 금액을 입력하세요. (현재 금액 : {money}원)")
        return road_path
    elif retry_op == "예" and num == 2:
        bot.sendMessage(chat_id=id, text=f"배팅 금액을 입력하세요. (현재 금액 : {money}원)")
        return door_path
    else:
        bot.sendMessage(chat_id=id, text="오늘은 여기까지!")
        bot.sendMessage(chat_id=id, text=f"최종 금액은 {money}원 입니다! 축하합니다")
        bot.send_animation(chat_id=id, animation=gif)
        return ConversationHandler.END
        







def cancel(update, context):
    bot.sendMessage(chat_id=id, text="도박 종료! 안녕!!")
    return ConversationHandler.END  


updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler("dop", casino)],
    states={
        dcasino_start : [MessageHandler(filters=~Filters.command, callback= casino_start)],
        road_path : [MessageHandler(filters=~Filters.command, callback= betting_road)],
        door_path : [MessageHandler(filters=~Filters.command, callback= betting_door)],
        result :  [MessageHandler(filters=~Filters.command, callback= judge)],
        re : [MessageHandler(filters=~Filters.command, callback= retry)]
    },
    fallbacks=[CommandHandler("cancel", cancel)]
))
#updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))