from DEADLYSPAM import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from DEADLYSPAM import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/0fc760cb0777ea04b7dfe.jpg"

DEAD_Help = "🔥 𝗗𝗛𝗜𝗠𝗔𝗡 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧🔥\n\n"
 
DEAD_Help += f"__𝗖𝗠𝗗𝗦 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗜𝗡 𝗗𝗛𝗜𝗠𝗔𝗡 𝗕𝗢𝗧__\n\n"

DEAD_Help += f" ↧ 𝗦𝗣𝗔𝗠𝗕𝗢𝗧 𝗖𝗠𝗗𝗦 ↧\n\n"

DEAD_Help += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n\n"
 
DEAD_Help += f" ↧ 𝗟𝗘𝗔𝗩𝗘 𝗖𝗠𝗗 ↧\n\n"

DEAD_Help += f" `!leave` - to leave public/private channel/groups\n\n"
 
DEAD_Help += f" ↧ 𝗦𝗣𝗔𝗠 𝗖𝗠𝗗𝗦 ↧\n\n"

DEAD_Help += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!bspam` - this cmd use for spamming on someone birthday!!\n `!delayspam` - this cmd use for delay spam\n\n"

DEAD_Help += f" !pornspam - 𝗜 𝗪𝗜𝗟𝗟 𝗦𝗨𝗚𝗚𝗘𝗦𝗧 𝗗𝗢𝗡'𝗧 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 🥵😂 ↧\n\n"

DEAD_Help += f"© @i_dxlvir\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DEAD_Help,
                                  buttons=[
        [
        Button.url("🌼 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 🌼", "https://t.me/Dhiman_Feelings"),
        Button.url("🌼 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🌼", "https://t.me/CHATTING_GRUP001")
        ] 
        ]
        )
