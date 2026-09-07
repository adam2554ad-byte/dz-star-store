import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_GROUP_ID = os.getenv("ADMIN_GROUP_ID")

if not TOKEN:
    print("Error: BOT_TOKEN is missing!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = (
        f"أهلاً بك يا {user_name} في بوت **DZ Star Store** للخدمات الرقمية! 🌟\n\n"
        "يمكنك من خلالنا طلب رصيد، شحن الألعاب، أو تبسيط معاملاتك بكل امن وسرعة.\n"
        "اختر ما تناسبك من الخدمات أدناه:"
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

print("Bot is running...")
bot.infinity_polling()
