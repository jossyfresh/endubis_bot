from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("8125507956:AAFS5f-Hq92hrURGnck5eALNR0KG_CXeBm4").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()