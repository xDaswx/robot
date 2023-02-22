import requests,discord,os,asyncio,hashlib,time as tm
from time import time

#carregar variaveis env 
from dotenv import load_dotenv
load_dotenv()

from stumble.User.new_version import stumble
from stumble.User.old_version import kitka

#-----------------------

#-----------------------
async def logint(account_data,ctx):
    try:
        async def console_add(ctx,console_log):
            info = f"∎ **Login Information**\n{replaced}\n∎ **User Information**\n⥼ [<:levelBG:1051909995681300481>:0 <:trophy_icon:1051909439562727425>:{user.SkillRating} <:crownIcon:1051909438233116732>:{user.Crowns}]\n ⥼ [<:customizeIcon:1051912577451565098>:{len(user.Skins)} <:Emote036_TooCool:1051912579078946816>:{len(user.Emotes)}]\n ⥼ [<:Victory020_Floss_Icon:1051912582757363742>:{len(user.Animations)} <:footstepsIcon:1051912580865736835>: {len(user.Footsteps)}]\n⥼ [<:gemIcon:1051908821469102120>:{user.Gems} <:gemIcon2:1051908823163600946>:{user.Dust}]\n[<:battlePassSprite_new:1051912575694164050>] HasBattlePass: {user.HasBattlePass[0]}\n\n{console_log}"
            await ctx.edit(embed=discord.Embed(color=0x990000, title=account_data['Usuario'],description=info))


        user = kitka.User(DeviceId=account_data['DeviceId'],FacebookId=account_data['FacebookId'],GoogleId=account_data['GoogleId'])
        login = user.Login()

        if login.status_code == 403 or login.status_code == 404 or login.status_code == 400 or login.text == "BANNED":
            print('Nao foi possivel logar', login.text)
            await ctx.edit(embed=discord.Embed(color=0x990000, title="Não foi possível logar",description=f"{login.text}"))
            return

        info_json = {'Username': {user.Username}, 'UserId': {user.UserId}, 'Token': {user.Token},'DeviceId': f'||{user.DeviceId}||','GoogleId': f'||{user.GoogleId}||', 'FacebookId': f'||{user.FacebookId}||', 'StumbleId': f'||{user.StumbleId}||' }    

        aa = ''

        for key in info_json.keys():
            aa += f"⥼ **{key}**: {info_json.get(key,'None?')}\n"

        replaced = aa.replace("'","").replace("{","").replace("}","")

        Logs = f"``Logs:\nStatus: {login.status_code} {login.reason}``\n"
        info = f"∎ **Login Information**\n{replaced}\n∎ **User Information**\n⥼ [<:levelBG:1051909995681300481>:0 <:trophy_icon:1051909439562727425>:{user.SkillRating} <:crownIcon:1051909438233116732>:{user.Crowns}]\n ⥼ [<:customizeIcon:1051912577451565098>:{len(user.Skins)} <:Emote036_TooCool:1051912579078946816>:{len(user.Emotes)}]\n ⥼ [<:Victory020_Floss_Icon:1051912582757363742>:{len(user.Animations)} <:footstepsIcon:1051912580865736835>: {len(user.Footsteps)}]\n⥼ [<:gemIcon:1051908821469102120>:{user.Gems} <:gemIcon2:1051908823163600946>:{user.Dust}]\n[<:battlePassSprite_new:1051912575694164050>] HasBattlePass: {user.HasBattlePass[0]}\n\n{Logs}"

        print('Login ok', login.json()['User']['Token'])
        await ctx.edit(embed=discord.Embed(color=0x990000, title=account_data['Usuario'],description=info))


        user.FreeGems()
        Logs += f"``Balance(FreeGems) Recebeu {str(user.FreeGemsAmount)} gemas``\n"
        await console_add(ctx,Logs)

        video = user.FreeGemsVideo()
        Logs += f"``Balance(FreeGemsVideo) Recebeu {video} gemas``\n"
        await console_add(ctx,Logs)

        menu = user.FreeGemsMenu()
        Logs += f"``Balance(Menu) {menu}``\n"
        await console_add(ctx,Logs)

        spin = user.FreeGemsSpin()
        Logs += f"``Balance(Spin) Recebeu {len(spin)} itens no spin``\n"
        await console_add(ctx,Logs)

        user.WinRound()

        #spinhistory = []
        #for item in spin:
            #if 'TypeInfo' in str(spin):
                #print(f"Recebeu {item['Amount']} {item['TypeInfo']}")
                #spinhistory.append(f"Recebeu {item['Amount']} {item['TypeInfo']}\n")

        Logs += f"``Gems logs: {user.FreeGemsAmount+int(video)}+Balance(Menu)\nSpin logs: none``\n"
        await console_add(ctx,Logs)
    except Exception as e:
        print('error:', e)



