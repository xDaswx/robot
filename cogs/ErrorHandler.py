import json
import discord,os
from discord.ext import commands
from discord import app_commands



class ErrorHandler(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=discord.Embed(color=0x990000, description=f"Esse comando não existe!"))
        
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(color=0x990000, description=f"O comando está faltando o argumento, por favor envie a mensagem com os argumentos necessários"))
        
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=discord.Embed(color=0x990000, description=f"O argumento está digitado de maneira errada, tentou conferir se executou o comando corretamente?"))
        
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=discord.Embed(color=0x990000, description=f"Erro na invocação do comando"))
        """
                if isinstance(error, commands.CommandError):
            await ctx.send(embed=discord.Embed(color=0x990000, description=f"O comando retornou um erro"))
        
        """

        if isinstance(error, AttributeError):
            await ctx.send(embed=discord.Embed(color=0x990000, description=f"Erro de atributo: {AttributeError}"))

        if isinstance(error, KeyError):
            print('KeyError')
            await ctx.send(embed=discord.Embed(color=0x990000, description=f"Erro de Key: {KeyError}"))

async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
