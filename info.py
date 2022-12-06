import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/6eda2868f11d2aa9d15da.jpg https://telegra.ph/file/409aa76ac48880b9ec372.jpg https://telegra.ph/file/1022ba35bd04684c735df.jpg https://telegra.ph/file/632353e2a60a8d9328f36.jpg https://telegra.ph/file/28162937f118c21da7fd2.jpg https://telegra.ph/file/e98ca270a4eb16e6d6f1a.jpg https://telegra.ph/file/3a4e24e3944d43694c2f1.jpg https://telegra.ph/file/8970b25968f5a7d55362a.jpg https://telegra.ph/file/8b1667c39b2f7ae3a098a.jpg https://telegra.ph/file/7b706f5799bfbe41d82c9.jpg https://telegra.ph/file/91baef50b7e09f2b98142.jpg https://telegra.ph/file/0b94e55c42932a36cddc8.jpg https://telegra.ph/file/ba5a1c44b0b539a3833f3.jpg https://telegra.ph/file/2f1784d624257dfc90e98.jpg https://telegra.ph/file/37efe917cf40145922696.jpg https://telegra.ph/file/fe2431b2a026c109cd2a7.jpg https://telegra.ph/file/cfd65f4df4d8c988d8028.jpg https://telegra.ph/file/3942e343b15d1558ab142.jpg https://telegra.ph/file/d953c8b31ae4366a13a39.jpg https://telegra.ph/file/9b738654f8ffe5aeba5f7.jpg https://telegra.ph/file/c4183bbf4e253d7b22579.jpg https://telegra.ph/file/fefb5ae913ae4aed64137.jpg https://telegra.ph/file/a7fc7fa687ee022ed853e.jpg https://telegra.ph/file/e652c917207d0096a64ac.jpg https://telegra.ph/file/dd5bb926ed38d991770e3.jpg https://telegra.ph/file/60ed0dd471f7e62df3ed9.jpg https://telegra.ph/file/2aa37a2aa5b6e91c619f4.jpg https://telegra.ph/file/d89451497b91db3972f79.jpg https://telegra.ph/file/91ea6b58ab3dce3406d8e.jpg https://telegra.ph/file/e6194badfbb89e6e34977.jpg https://telegra.ph/file/ca9d050d8caa895199ed4.jpg https://telegra.ph/file/5a8d1dead0a522c4cab95.jpg https://telegra.ph/file/4d840087dc3a1e1d08b2c.jpg https://telegra.ph/file/6b58c4cbf5ff676ebbf31.jpg https://telegra.ph/file/17c984fef5547480abaa1.jpg https://telegra.ph/file/ed7852ce049575456c262.jpg https://telegra.ph/file/7d3401b366294fbee7dc7.jpg https://telegra.ph/file/9584e2a6ad0fb85006c3e.jpg https://telegra.ph/file/817723926d8e6a028623c.jpg https://telegra.ph/file/692361ddff2cc85f71182.jpg https://telegra.ph/file/d288630be65014ae293f1.jpg https://telegra.ph/file/3e6f90722fb639709e37a.jpg https://telegra.ph/file/1e8633bd9a318bef75e49.jpg https://telegra.ph/file/8590d0a73058f82c22049.jpg https://telegra.ph/file/df286811e189329c61254.jpg https://telegra.ph/file/cf9113c9b9dc616451b0b.jpg https://telegra.ph/file/ea61cda17be942070dda7.jpg https://telegra.ph/file/4879e36e11b66215a239c.jpg https://telegra.ph/file/88b2b9700eb774780c5d1.jpg https://telegra.ph/file/91510496cd1ffb941f329.jpg https://telegra.ph/file/7b9a03a3a72f1d8780f1c.jpg https://telegra.ph/file/e3599923acd2f86509ecc.jpg https://telegra.ph/file/5cd62f0a282870639c704.jpg https://telegra.ph/file/b2f835904130fa125fdc3.jpg https://telegra.ph/file/347e209d961ad14dd1c51.jpg https://telegra.ph/file/854cdc547322b546e2129.jpg https://telegra.ph/file/17ad25f60b96cf1d80d04.jpg https://telegra.ph/file/c5d2ee2aa9b2bbe594cf7.jpg https://telegra.ph/file/1f00154e78820b4fda62c.jpg https://telegra.ph/file/d1b90d76bcfcf7277f578.jpg https://telegra.ph/file/3ea2fba441ace45444a53.jpg https://telegra.ph/file/28d03232faa332fa15238.jpg https://telegra.ph/file/c0db9f899d973867e1395.jpg https://telegra.ph/file/18c305bc3528cc52ed5df.jpg https://telegra.ph/file/1ee6fcd8f2eb9e31aabf0.jpg https://telegra.ph/file/53464697438a8aefd010a.jpg https://telegra.ph/file/0a48b3f02954d7c555baf.jpg https://telegra.ph/file/d4b4410710d086282ed17.jpg https://telegra.ph/file/20670f2affe74b8d6177a.jpg https://telegra.ph/file/ddd65bc309d1c5b5bad24.jpg https://telegra.ph/file/7db7539e75add09ce4d33.jpg https://telegra.ph/file/9dcb00c545207e2c75a8e.jpg https://telegra.ph/file/9458df790caf55b9338fe.jpg https://telegra.ph/file/019d114f7749c5d5f332f.jpg https://telegra.ph/file/0ab0858f54b4d4c9c59be.jpg https://telegra.ph/file/9f229638268196beac3c8.jpg https://telegra.ph/file/547b7a36e37f8ecc0b6d9.jpg https://telegra.ph/file/9d4d17d9aeb1fd3ac31a8.jpg https://telegra.ph/file/0a8fae35e63b8b67d7538.jpg https://telegra.ph/file/c4761a91947fb9fe3bf21.jpg https://telegra.ph/file/64c1dd202f0e2cdc4fb25.jpg https://telegra.ph/file/fdd899f8d65c278ac5ffe.jpg https://telegra.ph/file/fb0dec3b95f1d71e38f74.jpg https://telegra.ph/file/ac30018500437192e7979.jpg https://telegra.ph/file/bf8f60ee601a5f5dbe508.jpg https://telegra.ph/file/570b9488a925baf24574e.jpg https://telegra.ph/file/efe50ddafa6d5c2b5db16.jpg https://telegra.ph/file/a59da5faa8e0d47ac98ea.jpg https://telegra.ph/file/24c30b5577fd0ccfbe0d0.jpg https://telegra.ph/file/b3f63db70b525d5de4a31.jpg https://telegra.ph/file/3eb765b452f628d6cb653.jpg https://telegra.ph/file/1842d5ee8437a4faff9b8.jpg https://telegra.ph/file/d34569405868b6d7e4b2d.jpg https://telegra.ph/file/798cf6f8fca9ac5fab355.jpg https://telegra.ph/file/e2f3869ee620145a69c69.jpg https://telegra.ph/file/43dfa4504611fcfc9b6f8.jpg https://telegra.ph/file/e7df0a5fb705e65988a68.jpg https://telegra.ph/file/075e528e8cccb35aeb3e2.jpg https://telegra.ph/file/1b79f0df8f7d1340a3e3e.jpg https://telegra.ph/file/9a8ca3e8669d94ecfed8c.jpg https://telegra.ph/file/c1ac4c8c3f98f4fdcdc15.jpg https://telegra.ph/file/4326c264ace2262182119.jpg https://telegra.ph/file/ec00168905c5fdbf71674.jpg https://telegra.ph/file/1a7f33a68cd61bc1ece3c.jpg https://telegra.ph/file/de36738b17d5dc1d0292f.jpg https://telegra.ph/file/dc460b5d50f84c6a3cc66.jpg https://telegra.ph/file/990256fc14e3bf0bf1022.jpg https://telegra.ph/file/74e948444db4a6b9b067d.jpg https://telegra.ph/file/fe6993d39bb4257c71b47.jpg https://telegra.ph/file/22144e4e4c67ee38349d2.jpg https://telegra.ph/file/5d1306fd7bf864fabbaa9.jpg https://telegra.ph/file/ede47fd6cefef0492ffbb.jpg https://telegra.ph/file/e9d76f491c98f039eab4d.jpg https://telegra.ph/file/a71759472d8b95cbc4b43.jpg https://telegra.ph/file/750bc67b0a2b09c77750c.jpg https://telegra.ph/file/e8afcec4fa1731e0c007b.jpg https://telegra.ph/file/72e9932d4d5b469fca336.jpg')).split()
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/184b20d763e972f493bc0.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/SECL4u')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/SECLK')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001514899549'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/SECL4u')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🪄 𝚀𝚞𝚎𝚛𝚢 ➠ {query}</b>\n\n <b>𝚃𝚒𝚝𝚕𝚎 ➠ <a href={url}>{title}</a><b>({year})</b>\n <b>{release_date} • {runtime}min</b> \n\n <b>𝙶𝚎𝚗𝚛𝚎 ➠ {genres}</b> \n <b>𝚁𝚊𝚝𝚒𝚗𝚐 ⭐️ ➠ {rating}/10 ({votes})</b> \n <b>𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎 ➠ {languages}</b> \n\n <b>©️ sᴇᴄ ʙᴏᴛs(https://t.me/SECLK)</b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", '15')
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
