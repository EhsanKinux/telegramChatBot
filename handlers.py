from telegram import Update
import asyncio
from .openai_utils import ask_chatgpt

attempt_counter = 0

async def start(update: Update, context):
    await update.message.reply_text('سلام! من یک ربات هستم. عدد بفرستید تا بشمارم یا متن برای پردازش توسط ChatGPT')

async def handle_message(update: Update, context):
    global attempt_counter
    text = update.message.text.strip()
    if text.isdigit():
        attempt_counter += 1  # Increment the attempt counter
        asyncio.create_task(count_numbers(update, context, int(text), attempt_counter))
    else:
        # Process non-numeric text with ChatGPT
        response = await ask_chatgpt(text)
        await update.message.reply_text(response)

async def count_numbers(update: Update, context, number: int, attempt_no: int):
    for i in range(number + 1):
        await asyncio.sleep(1)  # Non-blocking sleep
        message_text = f"Trying no.{attempt_no}: {i}"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)