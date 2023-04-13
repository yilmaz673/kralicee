import telegram
import telegram.ext
import datetime
import pytz

TOKEN = '6245058500:AAEudc8D7yt1fvYDrKGscscJ_6JMsV2pJR0'
iftar_times = [
    (datetime.datetime(2023, 4, 12, 20, 5, tzinfo=pytz.timezone('Europe/Berlin')), "Çarşamba"),
    (datetime.datetime(2023, 4, 13, 20, 31, tzinfo=pytz.timezone('Europe/Berlin')), "Perşembe"),
    (datetime.datetime(2023, 4, 14, 20, 33, tzinfo=pytz.timezone('Europe/Berlin')), "Cuma"),
    (datetime.datetime(2023, 4, 15, 20, 34, tzinfo=pytz.timezone('Europe/Berlin')), "Cumartesi"),
    (datetime.datetime(2023, 4, 16, 20, 36, tzinfo=pytz.timezone('Europe/Berlin')), "Pazar"),
    (datetime.datetime(2023, 4, 17, 20, 38, tzinfo=pytz.timezone('Europe/Berlin')), "Pazartesi"),
    (datetime.datetime(2023, 4, 18, 20, 39, tzinfo=pytz.timezone('Europe/Berlin')), "Salı"),
    (datetime.datetime(2023, 4, 19, 20, 41, tzinfo=pytz.timezone('Europe/Berlin')), "Çarşamba"),
    (datetime.datetime(2023, 4, 20, 20, 42, tzinfo=pytz.timezone('Europe/Berlin')), "Perşembe"),
]

def get_iftar_time():
    now = datetime.datetime.now(tz=pytz.timezone('Europe/Berlin'))
    for iftar_time, day in iftar_times:
        if iftar_time > now:
            time_left = iftar_time - now
            time_left = time_left - datetime.timedelta(hours=2, minutes=7)
            return f"Kraliçemin karnının doymasına {(time_left.seconds // 3600)+1} saat, {(time_left.seconds // 60) % 60} dakika kaldı."
    return "Kraliçemin karnı doydu :)"

def iftar(update, context):
    message = get_iftar_time()
    context.bot.send_message(chat_id=update.message.chat_id, text=message, reply_to_message_id=update.message.message_id)

def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(telegram.ext.CommandHandler('iftar', iftar))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
