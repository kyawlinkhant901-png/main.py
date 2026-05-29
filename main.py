import telebot
import google.generativeai as genai

# မိမိရရှိထားသော Token များ ထည့်ရန်နေရာ
TELEGRAM_TOKEN = "မင်းရဲ့_TELEGRAM_BOT_TOKEN_ကိုဒီမှာထည့်ပါ"
GEMINI_API_KEY = "မင်းရဲ့_GEMINI_API_KEY_ကိုဒီမှာထည့်ပါ"

# AI Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Telegram Bot Setup
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # AI ထံမှ အဖြေတောင်းခြင်း
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခေတ္တအဆင်မပြေဖြစ်နေပါသည်။ ခဏနေမှ ပြန်ကြိုးစားကြည့်ပါ။")

print("AI Bot စတင်လည်ပတ်နေပါပြီ...")
bot.infinity_polling()
