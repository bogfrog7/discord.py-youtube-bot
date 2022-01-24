import discord
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from googleapiclient.discovery import build
from urllib.parse import urlparse

api_key = 'Your API Key'

class YoutubeChannelSearch(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="search_channel_by_username",
        description="Search for your favorite youtubers channel statistics by their username",
    )
    async def channel_name_search(self, ctx, *, username):

        youtube = build('youtube', 'v3', developerKey=api_key)

        requests = youtube.channels().list(
            part='statistics',
            forUsername=username
        )
        response = requests.execute()

        url_request = youtube.channels().list(
            part='snippet',
            forUsername=username
        )
        profile = url_request.execute()

        if response['pageInfo']['totalResults'] == 0:
            em = discord.Embed(
                title="No results found",
                description=f"There were no results found for {username} :x: ",
                colour=discord.Colour.red()
            )
            em.set_image(url='https://jonkuhrt.files.wordpress.com/2020/01/error-404-message.png')
            await ctx.send(embed=em)


        else:
            em = discord.Embed(
                title=f"{username}'s Statistics",
                description=f"{profile['items'][0]['snippet']['description']}\n",
                colour=discord.Colour.red()
            )
            em.add_field(
                name="Views ▶️",
                value=f"Views:{response['items'][0]['statistics']['viewCount']}"
            )
            em.add_field(
                name="Subscribers",
                value=f"Subscribers:{response['items'][0]['statistics']['subscriberCount']}"
            )
            em.add_field(
                name="Video Count 🎥",
                value=f"Videos: {response['items'][0]['statistics']['videoCount']}"
            )
            em.add_field(
                name="Created At",
                value=f"Time: {profile['items'][0]['snippet']['publishedAt']}"
            )
            em.add_field(
                name=f"{username}'s id",
                value=f"id: {response['items'][0]['id']}"
            )
            em.set_thumbnail(url=profile['items'][0]['snippet']['thumbnails']['default']['url'])
            await ctx.send(embed=em)

    @cog_ext.cog_slash(
        name="search_channel",
        description="Search for your favorite youtubers channel statistics by their youtube channel url",
    )
    async def search_channel(self, ctx, *, url):
        path = urlparse(url).path
        id = path.split("/")[-1]

        youtube = build('youtube', 'v3', developerKey=api_key)

        requests = youtube.channels().list(
            part='statistics',
            id=id

        )
        response =requests.execute()
        profile1 = youtube.channels().list(
            part='snippet',
            id=id
        )
        profile=profile1.execute()
        print(profile['items'][0]['snippet']['title'])

        em = discord.Embed(
            title=f"{profile['items'][0]['snippet']['title']}'s Statistics",
            description=f"{profile['items'][0]['snippet']['description']}\n",
            colour=discord.Colour.red()
        )
        em.add_field(
            name="Views ▶️",
            value=f"Views:{response['items'][0]['statistics']['viewCount']}"
        )
        em.add_field(
            name="Subscribers",
            value=f"Subscribers:{response['items'][0]['statistics']['subscriberCount']}"
        )
        em.add_field(
            name="Video Count 🎥",
            value=f"Videos: {response['items'][0]['statistics']['videoCount']}"
        )
        em.add_field(
            name="Created At",
            value=f"Time: {profile['items'][0]['snippet']['publishedAt']}"
        )
        em.set_thumbnail(url=profile['items'][0]['snippet']['thumbnails']['default']['url'])
        await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(YoutubeChannelSearch(bot))