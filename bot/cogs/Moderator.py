import discord
from discord.ext import commands

class Moderator(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command
  async def kick(self, ctx, member: discord.Member, *, reason):
    if ctx.message.author.guild_permissions.administrator:
      await ctx.kick(member, reason=reason) 
      await ctx.send(f'Kicked {member} for {reason}')
    else:
      await ctx.send(f"Sorry, you can't use that command")
  
  @commands.command
  async def ban(self, ctx, member: discord.Member, *, reason):
    if ctx.message.author.guild_permissions.administrator:
      await ctx.ban(member, reason=reason)
      await ctx.send(f'Banned {member} for {reason}')
    else:
      await ctx.send(f"Sorry, you can't use that command")
      
   @commands.command
   async def setdelay(ctx, seconds: int):
      if ctx.message.author.guild_permissions.administrator:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")
      else:
        await ctx.send("Sorry, you can't use that command!")
                       
