import discord
from discord.ext import commands
from better_profanity import profanity

blacklisted_wordlist = [
'anal',
'anus',
'ballsack',
'blowjob',
'blow job,
'boner',
'clitoris',
'cock',
'cunt',
'dick',
'dildo'
'dyke',
'fag',
'fuck',
'jizz',
'labia',
'muff',
'nigger',
'nigga',
'penis',
'piss',
'pussy',
'scrotum',
'sex',
'shit',
'slut',
'smegma',
'spunk',
'twat',
'vagina',
'wank',
'whore'
]

class Events(commands.Cog):
  
  def __init__(self, bot):
    self.bot=bot
    
    
  #listeners
  #muterole deleter
  @commands.Cog.listener
  async def on_message(self, message, ctx):
    if message.author.has_roles('Muted'):
       message.delete(message)
  
  #profanity filter
  @commands.Cog.listener
  async def on_message(self, ctx, message):
    if nsfw = True:
      for word in blacklisted_wordlist:
        if word in message.content:
           message.delete(message)
           dm = message.author.create_dm()
           await dm.send("Hey! you can't use that word. you've been warned.")
    else:
      return
      
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
    
  
