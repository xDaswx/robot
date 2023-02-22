import discord,os,json
from discord.ext import commands
from discord import app_commands
from discord import interactions

from stumble.Game import game

#-----------------------

class Search(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #@app_commands.command(name = "search", description = "look up an account")
    @commands.hybrid_command(name = "searchbeta", description = "look up an beta ccount")
    async def Search_user(self,ctx: discord.Interaction, username:str):
        search = game.Game()
        
        info = search.Search(username=username)
        print(info)
        if ("<@" and ">" in username[-1]):
            print(f'{username} user mention detected')
            await ctx.send(content='**EN-US:** I could not find this user because it was identified that you used a mention, apparently you are on discord mobile\n------------\n**PT-BR:** Não consegui encontrar esse usuário pois foi identificado que você utilizou uma menção, aparentemente você está no discord mobile')
            return
        if info['status'] != 200:
            contas_embed = discord.Embed(title=f"Errou na consulta [{username}]",description=f'Usuário não encontrado\n``Return: {info["new_search"]}``',color=0x990000)
            await ctx.send(embed=contas_embed)
            print('SearchError')
            return
        search.shared()
        Levels = [{"RequiredXP":1000},{"RequiredXP":2000},{"RequiredXP":4000},{"RequiredXP":8000},{"RequiredXP":12000},{"RequiredXP":20000},{"RequiredXP":30000},{"RequiredXP":40000},{"RequiredXP":60000},{"RequiredXP":80000},{"RequiredXP":120000},{"RequiredXP":140000},{"RequiredXP":160000},{"RequiredXP":180000},{"RequiredXP":200000},{"RequiredXP":220000},{"RequiredXP":240000},{"RequiredXP":260000},{"RequiredXP":280000},{"RequiredXP":300000}]
        level = len([True for req in Levels if req['RequiredXP']< info['new_search']['experience']])

        skin_nome = '???'
        online_check = str(info['new_search']['isOnline']).replace('False','❌').replace('True','✅')
        online_time_long = ['Yes' if info['new_search']['skin'] == None else 'No']
        
        for skin in search.Skins_v4:
            if skin['SkinID'] == info['new_search']['skin']:
                skin_nome = skin['FriendlyName']
        try:
            construtor = f"**⥼ID:** {info['new_search']['userId']}\n**⥼Nome do usuário:** {info['new_search']['userName']}\n**⥼País:** {check_country(info['new_search']['country'])}({info['new_search']['country']})\n**⥼<:trophy_icon:1051909439562727425>:** {'{:,}'.format(info['new_search']['trophies'])}\n**⥼<:crownIcon:1051909438233116732>:** {'{:,}'.format(info['new_search']['crowns'])}\n**⥼Online:** {online_check}\n**⥼Experience:** {info['new_search']['experience']}\n**⥼Level:** {level}\n<--------------------------->\n**⥼Suspicious behavior:** {sus(info)}\n**⥼SkinId:** {info['new_search']['skin']}\n**⥼SkinName:** {skin_nome}\n**⥼CreatedDate[ESTIMATED 📌]:** {timemab(info['new_search']['userId'])}\n**⥼Offline for a long time** {online_time_long[0]}"
            #construtor = '??'
            contas_embed = discord.Embed(title=f"Consulta feita com sucesso",description=f'{construtor}',color=0x990000)
            #print(f"https://cdn.glitch.global/efae7c5b-36f6-4b8b-86c4-dcc2d7153909/{str(info['new_search']['skin']).lower()}_icon.png")
            contas_embed.set_thumbnail(url=f"https://cdn.glitch.global/efae7c5b-36f6-4b8b-86c4-dcc2d7153909/{str(info['new_search']['skin']).lower()}_icon.png")
            contas_embed.set_footer(text=f"{self.bot.user.name}", icon_url='https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg')
        except Exception as Er:
             contas_embed = discord.Embed(title=f"Local error",description=f'💀: ``{Er}``',color=0x990000)
        await ctx.send(embed=contas_embed)


def check_country(country_code):
      countries = {'BR':'<:BR:1069397140033511434>',
      'DE':'<:DE:1069397142667526305>',
      'ES':'<:ES:1069397147000258650>',
      'ID':'<:ID:1069397148745076746>',
      'IT':'<:IT:1069397151345557504>',
      'JP':'<:JP:1069397152910032916>',
      'MA':'<:MA:1069397155883778088>',
      'NL':'<:NL:1069397157901254696>',
      'PL':'<:PL:1069397161072148551>',
      'TR':'<:TR:1069397162724687953>'}
      if country_code in countries:
        return countries[country_code]
      else:
        return '<:defaultFlag:1069397144395591700>'


def sus(info):
    rate = int(100 - ((info['new_search']['trophies'] - (info['new_search']['crowns']*30))/30))
    if info['new_search']['crowns'] < 100:
        return 'Ok'
    elif rate < -10000:
        return f'super legit account - rate: {rate}% 👑'
    elif rate > 90:
        return f'exploiter/hacker - rate: {rate}% 📛'
    elif rate > 80:
        return f'sus account - rate: {rate}% 🤨'
    elif rate < 0:
        return f'reasonable account - rate: {rate}%'
    else:
        return f'hmmm rate: {rate}%'

def timemab(id):
    if id <= 19016656:
        return 'Very old account'  
    elif id <= 49981280:
        return '2021'
    elif id >= 416762585:
        return '2023/02'
    elif id >= 400543763:
        return '2023'
    elif id >= 193589871:
        return '2022/2023 idk'

    else:
        return 'IDK'
#print(timemab(49681280))

async def setup(bot):
    await bot.add_cog(Search(bot))