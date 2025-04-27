
import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands, tasks
import asyncio
import sqlite3
import time

connection = sqlite3.connect("mod.db") 
cursor = connection.cursor()

        
class Bd(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS id(
            id INT,
            mutes INT,
            bans INT,
            warn INT,
            verify INT,
            vigovor INT,
            otpysk INT,
            staffban INT,
            given INT
        )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INT,
            mutes INT,
            bans INT,
            warn INT,
            verify INT,
            vigovor INT,
            otpysk INT,
            staffban INT,
            voice_time INTEGER,
            local_ban TEXT
        )""")


        cursor.execute("""CREATE TABLE IF NOT EXISTS history(
            id INT,
            date INT,
            punish_view TEXT,
            reason TEXT,
            given INT
        )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS given(
            id INT,
            date INT,
            mutes INT,
            bans INT,
            warn INT,
            given INT
        )""")
        
        for guild in self.client.guilds:
            for member in guild.members:    
                if cursor.execute(f"SELECT id FROM users WHERE id=?", [member.id]).fetchone() is None:
                    cursor.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [member.id, 0, 0, 0, 0, 0, 0, 0, 0, 'unban'])
                else:
                    pass
            connection.commit()
            print('Бот запустился')


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if cursor.execute(f"SELECT id FROM users WHERE id = ?", [member.id]).fetchone() is None:
            cursor.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [member.id, 0, 0, 0, 0, 0, 0, 0, 0, 'unban'])
            connection.commit()
        else:
            if cursor.execute("SELECT local_ban FROM users WHERE id=?", [member.id]).fetchone()[0] == 'ban':
                local_ban = disnake.utils.get(member.guild.roles, id=1119326997521383585)
                await member.add_role(local_ban)
        connection.commit()

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter, error):
        if isinstance(error, commands.MissingAnyRole):
            embed = disnake.Embed(title='Ошибка прав', description=f'{inter.author.mention}, У вас **недостаточно прав** для данной команды.',  color=0x2f3136)
            embed.set_thumbnail(url=inter.author.display_avatar)
            await inter.send(embed=embed, ephemeral=True)
        else:
            raise error    

def setup(client):
    client.add_cog(Bd(client))