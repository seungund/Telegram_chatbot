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
def echo(update, context):
    user_text = update.message.text 
    if user_text == "안녕":
        bot.sendMessage(chat_id=id, text="안녕안녕")   
    if user_text == "실험":
        a = 3
        bot.sendMessage(chat_id = id, text= a)
def ncal(update, context):
    input = context.args[0]
    bot.sendMessage(chat_id=id, text=input)

#메뉴 빌드   
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
#메뉴 함수
def get_school_level(update, context):
    show_list = []
    show_list.append(InlineKeyboardButton("초등학교", callback_data="초등학교")) # add on button
    show_list.append(InlineKeyboardButton("중학교", callback_data="중학교")) # add off button
    show_list.append(InlineKeyboardButton("고등학교", callback_data="고등학교")) # add cancel button
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list))) # make markup build_menu(리스트, 1줄에 표시할 리스트 수)
    bot.sendMessage(chat_id=id, text="학교 급을 선택해주세요", reply_markup = show_markup) #https://blog.psangwoo.com/coding/2018/08/20/python-telegram-bot-4.html


def get_school_name(update, context):
    show_list = []
    show_list.append(InlineKeyboardButton("초등학교", callback_data="초등학교")) # add on button
    show_list.append(InlineKeyboardButton("중학교", callback_data="중학교")) # add off button
    show_list.append(InlineKeyboardButton("고등학교", callback_data="고등학교")) # add cancel button
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list))) # make markup build_menu(리스트, 1줄에 표시할 리스트 수)
    bot.sendMessage(chat_id=id, text="학교 급을 선택해주세요", reply_markup = show_markup) #https://blog.psangwoo.com/coding/2018/08/20/python-telegram-bot-4.html


#Callback 함수
def callback_get(update, context):
    query = update.callback_query   
    data = query.data
    context.bot.edit_message_text(
        text=f"{data}작업을 완료했습니다."
        , chat_id=query.message.chat_id
        , message_id=query.message.message_id
    )
    get_school_name(update, context)




#Now i can reply
school_name = range(1)

def tt(update, context):
    bot.sendMessage(chat_id=id, text="학교 이름을 입력해주세요") 
    return school_name

def name(update, context):
    name = update.message.text
    if name[-1] == "고":
        bot.sendMessage(chat_id=id, text=f"당신의 고등학교 이름은 {name}입니다. ") 
    elif name[-1] == "중":
        bot.sendMessage(chat_id=id, text=f"당신의 중학교 이름은 {name}입니다. ") 
    elif name[-1] == "초":
        bot.sendMessage(chat_id=id, text=f"당신의 초등학교 이름은 {name}입니다. ") 
    elif name[-4] == "고":
        bot.sendMessage(chat_id=id, text=f"당신의 고등학교 이름은 {name}입니다. ") 
    elif name[-4] == "중":
        bot.sendMessage(chat_id=id, text=f"당신의 중학교 이름은 {name}입니다. ") 
    elif name[-4] == "초":
        bot.sendMessage(chat_id=id, text=f"당신의 초등학교 이름은 {name}입니다. ") 
    else:
        bot.sendMessage(chat_id=id, text=f"ERROR") 
    return ConversationHandler.END
def cancel(update, context):
    bot.sendMessage(chat_id=id, text="시간표 명령어 종료")
    return ConversationHandler.END 

echo_handler = MessageHandler(Filters.text, echo)
updater.dispatcher.add_handler(CommandHandler('ncal', ncal))

updater.dispatcher.add_handler(CommandHandler('meal', get_school_level))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))

updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler("tt", tt)],
    states={
        school_name : [MessageHandler(filters=~Filters.command, callback= name)]
    },
    fallbacks=[CommandHandler("cancel", cancel)]
))


dispatcher.add_handler(echo_handler)
