import discord
from discord.ext import commands

class Greetings(commands.Cog):
  
  def __init__(self, bot):
    self.bot=bot
    
  @commands.command
  async def hi(self, ctx):
    await ctx.send("Hello!")
    bot.add_reaction('thumbs_up')
    
  @commands.command
  @commands.guild_only
  async def joined(self, ctx, *, member:discord.Member):
     await ctx.send(f'{member.display_name} joined on {member.joined_at}')
      
def setup(bot):
  bot.add_cog(Greetings(bot))
