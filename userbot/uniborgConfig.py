import os
from telethon.tl.types import ChatBannedRights
ENV = bool(os.environ.get("ENV", False))

class Var(object):
        APP_ID = int(os.environ.get("APP_ID", 6))
        API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
        ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
        TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
        TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", None)
    
class Development(Var):
    LOGGER = True
    # Here for later purposes
if ENV:
    import os
    class Config(object):
        LOGGER = True
        # Get this value from my.telegram.org! Please do not steal
        LOCATION = os.environ.get("LOCATION", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
        # Get your own API KEY from remove.bg
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Send .get_id in any group to fill this value.
        PRIVATE_GROUP_BOT_ID = int(os.environ.get("PRIVATE_GROUP_BOT_ID", -1001221744590))
        # To get the new in your channel or group
        NEWS_CHANNEL_ID = os.environ.get("NEWS_CHANNEL_ID", None)
        # Send .get_id in any channel to fill this value. ReQuired for @Manuel15 inspiration to work!
        PRIVATE_CHANNEL_BOT_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_ID", -1001221744590))
        # for Tag notifications 
        TAG_ALERT = os.environ.get("TAG_ALERT", "DISABLE")
        # This is required for the plugins involving the file system.
        TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
        # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
        IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
        IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        # This is required for the hash to torrent file functionality to work.
        HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
        # This is required for the @telegraph functionality.
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "TamilBot")
        # Get a Free API Key from OCR.Space
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        # Send .get_id in any group with all your administration bots (added)
        G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001221744590))
        # TG API limit. An album can have atmost 10 media!
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # Telegram BOT Token from @BotFather
        TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
        TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", None)
        #
        #
        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
        MAX_MESSAGE_SIZE_LIMIT = 4095
        # set blacklist_chats where you do not want userbot's features
        UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
        # maximum number of messages for antiflood
        MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None,
            view_messages=None,
            send_messages=True
        )
        # chat ids or usernames, it is recommended to use chat ids,
        # providing usernames means an additional overhead for the user
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs.
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
        # define "spam" in PMs
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
        NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
        # send .get_id in any channel to forward all your NEW PMs to this group
        PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
        if PM_LOGGR_BOT_API_ID:
            PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
        # For Databases
        # can be None in which case plugins requiring
        # DataBase would not work
        DB_URI = os.environ.get("DATABASE_URL", None)
        # number of rows of buttons to be displayed in .helpme command
        NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 4))
        # specify command handler that should be used for the plugins
        # this should be a valid "regex" pattern
        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        # VeryStream only supports video formats
        VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
        VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
        GROUP_REG_SED_EX_BOT_S = os.environ.get("GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot")
        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        #Google Chrome Stuff
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
        # Google Drive ()
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
        if AUTH_TOKEN_DATA != None:
            os.makedirs(TMP_DOWNLOAD_DIRECTORY)
            t_file = open(TMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
            t_file.write(AUTH_TOKEN_DATA)
            t_file.close()
        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        JTM_CHANNEL_ID = int(os.environ.get("JTM_CHANNEL_ID", False))
        JTM_CHANNEL_USERNAME = os.environ.get("JTM_CHANNEL_USERNAME", None)
        #MongoDB
        MONGO_URI = os.environ.get("MONGO_URI", None)
        # PMPERMITMENU
        MAX_SPAM = int(os.environ.get("MAX_SPAM", 6))
        #Lydia API
        LYDIA_API = os.environ.get("LYDIA_API",None)
        PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", False))
        ALIVE_IMAGE = os.environ.get("ALIVE_IMAGE", "https://telegra.ph/file/2efb41858c95ebd7231e8.jpg")
        # PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", None))
        SUB_TO_MSG_ASSISTANT = os.environ.get("SUB_TO_MSG_ASSISTANT", False)
        ASSISTANT_START_PIC = os.environ.get(
            "ASSISTANT_START_PIC",
            "https://telegra.ph/file/84d536b464a2ca6962416.mp4",
        )
        
else:
    class Config(object):
        DB_URI = None
        # Add your UniBorg Vars Here
