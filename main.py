import telebot
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8603889920:AAFCNmy5wkMq4Okj5I1_VChkU3VRPjqV-jo")
bot = telebot.TeleBot(TOKEN)

# Обработчик новых участников
@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    for user in message.new_chat_members:
        text = f"""
❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️
🎉 **Приветствуем, {user.first_name}!** 🎉

Вы вступили в **Snow❄️Moscow🇷🇺RP** на сервере **Emergency Hamburg**!

💬 *Погружайтесь в атмосферу RP и не забывайте про правила:*

─────────────────────────
📌 **Советы новичкам:**
1️⃣ Представляйтесь в RP-чате.
2️⃣ Старайтесь сохранять атмосферу RP.
3️⃣ Следите за правилами сервера.
─────────────────────────

✨ Желаем вам крутых историй и незабываемого RP!  
❄️ Пусть ваше приключение начинается прямо сейчас! ❄️
❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️
"""
        # Отправляем сообщение с Markdown для жирного текста
        bot.send_message(message.chat.id, text, parse_mode='Markdown')

# Постоянно слушаем новые участники
if __name__ == "__main__":
    print("Бот запущен и слушает новых участников...")
    bot.polling(none_stop=True)