import discord
from discord.ext import commands

class Random(commands.Cog):
  
  def __init__(self, bot):
    self.bot=bot
    
    
  #listeners
  @commands.Cog.listener
  async def status_change(self):
    await bot.change_presence(activity = discord.Game(name = 'Cogs.py example'), status = discord.Status.dnd)
  
  #commands
  @commands.command(aliases=['8ball', 'ball'])
   async def _8ball(self, ctx, *, question):
            
             responses = ['As I see it, yes.',
                          'Ask again later.',
                          'Better not tell you now.',
                          'Cannot predict now.',
                          'Concentrate and ask again.',
                          'Don’t count on it.',
                          'It is certain.',
                          'It is decidedly so.',
                          'Most likely.',
                          'My reply is no.',
                          'My sources say no.',
                          'Outlook not so good.',
                          'Outlook good.',
                          'Reply hazy, try again.',
                          'Signs point to yes.',
                          'Very doubtful.',
                          'Without a doubt.',
                          'Yes.',
                          'Yes – definitely.',
                          'You may rely on it.']
              q = ("Question: " + question)
              a = ("Answer: " + random.choice(responses))
              embed = discord.Embed(
                  title=(q),
                  description=(a),
                  colour=discord.Colour.blue()
              )
              await ctx.send(embed=embed)
    
    #giphy command here!
def setup(bot):
  bot.add_cog(Random(bot))
    
  
