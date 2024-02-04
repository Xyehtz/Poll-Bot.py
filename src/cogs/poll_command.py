import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

dotenv_path = r'dotfiles/.env'
os.environ['DOTENV_PATH'] = dotenv_path
load_dotenv(dotenv_path)

class Button(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  class MyView(discord.ui.View):
    def __init__(self, options):
      super().__init__()
      self.options = options

    @discord.ui.button(label='Button 1', style=discord.ButtonStyle.blurple)
    async def button_callback(self, button, interaction):
      await interaction.response.send_message(f'You clicked {self.options}', ephemeral=True)

  @discord.slash_command(guild_ids=[os.getenv('GUILD_ID')], name='poll', description='Create a poll')
  async def button(
    self, 
    ctx, 
    text: discord.Option(str), 
    first_option: discord.Option(discord.User), 
    second_option: discord.Option(discord.Member)
  ):
    await ctx.respond(f'{text}\n<@{first_option.id}>\n<@{second_option.id}>', view=Button.MyView(options=first_option))

def setup(bot):
  bot.add_cog(Button(bot))