#importando as bibliotecas que fazem o robô de fato exitir
import discord
from discord import message
from discord import channel
from discord.ext import commands, tasks 
import datetime #biblioteca para trabalhar com data e hora no python

#comandos em inglês só por boa prática

bot = commands.Bot('!')

#nessa biblioteca as funções funcionam a partir de eventos

#evento de quando o bot funciona
@bot.event
async def on_ready(): #quando estiver pronto
    print(f'Estou vivo! Sou eu, {bot.user}')

    current_time.start()

@bot.event #criando as funções que enviam mensagens
async def on_message(message):
    if message.author == bot.user:
        return

    if 'buceta' in message.content:
        await message.channel.send(
           f"a luxúria é passageira {message.author.name}, mas a glória é eterna. continue firme até valhalla!"
       )

    if 'engenharia e ambiente' in message.content:
        await message.channel.send(
            f'mantenha-se firme {message.author.name}, este é um inimigo poderoso'
        )

    await bot.process_commands(message)


@bot.command(name='saudações') #criando a função de saudação
async def send_hello(ctx):
    name = ctx.author.name

    answer = 'Eu o saldo, ' + name

    await ctx.send(answer)

@tasks.loop(hours=24)
async def current_time(): #definir o que vai acontecer    
    now = datetime.datetime.now() #pega o horário atual

    now = now.strftime("%d/%m/%Y às %H:%M:%S")   #stringformattime pega dia mes e ano

    channel = bot.get_channel('id do channel que tu quiser que o bot use')

    await channel.send("ESTUDEM!")


bot.run('teu token') #rodando de fato o bot
