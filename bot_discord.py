#importando as bibliotecas que fazem o robô de fato exitir
import discord
from discord import message
from discord.ext import commands 

#comandos em inglês só por boa prática

bot = commands.Bot('!')

#nessa biblioteca as funções funcionam a partir de eventos
@bot.event
async def on_ready(): #quando estiver pronto
    print(f'Estou vivo! Sou eu, {bot.user}')

@bot.event #criando as funções que enviam mensagens
async def on_message(message):
    if message.author == bot.user:
        return

    if 'buceta' in message.content:
        await message.channel.send(
           f"a luxúria é passageira {message.author.name}, mas a glória é eterna. continue firme até valhalla!"
       )

    if 'scardua' in message.content:
        await message.channel.send(
            f'mantenha-se firme {message.author.name}, este é um inimigo poderoso'
        )

    await bot.process_commands(message)


@bot.command(name='saudações') #criando a função de saudação
async def send_hello(ctx):
    name = ctx.author.name

    answer = 'Eu o saldo, ' + name

    await ctx.send(answer)


bot.run('aqui tu coloca o token do teu bot') #rodando de fato o bot
