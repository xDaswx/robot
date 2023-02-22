import json
import discord,os
from discord.ext import commands
from discord import app_commands

from reactionmenu import ViewMenu, ViewButton,ViewSelect

#carregar variaveis env 
from dotenv import load_dotenv
load_dotenv()

PATH_COGS = os.getenv('path_accounts')



class Accounts(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name = "contas", description = "Informações sobre as contas no bot")
    async def accounts_info(self,ctx: discord.Interaction):
            json_contas = open(PATH_COGS,"r")
            contas = json.load(json_contas)  

            #await interaction.response.edit_message(embed=contas_embed, view=view_rank)
            menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed)

            for user in contas:
                contas_trans = f"⥼**Usuário(não é o nickname)**: {user['Usuario']}\n⥼**ID**: {str(user['Id'])[0:2]}...\n⥼**Dispositivo**: {user['DeviceId'][0:3]}...\n⥼**Google**: {user['GoogleId'][0:2]}...\n⥼**Facebook**: {user['FacebookId'][0:2]}...\n⥼**Rodando na versão**: {user['Version']}\n⥼**Logs:** [MassFarming](https://discord.com/channels/1041747923731488788/1051672999964708935)\n"
                contas_embed = discord.Embed(title=f"**🤖 - {user['Usuario']}**", description=f'**Informações**\n{contas_trans}', color=0x990000)
                contas_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/890792832208617485/1028331427374301336/account.png")
                contas_embed.set_footer(text=f"{self.bot.user.name}", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')
                menu.add_page(contas_embed)


            #menu.add_go_to_select(ViewSelect.GoTo(title="Ir para a pagina", page_numbers=...))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Voltar', custom_id=ViewButton.ID_PREVIOUS_PAGE, emoji='⬅️'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Proximo', custom_id=ViewButton.ID_NEXT_PAGE, emoji='➡️'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.red, label='Cancelar', custom_id=ViewButton.ID_END_SESSION, emoji='❌'))

            await menu.start()

async def setup(bot):
    await bot.add_cog(Accounts(bot))
