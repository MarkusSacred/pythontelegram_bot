from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ConversationHandler,
    filters, CallbackContext
)

TOKEN = "8038816092:AAH4P4-KS33BU8hVAQwpjkGbFka49o_QN0M"  # Replace with your actual bot token

# Defining conversation states
START_ROUTE, END_ROUTE = range(2)

async def start_route(update: Update, context: CallbackContext) -> int:
    """Handles the /start_route command and moves to the next step."""
    reply_keyboard = [["End Route"]]

    await update.message.reply_text(
        "🚀 Route started! Click 'End Route' when you are done.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return END_ROUTE  # Move to END_ROUTE state

async def end_route(update: Update, context: CallbackContext) -> int:
    """Handles the 'End Route' action and ends the conversation."""
    await update.message.reply_text(
        "✅ Route ended! Thank you for using our service.",
        reply_markup=ReplyKeyboardRemove()  # Remove the keyboard
    )
    return ConversationHandler.END  # End the conversation

async def cancel(update: Update, context: CallbackContext) -> int:
    """Handles user cancellation of the route."""
    await update.message.reply_text(
        "❌ Route process canceled.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END  # End the conversation

def main():
    """Main function to run the bot."""
    app = Application.builder().token(TOKEN).build()

    # Conversation handler with states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start_route", start_route)],
        states={
            END_ROUTE: [
                MessageHandler(filters.TEXT & filters.Regex("^End Route$"), end_route)
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(conv_handler)

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
