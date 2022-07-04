import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "bot whm")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "qq8qq")
ALIVE_NAME = getenv("ALIVE_NAME", "iamwhm")
BOT_USERNAME = getenv("BOT_USERNAME", "mus1whmbot")
BOT_PHOTO = getenv("BOT_PHOTO", "https://telegra.ph/file/e9258f1ae714616d2cdbb.jpg")
MONGODB_URL = getenv("MONGODB_URL")
DEV_NAME = getenv("DEV_NAME")
DEV_PHOTO = getenv("DEV_PHOTO")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "uui9uGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "uui9u")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/pqnzbmmwQ92/ll")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
