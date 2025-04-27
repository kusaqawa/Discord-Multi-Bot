
import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands

import asyncio
import datetime
import time

import sqlite3

connection = sqlite3.connect("mod.db") 
cursor = connection.cursor()

class Back(disnake.ui.View):
    def __init__(self, inter, target):
        super().__init__(timeout=None)

        self.inter = inter
        self.target = target

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Верификация', description=f'{self.inter.author.mention}, Выберите **взаимодействия** с  {self.target.mention}', color=0x2f3136)
        embed.add_field(
            name='> Аккаунт создан:',
            value=f'**```{self.target.created_at.strftime("%d.%m.%Y")}```**'
        )

        embed.add_field(
            name='> Зашел на сервер:',
            value=f'**```{self.target.joined_at.strftime("%d.%m.%Y")}```**'
        )
        embed.set_thumbnail(url=self.target.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Gender(self.inter, self.target))


class Gender(disnake.ui.View):
    def __init__(self, inter, target):
        super().__init__(timeout=None)

        self.inter = inter
        self.target = target

        global girl
        global boy
        global declined
        global unveref
        global adm
        girl = disnake.utils.get(self.inter.guild.roles, id=1242870721097629716)
        boy = disnake.utils.get(self.inter.guild.roles, id=1242870722150535301)
        declined = disnake.utils.get(self.inter.guild.roles, id=1242870757218975775)
        unveref = disnake.utils.get(self.inter.guild.roles, id=1242870758544244806)
        

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Девочка", style=ButtonStyle.blurple)
    async def girl(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await self.target.remove_roles(boy)
        await self.target.remove_roles(declined)
        await self.target.remove_roles(unveref)

        await self.target.add_roles(girl)
        
        cursor.execute("UPDATE users SET verify=verify +1 WHERE id=?", [interaction.author.id])
        connection.commit()
        embed = disnake.Embed(title='Верификация', description=f'{self.inter.author.mention}, Вы **изменили** роли {self.target.mention} на {girl.mention}', color=0x2f3136)
        embed.set_thumbnail(url=self.target.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Back(self.inter, self.target))

    @disnake.ui.button(label="Мальчик", style=ButtonStyle.blurple)
    async def boy(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await self.target.remove_roles(girl)
        await self.target.remove_roles(declined)
        await self.target.remove_roles(unveref)

        await self.target.add_roles(boy)
        cursor.execute("UPDATE users SET verify=verify +1 WHERE id=?", [interaction.author.id])
        connection.commit()
        embed = disnake.Embed(title='Верификация', description=f'{self.inter.author.mention}, Вы **изменили** роли {self.target.mention} на {boy.mention}', color=0x2f3136)
        embed.set_thumbnail(url=self.target.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Back(self.inter, self.target))

    @disnake.ui.button(label="Не допущен", style=ButtonStyle.red)
    async def declined(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await self.target.remove_roles(girl)
        await self.target.remove_roles(boy)
        await self.target.remove_roles(unveref)

        await self.target.add_roles(declined)

        embed = disnake.Embed(title='Верификация', description=f'{self.inter.author.mention}, Вы **изменили** роли {self.target.mention} на {declined.mention}', color=0x2f3136)
        embed.set_thumbnail(url=self.target.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Back(self.inter, self.target))

    @disnake.ui.button(label="Отмена", style=ButtonStyle.red)
    async def delete(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()

class Verify(commands.Cog):
    
    def __init__(self, client):
        self.client = client
      
    @commands.slash_command(name='verify', description='Верифицировать пользователя ')
    @commands.has_any_role(1242870657012732015, 1242870661505089746, 1242870665787211947, 1242870668656246885, 1242870683848146955) 
    async def verify(self, inter, target: disnake.Member = commands.Param(None, name="пользовaтель")):
        embed = disnake.Embed(title='Верификация', description=f'{inter.author.mention}, Выберите **взаимодействия** с  {target.mention}', color=0x2f3136)
        embed.add_field(
            name='> Аккаунт создан:',
            value=f'**```{target.created_at.strftime("%d.%m.%Y")}```**'
        )

        embed.add_field(
            name='> Зашел на сервер:',
            value=f'**```{target.joined_at.strftime("%d.%m.%Y")}```**'
        )
        embed.set_thumbnail(url=target.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await inter.send(embed=embed, view=Gender(inter, target))

    
def setup(client):
    client.add_cog(Verify(client))


