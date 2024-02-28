import discord
import numpy as np
from PIL import Image
import io

from dotenv import load_dotenv
import os

# 加載當前目錄下的.env文件
load_dotenv()

# 現在你可以像之前一樣從環境變量中獲取DISCORD_TOKEN了
discord_token = os.getenv('DISCORD_TOKEN')


# 定義機器人的意圖
intents = discord.Intents.default()
intents.messages = True  # 如果您打算讓機器人讀取訊息
intents.message_content = True  # 啟用對訊息內容的訪問

client = discord.Client(intents=intents)

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]  # ASCII字符集

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 設定預設寬度為400
    width = 400

    # 檢查消息是否包含寬度設定
    if 'width=' in message.content:
        try:
            width_str = message.content.split('width=')[1].split()[0]  # 獲取寬度數值字符串
            width = int(width_str)  # 轉換為整數
        except (IndexError, ValueError):
            await message.channel.send("無效的寬度值，使用預設值400。")

    if message.attachments:
        attachment = message.attachments[0]  # 假設只處理第一個附件
        if any(attachment.filename.lower().endswith(ext) for ext in ['png', 'jpg', 'jpeg', 'gif']):
            await message.channel.send("圖片已接收，正在處理...")

            # 將圖片保存並打開
            image_bytes = await attachment.read()
            img = Image.open(io.BytesIO(image_bytes)).convert('L')  # 轉換為灰階

            # 調整圖片大小
            original_width, original_height = img.size
            ratio = original_height / original_width
            new_height = int(width * ratio)
            img = img.resize((width, new_height))

            # 轉換圖片為ASCII
            pixels = np.array(img)
            normalized_pixels = pixels / 255
            ascii_pixels = (normalized_pixels * (len(ASCII_CHARS) - 1)).astype(int)
            ascii_image = [" ".join([ASCII_CHARS[pixel] for pixel in row]) for row in ascii_pixels]
            ascii_image_text = "\n".join(ascii_image)

            # 將ASCII藝術保存到文件
            with open('text_art.txt', 'w') as file:
                file.write(ascii_image_text)

            # 將文件發送回Discord
            await message.channel.send(file=discord.File('text_art.txt'))


client.run(discord_token)

