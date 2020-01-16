import os
from discord.ext import commands

API_KEY_FILE = "apikey.txt"
API_KEY = None

try:
    with open(API_KEY_FILE, 'r') as api_file:
        API_KEY = api_file.readline().rstrip()
except FileNotFoundError:
    print(f"API key file not found, it should be called {API_KEY_FILE}")
    exit(0)

bot = commands.Bot(command_prefix='\\')

for file in os.listdir('./extensions'):
    if file.endswith('.py'):
        bot.load_extension(f'extensions.{file[:-3]}')
        print(f'loaded extension {file[:-3]}.')

bot.run(API_KEY)