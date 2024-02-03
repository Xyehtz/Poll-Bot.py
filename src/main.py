import os
import discord
import logging
from dotenv import load_dotenv

# Import the .env file with the credentials
# ? Note to self: For some reason sometimes the path will not work properly, if so just copy the relative path from the code editor
dotenv_path = r'dotfiles/.env'
os.environ['DOTENV_PATH'] = dotenv_path
load_dotenv(dotenv_path)

# Logging discord info
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Declaration of intents
intents = discord.Intents.default()
intents.message_content = True

# Creation of Discord bot
bot = discord.Bot(intents=intents)


# Load commands inside of cogs folder
cog_list = [file[:-3] for file in os.listdir(r'src/cogs') if file.endswith('.py')]

for cog in cog_list:
  bot.load_extension(f'cogs.{cog}')
  print(f'Loaded {cog}')

bot.run(os.getenv('TOKEN'))
