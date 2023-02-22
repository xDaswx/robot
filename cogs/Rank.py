import discord,os,json,requests
from discord.ext import commands
from discord import app_commands
from discord import interactions
from stumble.Game import game
from reactionmenu import ViewMenu, ViewButton,ViewSelect



class Ranking(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @app_commands.command(name = "rank", description = "get info about rank in game")
    async def rank(self,ctx: discord.Interaction,country:str=''):

            menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed)
            jogo = game.Game()


            r = jogo.rank(type='rank',country=country)['scores']
            r1 = jogo.rank(type='crowns',country=country)['scores']
            players = []
            i = 0
            for count, player in enumerate(r, start=1):
                if i < 60:
                  players.append(f"**{count}.**[{check_country(player['User']['Country'])}] {player['User']['Username']} ``{'{:,}'.format(player['User']['SkillRating'])}``\n")
                i +=1
            del players[0]

            players1 = []
            i1 = 0
            for count, player1 in enumerate(r1, start=1):
                if i1 < 60:
                  players1.append(f"**{count}.**[{check_country(player1['User']['Country'])}] {player1['User']['Username']} ``{'{:,}'.format(player1['User']['Crowns'])}``\n")
                i1 +=1
            del players1[0]

            contas_embed = discord.Embed(title=f"🏆 **Leaderboard**", description=f"\n🥇.[{check_country(r[0]['User']['Country'])}] {r[0]['User']['Username']} `{'{:,}'.format(r[0]['User']['SkillRating'])}`\n{''.join(players)}", color=0x990000)
            contas_embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1051909439562727425.webp")
            contas_embed.set_footer(text=f"The rank cannot be shown in full due to limits of discord", icon_url='https://cdn.discordapp.com/attachments/899490070690672650/1069400264399917106/warning-icon-png-2749.png')
            menu.add_page(contas_embed)

            contas_embed_coroas = discord.Embed(title=f"👑 **Leaderboard**", description=f"\n🥇. {r1[0]['User']['Username']} `{'{:,}'.format(r1[0]['User']['Crowns'])}`\n{''.join(players1)}", color=0x990000)
            contas_embed_coroas.set_thumbnail(url="https://cdn.discordapp.com/emojis/1051909438233116732.webp")
            contas_embed_coroas.set_footer(text=f"The rank cannot be shown in full due to limits of discord", icon_url='https://cdn.discordapp.com/attachments/899490070690672650/1069400264399917106/warning-icon-png-2749.png')
            menu.add_page(contas_embed_coroas)

            #menu.add_go_to_select(ViewSelect.GoTo(title="Ir para a pagina", page_numbers=...))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Trophies', custom_id=ViewButton.ID_GO_TO_FIRST_PAGE,emoji='🏆'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.green, label='Crowns', custom_id=ViewButton.ID_GO_TO_LAST_PAGE, emoji='👑'))
            menu.add_button(ViewButton(style=discord.ButtonStyle.red, label='Cancelar', custom_id=ViewButton.ID_END_SESSION, emoji='❌'))

            await menu.start()

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

async def setup(bot):
    await bot.add_cog(Ranking(bot))