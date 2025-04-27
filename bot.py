
import telebot
import time

TOKEN = "ضع التوكن الخاص بك هنا"
CHANNEL_ID = "@ضع_اسم_قناتك_هنا"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحباً بك في BoltX - إشارات التداول الفورية! ⚡")

def send_signal():
    text = "⚡ إشارة جديدة!

زوج: EUR/USD
الاتجاه: صعود 🔼
مدة الصفقة: 5 دقائق ⏳

✅ التزم بإدارة رأس المال.
دعاء: (اللهم وفقنا لما تحب وترضى)"
    bot.send_message(CHANNEL_ID, text)

while True:
    # إرسال إشارة كل فترة (مثلاً كل 2 ساعة)
    send_signal()
    time.sleep(7200)  # 2 ساعة
