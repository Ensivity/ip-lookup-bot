import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
ipinfo_api_token = "2f3df9fe7b7604"
ip = "37.201.7.226"

token = "MTA1OTE5NTU0NDYyODY0MTkwMw.G8jkDO.LeGKcR_AbvQe4pPaGFiAodetS9P2oMrsAzDqPQ"
bot = commands.Bot(command_prefix='+', intents=intents)


@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = "+lookup IP to lookup !",
        url = 'https://www.twitch.tv/twitch'
    )
    await bot.change_presence(activity=stream)



@bot.command()
async def lookup(ctx, args):
	ipinfo_api_link = f"https://ipinfo.io/{args}?token={ipinfo_api_token}"
	look = requests.get(f"{ipinfo_api_link}")
	await ctx.send(f"""```{look.text}```""")

bot.run(token)

#Dev by Muzu#7983
