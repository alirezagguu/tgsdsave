import os
os.system('pip install pyrogram')
os.system('pip install TgCrypto')
os.system('pip install pyromod')
from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import Message


@Client.on_message(filters.photo | filters.video)
async def tsave(client,message):
  if message.photo:
    if message.photo.ttl_seconds :
      x = message.from_user.first_name
      name =  str(message.id) + '.jpg'
      a = await message.download(file_name=name)
      await client.send_photo('me', photo=a, caption=f'useriD:{message.chat.id}\nUsername:@{message.chat.username}\nname:{message.chat.first_name}')
      os.remove(f'downloads/{name}')
    else:pass
  elif message.video:
    if message.video.ttl_seconds :
      x = message.from_user.first_name
      name =  str(message.id) + '.mp4'
      a = await message.download(file_name=name)
      await client.send_vidoe('me', video=a, caption=f'useriD:{message.chat.id}\nUsername:@{message.chat.username}\nname:{message.chat.first_name}')
      os.remove(f'downloads/{name}')
    else:pass

@Client.on_message(filters.me)
async def ctsave(client,message):
  print(message.reply_to_message)
  if message.reply_to_message.photo:
    if message.reply_to_message.photo.ttl_seconds:
      x = message.from_user.first_name
      name =  str(message.id) + '.jpg'
      a = await message.reply_to_message.download(file_name=name)
      await client.send_photo('me', photo=a, caption=f'useriD:{message.reply_to_message.chat.id}\nUsername:@{message.reply_to_message.chat.username}\nname:{message.reply_to_message.chat.first_name}')
      os.remove(f'downloads/{name}')
    else:pass
  elif message.reply_to_message.video:
    if message.reply_to_message.video.ttl_seconds :
      x = message.from_user.first_name
      name =  str(message.id) + '.mp4'
      a = await message.reply_to_message.download(file_name=name)
      await client.send_video('me', video=a, caption=f'useriD:{message.reply_to_message.chat.id}\nUsername:@{message.reply_to_message.chat.username}\nname:{message.reply_to_message.chat.first_name}')
      os.remove(f'downloads/{name}')
    else:pass
  



bot = Client(
    name="Uploader",
    plugins = plugin,
    api_id = '27190869',
    api_hash = '8073198f096c675d6bc114c104f9a03b',
    )


bot.run()
