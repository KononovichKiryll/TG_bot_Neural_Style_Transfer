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
