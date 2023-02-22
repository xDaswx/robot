import discord,os,json
from discord.ext import commands
from discord import app_commands
from discord import interactions
from reactionmenu import ViewMenu, ViewButton,ViewSelect

from stumble.tournaments import backbone

#-----------------------

class TornamentClass(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @app_commands.command(name = "tournaments", description = "get all tournaments")
    async def TournamentGetAll(self,ctx: discord.Interaction):
        menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed)
        cl = backbone.Client()
        torneios = cl.tournamentGetList()
        tor1 = torneios['tournaments']
        #'status': 2, acontecendo
        #'status': 4, acabou
        #'status': 0, ainda não aconteceu
        #'status': 1, 
        for index,tournaments in enumerate(tor1, start=1):
            serverlocal = tournaments['data']['tournament-data']['invitation-setting'][0]['requirements'][0]['custom-requirement'][0]['@value']
            #gems = tournaments['data']['tournament-data']['invitation-setting'][0]['entry-fee'][0]['item'][0]['@amount']
            #construtor = f"[Steam]({tournaments['streamurl']} 'Clique para acessar a live!')\nServer Region:{serverlocal}\nPrice:{gems}<:gemIcon:1051908821469102120>"
            embed = discord.Embed(title=f"{tournaments['name']}",description=f'{index}-{serverlocal}',color=0x990000)
            #print(f"https://cdn.glitch.global/efae7c5b-36f6-4b8b-86c4-dcc2d7153909/{str(info['new_search']['skin']).lower()}_icon.png")
            embed.set_image(url=tournaments['icon'])
            embed.set_footer(text=f"{self.bot.user.name}", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')
            menu.add_page(embed)
        
        menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Next', custom_id=ViewButton.ID_PREVIOUS_PAGE,emoji='⬅'))
        menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Previous', custom_id=ViewButton.ID_NEXT_PAGE, emoji='➡'))
        menu.add_button(ViewButton(style=discord.ButtonStyle.red, label='Cancelar', custom_id=ViewButton.ID_END_SESSION, emoji='❌'))
        await menu.start()
        
        await ctx.response.send_message(content='das')

async def setup(bot):
    await bot.add_cog(TornamentClass(bot))