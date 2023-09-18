import random
import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def carp(ctx, birinci=0, ikinci=0):
    await ctx.send(str(birinci*ikinci))


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, birinci=0, ikinci=0):
    await ctx.send(str(birinci+ikinci))


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def mem(ctx):
   resimler = (os.listdir('images'))
   img_name = random.choice(resimler)
   with open(f'images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
   await ctx.send(file=picture)

bot.run("MTE0NTc5Mzc4MDI3Mjg3NzY5OQ.G15tXz.xPsr18Ui6WP3S2tcBCDJBr1IjngCWFvXL9HAe0")
