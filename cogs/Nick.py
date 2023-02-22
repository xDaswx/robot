import discord,os,json
from discord.ext import commands
from discord import app_commands
from discord import interactions
from stumble.User.old_version import kitka as stumble


from reactionmenu import ViewMenu, ViewButton, ViewSelect, Page

#carregar variaveis env 
from dotenv import load_dotenv
load_dotenv()

USER_LOGIN = os.getenv('user_login')
KEY = os.getenv('key')
USER_EDIT = os.getenv('user_edit')
PATH_COGS = os.getenv('path_accounts')
#-----------------------

class Nick(commands.Cog):
    def __init__(self,bot):
        self.bot: commands.Bot = bot


    @commands.hybrid_command(name="nick")
    #@app_commands.command(name = "nick", description = "change username")
    async def change_nick(self,ctx: commands.Context,username:str, device:str='e2c4941f2c15a255f926a7e2527bf55f', facebookid:str='',googleid:str='') -> None:
            """
            Cmd to change the username
            """
            json_contas = open(PATH_COGS,"r")
            contas = json.load(json_contas)
            if ('e2c4941f2c15a255f926a7e2527bf55f' in device) and (facebookid,googleid == ''):
                await ctx.reply('You specified the required argument?')
                return

            user = stumble.User(device,facebookid,googleid)
            try:
                login = user.Login()
                nick = user.ChangeUsername(username)
            
                conten = f"⥼**Username antigo**: {user.Username}\n⥼**Novo Username**: {nick['new_username']}\n⥼**ID**: {user.UserId}\n⥼**Dispositivo**: {device[0:3]}...\n⥼**Google**: ...\n⥼**Facebook**: ...\n⥼**Rodando na versão**: {user.Version}\n"
            except:
                conten = f"⥼Login: {login}\n"
            nick_embed = discord.Embed(title=f"**👾 Alteração de username**", description=f'**Retorno**\n{conten}', color=0x990000)
            
            nick_embed.set_footer(text=f"{self.bot.user.name}", icon_url='')
            
            await ctx.send(content='**Local Message**',embed=nick_embed,ephemeral=True)
            await ctx.send(content=f'**Public Message\nfrom: {ctx.author.id}**',embed=discord.Embed(description=f"⥼**Old username**: {user.Username}\n⥼**New username**: {nick['new_username']}", color=0x990000))

async def setup(bot):
    await bot.add_cog(Nick(bot))
