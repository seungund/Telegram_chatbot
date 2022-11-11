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


def ncal(update, context):
    cost = int(context.args[0])
    people = int(context.args[1])

    average = (cost / people)
    bot.sendMessage(chat_id=id, text=f"1인당 {average}원씩 지불하시면 됩니다")
    if (cost % people) != 0:
        bot.sendMessage(chat_id=id, text=f"남은 금액은 가위바위보를 통해 당첨자가 {cost % people}원을 지불할시면 됩니다.")
updater.dispatcher.add_handler(CommandHandler('ncal', ncal))
