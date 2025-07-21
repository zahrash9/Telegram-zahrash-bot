from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

TOKEN = os.environ['BOT_TOKEN']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! دستور بده مثلا: /random 100 تا برات عدد تصادفی بدم!")

async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        try:
            upper_limit = int(context.args[0])
            number = random.randint(1, upper_limit)
            await update.message.reply_text(f'عدد تصادفی بین 1 و {upper_limit}: {number}')
        except ValueError:
            await update.message.reply_text('لطفا یک عدد معتبر وارد کن.')
    else:
        await update.message.reply_text('مثال دستور: /random 100')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("random", random_number))

    print("Bot is running...")
    app.run_polling()
