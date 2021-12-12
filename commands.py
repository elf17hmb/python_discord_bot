import discord
import random
import ascii_art
from discord.ext import commands

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def ping(context):
    await context.send(f'pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question) :
    answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')

@client.command()
async def asciify(context):
    await context.send(ascii_art.test(10))