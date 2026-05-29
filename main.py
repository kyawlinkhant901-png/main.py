import os
import telebot
import google.generativeai as genai
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

# Render Free Tier Error မတက်အောင် Dummy Web Server ဆောက်ခြင်း
class DummyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), DummyServer)
    print(f"Starting dummy server on port {port}")
    server.serve_forever()

# Tokens Setup
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခေတ္တအဆင်မပြေဖြစ်နေပါသည်။ ခဏနေမှ ပြန်ကြိုးစားကြည့်ပါ။")

if __name__ == "__main__":
    # Web Server ကို နောက်ကွယ်ကနေ Thread နဲ့ Run ထားခြင်း
    Thread(target=run_server, daemon=True).start()
    
    print("AI Bot စတင်လည်ပတ်နေပါပြီ...")
    bot.infinity_polling()
