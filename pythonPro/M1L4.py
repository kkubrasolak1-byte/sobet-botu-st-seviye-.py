import discord
import os
from discord.ext import commands
import random
from pathlib import Path
import requests

import download_sound

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(
        f'{member.name} joined {discord.utils.format_dt(member.joined_at)}'
    )


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send(
            "Geçersiz zar formatı! Lütfen NdN formatında bir zar belirtin."
        )
        return

    result = ', '.join(
        str(random.randint(1, limit))
        for r in range(rolls)
    )

    await ctx.send(result)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    if not choices:
        await ctx.send("Bir seçim yazmalısın!")
        return

    await ctx.send(random.choice(choices))


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Yes, {ctx.subcommand_passed} is cool')


@bot.command()
async def mem(ctx):
    im_list = os.listdir('images')
    img_name = random.choice(im_list)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command()
async def kubra(ctx):
    im_list = os.listdir('kendimin')
    img_name = random.choice(im_list)
    with open(f'kendimin/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''dog komutunu çağırdığımızda, program köpek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_anime_image_url():    
    url = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
    res = requests.get(url)
    data = res.json()
    sec=random.randint(0, len(data['data']) - 1)
    return data['data'][sec]['attributes']['posterImage']['original']

@bot.command('anime')
async def anime(ctx):
    '''anime komutunu çağırdığımızda, program anime_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_anime_image_url()
    await ctx.send(image_url)


@bot.command('tirt')
async def tirt(ctx):
    '''tirt komutunu çağırdığımızda, bot tirt ses efektini gönderir.'''
    try:
        with open('sounds/tirt.mp3', 'rb') as f:
            sound = discord.File(f)
            await ctx.send(file=sound)
    except FileNotFoundError:
        #download_sound.py dosyasını çalıştırarak ses dosyasını indir
        download_sound.download_sound()
        await ctx.send("Ses dosyası bulunamadı!")


bot.run("token")