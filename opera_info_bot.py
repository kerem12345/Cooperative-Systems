from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import operas as op


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

DAY, OPERA, INFO, INFO_LIST = range(4)

def start(update, context):
    update.message.reply_text(
        "Hello there! I am a bot and will try to provide you with information about operas being held in our hall."
        "If you would like to see a list of performances being held today, type Today. If you would like to see a list"
        "of performances for tomorrow, type Tomorrow. Use /help at any time to display a list of my commands!"
    )

    return DAY

opera_day = ""
def select_opera(update, context): 
    global opera_day                    
    if update.message.text != "/back" and update.message.text != "/help":
        opera_day = update.message.text
    update.message.reply_text(op.choose_day(opera_day))

    update.message.reply_text(
        "Please select one by typing the corresponding number"
    )
    return OPERA

opera_choice = ""
def info_selection(update, context):
    global opera_day
    global opera_choice
    if update.message.text != "/back" and update.message.text != "/help":
        opera_choice = update.message.text

    update.message.reply_text(op.choose_opera(opera_day, opera_choice))
    return INFO
        


def info(update, context):
    query = update.message.text
    
    if query in ["Actors", "actors", "Actor", "Avtors", "Acrors"]:
        update.message.reply_text(op.actors(opera_day, opera_choice))     
        update.message.reply_text("Enter \"/back\" to go back to the previous section.") 

    if query in ["Composer", "composer", "Conposer", "Vomposer"]:
        update.message.reply_text(op.composer(opera_day, opera_choice))
        update.message.reply_text("Enter \"/back\" to go back to the previous section.") 

    if query in ["Plot", "plot", "Olot", "olot", "Plor", "Ploy"]:
        update.message.reply_text(op.plot(opera_day, opera_choice))
        update.message.reply_text("Enter \"/back\" to go back to the previous section.") 

    if query in ["Prices", "prices", "Price", "price", "orice", "Orice", "orices", "Orices"]:
        update.message.reply_text("Price overview available at: https://www.wiener-staatsoper.at/spielplan-karten/liste/refDate/2021-05-01/")  
        update.message.reply_text("Enter \"/back\" to go back to the previous section.") 

    if query in ["Discount", "discount", "Discounts", "discounts"]:
        update.message.reply_text(op.discounts(opera_day, opera_choice))
        update.message.reply_text("Enter \"/back\" to go back to the previous section.") 

    return INFO_LIST

def end(update, context):
    user = update.message.from_user
    update.message.reply_text(
        "Have a nice day!", reply_markup = ReplyKeyboardRemove()
    )

def help(update, context):
    update.message.reply_text(
            "Welcome to the help menu! Here is a lis of commands I support:\n\n"
            "/start or /restart - Returns you to the start of the conversation.\n"
            "/back - Returns you to the previous step\n"
            "/help - Displays this helpful menu.\n"
            "/bye - Bids me farewell.\n"
    )


def main():
    updater = Updater(token='1502982782:AAGLhgaQmIeg9NTcxn7x7DyWDQ6uhmTr4t4', use_context=True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start), CommandHandler('restart', start)],
        states = {
            DAY : [
                MessageHandler(Filters.regex('^(Today|Tomorrow|today|tomorrow)$'), select_opera),
                CommandHandler('help', help),
            ],
            OPERA : [
                MessageHandler(Filters.regex('^(1|2|3)$'), info_selection),
                CommandHandler('back', start),
                CommandHandler('help', help),  
            ],
            INFO : [
                MessageHandler(Filters.regex('^(Actors|actors|Actor|Avtors|Acrors|Composer|composer|Conposer|Vomposer|Plot|plot|'
                        'Olot|olot|Plor|Ploy|Prices|prices|price|Price|Orice|orice|Orices|orices|Discount|discount|Discounts|Discounts)'), info),
                CommandHandler('back', select_opera),
                CommandHandler('help', help),
            ],
            INFO_LIST : [
                CommandHandler('back', info_selection),
                CommandHandler('help', help),
            ]
        },
        fallbacks = [CommandHandler('bye', end)],
        allow_reentry=True
    )

    dispatcher.add_handler(conv_handler)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()