import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Mig, Mig2, Mig3, Mig4, Mig5, Mig6, Mig7, Mig8, Mig9, Mig10, ALIVE_PIC, OWNER_ID
from KeshavXSpam.plugins.help import *


MIG_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/a54c5f1aca50619d3374f.jpg"

Mig_Button = [
        [
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/@BTS_CHAT_ZONE")
        ],
        [
        Button.inline("⚡ ᴄᴏᴍᴍᴀɴᴅs ⚡", data="help_back")
        ]
        ]
               
MigX_Button = [
        [
        Button.url("✨ ᴀᴄᴄᴏᴜɴᴛ ✨", "https://t.me/NotReallyAlpha"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/BTS_CHAT_ZONE")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://github.com/theend-alpha/KeshavXBotSpam")
        ]
        ]
        
        
#USERS 


@Mig.on(events.NewMessage(pattern="/start"))
@Mig2.on(events.NewMessage(pattern="/start"))
@Mig3.on(events.NewMessage(pattern="/start"))
@Mig4.on(events.NewMessage(pattern="/start"))
@Mig5.on(events.NewMessage(pattern="/start"))
@Mig6.on(events.NewMessage(pattern="/start"))
@Mig7.on(events.NewMessage(pattern="/start"))
@Mig7.on(events.NewMessage(pattern="/start"))
@Mig8.on(events.NewMessage(pattern="/start"))
@Mig9.on(events.NewMessage(pattern="/start"))
@Mig10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       MigBot = await event.client.get_me()
       bot_name = MigBot.first_name
       bot_id = MigBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheMighty = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       ownermsg = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
       usermsg = f"**Hello !! [{firstname}](tg://user?id={userid})\nNice To Meet You, Well I Am [{bot_name}](tg://user?id={bot_id}), A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Given Below.** \n\n**Powered By : [𝙆𝙀𝙎𝙃𝘼𝙑 𝙓 𝙎𝙥𝙖𝙢](https://t.me/BTS_CHAT_ZONE)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheMighty,
                  MIG_IMG,
                  caption=ownermsg, 
                  buttons=Mig_Button)
       else:
            await event.client.send_file(TheMighty,
                  MIG_IMG,
                  caption=usermsg, 
                  buttons=MigX_Button)
                

