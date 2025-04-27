
import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands

import asyncio
import datetime
import time

from typing import List

import sqlite3

connection = sqlite3.connect("mod.db") 
cursor = connection.cursor()

class History(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name='history', description='Посмотреть историю наказаний')
    async def history(self, inter, target: disnake.Member = commands.Param(None, name="пользовaтель")):
        member = target or inter.author
        mutes = cursor.execute("SELECT mutes FROM users WHERE id = ?", [member.id]).fetchone()[0]
        bans = cursor.execute("SELECT bans FROM users WHERE id = ?", [member.id]).fetchone()[0]
        pred = cursor.execute("SELECT warn FROM users WHERE id = ?", [member.id]).fetchone()[0]

        rows = cursor.execute("SELECT date, punish_view, reason, given FROM history WHERE id = ?", [member.id])

        embeds = []
        if mutes+bans+pred == 0:
            embed = disnake.Embed(title=f'История нарушений — {member}', description=f'Пользователь {member.mention}, не получал нарушений!', color=0x2f3136)
            embed.set_thumbnail(url=member.display_avatar)
            embeds.append(embed)

        else:
            for i, row in enumerate(rows):
                if i % 5 == 0:
                    embed = disnake.Embed(title=f'История нарушений — {member}', description=f'Мутов: **{mutes}** Банов: **{bans}** Предов: **{pred}**', color=0x2f3136)
                    embed.set_thumbnail(url=member.display_avatar)
                    embeds.append(embed)

                embed.add_field(
                    name=f'** **',
                    value=f'`{i+1}.` [<t:{row[0]}:f>] **{row[1]}** *Причина:* {row[2]}\nМодератор: <@{row[3]}>',
                    inline=False
                )

        await inter.send(embed=embeds[0], view=Menu(inter, embeds))
            
class Menu(disnake.ui.View):
    def __init__(self, inter, embeds: List[disnake.Embed]):
        super().__init__(timeout=None)
        self.inter = inter
        self.embeds = embeds
        self.embed_count = 0

        self.prev_page.disabled = True

        if len(self.embeds) == 1:
            self.next_page.disabled = True

        for i, embed in enumerate(self.embeds):
            embed.set_footer(text=f"Страница {i + 1}/{len(self.embeds)}")

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Назад", style=disnake.ButtonStyle.gray)
    async def prev_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count -= 1
        embed = self.embeds[self.embed_count]

        self.next_page.disabled = False

        if self.embed_count == 0:
            self.prev_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    @disnake.ui.button(label="Удалить", style=disnake.ButtonStyle.red)
    async def remove(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message(view=None)

    @disnake.ui.button(label="Вперёд", style=disnake.ButtonStyle.gray)
    async def next_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count += 1
        embed = self.embeds[self.embed_count]

        self.prev_page.disabled = False
        
        if self.embed_count == len(self.embeds) - 1:
            self.next_page.disabled = True

        await interaction.response.edit_message(embed=embed, view=self)









    
def setup(client):
    client.add_cog(History(client))
