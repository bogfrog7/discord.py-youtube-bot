import discord
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from googleapiclient.discovery import build
from urllib.parse import urlparse


API_KEY = 'YOUR API KEY'

class YoutubePlaylistFinder(Cog):
    def __init__(self,bot: Bot):
        self.bot = bot


    @cog_ext.cog_slash(
        name="find_playlist",
        description="finds the playlist based on your favorite youtubers channel url",
    )
    async def find_playlist(self,ctx,channel_url):

        youtube = build('youtube', 'v3', developerKey=API_KEY)

        path = urlparse(channel_url).path
        id = path.split("/")[-1]
        print(id)

        request = youtube.playlists().list(
            part='contentDetails, snippet',
            channelId=id,
        )
        response = request.execute()
        print(response['items'])

        for items in response['items']:
            duration = 5

            title = items['snippet']['title']
            print(title)
            em = discord.Embed(
                title=f"{title}",
                description=items['snippet']['description']
            )
            em.set_thumbnail(
                url=f"{items['snippet']['thumbnails']['medium']['url']}"
            )
            await ctx.author.send(embed=em)
            em.set_footer(text=f'Sent in {duration}')
        await ctx.send(f'{ctx.author.mention} I sent you the list of playlists')




def setup(bot):
    bot.add_cog(YoutubePlaylistFinder(bot))