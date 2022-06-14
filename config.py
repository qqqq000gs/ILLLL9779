import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABHVBgNJ2DR6MM-fM6zDgq0GQXgluBsBbt7poa0Ew9c0kl52fkSPEb8kAfZolRyHvHWeafF3zqtSgu58yqtqQ5hSB4lXbjbfawx9RWkhTJe-qBn-35240Jt3k0NzHjcPZm0_mzfW9R8-Pcf4p4inA-Pu1_LoWXWBmlblvWQy5b0hfOhf3dAzlJ9cOPfKrEFbJMAWcty7Gh4LRwHrK5p14D9Uzo0LcBHw2qGHk1YPiSRDFVivp4nC9_JnQG6VkijEu9M-Hje8-Ydj3WRlZ8NnrK28CziywC8a9LvoVe-TXdD8Lo-LqByzlJqKpJ6SmmuvWO_PnTwT3NmFOA6cxLQCbb1AAAAAS1pE6QA")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "%100/𝑀𝑈𝑆𝐼𝐶 📀💯")
API_ID = int(getenv("API_ID", "15014116")
API_HASH = int(getenv("API_HASH", "ef9cf3efefc21e0d87696366a3f9431d")
OWNER_NAME = getenv("OWNER_NAME", "TTTLL0")
ALIVE_NAME = getenv("ALIVE_NAME", "محمد")
BOT_USERNAME = getenv("BOT_USERNAME", "Alkzsjekbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MUSIC100E")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "eithonsupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EITHON1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5302507827").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DevWaham/musvideostream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
