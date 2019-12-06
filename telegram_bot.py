import telebot
import time

token = 'your_token_here'

bot = telebot.TeleBot(token=token)

# for using webhook :
# @bot.setwebhook(token)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message,"""
        سلام خیلی خوش امدید
        برای دریافت راهنما /help
    """)


@bot.message_handler(commands=['help'])
def start_handler(message):
    bot.reply_to(message,"""
        برای ارسال نظر #comment
        برای دریافت اطلاعات پکیج #package pack-no
        ممنون از حسن انتخاب شما
    """)


@bot.message_handler(func=lambda msg: msg.text is not None and '#comment' in msg)
def zbits_handler(message):
    username = '' # TODO : check the message for user name
    bot.reply_to(message,"""{username} ممنون 
        نظر شما دریافت شد و بررسی میشود
    """.format(username=username))


@bot.message_handler(func=lambda msg: msg.text is not None and '#package' in msg)
def zbits_handler(message):
    # TODO : returning the location of the sent packet with the number asked
    bot.reply_to(message,'package# : \n location : \n time_to_rcv : \n Thank you for your choice.')

while True:
    try :
        bot.polling()
    except:
        time.sleep(5)