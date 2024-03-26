# Discord TextArt Bot

This is a bot that runs on [Discord](https://discord.gg/FNH7CVEJ)(Click here to join the server!!!), designed to transform picture into text art-style .txt files.


![img](https://github.com/MuChi2112/Text-Art-Generator/blob/main/example_pic/example_pic.png?raw=true)
[picture](https://yt3.googleusercontent.com/roGS60A8a_lDbVakIg1JU3u3hbtjHSTilMGHMizuPKh7tuoY2nl46raxuW2f_83IKFGMjL6Z=s176-c-k-c0x00ffffff-no-rj) from Laplus Darknesss Youtube profile

This project is hosted on [render](https://dashboard.render.com/), and uses [uptimerobot](https://uptimerobot.com/) to prevent the bot from sleeping.

## Features

- **Discord Bot**: Listens for images sent in messages and converts them to ASCII art.
- **Flask Web Server**: Provides a basic web interface indicating the bot's operational status.


## Dependencies

```
aiohttp==3.9.3
aiosignal==1.3.1
attrs==23.1.0
blinker==1.7.0
certifi==2023.7.22
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
discord.py==2.3.2
Flask==3.0.2
frozenlist==1.4.1
h11==0.14.0
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
multidict==6.0.5
numpy==1.26.4
outcome==1.3.0.post0
packaging==23.2
pillow==10.2.0
pycparser==2.21
PySocks==1.7.1
python-dotenv==1.0.0
requests==2.31.0
selenium==4.15.2
sniffio==1.3.0
sortedcontainers==2.4.0
trio==0.23.1
trio-websocket==0.11.1
urllib3==2.0.7
webdriver-manager==4.0.1
Werkzeug==3.0.1
wsproto==1.2.0
yarl==1.9.4
```

Please ensure all dependencies are installed to avoid any compatibility issues. You can install these packages using the following command:

```bash
pip install -r requirements.txt
```


---

## Setup

### Environment Variables

Create a `.env` file in the root directory of the project and add your Discord bot token:

```plaintext
DISCORD_TOKEN=your_discord_bot_token_here
```


### Running the Bot

To start the bot and the Flask server, run:

```bash
python discord_bot_2.py
```

## Usage

1. **Starting the Bot**: Execute the script. The Flask server will start, and the bot will log in to Discord.
2. **Sending Images**: In any Discord server where the bot is present, upload an image with or without the `set width 200` command (e.g., `set width 200`). Feel free to replace the number behind it. The bot will reply with the ASCII art representation of the image.


## Contributions

Contributions are welcome! Feel free to fork the project and submit a pull request with your improvements.



