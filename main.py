import discord
from discord.ext import commands
import calc
import bs4_scraper
import random
# import selenium_scraper
import googlebooks

client = commands.Bot(command_prefix='.')
TOKEN = 'NzE4Nzk5MDI4NDcyNzc0NjU2.XtuMHw.E7Zc1g3TrKOxXbAIX_bEfY-jmIQ'

@client.event
async def on_connect():
    print("Bot successfully connected to Discord")

@client.event
async def on_ready():
    print("Bot is ready...")
@client.event
async def on_disconnect():
    print("Bot has disconnected")
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.event
async def on_message(message):
    starts = ("Hello", "hello", "Hi", "hi", "Hey", "hey")
    thanks = ('Thanks', "thanks", "thank you", "Thank you")
    end = ('Bye', 'bye', 'tata', 'TATA', 'Tata', 'cya', 'Cya')
    am = ('i am', 'im', "i'm", 'I am', "I'm", 'Im')
    if message.author == client.user:
        return
    if message.content == "you":
        return
    if message.content.startswith(starts):
        await message.channel.send("Hello!")
    if message.content.startswith(thanks):
        await message.channel.send("Pleasure!")
    if message.content.startswith(end):
        await message.channel.send("Bye! Come back soon...")
    if message.content.startswith(am):
        await message.channel.send(f"Hi! I am Earnest...")
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def exe(ctx, *, inp:str):
    if "(" in inp:
        result = calc.brac(inp)
    else:
        result = calc.evaluate(inp)
    await ctx.send(result)

@exe.error
async def exe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please input an expression")

@client.command()
async def mustread(ctx):
    num = random.randint(0, len(bs4_scraper.books)) - 1
    book = bs4_scraper.books[num][0] + ' by ' + bs4_scraper.books[num][1]
    await ctx.send(book)

# @client.command()
# async def find(ctx, *, message):
#     desc = selenium_scraper.book_desc(message)
#     for i in desc:
#         await ctx.send(i)

@client.command()
async def allbooks(ctx):
    for i in bs4_scraper.books:
        await ctx.send(i)

@client.command()
async def quote(ctx):
    num = random.randint(0, len(bs4_scraper.quotes_list)) - 1
    text = bs4_scraper.quotes_list[num]
    await ctx.send(text)

@client.command()
async def book(ctx, *, search):
    details = googlebooks.info(search)
    for items in details:
        await ctx.send(items)

@client.command()
async def cover(ctx, *, search):
    image = googlebooks.other(search)
    await ctx.send(image)

# @client.command()
# async def gif(ctx, *, message):
#     url = selenium_scraper.gify(message)
#     await ctx.send(url)

@client.command()
async def context(ctx):
  await ctx.send(f"You are in {ctx.guild.name}")
  await ctx.send(f"You are in {ctx.channel.mention}")
  await ctx.send(f"You are {ctx.author.mention}")
  await ctx.send(f"Original message was {ctx.message.content}")
  await ctx.send(f'Bot is {ctx.bot}')

client.run(TOKEN)