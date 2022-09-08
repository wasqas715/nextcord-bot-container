import nextcord
import os
from nextcord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

# Set path to location of env file - this is set for in the same directory as everything else
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)



# ENV variables
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')

# Default intents for bot - default excludes privileged intents
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents = intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Enter your own commands here


bot.run(TOKEN)








