import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands, tasks
from config import *
import asyncio
import datetime
import time

class Clear(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.inter = iter
        
    @commands.slash_command(name='clear',description='Удалить кол-во сообщений')
    @commands.has_any_role(MODER, ADMIN, CURATOR, SECURITY)
    async def clear(self, inter, number: commands.Range[1, 99] = commands.Param(name="сообщений")):
        await inter.channel.purge(limit=number)
        embed = disnake.Embed(title='Очистка сообщений', description=f'{inter.author.mention}, Вы **успешно** очистили **{number}** сообщений.',  color=0x2f3136)
        embed.set_thumbnail(url=inter.author.display_avatar)
        await inter.send(embed=embed, ephemeral=True)
        
def setup(client):
    client.add_cog(Clear(client))