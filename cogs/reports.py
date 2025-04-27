import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
import asyncio
from urllib.parse import quote_plus

import datetime

class Buttons_staff(disnake.ui.View):
    def __init__(self, client, target, reason, author):
        super().__init__(timeout=None)
        self.client = client
        self.target = target
        self.reason = reason
        self.author = author

    @disnake.ui.button(label="Принять", style=ButtonStyle.green)
    async def done(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed_good = disnake.Embed(
            title = 'Репорт на пользователя',
            description  = f'> Куратор: **{interaction.author.mention}**\n> Отправитель: **{self.author.mention}**\n> Нарушитель: **{self.target.mention}**\n> Статус: **Принято**',
            color = 0x2f3136
        )
        embed_good.add_field(name = 'Причина', value = f'```{self.reason}```', inline = True)

        embed_member = disnake.Embed(
            title = 'Репорт',
            description = f'Ваш репорт был принят. Его будет рассматривать {interaction.author.mention}',
            color = 0x2f3136
        )

        await interaction.response.edit_message(embed=embed_good, view = None)
        await self.author.send(embed = embed_member)

    @disnake.ui.button(label="Отклонить", style=ButtonStyle.red)
    async def neet(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed_bad = disnake.Embed(
            title = 'Репорт на пользователя',
            description  = f'> Куратор: **{interaction.author.mention}**\n> Отправитель: **{self.author.mention}**\n> Нарушитель: **{self.target.mention}**\n> Статус: **Отклонено**',
            color = 0x2f3136
        )
        embed_bad.add_field(name = 'Причина', value = f'```{self.reason}```', inline = True)

        embed_member_bad = disnake.Embed(
            title = 'Репорт',
            description = f'Ваш репорт был отклонён. Его отклонил {interaction.author.mention}',
            color = 0x2f3136
        )
        await interaction.response.edit_message(embed=embed_bad, view = None)
        await self.author.send(embed = embed_member_bad)

class Buttons(disnake.ui.View):
    def __init__(self, client, target, reason, author):
        super().__init__(timeout=None)
        self.client = client
        self.target = target
        self.reason = reason
        self.author = author

    @disnake.ui.button(label="Принять", style=ButtonStyle.green)
    async def done(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed_good = disnake.Embed(
            title = 'Репорт на пользователя',
            description  = f'> Модератор: **{interaction.author.mention}**\n> Отправитель: **{self.author.mention}**\n> Нарушитель: **{self.target.mention}**\n> Статус: **Принято**',
            color = 0x2f3136
        )
        embed_good.add_field(name = 'Причина', value = f'```{self.reason}```', inline = True)

        embed_member = disnake.Embed(
            title = 'Репорт',
            description = f'Ваш репорт был принят. Его будет рассматривать {interaction.author.mention}',
            color = 0x2f3136
        )

        await interaction.response.edit_message(embed=embed_good, view = None)
        await self.author.send(embed = embed_member)

    @disnake.ui.button(label="Отклонить", style=ButtonStyle.red)
    async def neet(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed_bad = disnake.Embed(
            title = 'Репорт на пользователя',
            description  = f'> Модератор: **{interaction.author.mention}**\n> Отправитель: **{self.author.mention}**\n> Нарушитель: **{self.target.mention}**\n> Статус: **Отклонено**',
            color = 0x2f3136
        )
        embed_bad.add_field(name = 'Причина', value = f'```{self.reason}```', inline = True)

        embed_member_bad = disnake.Embed(
            title = 'Репорт',
            description = f'Ваш репорт был отклонён. Его отклонил {interaction.author.mention}',
            color = 0x2f3136
        )
        await interaction.response.edit_message(embed=embed_bad, view = None)
        await self.author.send(embed = embed_member_bad)



# ===================================================================



class Reports(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(name='report', description='Отправить жалобу')
    async def event_make(self, interaction, target: disnake.Member = commands.Param(name="пользовaтель")):
        await interaction.response.send_modal(
            title=f"Укажите причину",
            custom_id=f"status",
            components=[
                disnake.ui.TextInput(
                    label="Укажите причину жалобы",
                    placeholder=f"Введите текст",
                    custom_id="reason",
                    style=disnake.TextInputStyle.paragraph,
                ),
            ],
        )
        try:
            modal_inter: disnake.Modalinter = await self.client.wait_for(
                "modal_submit",
                check=lambda i: i.custom_id == f"status" and i.author.id == interaction.author.id,
                timeout=300,
            )
        except asyncio.TimeoutError:
            return
        for custom_id, value in modal_inter.text_values.items():
            if custom_id == "reason":
                reason = str(value)
            else:
                return
        embed_gotovo = disnake.Embed(
            title = 'Репорт',
            description = f'Вы успешно отправили жалобу на пользователя <@{target.id}>',
            color = 0x2f3136
        )
        embed_gotovo.set_thumbnail(url=interaction.author.display_avatar)
        embed_report = disnake.Embed(
            title = 'Репорт на пользователя',
            description  = f'> Отправил: **{interaction.author.mention}**\n> Нарушитель: **{target.mention}**\n> Статус: **Ожидание**',
            color = 0x2f3136
        )
        embed_report.set_thumbnail(url=interaction.author.display_avatar)
        embed_report.add_field(name = 'Причина', value = f'```{reason}```', inline = True)
        channel = self.client.get_channel(1247937557191462998)
        guild = interaction.guild
        author = interaction.author
        await channel.send(embed=embed_report, view = Buttons(self.client, target, reason, author))

        await modal_inter.send(embed=embed_gotovo)
        

def setup(client):
    client.add_cog(Reports(client))