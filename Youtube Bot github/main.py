from discord import Intents
from discord.ext.commands import Bot
from discord_slash import SlashCommand
import os

bot = Bot(command_prefix="!", self_bot=True,intents=Intents.default())
slash = SlashCommand(bot,sync_commands=True)

for filename in os.listdir('Commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'Commands.{filename[:-3]}')



bot.run('TOKEN')
