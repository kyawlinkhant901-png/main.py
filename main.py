import os
import telebot
import google.generativeai as genai

# ကွန်ပျူတာစနစ် (Environment) ထဲကနေ လျှို့ဝှက်ဖတ်ခိုင်းမယ့်ပုံစံ ပြောင်းလဲခြင်း
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# AI Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Telegram Bot Setup
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခေတ္တအဆင်မပြေဖြစ်နေပါသည်။ ခဏနေမှ ပြန်ကြိုးစားကြည့်ပါ။")

print("AI Bot စတင်လည်ပတ်နေပါပြီ...")
bot.infinity_polling()
