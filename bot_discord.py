#importando as bibliotecas que fazem o robô de fato exitir
import discord
from discord import message
from discord import channel
from discord.ext import commands, tasks 
import datetime #biblioteca para trabalhar com data e hora no python
import pandas as pd

#comandos em inglês só por boa prática

bot = commands.Bot('!') #definindo como vou chamar o brabo

#nessa biblioteca as funções funcionam a partir de eventos

#evento de quando o bot funciona
@bot.event
async def on_ready(): #quando estiver pronto
    print(f'Estou vivo! Sou eu, {bot.user}')

    """ current_time.start() """

@bot.event #criando as funções que enviam mensagens
async def on_message(message): # função assíncrona que é executada sempre que uma mensagem é enviada
    if message.author == bot.user:
        return

    if 'p!porngif' in message.content:
        await message.channel.send(
           f"a luxúria é passageira {message.author.name}, mas a glória é eterna. continue firme até valhalla!"
       )

    if 'desistir' in message.content:
        await message.channel.send(
            f'mantenha-se firme {message.author.name}, logo jantaremos no mesmo salão'
        )

    await bot.process_commands(message)


@bot.command(name='saudações') #criando a função de saudação
async def send_hello(ctx):
   
    name = ctx.author.name

    answer = 'Eu o saldo, ' + name

    await ctx.send(answer)

@bot.command(name='calcule')       #o asterisco antes de expression quer dizer que quero que pegue todos os argumentos como uma unica express
async def calculete_expression(ctx, *expression): #sempre tem que passar o contexto no comando, mesmo eu querendo a expressão
    expression = "".join(expression) #meio que crio uma string vazia e adiciono cada elemento de uma 'lista que não é lista' nessa string
    
    response = eval(expression) #a função eval tenta sempre executar e interpretar seu argumento
    
    
    await ctx.send('Eis o resultado:' + str(response))


 @tasks.loop(hours=24)
async def current_time(): #definir o que vai acontecer    
    now = datetime.datetime.now() #pega o horário atual

    now = now.strftime("%d/%m/%Y às %H:%M:%S")   #stringformattime pega dia mes e ano

    channel = bot.get_channel(ID do canal que tu quiser)

    await channel.send("ESTUDEM!") 


bot.run('teu token') #rodando de fato o bot

