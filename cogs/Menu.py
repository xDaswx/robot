import requests,json,hashlib,time as tm
from time import time 
import discord,platform,os
from discord.ext import commands
from discord.ui import Button, View
from discord import app_commands

from reactionmenu import ViewMenu, ViewButton,ViewSelect

#carregar variaveis env 
from dotenv import load_dotenv
load_dotenv()

RANKING = os.getenv('rank_highscoreBR')
PATH_COGS = os.getenv('path_accounts')
USER_LOGIN = os.getenv('user_login')
KEY = os.getenv('key')
KEY_LOGIN = os.getenv('key_login')
ROUND_PLAY = os.getenv('roundplay_finish')
PATH_COGS = os.getenv('path_accounts')


GEMS_1 = os.getenv('economy_gems')
GEMS_CHARGE = os.getenv('economy_charge')
GEMS_MENU = os.getenv('economy_menu')
GEMS_ROD = os.getenv('economy_rode')




class Menu(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def menu(self, ctx):
        emb = discord.Embed(title=self.bot.user.name, description=None, color=0x990000)
        emb.set_thumbnail(url="https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg")
        emb.add_field(name="Sistema 💻",value=f"◉{platform.system()} {platform.release()}", inline=True)
        emb.add_field(name="Versão do sistema 💽",value=f"◉{platform.version()}", inline=True)
        emb.set_footer(text=f"{self.bot.user.name}", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')
        
        button2 = Button(label="Contas", style=discord.ButtonStyle.green, emoji="🛠️")
        button3 = Button(label="Informações internas", style=discord.ButtonStyle.green, emoji="♨️", disabled=False)

        async def button_envs(interaction):
            emb = discord.Embed(title="Stumble Guys", description="❗**Informações armazenadas e utilizadas pelo o bot em .env, favor não mostrar**❗", color=0x990000)
            emb.set_thumbnail(url="https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg")
            emb.add_field(name="Versão",value=f"0.37", inline=False)
            emb.add_field(name="Api para login",value=f"||`{USER_LOGIN}`||", inline=False)
            emb.add_field(name="Api rank",value=f"||`{RANKING}`||", inline=False)
            emb.add_field(name="HashSALT_CODE_REQUESTS",value=f"||`{KEY}`||\n||`auth = hashstumble(AUTH,path_da_api)`||", inline=False)
            emb.add_field(name="HashSALT_LOGIN_REQUESTS",value=f"||`{KEY_LOGIN}`||", inline=False)
            emb.add_field(name="Gemas e skins",value=f"`{GEMS_1}\n{GEMS_CHARGE}\n{GEMS_MENU}\n{GEMS_ROD}BAU['Quantidade_bau']`", inline=False)
            emb.set_image(url="https://media.discordapp.net/attachments/739575553253834754/1050500255684247552/image.png?width=806&height=181")
            emb.set_footer(text=f"{self.bot.user.name}", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')

            await interaction.response.edit_message(content="❗**POR FAVOR NÃO MOSTRAR ESSAS INFORMAÇÕES**❗", embed=emb, view=None)
        

        async def button_accounts(interaction):
            await interaction.response.edit_message(content=None,embed=emb, view=viewNada)
            json_contas = open(PATH_COGS,"r")
            contas = json.load(json_contas)  

            #await interaction.response.edit_message(embed=contas_embed, view=view_rank)
            menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed)

            for user in contas['contas']:
                contas_trans = f"⥼**Usuário(não é o nickname)**: {user['Usuario']}\n⥼**ID**: {user['Id']}\n⥼**Dispositivo**: {user['DeviceId']}\n⥼**Google**: {user['GoogleId']}\n⥼**Facebook**: {user['FacebookId']}\n⥼**Rodando na versão**: {user['Version']}\n⥼**Logs:** [MassFarming](https://discord.com/channels/1041747923731488788/1051672999964708935)\n"
                contas_embed = discord.Embed(title=f"**🤖 - {user['Usuario']}**", description=f'**Informações**\n{contas_trans}', color=0x990000)
                contas_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/890792832208617485/1028331427374301336/account.png")
                contas_embed.set_footer(text=f"{self.bot.user.name}", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')
                menu.add_page(contas_embed)
            
            json_contas.close()

            menu.add_go_to_select(ViewSelect.GoTo(title="Ir para a pagina", page_numbers=...))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Voltar', custom_id=ViewButton.ID_PREVIOUS_PAGE, emoji='⬅️'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Proximo', custom_id=ViewButton.ID_NEXT_PAGE, emoji='➡️'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.red, label='Cancelar', custom_id=ViewButton.ID_END_SESSION, emoji='❌'))

            await menu.start()

        button2.callback = button_accounts
        button3.callback = button_envs

        view = View(timeout=20)
        view.add_item(button2)
        view.add_item(button3)

        viewNada = View()
    
        await ctx.send(embed=emb,view=view,delete_after=7)


async def setup(bot):
    await bot.add_cog(Menu(bot))
