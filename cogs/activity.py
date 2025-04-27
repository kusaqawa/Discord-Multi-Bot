
import disnake
from disnake.ext import commands
import datetime

import time
import sqlite3
import asyncio

tdict = {}

connection = sqlite3.connect("mod.db")
cursor = connection.cursor()


class Activity(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        if before.channel is None and after.channel is not None:
            time1 = int(time.time())
            tdict[member.name] = time1

        elif after.channel is None:
            voice_time = int(time.time()) - int(tdict[member.name])
            money = (voice_time % 3600) // 60

            cursor.execute(
                "UPDATE users SET voice_time = voice_time+? WHERE id = ?", [voice_time, member.id])
            connection.commit()



def setup(client):
    client.add_cog(Activity(client))
