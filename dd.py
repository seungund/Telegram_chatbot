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

def build_button(text_list, callback_header = "") : # make button list
    button_list = []
    text_header = callback_header
    if callback_header != "" :
        text_header += ","

    for text in text_list :
        button_list.append(InlineKeyboardButton(text, callback_data=text_header + text))

    return button_list

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def get_command(update, context) :
    print("get")
    button_list = build_button(["on", "off", "cancel"]) # make button list
    show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 1)) # make markup
    update.message.reply_text("원하는 값을 선택하세요", reply_markup=show_markup) # reply text with markup




def callback_get(update, context) :
    data_selected = update.callback_query.data
    print("callback : ", data_selected)
    if len(data_selected.split(",")) == 1 :
        button_list = build_button(["1", "2", "3", "cancel"], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 1))
        context.bot.edit_message_text(text="상태를 선택해 주세요.",
                                      chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id,
                                      reply_markup=show_markup)

    elif len(data_selected.split(",")) == 2 :
        context.bot.edit_message_text(text="{}이(가) 선택되었습니다".format(update.callback_query.data),
                                      chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id)

get_handler = CommandHandler('get', get_command)
updater.dispatcher.add_handler(get_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))  