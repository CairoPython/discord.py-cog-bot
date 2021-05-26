import discord
from discord.ext import commands

class Random(commands.Cog):
  
  def __init__(self, bot):
    self.bot=bot
    
    
  #listeners
  @commands.Cog.listener
  async def on_message(self, ctx):
    if message.author.has_roles('Muted'):
      await ctx.delete_message()
  
  
    
 
def setup(bot):
  bot.add_cog(Random(bot))
    
  
