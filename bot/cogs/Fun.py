import discord
from discord.ext import commands

class Fun(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  
   @commands.command()
   @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
   async def duck(self, ctx):
      await self.randomimageapi(ctx, "https://random-d.uk/api/v1/random", "url")
   
  
    @commands.command(aliases=["flip", "coin"])
    async def coinflip(self, ctx):
        """ Coinflip! """
        coinsides = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")
    
    
        @commands.command()
        async def f(self, ctx, *, text: commands.clean_content = None):
          hearts = ["❤", "💛", "💚", "💙", "💜"]
          reason = f"for **{text}** " if text else ""
          await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")   
  
        
    @commands.command()
    async def reverse(self, ctx, *, text: str):
      t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
      await ctx.send(f"🔁 {t_rev}")
    
    
        @commands.command(aliases=["slots", "bet"])
        @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
        async def slot(self, ctx):
          emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
          a = random.choice(emojis)
          b = random.choice(emojis)
          c = random.choice(emojis)

          slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

          if (a == b == c):
              await ctx.send(f"{slotmachine} All matching, you won! 🎉")
          elif (a == b) or (a == c) or (b == c):
              await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
          else:
              await ctx.send(f"{slotmachine} No match, you lost 😢")
          
          @commands.command(aliases=["Hello", "hello", "hi", "Hi"])
          async def hey(self, ctx):
            ctx.send("Hi!")
