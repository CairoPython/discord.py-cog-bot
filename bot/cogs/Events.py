import discord
from discord.ext import commands

class Random(commands.Cog):
  
  def __init__(self, bot):
    self.bot=bot
    
    
  #listeners
  @commands.Cog.listener
  async def status_change(self):
    await bot.change_presence(activity = discord.Game(name = 'Cogs.py example'), status = discord.Status.dnd)
  
  
    
 
def setup(bot):
  bot.add_cog(Random(bot))
    
  
