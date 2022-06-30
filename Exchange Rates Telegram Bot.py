import requests
from datetime import datetime
import telebot

# Проверка ответа api
# result = requests.get('https://yobit.net/api/3/ticker/usd_rur')
# result = result.json()
# sell_price = result["usd_rur"]["sell"]
# buy_price = result["usd_rur"]["buy"]
# print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell USD price: {sell_price}\nBuy USD price: {buy_price}")

bot = telebot.TeleBot("Your bot token")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет. Напиши price и узнаешь курс доллара.")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                result = requests.get('https://yobit.net/api/3/ticker/usd_rur')
                result = result.json()
                sell_price = result["usd_rur"]["sell"]
                buy_price = result["usd_rur"]["buy"]
                bot.reply_to(message,f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\nSell USD price: {sell_price}\nBuy USD price: {buy_price}")

            except Exception as ex:
                print(ex)
                bot.reply_to(
                    message,
                    "Упс! Что то пошло не так..."
                )
        else:
            bot.reply_to(message, "Проверь запрос, нужно написать price.")

bot.infinity_polling()