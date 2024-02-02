from openai import AsyncOpenAI
from .config import OPENAI_API_KEY

async_openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY) 

async def ask_chatgpt(question: str) -> str:
    try:
        chat_completion = await async_openai_client.chat.completions.create(
            messages=[{"role": "user", "content": question}],
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message['content']  # Adjust based on the API version and response format
    except Exception as e:
        return f"An error occurred: {str(e)}"