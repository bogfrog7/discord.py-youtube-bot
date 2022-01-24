import discord
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice,create_option
from googleapiclient.discovery import build
import urllib.parse as p

API_KEY = 'YOUR API KEY'


class YoutubeVideoSearch(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    @cog_ext.cog_slash(
        name="search_video",
        description="Search your favorite youtube video and get its statistics",
    )
    async def search_video(self,ctx,video_url):

        youtube = build('youtube', 'v3', developerKey=API_KEY)

        # split URL parts
        parsed_url = p.urlparse(video_url)
        # get the video ID by parsing the query of the URL
        video_id = p.parse_qs(parsed_url.query).get("v")

        requests = youtube.videos().list(
            part='statistics',
            id=video_id
        )
        response = requests.execute()


        request2 = youtube.videos().list(
            part='snippet',
            id=video_id
        )
        response2 = request2.execute()

        if int(response["items"][0]["statistics"]["likeCount"]) > 1000000:

            em = discord.Embed(
                title=f"{response2['items'][0]['snippet']['title']}",
                description="This video has more than 1,000,000 likes :partying_face:",
                colour=discord.Colour.red()
            )
            em.add_field(
                name="Views",
                value=f'views: {response["items"][0]["statistics"]["viewCount"]}'
            )
            em.add_field(
                name="Likes",
                value=f'Likes:{response["items"][0]["statistics"]["likeCount"]}'
            )
            em.add_field(
                name="Dislikes",
                value=f'Dislikes: No information'
            )
            em.add_field(
                name="Comments",
                value=f'comment count:{response["items"][0]["statistics"]["commentCount"]}'
            )
            em.set_thumbnail(
                url=f"{response2['items'][0]['snippet']['thumbnails']['medium']['url']}"
            )
            await ctx.send(embed=em)
        else:
            em = discord.Embed(
                title=f"{response2['items'][0]['snippet']['title']}",
                colour=discord.Colour.red()
            )
            em.add_field(
                name="Views",
                value=f'views: {response["items"][0]["statistics"]["viewCount"]}'
            )
            em.add_field(
                name="Likes",
                value=f'Likes:{response["items"][0]["statistics"]["likeCount"]}'
            )
            em.add_field(
                name="Dislikes",
                value=f'Dislikes: No information'
            )
            em.add_field(
                name="Comments",
                value=f'comment count:{response["items"][0]["statistics"]["commentCount"]}'
            )
            em.set_thumbnail(
                url=f"{response2['items'][0]['snippet']['thumbnails']['medium']['url']}"
            )
            await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(YoutubeVideoSearch(bot))