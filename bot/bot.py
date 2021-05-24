import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!f') #my bot's prefix outside of the example

cog_extensions = [
  cogs.Greetings,
  cogs.Moderator,
  cogs.Economy
]

if __name__ == '__main__':
  for cogs in cog_extensions:
    bot.load_extension(cogs)
    
 
@bot.event
async def on_ready():
  print(f'Logged on as {client.id} on Discord version {discord.__version__}')
  
  await bot.change_presence(activity = discord.Game(name = 'Cogs.py example'))
  
  
  
