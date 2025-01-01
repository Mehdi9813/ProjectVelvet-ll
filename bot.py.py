from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# توکن API بات تلگرام
TOKEN = "7842366836:AAFxrMQAVlHk6jXR5-eiE7buqJHkWYjPp94"

# چت آیدی‌های شما
CHAT_IDS = [7853304554, 5793439133]  # جای اعداد را با چت‌آیدی واقعی خودتان جایگزین کنید

# تابع برای ارسال پیام‌های دریافتی به چت آیدی‌ها
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    sender_id = update.effective_chat.id
    for chat_id in CHAT_IDS:
        await context.bot.send_message(chat_id=chat_id, text=f"From {sender_id}: {message_text}")

if __name__ == "__main__":
    # ساخت اپلیکیشن
    app = Application.builder().token(TOKEN).build()

    # افزودن هندلر پیام‌ها
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    # اجرای بات
    print("بات در حال اجرا است...")
    app.run_polling()

