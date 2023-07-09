import os
from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = str(os.getenv('TG_BOT_TOKEN'))

ADMINS_ID = [
    "283245864",
]

CACHE_PATH = 'local_storage'
