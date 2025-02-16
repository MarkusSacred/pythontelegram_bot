from typing import Final
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

TOKEN : Final = "8038816092:AAH4P4-KS33BU8hVAQwpjkGbFka49o_QN0M"

###
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
start_route, end_route = range(2)
ONE, TWO = range(2)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    
    await query.answer()
    
    callback_data = query.data
    print(f"Callback data received: {callback_data}")

async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.edit_text(chat_id=update.effective_chat.id, text="testing route")
    return start_route
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(start_handler)
    
    application.run_polling()