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


#입력 형식: /ncal 금액 사람명수

        
def jaebee(update, context):
    range = context.args[0]
    num = int(context.args[1])
    if re.match("\d",range):
        range=int(range)
        winner = random.randint(1,range)
        count = []
        #제비뽑기 진행
        #범위 판독
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
        

    else:
        bot.sendMessage(chat_id=id, text="숫자로 다시 입력해주세요.")

    

    
updater.dispatcher.add_handler(CommandHandler('j', jaebee))


