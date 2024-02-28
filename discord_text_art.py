from flask import Flask
from threading import Thread
import discord
import numpy as np
from PIL import Image
import io
from dotenv import load_dotenv
import os

# 加載環境變量
load_dotenv()

# Discord Bot 部分
discord_token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)
<<<<<<< HEAD
# ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

ASCII_CHARS = ["█", "▓", "@","G","8","L", "*", "+", ";", ":", ",", " "]
=======

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
>>>>>>> 7d1b735b66fd179085a74fd29113531d45575e68

# ASCII_CHARS = ["█", "▓", "@","G","8","L", "*", "+", ";", ":", ",", " "]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    width = 400  # 設定預設寬度為400

    if 'width=' in message.content:
        try:
            width_str = message.content.split('width=')[1].split()[0]
            width = int(width_str)
        except (IndexError, ValueError):
            await message.channel.send("無效的寬度值，使用預設值400。")

    if message.attachments:
        attachment = message.attachments[0]
        if any(attachment.filename.lower().endswith(ext) for ext in ['png', 'jpg', 'jpeg', 'gif']):
            await message.channel.send("圖片已接收，正在處理...")

            image_bytes = await attachment.read()
            img = Image.open(io.BytesIO(image_bytes)).convert('L')

            original_width, original_height = img.size
            ratio = original_height / original_width
            new_height = int(width * ratio)
            img = img.resize((width, new_height))

            pixels = np.array(img)
            normalized_pixels = pixels / 255
            ascii_pixels = (normalized_pixels * (len(ASCII_CHARS) - 1)).astype(int)
            ascii_image = [" ".join([ASCII_CHARS[pixel] for pixel in row]) for row in ascii_pixels]
            ascii_image_text = "\n".join(ascii_image)

            with open('text_art.txt', 'w') as file:
                file.write(ascii_image_text)

            await message.channel.send(file=discord.File('text_art.txt'))

# Flask Web Server 部分
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

if __name__ == "__main__":
    keep_alive()  # 啟動 Flask server
    client.run(discord_token)  # 啟動 Discord bot
