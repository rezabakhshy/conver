import random
import os
from pyrogram import Client, filters
from PIL import Image


api_id = 12721742 
api_hash="2a81674bd5e1ccbaed8c07f898d614ca"
token = '5121373236:AAEYdCgi0-WBX9bnA-tfY1sTNwmsmdoc6Mo'

bot = Client('Session_Name', api_id, api_hash, bot_token=token, workers = 4 )


bot.set_parse_mode('md')
@bot.on_message(filters.command("start",'/'))
def start_messgae(c, m):
    m.reply_text("helo")

@bot.on_message(filters.photo)
def photo_convert(c, m):
    rand_id = random.randint(100,900) # generate random number between 100 to 900
    m.download(f"{m.chat.id}-{rand_id}.jpg")
    img = Image.open(f'downloads/{m.chat.id}-{rand_id}.jpg')
    img.save(f"{m.chat.id}-{rand_id}.png","PNG")
    m.reply_document(f"{m.chat.id}-{rand_id}.png")
    os.remove(f"{m.chat.id}-{rand_id}.png")
    os.remove(f'downloads/{m.chat.id}-{rand_id}.jpg')

@bot.on_message(filters.sticker)
def conver_webp(c, m):
    rand_id = random.randint(100,900) # generate random number between 100 to 900
    if (m.sticker.is_animated) == False:
        m.download(f"{m.chat.id}-{rand_id}.webp")
        img = Image.open(f'downloads/{m.chat.id}-{rand_id}.webp').convert("RGBA")
        img.save(f"{m.chat.id}-{rand_id}.png","PNG")
        m.reply_photo(f"{m.chat.id}-{rand_id}.png")
        m.reply_document(f"{m.chat.id}-{rand_id}.png")
        os.remove(f"{m.chat.id}-{rand_id}.png")
        os.remove(f'downloads/{m.chat.id}-{rand_id}.webp')
    if m.sticker.is_animated == True:

        m.download(f"{m.chat.id}-{rand_id}.tgs")
        os.system(f"lottie_convert.py downloads/{m.chat.id}-{rand_id}.tgs {m.chat.id}-{rand_id}.gif")
        m.reply_animation(f"{m.chat.id}-{rand_id}.gif")

        os.remove(f"{m.chat.id}-{rand_id}.gif")
        os.remove(f'downloads/{m.chat.id}-{rand_id}.tgs')

bot.run()
