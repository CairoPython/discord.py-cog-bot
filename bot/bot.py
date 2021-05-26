import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '?l ')

cog_extensions = [
  'cogs.Greetings',
  'cogs.Moderator',
  'cogs.Events',
  'cogs.Fun',
  'cogs.presenceloop',
  'cogs.Tags'
]

if __name__ == '__main__':
  for cogs in cog_extensions:
    bot.load_extension(cogs)
    
 
@bot.event
async def on_ready():
  print(f'Logged on as {client.id} on Discord version {discord.__version__}')
  
  
  
  
  
