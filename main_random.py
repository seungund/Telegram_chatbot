import random
import re
import telegram
from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CommandHandler, Updater, CallbackQueryHandler
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


def jaebee(update, context):
    global range1
    range1 = int(context.args[0])
    play_range(update, context)

def play_range(update, context):
    show_list = []
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list)))
    for i in range(1, range1 + 1):
        show_list.append(InlineKeyboardButton(f"{i}", callback_data=f"{i}")) # add on button
        show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list)))
    bot.sendMessage(chat_id=id, text="숫자를 선택해주세요", reply_markup = show_markup) #https://blog.psangwoo.com/coding/2018/08/20/python-telegram-bot-4.html




def play(range1, num):  
   
    if num<1 or num>range:
        bot.sendMessage(chat_id=id, text="범위 내의 숫자를 다시 입력해주세요.")
    #당첨
    elif num == winner:
        bot.sendMessage(chat_id=id, text="당첨입니다.")

    #입력했던값이랑 중복되는지 판별
    elif num in count:
        bot.sendMessage(chat_id=id, text="중복된 숫자입니다.")
    #탈락
    elif num != winner:
        bot.sendMessage(chat_id=id, text="아쉽네요~")
        count.append(num)







updater.dispatcher.add_handler(CommandHandler('j', jaebee))




