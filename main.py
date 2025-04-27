import os
from config import *
import disnake
from disnake.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), intents=disnake.Intents.all(), test_guilds=[1140249059991498892])
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    guild = client.get_guild(1140249059991498892)
    voice_channel = guild.get_channel(1242871121695477881)
    if voice_channel:
        if guild.voice_client is None:
            await voice_channel.connect()

@client.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=1242870758544244806)
    await member.add_roles(role)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("MTI0NzkzODgxMzk1OTg2NDM3Mw.G5zhk2.PvDWhb6w0lnVhg9eFJ77Gvgjmf4PmdP0pe1P1U")
