import os
from dotenv import load_dotenv
# from dotenv import dotenv_values

load_dotenv()
# TOKEN = dotenv_values()['TOKEN']

BOT_TOKEN = str(os.getenv('TOKEN'))

# admins_id = os.getenv('ADMIN_ID')
admins_id = [
    "283245864",
]

CACHE_PATH = 'local_storage'

# STYLE_IMG_PATH = r'local_storage\style.jpg'
# CONTEXT_IMG_PATH = r'local_storage\context.jpg'
# OUTPUT_PATH = r'local_storage\output.jpg'
