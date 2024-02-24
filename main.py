import asyncio

from bot.loader import main
from bot.utils.logger import logger



if __name__ == "__main__":
    logger.info("Starting bot...")
    asyncio.run(main())
    logger.info("Stopping bot...")
