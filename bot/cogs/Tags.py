import discord
from discord.ext import commands

class Arguments(argparse.ArgumentParser):
    def error(self, message):
        raise RuntimeError(message)
class TagName(commands.clean_content):
    def __init__(self, *, lower=False):
        self.lower = lower
        super().__init__()

    async def convert(self, ctx, argument):
        converted = await super().convert(ctx, argument)
        lower = converted.lower().strip()

        if not lower:
            raise commands.BadArgument('Missing tag name.')

        if len(lower) > 100:
            raise commands.BadArgument('Tag name is a maximum of 100 characters.')

        first_word, _, _ = lower.partition(' ')

        # get tag command.
        root = ctx.bot.get_command('tag')
        if first_word in root.all_commands:
            raise commands.BadArgument('This tag name starts with a reserved word.')

        return converted if not self.lower else lower
      
        
class Tags(commands.Cogs):
  
  def __init__(self, bot):
    self.bot = bot
    
  async def create_tag(self, ctx, name: str, content):
        async with ctx.acquire():
            tr = ctx.db.transaction()
            await tr.start()

            try:
                await ctx.db.execute(query, name, content, ctx.author.id, ctx.guild.id)
            except asyncpg.UniqueViolationError:
                await tr.rollback()
                await ctx.send('This tag already exists.')
            except:
                await tr.rollback()
                await ctx.send('Could not create tag.')
            else:
                await tr.commit()
                await ctx.send(f'Tag {name} successfully created.')
            
        @tag.command(aliases=['add'])
        @suggest_box()
        async def create(self, ctx, name: TagName, *, content: commands.clean_content):
        if self.is_tag_being_made(ctx.guild.id, name):
            return await ctx.send('This tag is currently being made by someone.')

        await self.create_tag(ctx, name, content)
        
