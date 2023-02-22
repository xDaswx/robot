# discord.py recently added full hybrid commands. They work as follows:
## Note: as I don't see a reason not to, I will present an example using a commands.Cog.

## IMPORTANT: hybrid commands only work if the signature is compatible with app commands.
# this means that all parameters must have a type annotation, even if it is just `str`.
# this also means that you must use `Transformers` not `Coverters` in these cases.


import discord
from discord.ext import commands

class MyCog(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot: commands.Bot = bot
  
  @commands.hybrid_command(name="ping")
  async def ping_command(self, ctx: commands.Context, arg:str) -> None:
    """
    Comando hibrido, testes
    """

    await ctx.send(f"Hello! {arg}", ephemeral=True)
    await ctx.reply(f"Helsdaasdasdsdalo! {arg}")
    # we use ctx.send and this will handle both the message command and app command of sending.
    # added note: you can check if this command is invoked as an app command by checking the `ctx.interaction` attribute.
    

    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(MyCog(bot))
      