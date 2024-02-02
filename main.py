from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, Application
from .handlers import start, handle_message
from .config import T_TOKEN

def main():
    print('Starting bot...')
    app = Application.builder().token(T_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print('Polling...')
    app.run_polling()

if __name__ == '__main__':
    main()
