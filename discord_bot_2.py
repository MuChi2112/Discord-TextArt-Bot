from flask import Flask
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio
from PIL import Image
import aiohttp  # 引入 aiohttp 庫
import io
import os

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='/', intents=intents)

# ASCII 字符映射
ASCII_CHARS = ["█", "▓", "@", "G", "8", "L", "*", "+", ";", ":", ",", " "]

# 使用字典來管理每個用戶的寬度設置
user_widths = {}

async def convert_image_to_ascii(image, width):
    image = image.resize((width, int(width * image.height / image.width)))
    image = image.convert('L')
    pixels = image.getdata()
    ascii_str = ''.join(ASCII_CHARS[pixel//25] for pixel in pixels)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + '\n'
    return ascii_img

@bot.event
async def on_message(message):
    if message.content.startswith('/start-textart'):
        print("接收到start-textart")
        guild = message.guild
        user = message.author

        # 檢查私人頻道是否已存在
        for channel in guild.channels:
            if channel.name == f'private-{user.name}':
                await message.channel.send('私人頻道已經存在。')
                return

        # 創建身份組和私人頻道
        role = await guild.create_role(name=user.name)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            role: discord.PermissionOverwrite(read_messages=True)
        }
        private_channel = await guild.create_text_channel(f'private-{user.name}', overwrites=overwrites)
        await user.add_roles(role)

        # 設置 15 分鐘後關閉頻道的定時器
        await asyncio.sleep(900)  # 15 分鐘
        await private_channel.delete()
        await role.delete()

    elif message.content.startswith('/set width'):
        # 設置自定義寬度
        parts = message.content.split()
        if len(parts) == 3 and parts[2].isdigit():
            width = int(parts[2])
            user_widths[message.author.id] = width  # 使用作者的 ID 作為鍵來存儲寬度
            await message.channel.send(f'寬度已設定為 {width}。')
        else:
            await message.channel.send('請輸入有效的寬度值。')

    # 處理圖片消息並將其轉換為 ASCII 藝術
    if message.channel.name.startswith('private-') and message.attachments:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(ext) for ext in ['png', 'jpg', 'jpeg', 'gif']):
                async with aiohttp.ClientSession() as session:
                    async with session.get(attachment.url) as resp:
                        if resp.status == 200:
                            data = io.BytesIO(await resp.read())
                            image = Image.open(data)
                            # 檢查用戶是否設置了自定義寬度
                            width = user_widths.get(message.author.id, 100)  # 使用預設值100如果沒有設置
                            ascii_art = await convert_image_to_ascii(image, width)
                            # 生成唯一的檔案名
                            filename = f"text_art_{message.author.id}_{int(time.time())}.txt"
                            with open(filename, "w") as file:
                                file.write(ascii_art)
                            await message.channel.send(file=discord.File(filename))
                            os.remove(filename)  # 刪除檔案以避免佔用空間

    await bot.process_commands(message)

# 你的其他事件和命令...

# 使用環境變量是一種更安全的方法來處理您的 Token。
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

load_dotenv()  # 加載 .env 文件中的環境變量
discord_token = os.getenv('DISCORD_TOKEN')  # 從 .env 文件中獲取 Discord Token
bot.run(discord_token)  # 使用從環境變量獲取的 Token 運行 Discord 機器人