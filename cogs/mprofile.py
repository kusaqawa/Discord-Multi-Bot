import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands, tasks
from config import *
import asyncio
import datetime
import time
from typing import List

import sqlite3

connection = sqlite3.connect("mod.db") 
cursor = connection.cursor()

class Mprofile(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.inter = iter
        
    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()
    

    @commands.slash_command(name='mprofile', description='Посмотреть профиль стаффа')
    @commands.has_any_role(ADMIN, CURATOR, MODER, SECURITY, SUPPORT)
    async def mprofile(self, inter, target: disnake.Member = commands.Param(None, name="пользовaтель")):
        member = target or inter.author    
        if inter.guild.get_role(ADMIN) in member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Администратора - {member}**',color=0x2f3136)
            embed.set_thumbnail(url=member.display_avatar)
            
            embed.add_field(
                name=f'> Голосовая активность',
                value=f'```{author_online // 3600} ч. {(author_online % 3600) // 60} мин.```',
                inline=False
                )
            
            embed.add_field(
                name=f'> Выговоры',
                value=f'```{vigovors}/3```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано мутов',
                value=f'```{mute}```',
                inline=True
                )
            embed.add_field(
                name=f'> Верифицировано',
                value=f'```{veref}```',
                inline=True
                )
            embed.add_field(
                name=f'> Группа',
                value=f'```Администратор```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано варнов',
                value=f'```{warn}```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано банов',
                value=f'```{ban}```',
                inline=True
                )
            await inter.send(embed=embed, view=Delete(self.inter))        
        
        elif inter.guild.get_role(CURATOR) in member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Куратора - {member}**',color=0x2f3136)
            embed.set_thumbnail(url=member.display_avatar)
            
            embed.add_field(
                name=f'> Голосовая активность',
                value=f'```{author_online // 3600} ч. {(author_online % 3600) // 60} мин.```',
                inline=False
                )
            
            embed.add_field(
                name=f'> Выговоры',
                value=f'```{vigovors}/3```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано мутов',
                value=f'```{mute}```',
                inline=True
                )
            embed.add_field(
                name=f'> Верифицировано',
                value=f'```{veref}```',
                inline=True
                )
            embed.add_field(
                name=f'> Группа',
                value=f'```Куратор```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано варнов',
                value=f'```{warn}```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано банов',
                value=f'```{ban}```',
                inline=True
                )
            await inter.send(embed=embed, view=Delete(self.inter))    
            
        elif inter.guild.get_role(MODER) in member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Модератора - {member}**',color=0x2f3136)
            embed.set_thumbnail(url=member.display_avatar)
            
            embed.add_field(
                name=f'> Голосовая активность',
                value=f'```{author_online // 3600} ч. {(author_online % 3600) // 60} мин.```',
                inline=False
                )
            
            embed.add_field(
                name=f'> Выговоры',
                value=f'```{vigovors}/3```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано мутов',
                value=f'```{mute}```',
                inline=True
                )
            embed.add_field(
                name=f'> Верифицировано',
                value=f'```{veref}```',
                inline=True
                )
            embed.add_field(
                name=f'> Группа',
                value=f'```Модератор```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано варнов',
                value=f'```{warn}```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано банов',
                value=f'```{ban}```',
                inline=True
                )
            await inter.send(embed=embed, view=Delete(self.inter))    
        
            
        elif inter.guild.get_role(SECURITY) in member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Мастера - {member}**',color=0x2f3136)
            embed.set_thumbnail(url=member.display_avatar)
            
            embed.add_field(
                name=f'> Голосовая активность',
                value=f'```{author_online // 3600} ч. {(author_online % 3600) // 60} мин.```',
                inline=False
                )
            
            embed.add_field(
                name=f'> Выговоры',
                value=f'```{vigovors}/3```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано мутов',
                value=f'```{mute}```',
                inline=True
                )
            embed.add_field(
                name=f'> Группа',
                value=f'```Мастер```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано варнов',
                value=f'```{warn}```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано банов',
                value=f'```{ban}```',
                inline=True
                )
            await inter.send(embed=embed, view=Delete(self.inter))            
            
        elif inter.guild.get_role(SUPPORT) in member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Саппорта - {member}**',color=0x2f3136)
            embed.set_thumbnail(url=member.display_avatar)
            
            embed.add_field(
                name=f'> Голосовая активность',
                value=f'```{author_online // 3600} ч. {(author_online % 3600) // 60} мин.```',
                inline=False
                )
            
            embed.add_field(
                name=f'> Выговоры',
                value=f'```{vigovors}/3```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано мутов',
                value=f'```{mute}```',
                inline=True
                )
            embed.add_field(
                name=f'> Верифицировано',
                value=f'```{veref}```',
                inline=True
                )
            embed.add_field(
                name=f'> Группа',
                value=f'```Саппорт```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано варнов',
                value=f'```{warn}```',
                inline=True
                )
            embed.add_field(
                name=f'> Выдано банов',
                value=f'```{ban}```',
                inline=True
                )
            await inter.send(embed=embed, view=Delete(self.inter))                   
        else:         
            embed = disnake.Embed(title='Профиль стаффа', description=f'Пользователь {member.mention} не находится на ветке, или же у него нет стафф профиля ветки', color=0x2f3136)
            embed.set_thumbnail(url=inter.author.display_avatar)
            await inter.send(embed=embed)
        
class Delete(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)

        self.inter = inter
            
    @disnake.ui.button(label="Отменить просмотр", style=ButtonStyle.gray)
    async def delete(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()
        

    
def setup(client):
    client.add_cog(Mprofile(client))