import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

my_token = "5336689796:AAGL3VEA1xM9dDodIbDxDNvv6Fv-VirCQoA"
bot = telegram.Bot(token=my_token)
id = 5775004281
bot.sendMessage(chat_id=id, text="나는 대화챗봇입니다.")

updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def echo(update, context):
    #  user_text = update.message.text 
    #  if user_text == "안녕":
    #     bot.send_message(chat_id=id, text="안녕안녕")

    bot.send_message(chat_id=id, text="어쩔 ㅋ")

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
