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
  async def ban(self, ctx, member: MemberID, *, reason):
    if ctx.message.author.guild_permissions.administrator:
      await ctx.guild.unban(discord.Object(id=member), reason=default.responsible(ctx.author, reason))
      await ctx.send(f'Banned {member} for {reason}')
      dm = member.create_dm()
      await dm.send(f"Hey, {member}. unfortunately, you were banned for {reason}. sucks to suck right? GET REKT")
    else:
      await ctx.send(f"Sorry, you can't use that command")
      
   @commands.command
   async def sm(ctx, seconds: int):
      if ctx.message.author.guild_permissions.administrator:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")
      else:
        await ctx.send("Sorry, you can't use that command!")
        
   @commands.command()
   async def mute(self, ctx, member: discord.Member, *, reason: str = None):
      if ctx.message.author.guild_permissions.administrator:
        muted_role = next((g for g in ctx.guild.roles if g.name == "Muted"), None)
        if not muted_role:
          return await ctx.send("Are you sure you've made a role called **Muted**? Remember that it's case sensitive too...")
        try:
            await member.add_roles(muted_role, reason=default.responsible(ctx.author, reason))
            await ctx.send(f"{member} is muted!)
      else:
        await ctx.send("Sorry, you can't use that command!")
    
    @commands.command()
    async def unmute(self, ctx, member: discord.Member, *, reason: str = None):
       
        if ctx.message.author.guild_permissions.administrator:
          muted_role = next((g for g in ctx.guild.roles if g.name == "Muted"), None)

          if not muted_role:
              return await ctx.send("Are you sure you've made a role called **Muted**? Remember that it's case sensitive too...")

          try:
            await member.remove_roles(muted_role, reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("unmuted"))
        else:
          await ctx.send("Sorry, you can't use that command!") 
        
   
  @commands.command
  async def unban(self, ctx, member: MemberID, *, reason):
    if ctx.message.author.guild_permissions.administrator:
      await ctx.guild.unban(discord.Object(id=member), reason=default.responsible(ctx.author, reason))  
      await ctx.send(f'Unbanned {member}! sending them a message now.')
      link = await ctx.channel.create_invite(max_age = 300)
      dm = member.create_dm()
      await dm.send(f"Hi, {member}! {ctx.message_author} unbanned you for {reason}. Here's a link back to the server!")
      await dm.send(link)
    else:
      await ctx.send("Sorry, you can't use that command!")
      
def setup(bot):
  bot.add_cog(Moderator(bot))
