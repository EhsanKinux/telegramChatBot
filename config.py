import os
from dotenv import load_dotenv

load_dotenv()

# telegram token
T_TOKEN = os.environ.get("TELEGRAM_TOKEN")
BOT_USERNAME = '@osFinalProject_bot'

# OpenAI API key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")