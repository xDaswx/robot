import requests,discord,time,string,hashlib,random,time as tm
from discord.ext import commands
from datetime import datetime
dicte = {
    'active_day_number':'Dias jogados',
    'achievement_number':'Conquistas',
    'anemoculus_number':'Anemoculus',
    'geoculus_number':'Geoculus',
    'avatar_number':'Personagens',
    'way_point_number':'Waypoints',
    'domain_number':'Dominios',
    'spiral_abyss':'Abismo',
    'precious_chest_number':'Baus preciosos',
    'luxurious_chest_number':'Baus luxuosos',
    'exquisite_chest_number':'Baus requintados',
    'common_chest_number':'Baus comuns',
    'electroculus_number':'Electroculus',
    'magic_chest_number':'Magic chests',
    'dendroculus_number':'Dendroculus'
}

reason = {
    '31':'Craft',
    '52':'Domínios',
    '26':'Diaria premio',
    '27':'Missão diaria',
    '27':'Missão diaria',
    '1046':'Teste de person',
    '1046':'Teste de person',
    '4':'Compra na loja ou gacha',
    '67':'Evento premio'
}

async def genshin_impactstats(ctx,auth) -> str:
    cookies = auth['cookie']
    authkey = auth['authkey']
    try:
        async def generate_ds(salt: str) -> str:
            """Creates a new ds for authentication."""
            t = int(time.time())  # current seconds
            r = "".join(random.choices(string.ascii_letters, k=6))  # 6 random chars
            h = hashlib.md5(f"salt={salt}&t={t}&r={r}".encode()).hexdigest()  # hash and get hex
            return f"{t},{r},{h}"
        headers = {
            'ds': await generate_ds('6s25p5ox5y14umn1p61aqyyvbvvl3lrt'),#hash da rpc-client 5 = 6s25p5ox5y14umn1p61aqyyvbvvl3lrt 
            #'ds':'1676329113,GadGkT,4806330acee3fca984b6bf810c44324c',
            #hash da rpc client 4 = 6cqshh5dhw73bzxn20oexa9k516chk7s
            #'ds': '1676318831,AknP6J,4eb5f3830eb621dfa96f8f0cb8bfc85c',
            'x-rpc-app_version': '1.5.0',
            'x-rpc-client_type': '5',
            'x-rpc-language': 'en-us',
        }
        async def historylogin():
            cookies = {'mi18nLang': 'pt-pt'}
            get = requests.get(f'https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?&authkey_ver=1&sign_type=2&gacha_id=571ac4874a65c05ac8f32fb247494ff987c5be14&lang=pt&authkey={authkey}&gacha_type=301&size=20',cookies=cookies)
            return get.text

            #https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie

        async def logs():
            #card/wapi/getGameRecordCard
            #https://mi18n-os.hoyoverse.com/webstatic/admin/mi18n/hk4e_global/m02251421001311/m02251421001311-en-us.json
            return 
        async def gachalog():
            cookies = {'mi18nLang': 'pt-pt'}
            get = requests.get(f'https://hk4e-api-os.hoyoverse.com/event/gacha_info/api/getGachaLog?&authkey_ver=1&sign_type=2&gacha_id=571ac4874a65c05ac8f32fb247494ff987c5be14&lang=pt&authkey={authkey}&gacha_type=301&size=70',cookies=cookies)
            return get.text
        async def get_log(get):
            #getPrimogemLog
            #getCrystalLog
            #getResinLog
            #getArtifactLog
            #getWeaponLog
            cookies = {'mi18nLang': 'pt-pt'}
            
            gete = requests.get(f'https://hk4e-api-os.hoyoverse.com/ysulog/api/{get}?&authkey_ver=1&sign_type=2&gacha_id=571ac4874a65c05ac8f32fb247494ff987c5be14&lang=pt&authkey={authkey}&gacha_type=301&size=20',cookies=cookies)
            if 'authkey' in gete.json()['message']:
                return 'Erro de autenticação ao servidor, favor reiniciar'
            return [f'[{item.get("time")}] {item.get("add_num")} {reason.get(item["reason"],"???")}\n' for item in gete.json()['data']['list']]
        
        async def resin_info(uid):
            resin = requests.get(f'https://bbs-api-os.hoyolab.com/game_record/genshin/api/dailyNote?server=os_usa&role_id={uid}',cookies=cookies,headers=headers)
            return resin.json()['data']

        #https://bbs-api-os.hoyolab.com/game_record/genshin/api/dailyNote?server=os_usa&role_id=603196971 get resina
        uid = auth['uid']#list 0 que fica o uid do player
        req = requests.get(f'https://bbs-api-os.hoyolab.com/game_record/genshin/api/index?server=os_usa&role_id={uid}',cookies=cookies,headers=headers)
        if ('invalid request' or 'Please login' or 'Data is not public for the user') in req.json()['message']:
            print(req.text)
            await ctx.edit(content='errrorrr')
            return
        daily = await resin_info(uid)
        if None in daily:
             await ctx.edit(content='errrorrr in dailyyyy')
        getsimple = req.json()['data']['role']
       
        expedições = [0 for exped in daily['expeditions'] if 'Finished' in exped.get('status')]

        userinfo = [f"* {dicte.get(item)}: `{req.json()['data']['stats'][item]}`\n" for item in req.json()['data']['stats']]

        userdaily = f"- Resinas: `{daily['current_resin']}` cheio em {int(int(daily['resin_recovery_time'])/3600)}hrs \n- Missões diarias completadas hoje: `{daily['finished_task_num']}`\n- Expedições resgatar: `{len(expedições)}`\n- Bule resgatar: `{daily['current_home_coin']}` moedas\n- Bule maximo: `{daily['max_home_coin']}` moedas\n- Transformador paramétrico : `{str(daily['transformer']['recovery_time'].get('reached')).replace('False','⛔').replace('True','✅')}`"

        embed =  discord.Embed(title=f"{getsimple['nickname']} - {getsimple['level']} - {getsimple['region']}", color=auth['color'])#config 2 é a cor em hexadecimal

        embed.add_field(name='Account Info',value=f'{"".join(userinfo)}',inline=True)
        embed.add_field(name='Informações de agora',value=userdaily,inline=True)
        primolog = await get_log('getPrimogemLog')
        resinlog = await get_log('getResinLog')
        artlo = await get_log('getArtifactLog')

        embed.add_field(name='Logs Primogens',value=f'```\n{"".join(primolog)}\n```',inline=False)
        embed.add_field(name='Logs Resina',value=f'```\n{"".join(resinlog)}\n```',inline=False)
        #embed.add_field(name='Logs Resina',value=f'```\n{"".join(artlo)}\n```',inline=False)
        embed.set_thumbnail(url=auth['avatar'])
        await ctx.edit(content=f'<@{auth["discord_id"]}> você precisa gastar suas resinas, já chegou ao estoque máximo.' if '160' in str(daily['current_resin']) else 'Nada a notificar',embed=embed)
    except Exception as e:
        print(e)
        await ctx.edit(content=f'{Exception} {e}')




