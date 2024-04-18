
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("36ab9aae4dfc711daf2158f1209c8ce9", "")
API_ID = int(getenv("27276217", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001649838443]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "") or 0)
BOT_VER = "0.1.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "VenomOwners")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("-4126051610", "Venom_Chatz")
HEROKU_API_KEY = getenv("HRKU-37ea5a6f-4726-4a9e-b42a-eb0185becf25", None)
HEROKU_APP_NAME = getenv("userbotsmolarek", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", "https://te.legra.ph/file/0b373de1c657129297c39.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/venombolteop/VenomX")
STRING_SESSION1 = getenv("BAGgM7kAr_vlhBZx1DFNK7H0RCUqUsVc72QDoF4tv3BiBpDCuVXyT4MUfbbOV_SOfAnX0XhuJjVWwetenL5AWJtjJZgznAomk5qLa7feY70q-8aSdJTWrMuGeUOdXHBhw8RXJTwS0h1hG49Cs1LO2Io7Tb98kZ_LTjmcmzWIBp5ncVwzHly2ajNr4KiZzVrgWB30xaYrdmelgGUmk4R4ilzDD9wb78-YeNIfc6-8KVWlypDDttplbolJ7bSj6a7um-tjHdsH0rh5DU4plZk57LinMWcBhayiwGEBLAcDwmfPoZ1PPZe9aRIk_7AWxElw5QGlSPIxgum9yZ535FKOvZ03tP9muQAAAAGiwNAVAA", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5822700831").split()))
