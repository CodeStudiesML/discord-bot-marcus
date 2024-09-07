import discord
from discord.ext import commands
import requests
import json
import random

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='/', intents=intents)

def get_dog_image():
  response = requests.get('https://dog.ceo/api/breeds/image/random')
  json_data = json.loads(response.text)
  return json_data["message"]

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Game(name="@marcusaw")
    )
    print(f'Conectado como: {bot.user}')
    await bot.tree.sync()

@bot.hybrid_command(name="avatar", description="Ve a sua foto de perfil, ou de um Usuario marcado")
async def avatar(ctx: commands.Context, user: discord.User = None):
    if user is None:
        user = ctx.author
    await ctx.send(user.avatar.url)

@bot.hybrid_command(name="dog", description="Uma imagem aleatoria de um cachorro :)")
async def dog(ctx: commands.Context):
    await ctx.send(get_dog_image())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.strip().lower().startswith('oi kenji'):
        listHi = [f'Iae {message.author.mention}', f'Fala {message.author.mention}, como vai?',f'Só de boa {message.author.mention}?']
        await message.channel.send(random.choice(listHi))


bot.run('TOKEN')