import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReactionTypeEmoji

MAIN_TOKEN = os.getenv("MAIN_BOT_TOKEN")
WORKER_TOKENS = os.getenv("WORKER_TOKENS", "").split(",")
EMOJIS = ["👍", "❤️", "🔥", "🥰", "👏", "⚡️", "🎉", "🤩"]

main_bot = Bot(token=MAIN_TOKEN)
worker_bots = [Bot(token=t.strip()) for t in WORKER_TOKENS if t.strip()]
dp = Dispatcher()

@dp.channel_post()
async def auto_reaction(message: Message):
    for i, w_bot in enumerate(worker_bots):
        try:
            emoji = EMOJIS[i % len(EMOJIS)]
            await w_bot.set_message_reaction(
                chat_id=message.chat.id,
                message_id=message.message_id,
                reaction=[ReactionTypeEmoji(emoji=emoji)]
            )
            await asyncio.sleep(0.4)
        except Exception as e:
            print(f"Xatolik: {e}")

async def main():
    await dp.start_polling(main_bot)

if __name__ == "__main__":
    asyncio.run(main())
