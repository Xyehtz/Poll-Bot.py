import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

dotenv_path = r'secrets/.env'
os.environ['DOTENV_PATH'] = dotenv_path
load_dotenv(dotenv_path)

class Button(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  class MyView(discord.ui.View):
    def __init__(self, options):
      super().__init__()
      self.options = options

    @discord.ui.button(label='button', style=discord.ButtonStyle.blurple)
    async def button_callback(self, button, interaction):
      await interaction.response.send_message(f'You clicked {self.options}', ephemeral=True)

  @discord.slash_command(guild_ids=[os.getenv('GUILD_ID')], name='poll', description='Create a poll')
  async def button(
    self, 
    ctx, 
    title: discord.Option(
      str, 
      name = 'title',
      description= 'The title of the poll',
      required=True
    ),
    description: discord.Option(
      str,
      name = 'description',
      description= 'Add a description to the poll',
      required = True
    ),
    first_user_option: discord.Option(
      discord.User, 
      description= 'Choose a user', 
      name = 'first-user',
      required=True
    ), 
    second_user_option: discord.Option(
      discord.User,
      name = 'second-user',
      description= 'Choose a second user',
      required = True
    ),
    third_user_option: discord.Option(
      discord.User,
      name = 'third-user',
      description= 'Choose a second user',
      required = False
    ),
    fourth_user_option: discord.Option(
      discord.User,
      name = 'fourth-user',
      description= 'Choose a second user',
      required = False
    )
  ):
    embed = discord.Embed(
      title=title,
      description=description,
      color=discord.Color.random(),
    )
    embed.add_field(
      name='Author',
      value=f'<@{ctx.author.id}>',
    )

    # if third_user_option:
    #   pass
    # elif fourth_user_option:
    #   pass
    # elif third_user_option and fourth_user_option:
    #   pass
    # else:
    #   pass

    await ctx.respond(
      f'## **New poll @everyone**', 
      embed=embed, 
      view=(Button.MyView(options=[first_user_option, second_user_option]))*5)

def setup(bot):
  bot.add_cog(Button(bot))