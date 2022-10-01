#Webscrapes posts from reddit and sends them to discord channels
import os
import requests
import discord
from discord.ext import commands

intents = discord.Intents().all()
client = commands.Bot(command_prefix=',', intents=intents)


@client.event
async def on_ready():
  print("Shitposter is online")

@client.command()
async def c(ctx):
  await ctx.send("This bot sends memes from certain subreddits to a discord channel")
  await ctx.send("As of version 1.0, the bot sends memes from memes, dankmemes, and shitposting")
  await ctx.send("Type ',[insert subreddit here]'... for example: ',shitpost'")

@client.command()
async def insult(ctx, task=None):
  if task.lower() == 'roland':
    await ctx.send("shut the fuck up bitch")
  elif (task.lower() == 'ashish') or (task.lower() == 'anton') or (task.lower() == 'akshay') or (task.lower() == 'devesh') or (task.lower() == 'vansh'):
    await ctx.send(f"{task} is a monkey")

@client.command()
async def shitpost(ctx):
  for subData in requests.get("https://old.reddit.com/r/shitposting.json", headers={"User-Agent": "DiscordBot"}).json()["data"]["children"]:
    await ctx.send(str(subData["data"].get("url_overridden_by_dest")))

@client.command()
async def meme(ctx):
  for subData in requests.get("https://old.reddit.com/r/memes.json", headers={"User-Agent": "DiscordBot"}).json()["data"]["children"]:
    await ctx.send(str(subData["data"].get("url_overridden_by_dest")))

@client.command()
async def dankmeme(ctx):
  for subData in requests.get("https://old.reddit.com/r/dankmemes.json", headers={"User-Agent": "DiscordBot"}).json()["data"]["children"]:
    await ctx.send(str(subData["data"].get("url_overridden_by_dest")))

@client.command()
async def subreddit(ctx, task=None):
  for subData in requests.get(f"https://old.reddit.com/r/{task}.json", headers={"User-Agent": "DiscordBot"}).json()["data"]["children"]:
    if subData["data"].get("url_overridden_by_dest") == None:
      continue
    await ctx.send(str(subData["data"].get("url_overridden_by_dest")))

client.run(os.environ['Token'])
