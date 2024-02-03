import os
import discord
from dotenv import load_dotenv

# Import the .env file with the credentials
# ? Note to self: For some reason sometimes the path will not work properly, if so just copy the relative path from the code editor
dotenv_path = r'dotfiles/.env'
os.environ['DOTENV_PATH'] = dotenv_path
load_dotenv(dotenv_path)

# Declaration of intents
intents = discord.Intents.default()
intents.message_content = True

# Creation of Discord Client
client = discord.Client(intents=intents)

# Login event
@client.event
async def on_ready():
  print(f'Logged in as {client.user}')

# Message event
@client.event
async def on_message(message):
  print(f'Message from {message.author}: {message.content}')
  if message.author == client.user:
    return
  
  if message.content.lower().startswith('hello'):
    await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
