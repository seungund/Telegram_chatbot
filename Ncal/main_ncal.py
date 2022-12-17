import telegram
from telegram import *
from telegram.ext import *
my_token = "5336689796:AAGL3VEA1xM9dDodIbDxDNvv6Fv-VirCQoA"
bot = telegram.Bot(token=my_token)
id = 5775004281
bot.sendMessage(chat_id=id, text="나는 대화챗봇입니다.")
updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


#입력 형식: /ncal 금액 사람명수




Money, People, Ncal = range(3)
def ncal(update, context): 
    bot.sendMessage(chat_id=id, text="금액을 입력해주세요")
    return Money

def money(update, context):
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

def cancel(update, context):
    bot.sendMessage(chat_id=id, text="명령어 종료")
    return ConversationHandler.END 


updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler("ncal", ncal)],
    states={
        Money : [MessageHandler(filters=~Filters.command, callback= money)],
        People : [MessageHandler(filters=~Filters.command, callback= people)],
    },
    fallbacks=[CommandHandler("cancel", cancel)]
))
