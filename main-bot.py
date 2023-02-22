import asyncio,json
import discord,os
from discord.ext import commands,tasks
from gemas import logint
from genshin import genshin_impact
from genshin_stats import genshin_impactstats
from datetime import datetime
import datetime as dtime
import pytz
from discord import app_commands

from dotenv import load_dotenv
load_dotenv()

token_type = "token_BETA"
TOKEN = os.getenv(token_type)
DISCORD_CHANNEL = int(os.getenv('discord_channel_id'))
PATH_MAIN = os.getenv('main_path_accounts')

if "BETA" in token_type:
    prefix = "B>"
else:
    prefix = ">"

prefix = 'sg!'
 
bot = commands.Bot(command_prefix=prefix,
                   description='Prefix: >\n!!GITUHB!!!!',
                   activity=discord.Activity(type=discord.ActivityType.playing,
                                             name="!GITUHB!!!!"),
                   status=discord.Status.idle,intents=discord.Intents.all())

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} online")
    print(bot.user.avatar)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
        
    except Exception as e:
        print(e)
        
    #genshin_daily.start()
    #genshin_daily_stats.start()
    #Stumble_Gemas.start()
    

json_contas = open(PATH_MAIN,"r")
contas = json.load(json_contas)
@bot.command()
async def emoji(ctx):
    for emoji in ctx.guild.emojis:
        print({f'{emoji.name}':f"<:{emoji.name}:{emoji.id}>"})
    await ctx.reply(f'aaa')

@bot.command()
async def emoji2(ctx,moji):
    with open('emojis.json','r') as f:
        mojiload = json.load(f)
        print(mojiload.get(moji,'??'))
        
        await ctx.reply(mojiload.get(moji,'??'))
tz = pytz.timezone('America/Fortaleza')
@tasks.loop(hours=1)
async def genshin_daily():
    channel = bot.get_channel(1074747371033989190)
    cookie_caio = {'cookie':{'ltoken': 'GITHUB','ltuid': '0'},'uid':0,'nome':'GITHUB'}
    cookie_dasw = {'cookie':{'ltoken': 'GITHUB','ltuid': '0'},'uid':0,'nome':'GITHUB'}
    cookie_nat = {'cookie':{'ltoken': 'GITHUB','ltuid': '0'},'uid':0,'nome':'GITHUB'}
    logar = [cookie_dasw,cookie_caio,cookie_nat]
    for login in logar:
        now = datetime.now(tz=tz)
        dt = now.strftime("%H")
        if '10' not in dt:
            return
        msg = await channel.send('Genshin daily')
        await genshin_impact(ctx=msg,cookie=login)  

@tasks.loop(hours=1)
async def genshin_daily_stats():
    ganyu = 'https://i.pinimg.com/736x/82/33/74/823374b1d22f2c7460ba73bce01acdc0.jpg'
    traveler = 'https://i.pinimg.com/564x/c7/7f/7b/c77f7b0bd563899146c290214263fef9.jpg'
    authkey_dasw = ''
    authkey_caio = ''
    authkey_nat = ''
    
    cookie = {'ltoken': 'GITHUB','ltuid': '0'}
    cookie_caio = {'ltoken': 'GITHUB','ltuid': '0'}#caio
    cookie_nat = {'ltoken': 'GITHUB','ltuid': '0'}
    
    auth_things_caio = {'cookie':cookie_caio,'uid':0,'avatar':traveler,'color':0x75b6bb,'discord_id':0,'authkey':authkey_caio}
    auth_things_dasw = {'cookie':cookie,'uid':0,'avatar':ganyu,'color':0xbb7575,'discord_id':0,'authkey':authkey_dasw}
    auth_things_nat = {'cookie':cookie_nat,'uid':0,'avatar':ganyu,'color':0xdd4040,'discord_id':0,'authkey':authkey_dasw}
    logar = [auth_things_caio,auth_things_dasw,auth_things_nat]
    channel = bot.get_channel(1074797822681034833)
    for login in logar:
        msg = await channel.send('Genshin info')
        await genshin_impactstats(ctx=msg,auth=login)  

@tasks.loop(hours=4)#4 horas14400
async def Stumble_Gemas():
    print(f"[{dtime.datetime.now()}]Stumble guys task")
    index = [n for n in range(len(contas['contas']))] #for loop to get all acccounts in contas.json file
    #index = [0] #for loop to get all acccounts in contas.json file
    channel = bot.get_channel(DISCORD_CHANNEL)
    try:
        for conta in index:
            a_conta = contas['contas'][conta]
            print(contas['contas'][conta]['Usuario'])
            msg = await channel.send(content=contas['contas'][conta]['Usuario'], embed=discord.Embed(color=0x990000 ,title="Iniciando 📡 [TESTES]",description="Processo para farming"))
            await logint(a_conta,msg)

    except Exception as r:
        print(r)

@bot.command()
async def toast(ctx):
    user = await bot.fetch_user('0')
    await user.send('aaa')
    await ctx.reply('aa')

async def main():
    await load()
    await bot.start(TOKEN)
    

asyncio.run(main())
