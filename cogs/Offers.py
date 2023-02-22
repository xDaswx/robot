


import discord,os,json
from discord.ext import commands
from discord import app_commands
from discord import interactions
from stumble.Game import game

from reactionmenu import ViewMenu, ViewButton, ViewSelect, Page

#carregar variaveis env 
from dotenv import load_dotenv
load_dotenv()

USER_LOGIN = os.getenv('user_login')
KEY = os.getenv('key')
USER_EDIT = os.getenv('user_edit')
PATH_COGS = os.getenv('path_accounts')
#-----------------------

class Offers(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name = "offer", description = "offers")
    async def offer(self,ctx: discord.Interaction):

            #await interaction.response.edit_message(embed=contas_embed, view=view_rank)
            menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed)
            server = game.Game()
            server.shared()
            coisas = server.Offers_v2
            aa = server.PurchasableItems

            to_delete = [0,1,2,3,4,5,6,7,8]

            #for offset, index in enumerate(to_delete):
              #index -= offset
              #del coisas[index]
            
            for item in coisas:
                rewards = []
                price = []
                for informa in aa:
                    if informa['Name'] == item['PurchasableItem']:
                        get_price = [f"{info.get('amount')} {info.get('currency')}\n" if informa['prices'][0]['currency'] == 'gems' else 'Real Money' for info in informa.get('prices')]
                        price.append(get_price)
                        get = [f"**Item:** ``{info['typeInfo']}``\n" for info in informa['rewards']]
                        rewards.append(get)

                contas_trans = f"**⥼BackgroundColor:** ``{item.get('BackgroundColor','none')}``\n**⥼Description:** ``{item.get('Description','none')}``\n**⥼EndDateTime:** ``{item.get('EndDateTime','none')}``\n**⥼Header:** ``{item.get('Header','none')}``\n**⥼Popup:** ``{item.get('Popup','without popup')}``\n**⥼PurchasableItem:** ``{item.get('PurchasableItem','none')}``\n**⥼StartDateTime:** ``{item.get('StartDateTime','000000')}``\n**⥼Version:** ``{item.get('Version','unknown')}``"
                contas_embed = discord.Embed(title="In-game offers", description=f'**Offers**\n\n{contas_trans}\n\n**PRICE**: ``{"".join(price[0])}``\n\n{"".join(rewards[0])}', color=0x990000)
                contas_embed.set_thumbnail(url="https://cdn.glitch.global/efae7c5b-36f6-4b8b-86c4-dcc2d7153909/gift.png")
                contas_embed.set_footer(text=f"Game Offers", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')
                menu.add_page(contas_embed)

            #menu.add_go_to_select(ViewSelect.GoTo(title="Ir para a pagina", page_numbers=...))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Voltar', custom_id=ViewButton.ID_PREVIOUS_PAGE, emoji='⬅️'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Proximo', custom_id=ViewButton.ID_NEXT_PAGE, emoji='➡️'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.red, label='Cancelar', custom_id=ViewButton.ID_END_SESSION, emoji='❌'))

            await menu.start()



async def setup(bot):
    await bot.add_cog(Offers(bot))
