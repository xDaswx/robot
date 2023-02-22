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

class Gachas(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name = "gachas", description = "gachas in game")
    async def gacha(self,ctx: discord.Interaction):

            #await interaction.response.edit_message(embed=contas_embed, view=view_rank)
            menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed)
            server = game.Game()
            server.shared()
            coisas = server.Gachas
            
            aa = server.PurchasableItems

            for item in coisas:
                
                rewards = []
                skin_translanted = []
                emotes_translanted = []
                anim_translanted = []
                price = []
                for informa in aa:
                    if informa['Name'] == item['PurchasableItem']:
                        price.append(f"{informa['prices'][0]['amount']} {informa['prices'][0]['currency']}")
                        #get_skin = [skin.get('FriendlyName','???') for skin in server.Skins_v4 if skin['SkinID'] == info['typeInfo']]

                        for info in informa['rewards']:
                            for skin in server.Skins_v4:
                                if skin['SkinID'] == info['typeInfo']:
                                    #print(skin.get('FriendlyName','???'),info['typeInfo'],info['chance'])
                                    skin_translanted.append(f"**{skin.get('FriendlyName','???')}** | `{info['typeInfo']}` | {int(info['chance'])}%\n")

                            for emote in server.Emotes:
                                if emote['ID'] == info['typeInfo']:
                                    emotes_translanted.append(f"**{emote.get('FriendlyName','???')}** | `{info['typeInfo']}` | {int(info['chance'])}%\n")
                                    #print(skin_translanted)
                            
                            for anim in server.Animations:
                                if anim['ID'] == info['typeInfo']:
                                    anim_translanted.append(f"**{anim.get('FriendlyName','???')}** | `{info['typeInfo']}` | {int(info['chance'])}%\n")
                                    #print(skin_translanted)

                        get_v2 = [skin.get('FriendlyName','???') ,info['typeInfo'],info['chance']]
                        get = (f"{[skin.get('FriendlyName','???')[0] for skin in server.Skins_v4 if skin['SkinID'] == info['typeInfo']]} {info['typeInfo']} {int(info['chance'])}%\n" for info in informa['rewards'])
                        #rewards.append(skin_translanted)

                contas_trans = f"**⥼EndDateTime:** ``{item['EndDateTime']}``\n**⥼Id:** ``{item['Id']}``\n**⥼Popup:** ``{item['Popup']}``\n**⥼PurchasableItem:** ``{item['PurchasableItem']}``\n**⥼StartDateTime:** ``{item['StartDateTime']}``\n**⥼Version:** ``{item['Version']}``"
                contas_embed = discord.Embed(title="In-game gachas", description=f'**Gachas(Roletas)**\n\n{contas_trans}\n\n**PRICE**: ``{"".join(price[0])}``\n\n**_Skins_** _name | backend id | chance_\n{"".join(skin_translanted)}\n**_Emotes_** _name | backend id | chance_\n{"".join(emotes_translanted)}\n**_Anims_** _name | backend id | chance_\n{"".join(anim_translanted)}', color=0x990000)
                contas_embed.set_thumbnail(url="https://cdn.glitch.global/efae7c5b-36f6-4b8b-86c4-dcc2d7153909/spinner.png")
                contas_embed.set_footer(text=f"Gachas", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')

                menu.add_page(embed=contas_embed)
            
                #print(menu)


            #menu.add_go_to_select(ViewSelect.GoTo(title="Ir para a pagina", page_numbers=...))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Voltar', custom_id=ViewButton.ID_PREVIOUS_PAGE, emoji='⬅️'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Proximo', custom_id=ViewButton.ID_NEXT_PAGE, emoji='➡️'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.red, label='Cancelar', custom_id=ViewButton.ID_END_SESSION, emoji='❌'))

            await menu.start()

async def setup(bot):
    await bot.add_cog(Gachas(bot))
