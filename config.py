import os
import logging
from logging.handlers import RotatingFileHandler


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "2468192"))
API_HASH = os.environ.get("API_HASH", "4906b3f8f198ec0e24edb2c197677678")


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "100"))


OWNER_ID = int(os.environ.get("OWNER_ID", "2068233407"))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Filter01")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001683081282"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001910769204"))
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "2098589219 2068233407").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"

USER_REPLY_TEXT = "❌Dᴏɴ'ᴛ Sᴇɴᴅ Mᴇ Mᴇꜱꜱᴀɢᴇꜱ Dɪʀᴇᴄᴛʟʏ ɪ'ᴍ Oɴʟʏ Fɪʟᴇ Sʜᴀʀᴇ Bᴏᴛ ! \n \nRᴇQᴜᴇꜱᴛ Mᴏᴠɪᴇꜱ Hᴇʀᴇ: https://t.me/+x6OfRDdUPrUwZTZl"

START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ {mention} \n \nI Cᴀɴ Sᴛᴏʀᴇ Pʀɪᴠᴀᴛᴇ Fɪʟᴇꜱ Iɴ Sᴘᴇᴄɪꜰɪᴇᴅ Cʜᴀɴɴᴇʟ Aɴᴅ Oᴛʜᴇʀ Uꜱᴇʀꜱ Cᴀɴ Aᴄᴄᴇꜱꜱ Iᴛ Fʀᴏᴍ Sᴘᴇᴄɪᴀʟ Lɪɴᴋ. Tᴇᴀᴍ: @KR_Picture")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ನಮಸ್ಕಾರ {mention} 🙏  ,\n \nಚಲನಚಿತ್ರವನ್ನು ಪಡೆಯಲು 'JOIN CHANNEL' ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಚಾನಲ್‌ನಲ್ಲಿ ಸೇರಿಕೊಳ್ಳಿ.\n \n────── • ◆ • ───────\n \nYou Need to Join My Channel to Receive the Movie file. CLICK HERE 👇👇</b>")

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
