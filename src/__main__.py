import asyncio

from config import settings
from src.bot import Orion


async def main() -> None:
    bot = Orion()
    await bot.start(settings.BOT_TOKEN)


try:
    asyncio.run(main())

except KeyboardInterrupt:
    print("Shutting down...")
