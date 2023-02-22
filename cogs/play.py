import discord,json,asyncio,os
from discord.ext import commands
import requests,hashlib,time as tm
from time import time 
from discord.ui import Button, View
from random import randint

#carregar variaveis env 
from dotenv import load_dotenv
load_dotenv()

USER_LOGIN = os.getenv('user_login')
KEY = os.getenv('key')
ROUND_PLAY = os.getenv('roundplay_finish')
PATH_COGS = os.getenv('path_accounts')

#-----------------------


class Play(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def play(self,ctx, numero:int,rounds_player:int):


        json_contas = open(PATH_COGS,"r")
        contas = json.load(json_contas)
        json_contas.close()
        
        if len(contas['contas']) < numero:
            print(len(contas['contas']))
            await ctx.send(embed=discord.Embed(color=0x990000, description=f"Tem certeza que esse número está na lista de contas?"))

        
        async def button_callback1(interaction):

            data = f"{contas['contas'][numero-1]}"
            headers = {
            'Content-Type': 'application/json',
            'use_response_compression': 'true',
            'Host': 'kitkabackend.eastus.cloudapp.azure.com:5010',}
            r = requests.post(USER_LOGIN, headers=headers,data=data)
            if r.status_code == 403 or r.status_code == 404 or r.status_code == 400 or r.text == "BANNED":
                await ctx.send(embed=discord.Embed(color=0x990000, title="Não foi possível logar",description=f"{r.text}"))
    
            balances = []
            for i in r.json()['User']['Balances']:
                if i['Name'] == "gems":
                    balances.append(f"**Gemas**: {i['Amount']}\n")
                elif i['Name'] == "dust":
                    balances.append(f"**Dust:** {i['Amount']}")
    
            informacoe = f"**Ordem**: <@{ctx.author.id}>\n**Conta[NUMERO]**:  {numero}\n**Nick**: {r.json()['User']['Username']}\n**Token**:  ||1||\n**GoogleId**:  ||1||\n**FacebookId**:  ||1||\n**Tempo estimado para o bot parar de jogar**: `{(rounds_player*55)//60}` minutos ou `{(rounds_player*55)//3600}` horas!"
    
            Login_Embed = discord.Embed(color=0x990000, title="Confirmado ✅", description=f"{informacoe}")
            Login_Embed.set_footer(text="Stringoff", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')
    
            auth_defalt = {"DeviceId":f'{r.json()["User"]["DeviceId"]}',"GoogleId":f'{r.json()["User"]["GoogleId"]}',"FacebookId":f'{r.json()["User"]["FacebookId"]}',"AppleId":"","Token":f'{r.json()["User"]["Token"]}',"Timestamp":1657411202,"Hash":"128053146036d1bfcda08eedcc177bb625f90bb1"}
    
            await interaction.response.edit_message(embed=Login_Embed, view=None)
            await loop_wins(auth_defalt,rounds_player,ctx)
    
        async def cancelar_callback(interaction):
            await interaction.response.edit_message(content="Cancelado pelo o usuário",view=None,embed=None)

        button_play = Button(label="[OK] Continuar", style=discord.ButtonStyle.green, disabled=False)
        button_cancelar = Button(label="Cancelar", style=discord.ButtonStyle.red, disabled=False)

        play_view = View(timeout=None)

        button_play.callback = button_callback1
        button_cancelar.callback = cancelar_callback


        play_view.add_item(button_play)
        play_view.add_item(button_cancelar)

        informacoe = f"**Ordem**: <@{ctx.author.id}>\n**Conta[NUMERO]**:  {numero}\n**Nick**:  *\n**Token**:  ||*||\n**GoogleId**:  ||*||\n**FacebookId**:  ||*||\n**Tempo estimado para o bot parar de jogar**: `{(rounds_player*55)//60}` minutos ou `{(rounds_player*55)//3600}` horas!"

        Login_Embed = discord.Embed(color=0x990000, title="Esperando confirmação 🔁", description=f"{informacoe}")
        Login_Embed.set_footer(text="Stringoff", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')

        await ctx.send(content="❗ **POR FAVOR NÃO LOGAR NA CONTA ENQUANTO O BOT ESTIVER JOGANDO** ❗", embed=Login_Embed, view=play_view)

        

    

async def setup(bot):
    await bot.add_cog(Play(bot))

#gerador de hash
I =str 
B =''
def hash_stumble (OO00O0O0OOOOOOO00 ,OO0O0000000O00000 ,data =B ):O00O00OOOO0O0OOO0 ='StumbleId';OO00O000OOOOO0000 ='Token';O00OOOO00000O00O0 ='FacebookId';O000O000000OOO000 ='GoogleId';OO0OOOO0OOO0O000O ='DeviceId';OOO00OOOOO00000O0 =OO00O0O0OOOOOOO00 ;OOO0OOO0O0O000O0O ='SECREKEY';OOOOOO0O000000OO0 =int (time ());O0OOOO000OO000OOO =B ;OOOO00000000O0OO0 =f"{OOO0OOO0O0O000O0O}{OOO00OOOOO00000O0[OO0OOOO0OOO0O000O]}{OOO00OOOOO00000O0[O000O000000OOO000]}{OOO00OOOOO00000O0[O00OOOO00000O00O0]}{OOO00OOOOO00000O0[OO00O000OOOOO0000]}{I(OOOOOO0O000000OO0)}{OO0O0000000O00000}{data}{OOO00OOOOO00000O0[O00O00OOOO0O0OOO0]}";O0OOO0OOOO0OO0O00 ={OO0OOOO0OOO0O000O :OOO00OOOOO00000O0 [OO0OOOO0OOO0O000O ],O000O000000OOO000 :OOO00OOOOO00000O0 [O000O000000OOO000 ],O00OOOO00000O00O0 :OOO00OOOOO00000O0 [O00OOOO00000O00O0 ],'AppleId':B ,OO00O000OOOOO0000 :OOO00OOOOO00000O0 [OO00O000OOOOO0000 ],'Timestamp':OOOOOO0O000000OO0 ,O00O00OOOO0O0OOO0 :OOO00OOOOO00000O0 [O00O00OOOO0O0OOO0 ],'Hash':hashlib .sha1 (bytes (O0OOOO000OO000OOO .join (OOOO00000000O0OO0 ),'utf-8')).hexdigest ()};return I (O0OOO0OOOO0OO0O00 )
print('secret key não é mostrada')

async def win(auth_defalt,completados,rounds_player,ctx):
    getauth = hash_stumble(auth_defalt)

    auth = getauth[0]
    headers = {
    'Content-Type': 'application/json',
    'authorization': str(auth),
    'use_response_compression': 'true'}
    r = requests.get(f'{ROUND_PLAY}{getauth[1]}', headers=headers)
    if "Crowns" not in r.text:
        await ctx.edit(content=f"<@{ctx.author.id}> algo me atrapalhou, possível entrada na conta, mais informações abaixo 😥",embed=discord.Embed(color=0x990000, title="Não foi possível continuar",description=f"Interno: {r.text}"))

    informações = f"EXP: {r.json()['User']['SkillRating']}\nPartidas ganhas: {r.json()['User']['Crowns']}\nNivel no passe de batalha: {r.json()['User']['BattlePass']['PassTokens']/100}\nPasse pago: {''.join(['Não' if r.json()['User']['BattlePass']['HasPurchased'] == False else 'Sim'])}**)"
    playEmbed = discord.Embed(color=0x990000, title=f"**Rodando em {r.json()['User']['Username']}** 🔰", description=f"{informações}")
    playEmbed.set_footer(text="Stringoff", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')

    await ctx.edit(embed=playEmbed)

async def loop_wins(auth_defalt,rounds_player,ctx):
    message = await ctx.send(embed=discord.Embed(color=0x990000, title=f"Iniciando rodada com {rounds_player} rounds", description="Iniciando\nde 10 a 60 segundos para iniciar"))
    rounds_player_completed = 1
    for _ in range(rounds_player):
        await win(auth_defalt,rounds_player_completed,rounds_player,message)
        await asyncio.sleep(55)
        rounds_player_completed += 1

