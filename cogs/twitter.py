import requests,discord,json,re,urllib.request,os
from discord.ext import commands
from discord import app_commands



#carregar variaveis env 
from dotenv import load_dotenv
load_dotenv()

auth_multi = os.getenv('twitter_auth_multi')
auth_token = os.getenv('twitter_auth_token')
ct0 = os.getenv('twitter_ct0') #ct0 é a mesma coisa do x-csrf-token

#-----------------------



class Twitterbaixador(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name = "twitter", description = "Baixar videos do twitter")
    async def twitter(self,interaction: discord.Interaction, link:str):

        x = re.split("/status/|\?t=", link)


        cookies = {
        'auth_multi': auth_multi,
            'auth_token': auth_token,
            'ct0': ct0,
        }
        
        headers = {
            'authority': 'twitter.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-csrf-token': ct0,
        }
        
        
        focal = {"focalTweetId":x[1],"includePromotedContent":"true","withBirdwatchNotes":"false","withSuperFollowsUserFields":"true","withDownvotePerspective":"false","withReactionsMetadata":"false","withReactionsPerspective":"false","withSuperFollowsTweetFields":"true","withVoice":"true","withV2Timeline":"true"}
        
        params = {
            'variables': json.dumps(focal),
            'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true,"unified_cards_ad_metadata_container_dynamic_card_content_query_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_uc_gql_enabled":true,"vibe_api_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"interactive_text_enabled":true,"responsive_web_text_conversations_enabled":false,"responsive_web_enhance_cards_enabled":true}',
        }
        try:
            response = requests.get('https://twitter.com/i/api/graphql/BoHLKeBvibdYDiJON1oqTg/TweetDetail', params=params, cookies=cookies, headers=headers)
        except Exception as e:
            print(e)
        
        
        tweet = response.json()['data']['threaded_conversation_with_injections_v2']['instructions'][0]['entries']
        for id in tweet:
            try:
                if id['entryId'] == f'tweet-{x[1]}':
                    entities = id['content']['itemContent']['tweet_results']['result']['legacy']['extended_entities']
            except:
                await interaction.response.send_message('Não encontrei nenhuma midia')
        
        if 'media' in entities:
            ur = entities['media'][0]['video_info']['variants']
            try:
                for content_type in ur:
                    if content_type['content_type'] == 'video/mp4':
                        print('mp4')
                        print(content_type["url"])
                    
                        urllib.request.urlretrieve(content_type["url"], "V1deo_twitter_stringoff.mp4")
                
                        emb = discord.Embed(title="Download", description=f"Simplesmente um comando para baixar diretamente videos do twitter 🐦\nMp4 direto:{content_type['url']}", color=0x990000)
                        emb.set_thumbnail(url="https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg")
                        emb.set_footer(text=f"{self.bot.user.name}", icon_url="https://i.pinimg.com/564x/7c/e1/fe/7ce1feb183febb3dfbd56753b1f1cea9.jpg")
                        file = discord.File(fp="V1deo_twitter_stringoff.mp4", filename="V1deo_twitter_stringoff.mp4")
                        await interaction.response.send_message(content=f'**Link:** {link}\n**Video Id:** {x[1]}',embed=emb)
                        await interaction.followup.send(file=file)




                        break

            except Exception as Error:
                print(Error)
        
        else:
            print('não nenhuma midia')
        



async def setup(bot):
    await bot.add_cog(Twitterbaixador(bot))