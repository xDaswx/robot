import discord,os,json,requests
from discord.ext import commands
from discord import app_commands
from discord import interactions
from stumble.User.old_version import kitka as stumble



#carregar variaveis env 
from dotenv import load_dotenv
load_dotenv()

USER_LOGIN = os.getenv('user_login')
PATH_COGS = os.getenv('path_accounts')

#-----------------------

class LoginInformação(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @app_commands.command(name = "info", description = "get info about private accounts stored in bot")
    async def info(self,ctx: discord.Interaction, numero:int):
    
        json_contas = open(PATH_COGS,"r")
        contas = json.load(json_contas)
        json_contas.close()

        if len(contas['contas']) < numero:
            print(len(contas['contas']))

            await ctx.response.send_message(embed=discord.Embed(color=0x990000, description=f"Tem certeza que esse número está na lista de contas?"))
            

        data = f"{contas['contas'][numero-1]}"
        headers = {
        'Content-Type': 'application/json',
        'use_response_compression': 'true'}
        r = requests.post(USER_LOGIN, headers=headers,data=data)
        if r.status_code == 403 or r.status_code == 404 or r.status_code == 400 or r.text == "BANNED":
            await ctx.response.send_message(embed=discord.Embed(color=0x990000, title='Não foi possível logar',description=f"{r.text}"))

        balances = []
        for i in r.json()['User']['Balances']:
            if i['Name'] == "gems":
                balances.append(f"**Gemas**: {i['Amount']}\n")
            elif i['Name'] == "dust":
                balances.append(f"**Dust:** {i['Amount']}")
        print('\n'.join(balances))

        informacoe = f"**Usuário(não é o nickname)**: {contas['contas'][numero-1]['Usuario']}\n**Token(ATUALIZADO AGORA)**: `NÃO MOSTRAR...`\n**Google**: `NÃO MOSTRAR`\n**Facebook**: `NÃO MOSTRAR`\n**Localização:** `{r.json()['User']['Country']}`\n[Formato: ANO/MES/DIA]\n**Criado em:** `{r.json()['User']['Created'][0:10]}`\n**Ultimo login:** `{r.json()['User']['LastLogin'][0:10]}`\n**Skill:** `{r.json()['User']['SkillRating']}`\n**Exp:** `{r.json()['User']['Experience']}`\n**Coroas:** `{r.json()['User']['Crowns']}`\n**Quantidade de skins:** `{len(r.json()['User']['Skins'])}`\n**Passe de batalha[PAGO]:** `{''.join(['Não' if r.json()['User']['BattlePass']['HasPurchased'] == False else 'Sim'])}`\n**Nível no passe:** `{r.json()['User']['BattlePass']['PassTokens']/100}`\n{''.join(balances)}"

        Login_Embed = discord.Embed(color=0x990000, title=f"**NÃO MOSTRAR** 🔰", description=f"{informacoe}")
        Login_Embed.set_footer(text=f"{self.bot.user.name}", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')


        await ctx.response.send_message(embed=Login_Embed)


async def setup(bot):
    await bot.add_cog(LoginInformação(bot))