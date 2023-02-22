import requests,discord,time,string,hashlib,random,time as tm
from datetime import datetime

async def genshin_impact(ctx,cookie):
    try:

        now = datetime.now()
        dt = now.strftime("%H")
        print(dt)
        dt_string = now.strftime(" Hoje: %d/%m/%Y \n Hora: %H:%M:%S\n") 
        if '10' not in dt:
            return
            
        cookies = cookie['cookie']

        r = requests.post('https://hk4e-api-os.mihoyo.com/event/sol/sign?act_id=e202102251931481&lang=en-us',cookies=cookies).json()
        print(r)
        if "Traveler, you've already checked in today~" in r['message']:
            chk = '**Já pegou o daily!!**\n'
        else:
            chk = '**Daily resgatado** 😎'
        day = requests.get('https://hk4e-api-os.mihoyo.com/event/sol/info?lang=en-us&act_id=e202102251931481',cookies=cookies).json()
        print(day)
        if day['data']['total_sign_day'] in (1,6,8,13,15,20,22,27):
            imge = 'https://upload-static.hoyoverse.com/event/2021/02/25/01ba12730bd86c8858c1e2d86c7d150d_5665148762126820826.png'
        elif day['data']['total_sign_day'] in (2,9,16,23):
            imge = 'https://upload-static.hoyoverse.com/event/2021/02/25/22542ef6122f5ad4ac1c3834d11cdfb4_8505332314511574414.png'
        elif day['data']['total_sign_day'] in (3,7,10,14,17,21,24,29,30):
            imge = 'https://upload-static.hoyoverse.com/event/2021/02/25/cb0d79765ac1b39571d2e8d09e24825c_7671070233748405953.png'
        elif day['data']['total_sign_day'] in (4,11,18):
            imge = 'https://upload-static.hoyoverse.com/event/2021/02/25/f4450e0ef470f777fca0b3dd95813734_1653002626503274756.png'
        elif day['data']['total_sign_day'] in (25,28):
            imge = 'https://upload-static.hoyoverse.com/event/2021/02/25/6ef98074e6e8c9c838e144d4db496434_4740225561143115197.png'
        elif day['data']['total_sign_day'] in (5,12,19,26):
            imge = 'https://i.ebayimg.com/images/g/ZZIAAOSwXY5hMwx7/s-l500.jpg'
        embed = discord.Embed(title="Check-in daily genshin 👽",description=f"{chk} \n {dt_string} \n 👨‍💻 -> {cookie['nome']} \n 🎈 -> UID: {cookie['uid']} \n 📲 - > log retorno: ||{r['message']}||",color=0xBB7575)
        embed.set_image(url=imge)
    
        await ctx.edit(content='check-in daily', embed=embed)
    except Exception as e:
        print(e)
        await ctx.edit(content=e)

