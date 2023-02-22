import discord,os,json
from discord.ext import commands
from discord import app_commands
from discord import interactions

from stumble.Game import game

#-----------------------

class SkinInfo(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @app_commands.command(name = "skininfo", description = "return skin info")
    async def skininfo(self,ctx: discord.Interaction, skinid:str):
        search = game.Game()
        info = search.shared()
        
        for skin in search.Skins_v4:
            try:
                if skin['SkinID'] == skinid.upper():
                    construtor = f"**⥼SkinName:** {skin['FriendlyName']}\n**⥼SkinId:** {skin['SkinID']}\n**⥼Hidden:** {skin['Hidden']}\n"
                    contas_embed = discord.Embed(title=f"Skin info",description=f'{construtor}',color=0x990000)
                    contas_embed.set_thumbnail(url=f"https://cdn.glitch.global/efae7c5b-36f6-4b8b-86c4-dcc2d7153909/{str(skinid).lower()}_icon.png")
                    contas_embed.set_footer(text=f"{self.bot.user.name}", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')

            except Exception as Er:
                contas_embed = discord.Embed(title=f"Error",description=f'``not found {Er}``',color=0x990000)
        await ctx.response.send_message(embed=contas_embed)

async def setup(bot):
    await bot.add_cog(SkinInfo(bot))