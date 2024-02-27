from sqlalchemy import create_engine

from bot.utils.files import config
from bot.data.models import Base


DATABASE_URL = config.get('database', {}).get('url', None)

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={'check_same_thread': False}
)

Base.metadata.create_all(engine)
