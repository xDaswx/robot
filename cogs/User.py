import discord,os,json,asyncio
from discord.ext import commands
from discord import app_commands
from discord import interactions
from stumble.User.new_version import stumble
#from stumble.User.old_version import kitka
from stumble.Game import game

from reactionmenu import ViewMenu, ViewButton, ViewSelect, Page


#-----------------------

class User(commands.Cog):
    def __init__(self,bot):
        self.bot: commands.Bot = bot


    @commands.hybrid_command(name="user")
    async def user_api(self,ctx: commands.Context) -> None:
            """
            Auth account
            """
            async def account_exists(id,name):
                with open('user_ids.json',"r") as json_contas:
                    if await checkid(id,name) == False:
                        await ctx.send('There is no account linked to your discord')
                        return
                    contas = json.load(json_contas)
                    
                    await ctx.send(f'Your user has been found {ctx.author.mention}',delete_after=5)
                    
                    for auth in contas['accounts']:
                        if str(id) in auth['Discord_id']:
                            print('Auth Found from user:',id, name)
                            await accounts_add(auth['Accounts_auth'])
            
            
            menu = ViewMenu(ctx,menu_type=ViewMenu.TypeEmbed,name='api_login')
            userapi = discord.Embed(title="Select an account",description='free robucs 2013 accounts test')
            menu.add_page(userapi)
            
            async def login_auth(info_exist):
                await menu.message.edit(embed=discord.Embed(title='Account manager',description=f'{ctx.author}\n**Id:**{ctx.author.id}\n**Selected account:**{info_exist["AccountUsername"]}',color=discord.Color.green()))
                menu.remove_all_buttons()
                await menu.refresh_menu_items()
                
                async def returnfunction():
                    await login_menu.message.delete()
                    await login_auth(info_exist)
                return_button = ViewButton(style=discord.ButtonStyle.red, label='Refresh and login again', custom_id=ViewButton.ID_CALLER, followup=ViewButton.Followup(details=ViewButton.Followup.set_caller_details(returnfunction)),event=ViewButton.Event('disable', 1))
        
                async def free_stuff():
                    async def console_add(console_log):
                        info = f"```js\n{console_log}\n```"
                        await login_menu.update(new_pages=[discord.Embed(color=0x990000, title='Mini-console 📃',description=info)],new_buttons=None)
                    
                    async def gems_function(function):
                        login_menu.disable_button(return_button)
                        
                        if 'All Free Functions' in function:
                            Logs = ""
                            login_menu.disable_all_buttons()
                            await login_menu.refresh_menu_items()
                            await login_menu.update(new_pages=[discord.Embed(color=0x990000, title='Mini-console 📃',description='**⚙ Waiting functions...**')],new_buttons=None)
                            
                            user.FreeGems()
                            Logs += f"[{login.status_code} {login.reason}]Economy(FreeGems) Receive {str(user.FreeGemsAmount)} gems\n"
                            await console_add(Logs)
                            video = user.FreeGemsVideo()
                            Logs += f"[{login.status_code} {login.reason}]Balance(FreeGemsVideo) Receive {video} gems\n"
                            await console_add(Logs)
                            try:
                                menu =  user.FreeGemsMenu()
                                Logs += f"[{login.status_code} {login.reason}]Balance(Menu) {menu}\n"
                            except:
                                Logs += f"[{login.status_code} {login.reason}]Balance(Menu) RETURN A ERROR!📌\n"
                                await console_add(Logs)
                            spin =  user.FreeGemsSpin()
                            spinhistory = []
                            for item in spin:
                                if 'TypeInfo' in str(spin):
                                    print(f"Recebeu {item['Amount']} {item['TypeInfo']}")
                                    spinhistory.append(f"[{login.status_code} {login.reason}]Balance(Spin) Receive {item['Amount']} {item['TypeInfo']}\n")

                            Logs += f"---Balance(Spin)---\n{''.join(spinhistory)}\n"
                            await console_add(Logs)
                            login_menu.enable_button(return_button)
                            await login_menu.refresh_menu_items()                  


                    free_gems = ViewButton(style=discord.ButtonStyle.primary, label='All Free Functions',custom_id=ViewButton.ID_CALLER, followup=ViewButton.Followup(details=ViewButton.Followup.set_caller_details(gems_function,'All Free Functions')),event=ViewButton.Event('disable', 1))
                    main = discord.Embed(color=0x990000, title='Free stuff log',description=f'Free gems amount to receive: {user.FreeGemsAmount_get}')
                    await login_menu.update(new_pages=[main],new_buttons=[free_gems,return_button])
                
                async def friend_management():
                    async def log_creator(input):
                        return [f"[{friend_info.get('userId','???')}] {friend_info.get('userName','???')}｜{str(friend_info.get('isOnline','???')).replace('True','🟩').replace('False','🟥')}｜{friend_info.get('skin','???')}\n" for friend_info in input]

                    #pages
                    friend_get = user.Friends()
                    friend_request = user.friend_getrequests()

                    all_friends = await log_creator(friend_get['friends'])
                    all_friend_request = await log_creator(friend_request['requests'])
                    
                    main_friend = discord.Embed(color=0x990000, title='Friend Management',description=f"ID｜USERNAME｜ONLINE｜SKIN\n```\n{''.join(all_friends)}\n```")
                    main_requests_friend = discord.Embed(color=0x990000, title='Friend Management',description=f"ID｜USERNAME｜ONLINE｜SKIN\n```\n{''.join(all_friend_request)}\n```")
                    #button pages

                    button_friend_list = ViewButton(style=discord.ButtonStyle.green, label='Friend list',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=main_friend))
                    button_friend_get_requests = ViewButton(style=discord.ButtonStyle.green, label='Get Friend request',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=main_requests_friend))
            
                    await login_menu.update(new_pages=[main_friend,main_requests_friend], new_buttons=[button_friend_list,button_friend_get_requests,return_button])
                async def items():
                    server = game.Game()
                    server.shared()
                    skins_names = {skin.get('SkinID','Wrong skin id'):skin.get('FriendlyName','Wrong skin name') for skin in server.Skins_v4}
                    emotes_names = {emote.get('ID','Wrong skin id'):emote.get('FriendlyName','Wrong skin name') for emote in server.Emotes}
                    animations_names = {anim.get('ID','Wrong skin id'):anim.get('FriendlyName','Wrong skin name') for anim in server.Animations}
                    footsteps_names = {foot.get('ID','Wrong skin id'):foot.get('FriendlyName','Wrong skin name') for foot in server.Footsteps}
                    f = open('emojis.json','r') 
                    mojiload = json.load(f)
                    skins = [f"[{mojiload.get(f'{str(skin).lower()}_icon','??')}]{skins_names.get(skin,'???')}\n" for skin in user.Skins if skin in skins_names]
                    f.close()

                    emotes = [f"[{emote}] {emotes_names.get(emote,'???')}\n" for emote in user.Emotes if emote in emotes_names]
                    animations = [f"[{animm}] {animations_names.get(animm,'???')}\n" for animm in user.Animations if animm in animations_names]
                    footsteps =  [f"[{foote}] {footsteps_names.get(foote,'???')}\n" for foote in user.Footsteps if foote in footsteps_names]
                    embed_skins = discord.Embed(title='Skins',description=f'{"".join(skins[0:80])}',color=discord.Color.green())
                    embed_skins.set_footer(text=f'{len(user.Skins)} skins total! [{len(skins[0:80])} in this page]')
                    embed_skins_2 = discord.Embed(title='Skins#2')
                    button_skins_2 = ViewButton(style=discord.ButtonStyle.gray, label='Skin page #2',disabled=True)
                    embed_skins_3 = discord.Embed(title='Skins#3')
                    button_skins_3 = ViewButton(style=discord.ButtonStyle.gray, label='Skin page #3',disabled=True)
                    embed_skins_4 = discord.Embed(title='Skins#4')
                    button_skins_4 = ViewButton(style=discord.ButtonStyle.gray, label='Skin page #4',disabled=True)
                    
                    if len(skins) > 80:
                        embed_skins_2 = discord.Embed(title='Skins#2',description=f'{"".join(skins[80:160])}',color=discord.Color.green())
                        embed_skins_2.set_footer(text=f'{len(user.Skins)} skins total! [{len(skins[80:160])} in this page]')
                        button_skins_2 = ViewButton(style=discord.ButtonStyle.green, label='Skin page #2',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=embed_skins_2))

                    if len(skins) > 160:
                        embed_skins_3 = discord.Embed(title='Skins#3',description=f'{"".join(skins[160:240])}',color=discord.Color.green())
                        embed_skins_3.set_footer(text=f'{len(user.Skins)} skins total! [{len(skins[160:240])} in this page]')
                        button_skins_3 = ViewButton(style=discord.ButtonStyle.green, label='Skin page #3',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=embed_skins_3))
                    
                    if len(skins) > 240:
                        embed_skins_4 = discord.Embed(title='Skins#4',description=f'{"".join(skins[240:])}',color=discord.Color.green())
                        embed_skins_4.set_footer(text=f'{len(user.Skins)} skins total! [{len(skins[240:])} in this page]')
                        button_skins_4 = ViewButton(style=discord.ButtonStyle.green, label='Skin page #4',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=embed_skins_4))

                    embed_emotes = discord.Embed(title='Emotes',description=f'{"".join(emotes)}',color=discord.Color.green())
                    embed_animations = discord.Embed(title='Animations',description=f'{"".join(animations)}',color=discord.Color.green())
                    embed_footsteps = discord.Embed(title='Footsteps',description=f'{"".join(footsteps)}',color=discord.Color.green())
                    
                    button_skins = ViewButton(style=discord.ButtonStyle.green, label='Skin page #1',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=embed_skins))
                    
                    button_emotes = ViewButton(style=discord.ButtonStyle.green, label='Emotes list',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=embed_emotes))
                    button_animations = ViewButton(style=discord.ButtonStyle.green, label='Animations list',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=embed_animations))
                    button_footsteps = ViewButton(style=discord.ButtonStyle.green, label='Footsteps list',custom_id=ViewButton.ID_CUSTOM_EMBED, followup=ViewButton.Followup(embed=embed_footsteps))
                    await login_menu.update(new_buttons=[button_skins,button_skins_2,button_skins_3,button_skins_4,button_emotes,button_animations,button_footsteps,return_button], new_pages=[embed_skins,embed_skins_2,embed_skins_3,embed_skins_4,embed_emotes,embed_animations,embed_footsteps])
                
                login_menu = ViewMenu(ctx,menu_type=ViewMenu.TypeEmbed,name='login_menu')
                user = stumble.User_debug(DeviceId=info_exist['Stumble_deviceId_1'],StumbleId_login=info_exist['STUMBLE_ID'],Version='0.45.1')

                try:
                    login = user.Login()
                except ValueError:
                    await ctx.send('Wait 3s')
                    await asyncio.sleep(3)
                    login = user.Login()
                
                if login.status_code == 403 or login.status_code == 404 or login.status_code == 400 or login.text == "BANNED":
                    print('Nao foi possivel logar', login.text)
                    await ctx.send(embed=discord.Embed(color=0x990000, title="Não foi possível logar",description=f"{login.text}"))
                    return
                
                info_json = {'Username': user.Username, 'UserId': user.UserId, 'Token': user.Token,'DeviceId': user.DeviceId,'GoogleId': user.GoogleId, 'FacebookId': f'{user.FacebookId}', 'StumbleId': user.StumbleId}    
                aa = ''
                
                for key in info_json.keys():
                    aa += f"⥼ **{key}**: {info_json.get(key,'None?')}\n"
                replaced = aa.replace("'","").replace("{","").replace("}","")
                Logs = f"``Logs:\nStatus: {login.status_code} {login.reason}``\n``Free gems amount to receive: {user.FreeGemsAmount_get}``\n``Gems2 var: {user.special_video_amount}``"
                info = f"\n⥼ **Linked to:** {ctx.author.name}\n⥼ **Username:** spoof\n⥼ **AccountId:** spoof\n\n**User Information**\n⥼ [<:levelBG:1051909995681300481>:0 <:trophy_icon:1051909439562727425>:{user.SkillRating} <:crownIcon:1051909438233116732>:{user.Crowns}]\n ⥼ [<:customizeIcon:1051912577451565098>:{len(user.Skins)} <:Emote036_TooCool:1051912579078946816>:{len(user.Emotes)}]\n ⥼ [<:Victory020_Floss_Icon:1051912582757363742>:{len(user.Animations)} <:footstepsIcon:1051912580865736835>: {len(user.Footsteps)}]\n⥼ [<:gemIcon:1051908821469102120>:{user.Gems} <:gemIcon2:1051908823163600946>:{user.Dust}]\n[<:battlePassSprite_new:1051912575694164050>] HasBattlePass: {user.HasBattlePass[0]}\n\n{Logs}"
                info_secret = f"**Login Information**\n{replaced}\n∎ Do not show this information to anyone."
                print('Login ok', login.json()['User']['Token'])
                await ctx.send(embed=discord.Embed(color=0x990000, title='Account login info ⚠',description=info_secret),ephemeral=True)
                
                login_menu.add_page(discord.Embed(color=0x990000, title=info_exist['AccountUsername'],description=f'{info}\n⚠ this command is still under development, so errors may still happen'))
                #buttons add
                free_stuff_followup = ViewButton.Followup(details=ViewButton.Followup.set_caller_details(free_stuff))
                login_menu.add_button(ViewButton(style=discord.ButtonStyle.primary, label='Free stuff', custom_id=ViewButton.ID_CALLER, followup=free_stuff_followup,event=ViewButton.Event('disable', 1),emoji='🆓',))
                
                friend_management_followup = ViewButton.Followup(details=ViewButton.Followup.set_caller_details(friend_management))
                login_menu.add_button(ViewButton(style=discord.ButtonStyle.primary, label='Friend Management', custom_id=ViewButton.ID_CALLER, followup=friend_management_followup,event=ViewButton.Event('disable', 1),emoji='🧩'))
                
                #friend_management_followup = ViewButton.Followup(details=ViewButton.Followup.set_caller_details(friend_management))
                login_menu.add_button(ViewButton(style=discord.ButtonStyle.primary, label='Rounds thing [doenst exists]',emoji='😳',custom_id=ViewButton.ID_CALLER, followup=friend_management_followup,event=ViewButton.Event('disable', 1)))
                login_menu.add_button(ViewButton(style=discord.ButtonStyle.primary, label='Account Management [doenst exists]',emoji='⚙',custom_id=ViewButton.ID_CALLER, followup=friend_management_followup,event=ViewButton.Event('disable', 1)))
                login_menu.add_button(ViewButton(style=discord.ButtonStyle.primary, label='BattlePasses [doenst exists]',emoji='👑',custom_id=ViewButton.ID_CALLER, followup=friend_management_followup,event=ViewButton.Event('disable', 1)))
                login_menu.add_button(ViewButton(style=discord.ButtonStyle.primary, label='Shop [doenst exists]',emoji='👑',custom_id=ViewButton.ID_CALLER, followup=friend_management_followup,event=ViewButton.Event('disable', 1)))
                
                items_followup = ViewButton.Followup(details=ViewButton.Followup.set_caller_details(items))
                login_menu.add_button(ViewButton(style=discord.ButtonStyle.primary, label='Account items',emoji='<:customizeIcon:1051912577451565098>',custom_id=ViewButton.ID_CALLER, followup=items_followup,event=ViewButton.Event('disable', 1)))
                await login_menu.start()
               

            async def accounts_add(accounts):
                #junk code beaucs im lazy
                for index, account in enumerate(accounts):
                    call_followup = ViewButton.Followup(details=ViewButton.Followup.set_caller_details(login_auth, account))
                    botao = ViewButton(style=discord.ButtonStyle.green, label=account['AccountUsername'],custom_id=ViewButton.ID_CALLER, followup=call_followup,event=ViewButton.Event('disable', 1))
                    menu.add_button(botao)
                await menu.start()
                
                
                """
                                if len(accounts) >= 2:
                    call_followup = ViewButton.Followup(details=ViewButton.Followup.set_caller_details(login_auth, accounts[0]))
                    botao = ViewButton(style=discord.ButtonStyle.green, label=accounts[0]['AccountUsername'],custom_id=ViewButton.ID_CALLER, followup=call_followup,event=ViewButton.Event('disable', 1))
                    menu.add_button(botao)
                    
                    call_followup_2 = ViewButton.Followup(details=ViewButton.Followup.set_caller_details(login_auth, accounts[1]))
                    botao_2 = ViewButton(style=discord.ButtonStyle.green, label=accounts[1]['AccountUsername'],custom_id=ViewButton.ID_CALLER, followup=call_followup_2,event=ViewButton.Event('disable', 1))
                    menu.add_button(botao_2)
                    await menu.start()
                else: 
                    call_followup = ViewButton.Followup(details=ViewButton.Followup.set_caller_details(login_auth, accounts[0]))
                    botao = ViewButton(style=discord.ButtonStyle.green, label=accounts[0]['AccountUsername'],custom_id=ViewButton.ID_CALLER, followup=call_followup,event=ViewButton.Event('disable', 1))
                    menu.add_button(botao)
                    await menu.start()
                
                """

            
            async def checkid(id,name):
                with open('user_ids.json',"r") as json_contas:
                    if str(id) in json_contas.read():
                        print('found:',id, name)
                    else:
                        print('not found:',id, name)
                        return False
            
            await account_exists(id=str(ctx.author.id), name=ctx.author.name)
            

async def setup(bot):
    await bot.add_cog(User(bot))
