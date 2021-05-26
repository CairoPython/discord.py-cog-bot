import discord
from discord.ext import commands
from better_profanity import profanity


class Events(commands.Cog):
  
  def __init__(self, bot):
    self.bot=bot
    
    
  #listeners
  @commands.Cog.listener
  async def on_message(self, message, ctx):
    if message.author.has_roles('Muted'):
      await ctx.delete_message()
      
  @commands.Cog.listener
  async def on_message(self, ctx, message):
      
  #commands
  @commands.command
  async def nsfw_on(self, ctx):
    if ctx.message.author.guild_permissions.administrator:
      nsfw = True
      await ctx.send("NSFW message filters off!")
    else:
      await ctx.send("Sorry, you can't use that command!")
    return nsfw
   
    @commands.command
  async def nsfw_off(self, ctx):
    if ctx.message.author.guild_permissions.administrator:
      nsfw = False
      await ctx.send("NSFW message filters on!")
    else:
      await ctx.send("Sorry, you can't use that command!")
    return nsfw  
   
  
  
    
 
def setup(bot):
  bot.add_cog(Events(bot))
    
  
