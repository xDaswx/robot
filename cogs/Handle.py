# cogs/exception-handler.py

import discord
from discord.ext import commands
from datetime import datetime
import pytz

class ExceptionHandler(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        now = datetime.now()
        print('error handler handler')
        tz_NY = pytz.timezone('America/Sao_Paulo')
        datetime_NY = datetime.now(tz_NY)

        construt = f"```js\n{error}\n```"
        await ctx.send(embed=discord.Embed(title='Try running the command again', description=f"Brazil time: {datetime_NY.strftime('%H:%M:%S')} \n{construt}"))
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExceptionHandler(bot))