import os

API_ID = API_ID = 26451206

API_HASH = os.environ.get("API_HASH", "32984406271d6f3945bb536671b143a7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7270419558:AAFl_wPWcKB053DqfyMjEgrOq1BxqqKjkNk")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6830450483))

LOG = -1002192999464

try:
    ADMINS=[6830450483]
    for x in (os.environ.get("ADMINS", "6830450483").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


