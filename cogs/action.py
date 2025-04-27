
import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands
from config import *
import asyncio
import datetime
import time

from typing import List

import sqlite3

test_guild = [1234567890987654321]


connection = sqlite3.connect("mod.db") 
cursor = connection.cursor()

class BackSecurity(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()     

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Security(self.client, self.inter, self.member))
        return    

class BackControl(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()     

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Control(self.client, self.inter, self.member))
        return    

class BackAdmin(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Admin(self.client, self.inter, self.member))
        return    

class BackCreative(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Creative(self.client, self.inter, self.member))
        return    

class CreativeRole(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)

        self.inter = inter
        self.member = member
        self.client = client

        global music
        global club
        global painter

        music = disnake.utils.get(self.inter.guild.roles, id=MUSIC)
        club = disnake.utils.get(self.inter.guild.roles, id=CLUB)
        painter = disnake.utils.get(self.inter.guild.roles, id=PAINTER)

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="🎵", style=ButtonStyle.grey)
    async def music(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=MUSIC)  # Роль музыканта
        if role in self.member.roles:
            await self.member.remove_roles(music)           
            embed = disnake.Embed(title='Снятие роли - Музыкант', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль **Музыкант**, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_CREATIVE)
            embed_log = disnake.Embed(
                title = 'Снятие роли', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Снял:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому снял:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Роль',
                value = '```Музыкант```',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
                
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:  # Роль SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
                
            elif interaction.guild.get_role(CREATIVE) in interaction.author.roles:  # Роль Креатиава
                await interaction.response.edit_message(embed=embed, view=BackCreative(self.client, self.inter, self.member))
                return
            
        else:
            await self.member.add_roles(music)       
            embed = disnake.Embed(title='Выдача ролей', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль музыканта {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_CREATIVE)
            embed_log = disnake.Embed(
                title = 'Выдача роли', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Выдал:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому выдал:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Роль',
                value = '```Музыкант```',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:  # Роль SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
                
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(CREATIVE) in interaction.author.roles: # Роль Creative
                await interaction.response.edit_message(embed=embed, view=BackCreative(self.client, self.inter, self.member))
                return

    @disnake.ui.button(label="📚", style=ButtonStyle.grey)
    async def club(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=CLUB)  # Роль литературного клуба
        if role in self.member.roles:
            await self.member.remove_roles(club)           
            embed = disnake.Embed(title='Снятие роли - Литературный клуб', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль **Литературный клуб**, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_CREATIVE)
            embed_log = disnake.Embed(
                title = 'Снятие роли', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Снял:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому снял:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Роль',
                value = '```Литературный клуб```',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:  # Роль SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
                
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(CREATIVE) in interaction.author.roles: # Роль Creative
                await interaction.response.edit_message(embed=embed, view=BackCreative(self.client, self.inter, self.member))
                return
            
        else:
            await self.member.add_roles(music)       
            embed = disnake.Embed(title='Выдача ролей', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль **Литературный клуб** {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_CREATIVE)
            embed_log = disnake.Embed(
                title = 'Выдача роли', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Выдал:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому выдал:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Роль',
                value = '```Литературный клуб```',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
            
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:  # Роль SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
                
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(CREATIVE) in interaction.author.roles: # Роль Creative
                await interaction.response.edit_message(embed=embed, view=BackCreative(self.client, self.inter, self.member))
                return
    
    @disnake.ui.button(label="🎨", style=ButtonStyle.grey)
    async def painterss(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=PAINTER)  # Роль художника
        if role in self.member.roles:
            await self.member.remove_roles(painter)           
            embed = disnake.Embed(title='Снятие роли - Художник', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль **Художник**, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_CREATIVE)
            embed_log = disnake.Embed(
                title = 'Снятие роли', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Снял:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому снял:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Роль',
                value = '```Художник```',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:  # Роль SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
                
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(CREATIVE) in interaction.author.roles: # Роль Creative
                await interaction.response.edit_message(embed=embed, view=BackCreative(self.client, self.inter, self.member))
                return
            
        else:
            await self.member.add_roles(music)       
            embed = disnake.Embed(title='Выдача ролей', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль **Художник** {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_CREATIVE)
            embed_log = disnake.Embed(
                title = 'Выдача роли', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Выдал:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому выдал:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Роль',
                value = '```Художник```',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)  
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:  # Роль SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
                
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
        
            elif interaction.guild.get_role(CREATIVE) in interaction.author.roles: # Роль Creative
                await interaction.response.edit_message(embed=embed, view=BackCreative(self.client, self.inter, self.member))
                return

                
    @disnake.ui.button(label="Назад", style=ButtonStyle.gray)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            return
        
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:  # Роль SECURITY
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            return
        
        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            return
        
        elif interaction.guild.get_role(CREATIVE) in interaction.author.roles: # Роль Creative
            await interaction.response.edit_message(embed=embed, view=BackCreative(self.client, self.inter, self.member))
            return


class VerifySupport(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
  
        self.inter = inter
        self.member = member
        self.client = client

        global girl
        global boy
        global declined
        global unveref
        girl = disnake.utils.get(self.inter.guild.roles, id=GIRL)
        boy = disnake.utils.get(self.inter.guild.roles, id=BOY)
        declined = disnake.utils.get(self.inter.guild.roles, id=DECLINED)
        unveref = disnake.utils.get(self.inter.guild.roles, id=UNVEREF)


    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(emoji="♀️", style=ButtonStyle.grey)
    async def girl(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await self.member.remove_roles(boy)
        await self.member.remove_roles(declined)
        await self.member.remove_roles(unveref)

        await self.member.add_roles(girl)

        
        cursor.execute("UPDATE users SET verify=verify +1 WHERE id=?", [interaction.author.id])
        connection.commit()
        embed = disnake.Embed(title='Верификация', description=f'{self.inter.author.mention}, Вы **верифицировали** пользователя {self.member.mention}, гендер {girl.mention}', color=0x2f3136)
        embed.set_thumbnail(url=self.member.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)
        channel = self.client.get_channel(LOG_VERIFY)
        embed_log = disnake.Embed(
            title = 'Верификация', color=0x2f3136
        )
        embed_log.add_field(
            name = '> Верифицировал:',
            value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
            inline=False
        )
        embed_log.add_field(
            name = '> Верифицирован:',
            value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
            inline=False
        )
        embed_log.add_field(
            name = '> Гендер',
            value = '```Женский```',
            inline=False
        )
        embed_log.set_thumbnail(url=interaction.author.display_avatar)  
        embed_log.timestamp = datetime.datetime.now()
        await channel.send(embed=embed_log)

    @disnake.ui.button(emoji="♂️", style=ButtonStyle.grey)
    async def boy(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await self.member.remove_roles(girl)
        await self.member.remove_roles(declined)
        await self.member.remove_roles(unveref)

        await self.member.add_roles(boy)

        cursor.execute("UPDATE users SET verify=verify +1 WHERE id=?", [interaction.author.id])
        connection.commit()
        embed = disnake.Embed(title='Верификация', description=f'{self.inter.author.mention}, Вы **верифицировали** пользователя {self.member.mention}, гендер {boy.mention}', color=0x2f3136)
        embed.set_thumbnail(url=self.member.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)
        channel = self.client.get_channel(LOG_VERIFY)
        embed_log = disnake.Embed(
            title = 'Верификация', color=0x2f3136
        )
        embed_log.add_field(
            name = '> Верифицировал:',
            value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
            inline=False
        )
        embed_log.add_field(
            name = '> Верифицирован:',
            value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
            inline=False
        )
        embed_log.add_field(
            name = '> Гендер',
            value = '```Мужской```',
            inline=False
        )
        embed_log.set_thumbnail(url=interaction.author.display_avatar)  
        embed_log.timestamp = datetime.datetime.now()
        await channel.send(embed=embed_log)

    @disnake.ui.button(label="Не допущен", style=ButtonStyle.grey)
    async def declined(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await self.member.remove_roles(girl)
        await self.member.remove_roles(boy)
        await self.member.remove_roles(unveref)

        await self.member.add_roles(declined)

        embed = disnake.Embed(title='Верификация', description=f'{self.inter.author.mention}, Вы **изменили** роли {self.member.mention} на {declined.mention}', color=0x2f3136)
        embed.set_thumbnail(url=self.member.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)
        embed_done = disnake.Embed(
            title = 'Верификация',
            description = f'{self.member.mention}, вы получили недопуск от {self.inter.author.mention}',
            color = 0x2f3136
        )
        await self.member.mention.send(embed = embed_done)
        channel = self.client.get_channel(LOG_VERIFY)
        embed_log = disnake.Embed(
            title = 'Верификация', color=0x2f3136
        )
        embed_log.add_field(
            name = '> Верифицировал:',
            value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
            inline=False
        )
        embed_log.add_field(
            name = '> Верифицирован:',
            value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
            inline=False
        )
        embed_log.add_field(
            name = '> Гендер',
            value = '```недопуск```',
            inline=False
        )  
        embed_log.set_thumbnail(url=interaction.author.display_avatar)  
        embed_log.timestamp = datetime.datetime.now()
        await channel.send(embed=embed_log)
        
    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, member, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
            await interaction.response.edit_message(embed=embed, view=Admin(self.client, self.inter, self.member))
            return
        
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:  # Роль SECURITY
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            return 
        
        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
            await interaction.response.edit_message(embed=embed, view=Curator(self.client, self.inter, self.member))
            return
        
        elif interaction.guild.get_role(SUPPORT) in interaction.author.roles: # Роль SUPPORT
            await interaction.response.edit_message(embed=embed, view=Support(self.client, self.inter, self.member))
            return


class Staff(disnake.ui.View):
    def __init__(self, inter, client, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

        global moderator
        global support
        global closemaker
        global security
        global clanmaster
        global broadcaster
        global eventer
        global vigovor
        global vigovors
        global otpysk
        global otpysks
        global staff
        global curator
        global creative
        global media
        global helper
        moderator = disnake.utils.get(self.inter.guild.roles, id=MODER)
        curator = disnake.utils.get(self.inter.guild.roles, id=CURATOR)
        security = disnake.utils.get(self.inter.guild.roles, id=SECURITY)
        support = disnake.utils.get(self.inter.guild.roles, id=SUPPORT)
        creative = disnake.utils.get(self.inter.guild.roles, id=CREATIVE)
        helper = disnake.utils.get(self.inter.guild.roles, id=HELPER)
        media = disnake.utils.get(self.inter.guild.roles, id=MEDIA)
        broadcaster = disnake.utils.get(self.inter.guild.roles, id=BROADCASTER)
        closemaker = disnake.utils.get(self.inter.guild.roles, id=CLOSEMAKER)
        eventer = disnake.utils.get(self.inter.guild.roles, id=EVENTER)
        staff = disnake.utils.get(self.inter.guild.roles, id=STAFF_ROLE)
    
            
        curators = {self.inter.guild.get_role(ADMIN), self.inter.guild.get_role(1119326953804152922)} #АЙДИ АДМИНА

        if not curators.intersection(self.inter.author.roles):
            self.curator.disabled = True
            self.security.disabled = True
            



    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()
            
    @disnake.ui.button(label="Curator", style=ButtonStyle.gray)
    async def curator(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=CURATOR)  # РОЛЬ Curator
        if role in self.member.roles:
            await self.member.remove_roles(role)           
            embed = disnake.Embed(title='Снятие роли - Curator', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Curator, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Curator', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Сняли:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Curator```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        else:
            role = disnake.utils.get(self.inter.guild.roles, id=CURATOR)  # РОЛЬ Curator
            await self.member.add_roles(role)

            embed = disnake.Embed(title='Выдача роли - Curator', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Curator, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Curator', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Curator```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))

    @disnake.ui.button(label="Master", style=ButtonStyle.gray)
    async def security(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=SECURITY)  # РОЛЬ Curator
        if role in self.member.roles:
            await self.member.remove_roles(role)           
            embed = disnake.Embed(title='Снятие роли - Master', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Master, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Master', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Сняли:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Master```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        else:
            role = disnake.utils.get(self.inter.guild.roles, id=SECURITY)  # РОЛЬ Curator
            await self.member.add_roles(role)

            embed = disnake.Embed(title='Выдача роли - Master', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Master, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Master', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Master```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # SECURITY
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
                
    @disnake.ui.button(label="Moderator", style=ButtonStyle.gray)
    async def moderator(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=MODER)  # РОЛЬ ModeratorА
        if role in self.member.roles:
            await self.member.remove_roles(moderator)           
            await self.member.remove_roles(staff)           
            embed = disnake.Embed(title='Снятие роли - Moderator', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Moderator, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Moderator', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Сняли:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Moderator```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # SECURITY
               await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))           
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))

        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))      
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        else:
            await self.member.add_roles(moderator)
            await self.member.add_roles(staff)

            embed = disnake.Embed(title='Выдача роли - Moderator', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Moderator, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Moderator', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Moderator```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        
    @disnake.ui.button(label="Trubinemod", style=ButtonStyle.gray)
    async def broadcaster(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BROADCASTER)  # РОЛЬ БРОАДКАСТЕРА
        if role in self.member.roles:
            await self.member.remove_roles(broadcaster)           
            await self.member.remove_roles(staff)   
            embed = disnake.Embed(title='Снятие роли - Trubinemod', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Trubinemod, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Trubinemod', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Сняли:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Trubinemod```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))      
        
        else:
            await self.member.add_roles(broadcaster)
            await self.member.add_roles(staff)

            embed = disnake.Embed(title='Выдача роли - Trubinemod', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Trubinemod, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Trubinemod', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Trubinemod```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))

    @disnake.ui.button(label="Closemod", style=ButtonStyle.gray)
    async def clanmaster(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=CLOSEMAKER)  # РОЛЬ КЛАН МАСТЕРА
        if role in self.member.roles:
            await self.member.remove_roles(role)           
            await self.member.remove_roles(staff)
            embed = disnake.Embed(title='Снятие роли - Closemod', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Closemod, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Closemod', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Сняли:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Closemod```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        else:
            await self.member.add_roles(closemaker)
            await self.member.add_roles(staff)
            
            embed = disnake.Embed(title='Выдача роли - Closemod', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Closemod, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Closemod', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Closemod```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))

    @disnake.ui.button(label="Eventsmod", style=ButtonStyle.gray)
    async def eventers(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=EVENTER)  # РОЛЬ EVENTER
        if role in self.member.roles:
            await self.member.remove_roles(staff)   
            await self.member.remove_roles(eventer)           
            embed = disnake.Embed(title='Снятие роли - Eventsmod', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Eventsmod, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Eventsmod', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Eventsmod```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
       
        else:
            await self.member.add_roles(eventer)
            await self.member.add_roles(staff)
            
            embed = disnake.Embed(title='Выдача роли - Eventsmod', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Eventsmod, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Eventsmod', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Eventsmod```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
    @disnake.ui.button(label="Creative", style=ButtonStyle.gray)
    async def creat(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=CREATIVE)  # РОЛЬ CREATIVE
        if role in self.member.roles:
            await self.member.remove_roles(staff)   
            await self.member.remove_roles(creative)           
            embed = disnake.Embed(title='Снятие роли - Creative', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Creative, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Cнятие роли - Creative', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Сняли:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Creative```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        else:
            await self.member.add_roles(creative)
            await self.member.add_roles(staff)
            
            embed = disnake.Embed(title='Выдача роли - Creative', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Creative, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Creative', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Creative```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))

    @disnake.ui.button(label="Helper", style=ButtonStyle.grey)
    async def Helper(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=HELPER)  # РОЛЬ Helper
        if role in self.member.roles:
            await self.member.remove_roles(staff)   
            await self.member.remove_roles(role)           
            embed = disnake.Embed(title='Снятие роли - Helper', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Helper, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Helper', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Сняли:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Helper```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))       
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        else:
            helper = disnake.utils.get(self.inter.guild.roles, id=HELPER)
            await self.member.add_roles(helper)
            await self.member.add_roles(staff)

            embed = disnake.Embed(title='Выдача роли - Helper', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Helper, пользователю  {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Helper', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Helper```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
    @disnake.ui.button(label="Media", style=ButtonStyle.grey)
    async def Media(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=MEDIA)  # РОЛЬ MEDIA
        if role in self.member.roles:
            await self.member.remove_roles(staff)   
            await self.member.remove_roles(media)           
            embed = disnake.Embed(title='Снятие роли - Media', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Media, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Media', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Сняли:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Media```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))      
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        else:
            await self.member.add_roles(media)
            await self.member.add_roles(staff)

            embed = disnake.Embed(title='Выдача роли - Media', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Media, пользователю  {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Media', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Media```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))        
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))

    @disnake.ui.button(label="Support", style=ButtonStyle.grey)
    async def support(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=SUPPORT)  # РОЛЬ САППОРТА
        if role in self.member.roles:
            await self.member.remove_roles(staff)   
            await self.member.remove_roles(support)           
            embed = disnake.Embed(title='Снятие роли - Support', description=f'{self.inter.author.mention}, Вы **успешно сняли** роль Support, пользователю {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Снятие роли - Support', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Support```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        
        elif cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Выдача ветки', description=f'{interaction.author.mention}, пользователь находиться в чс состава, и вы не можете выдать ему ветку.', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))       
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
        else:
            await self.member.add_roles(support)
            await self.member.add_roles(staff)

            embed = disnake.Embed(title='Выдача роли - Support', description=f'{self.inter.author.mention}, Вы **успешно выдали** роль Support, пользователю  {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            channel = self.client.get_channel(LOG_VETOK)
            embed_log = disnake.Embed(
                title = 'Выдача роли - Support', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Выдали:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Ветка',
                value = '```Support```',
                inline=False
            )  
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # BackSecurity
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                
                
        
    @disnake.ui.button(label="Назад", style=ButtonStyle.blurple)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.guild.get_role(CURATOR) in interaction.author.roles: #CURATOR РОЛЬ
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Curator(self.client, self.inter, self.member))
        
        elif interaction.guild.get_role(ADMIN) in interaction.author.roles: #ADMIN РОЛЬ
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Admin(self.client, self.inter, self.member))    
        
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles: #ADMIN РОЛЬ
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Admin(self.client, self.inter, self.member)) 


class Razmut(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Текстовой мут", style=ButtonStyle.green)
    async def unmutetext(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):          
        cmute = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)
        await self.member.remove_roles(cmute)       
        embed = disnake.Embed(title='Управление - Размут', description=f'{interaction.author.mention}, Вы размутили пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        if interaction.guild.get_role(CURATOR) in interaction.author.roles:    # CURATOR
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles: #SECURITY
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        else:
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
                
            
    @disnake.ui.button(label="Голосовой мут", style=ButtonStyle.green)
    async def gmutss(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):        
        vmute = disnake.utils.get(self.inter.guild.roles, id=VOICE_MUTE)
        await self.member.remove_roles(vmute)  
        embed = disnake.Embed(title='Управление - Размут', description=f'{interaction.author.mention}, Вы размутили пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        if interaction.guild.get_role(CURATOR) in interaction.author.roles: # CURATOR
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles: #SECURITY
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        else:
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        

class BackSupport(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Support(self.client, self.inter, self.member))
        return

class Back(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Moderations(self.client, self.inter, self.member))
        return

class BackAdmin(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Admin(self.client, self.inter, self.member))
        return    
    
class BackCurator(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Curator(self.client, self.inter, self.member))
        return    

class Gender(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)

        self.inter = inter
        self.member = member
        self.client = client

        global girl
        global boy
        girl = disnake.utils.get(self.inter.guild.roles, id=GIRL)
        boy = disnake.utils.get(self.inter.guild.roles, id=BOY)

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Девочка", style=ButtonStyle.blurple)
    async def girl(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await self.member.remove_roles(boy)

        await self.member.add_roles(girl)
        
        embed = disnake.Embed(title='Смена пола', description=f'{self.inter.author.mention}, Вы **изменили** пол {self.member.mention} на {girl.mention}', color=0x2f3136)
        embed.set_thumbnail(url=self.member.display_avatar)
        embed.timestamp = datetime.datetime.now()

        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль Admin
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
 
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль SECURITY
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            
        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
                    
        elif interaction.guild.get_role(MODER) in interaction.author.roles:    # Роль Moderatorа
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            
        elif interaction.guild.get_role(HELPER) in interaction.author.roles:    # Роль Control
            await interaction.response.edit_message(embed=embed, view=BackControl(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            

    @disnake.ui.button(label="Мальчик", style=ButtonStyle.blurple)
    async def boy(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await self.member.remove_roles(girl)

        await self.member.add_roles(boy)
        embed = disnake.Embed(title='Смена пола', description=f'{self.inter.author.mention}, Вы **изменили** пол {self.member.mention} на {boy.mention}', color=0x2f3136)
        embed.set_thumbnail(url=self.member.display_avatar)
        embed.timestamp = datetime.datetime.now()
        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль Admin
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
         
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль SECURITY
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            
        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
                    
        elif interaction.guild.get_role(MODER) in interaction.author.roles:    # Роль Moderatorа
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            
        elif interaction.guild.get_role(HELPER) in interaction.author.roles:    # Роль Control
            await interaction.response.edit_message(embed=embed, view=BackControl(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_SMENA_POLA)
            embed_log = disnake.Embed(
                title = 'Смена пола', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Сменил пол:',
                value = f'・{self.inter.author.mention}\n・{self.inter.author.name}\n・{self.inter.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Кому сменил:',
                value = f'・{self.member.mention}\n・{self.member.name}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> пол',
                value = '・Женский',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)  
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
        
    @disnake.ui.button(label="Назад", style=ButtonStyle.gray, row=3)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
        embed.set_thumbnail(url=self.inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль admin
            await interaction.response.edit_message(embed=embed, view=Admin(self.client, self.inter, self.member))
            return
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль SECURITY
            await interaction.response.edit_message(embed=embed, view=Security(self.client, self.inter, self.member))
            return
        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
            await interaction.response.edit_message(embed=embed, view=Curator(self.client, self.inter, self.member))
            return
        elif interaction.guild.get_role(MODER) in interaction.author.roles: # Роль MODERA
            await interaction.response.edit_message(embed=embed, view=Moderations(self.client, self.inter, self.member))
            return
        elif interaction.guild.get_role(HELPER) in interaction.author.roles: # Роль Control
            await interaction.response.edit_message(embed=embed, view=Control(self.client, self.inter, self.member))
            return

class Mute(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member
        
        global moderator
        global support
        moderator = disnake.utils.get(self.inter.guild.roles, id=MODER)
        support = disnake.utils.get(self.inter.guild.roles, id=SUPPORT)

        voiced = {self.inter.guild.get_role(MODER), self.inter.guild.get_role(CURATOR), self.inter.guild.get_role(ADMIN), self.inter.guild.get_role(SECURITY)} #АЙДДИ КУРАТОРА И МОДЕРА И АДДМИНА

        if not voiced.intersection(self.inter.author.roles):
            self.voice.disabled = True
            
    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Текстовой мут", style=ButtonStyle.green)
    async def chat(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):        
        role = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)                
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, У пользователя уже есть мут', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль security
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member)) 
                
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            
            elif interaction.guild.get_role(MODER) in interaction.author.roles: # Роль Modera
                await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
                
            elif interaction.guild.get_role(HELPER) in interaction.author.roles: # Роль Control
                await interaction.response.edit_message(embed=embed, view=BackControl(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Текстовой мут', description=f'{interaction.author.mention} Укажите причину **мута** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление пользователем — Текстовой мут', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление пользователем — Текстовой мут', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление пользователем — Текстовой мут', description=f'{interaction.author.mention} Укажите время **мута** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Пример: 10s/10m/10h/10d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление пользователем — Текстовой мут', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        
                        cursor.execute("UPDATE users SET mutes=mutes +1 WHERE id=?", [self.member.id])
                        cursor.execute("UPDATE users SET mutes=mutes +1 WHERE id=?", [interaction.author.id])
                        cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Текстовой мут', reason, interaction.author.id])
                        connection.commit()
                        embed = disnake.Embed(title='Управление пользователем — Текстовой мут', description=f'{interaction.author.mention}, Вы **замутили** {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        
                        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль security
                            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member)) 
                            
                        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        
                        elif interaction.guild.get_role(MODER) in interaction.author.roles: # Роль Modera
                            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                            
                        elif interaction.guild.get_role(HELPER) in interaction.author.roles: # Роль Control
                            await interaction.edit_original_message(embed=embed, view=BackControl(self.client, self.inter, self.member))
                        channel = self.client.get_channel(LOG_NAKAZANIA)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Мут', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Нарушитель:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Выдал:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Тип:',
                            value = f'・Текстовой мут',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed = embed_log)
                        try:
                            embed = disnake.Embed(title='Вам был выдан мут на сервере Hakone', color=0x2f3136)
                            embed.add_field(
                                name=f'> Выдал:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Тип:',
                                value=f'・Текстовой мут'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass

                        warn = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)
                        await self.member.remove_roles(warn)

                        role = disnake.utils.get(self.member.guild.roles, id=TEXT_MUTE)
                        await self.member.add_roles(role)
                        await asyncio.sleep(times)
                        await self.member.remove_roles(role)

                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление пользователем — Текстовой мут', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        
                        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль security
                            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member)) 
                            
                        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        
                        elif interaction.guild.get_role(MODER) in interaction.author.roles: # Роль Modera
                            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                            
                        elif interaction.guild.get_role(HELPER) in interaction.author.roles: # Роль Control
                            await interaction.edit_original_message(embed=embed, view=BackControl(self.client, self.inter, self.member))

    @disnake.ui.button(label="Голосовой мут", style=ButtonStyle.green)
    async def voice(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=VOICE_MUTE)                    
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, У пользователя уже есть мут', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                
            elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль security
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member)) 
            
            elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            
            elif interaction.guild.get_role(MODER) in interaction.author.roles: # Роль Modera
                await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
                
            elif interaction.guild.get_role(HELPER) in interaction.author.roles: # Роль Control
                await interaction.response.edit_message(embed=embed, view=BackControl(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Голосовой мут', description=f'{interaction.author.mention} Укажите причину **мута** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление пользователем — Голосовой мут', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление пользователем — Голосовой мут', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление пользователем — Голосовой мут', description=f'{interaction.author.mention} Укажите время **мута** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Пример: 10s/10m/10h/10d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление пользователем — Голосовой мут', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        
                        cursor.execute("UPDATE users SET mutes=mutes +1 WHERE id=?", [self.member.id])
                        cursor.execute("UPDATE users SET mutes=mutes +1 WHERE id=?", [interaction.author.id])
                        cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Текстовой мут', reason, interaction.author.id])
                        connection.commit()

                        
                        embed = disnake.Embed(title='Управление пользователем — Голосовой мут', description=f'{interaction.author.mention}, Вы **замутили** {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                            
                        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль security
                            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member)) 
                            
                        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        
                        elif interaction.guild.get_role(MODER) in interaction.author.roles: # Роль Modera
                            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))

                        channel = self.client.get_channel(LOG_NAKAZANIA)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Мут', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Нарушитель:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Выдал:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Тип:',
                            value = f'・Голосовой мут',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed = embed_log)
                        try:
                            embed = disnake.Embed(title='Вам был выдан мут на сервере tokame', color=0x2f3136)
                            embed.add_field(
                                name=f'> Выдал:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Тип:',
                                value=f'・Голосовой мут'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)
                        
                        except disnake.Forbidden:
                            pass

                        warn = disnake.utils.get(self.inter.guild.roles, id=VOICE_MUTE)
                        await self.member.remove_roles(warn)

                        role = disnake.utils.get(self.member.guild.roles, id=VOICE_MUTE)
                        await self.member.add_roles(role)
                        await self.member.move_to(None)
                        await asyncio.sleep(times)
                        await self.member.remove_roles(role)

                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление пользователем — Голосовой мут', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        if interaction.guild.get_role(ADMIN) in interaction.author.roles:    # Роль ADMIN
                            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        
                        elif interaction.guild.get_role(SECURITY) in interaction.author.roles:    # Роль security
                            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member)) 
                            
                        elif interaction.guild.get_role(CURATOR) in interaction.author.roles:    # Роль куратора
                            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        
                        elif interaction.guild.get_role(MODER) in interaction.author.roles: # Роль Modera
                            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                            
                        elif interaction.guild.get_role(HELPER) in interaction.author.roles: # Роль Control
                            await interaction.edit_original_message(embed=embed, view=BackControl(self.client, self.inter, self.member))

    @disnake.ui.button(label="Назад", style=ButtonStyle.blurple)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.guild.get_role(ADMIN) in interaction.author.roles: #роль admina
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Admin(self.client, self.inter, self.member))
         
        elif interaction.guild.get_role(SECURITY) in interaction.author.roles: #роль security
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Security(self.client, self.inter, self.member))
            
        elif interaction.guild.get_role(CURATOR) in interaction.author.roles: #роль куратора
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Curator(self.client, self.inter, self.member))
        
        elif interaction.guild.get_role(HELPER) in interaction.author.roles: #роль control
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Control(self.client, self.inter, self.member))
            return
        
        elif interaction.guild.get_role(MODER) in interaction.author.roles: #роль modera
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Moderations(self.client, self.inter, self.member))
            return
            
 

class Moderations(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member
        
        self.verifyzalupa.disabled = True
        self.creativerole.disabled = True

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Забанить", style=ButtonStyle.gray)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)                
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, У пользователя уже есть бан', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))   
        
        elif self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
            
        else:
            embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention} Укажите причину **бана** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

            def check(m: disnake.Message):
                return m.author == interaction.author and m.channel.id == interaction.channel.id 
            try:
                msg = await self.client.wait_for('message', check=check, timeout=30)
                await msg.delete()
                
            except asyncio.TimeoutError: 
                embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                return
            
            else:
                reason = msg.content

                if len(msg.content) > 35:
                        embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                        return
                
                else:
                    embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention} Укажите время **бана** пользователя {self.member.mention}', color=0x2f3136)
                    embed.set_footer(text='Пример: 10s/10m/10h/10d')
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=None)

                    def check(m: disnake.Message):
                        return m.author == interaction.author and m.channel.id == interaction.channel.id 
                    try:
                        msg = await self.client.wait_for('message', check=check, timeout = 30)
                        await msg.delete()
                        
                    except asyncio.TimeoutError: 
                        embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                        return
                    
                    else:
                        try:
                            if 's' in msg.content:
                                i = msg.content.replace("s", "")
                                times = int(i)

                                a = msg.content.replace("s", " секунд")

                            if 'm' in msg.content:
                                i = msg.content.replace("m", "")
                                times = int(i)*60

                                a = msg.content.replace("m", " минут")
                                
                            if 'h' in msg.content:
                                i = msg.content.replace("h", "")
                                times = int(i)*3600

                                a = msg.content.replace("h", " часов")

                            if 'd' in msg.content:
                                i = msg.content.replace("d", "")
                                times = int(i)*86400

                                a = msg.content.replace("d", " дней")

                            
                            cursor.execute("UPDATE users SET bans=bans+1 WHERE id=?", [self.member.id])
                            cursor.execute("UPDATE users SET bans=bans +1 WHERE id=?", [interaction.author.id])
                            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['ban', self.member.id])
                            cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Локальный бан', reason, interaction.author.id])
                            connection.commit()
    
                            
                            embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, Вы **забанили** {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))

                            channel = self.client.get_channel(LOG_NAKAZANIA)                       
                            embed_log = disnake.Embed(
                                title = 'Логи - Бан', color=0x2f3136
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Выдал:',
                                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Длительность:',
                                value = f'・{a}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Тип:',
                                value = f'・Локальный бан',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Причина:',
                                value = f'・{reason}',
                                inline=True
                            )
                            embed_log.set_thumbnail(url=interaction.author.display_avatar)
                            embed_log.timestamp = datetime.datetime.now()
                            await channel.send(embed = embed_log)
                            try:
                                embed = disnake.Embed(title='Вам был выдан бан на сервере tokame', color=0x2f3136)
                                
                                embed.add_field(
                                    name=f'> Выдал:',
                                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                                )
                                embed.add_field(
                                    name=f'> Длительность:',
                                    value=f'```{a}```'
                                )
                                embed.add_field(
                                    name=f'> Тип:',
                                    value=f'・Локальный бан'
                                )
                                embed.add_field(
                                    name=f'> Причина:',
                                    value=f'**```{reason}```**',
                                    inline=True
                                )

                                embed.set_thumbnail(url=interaction.author.display_avatar)
                                embed.timestamp = datetime.datetime.now()
                                await self.member.send(embed=embed)

                            except disnake.Forbidden:
                                pass


                            await self.member.edit(roles=[])
                            role = disnake.utils.get(self.member.guild.roles, id=BAN_ROLE)
                            await self.member.add_roles(role)
                            
                            await asyncio.sleep(times)
                            await self.member.remove_roles(role)
                            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['unban', self.member.id])
                            connection.commit()

                        except UnboundLocalError or ValueError:
                            embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                            return
                        
    @disnake.ui.button(label="Разбанить", style=ButtonStyle.gray)
    async def unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
           
        elif role in self.member.roles:    
            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['unban', self.member.id])
            connection.commit()

            local_ban = disnake.utils.get(self.member.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(local_ban)

            embed1 = disnake.Embed(title='Управление пользователем — Разбан', description=f'{interaction.author.mention}, Вы успешно **сняли** бан у {self.member.mention}!', color=0x2f3136)
            embed1.timestamp = datetime.datetime.now()
            embed1.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed1, view=Back(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Разбанить', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли бан', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)                            
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** бана ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
            
         
        
        
    @disnake.ui.button(label="Выдать мут", style=ButtonStyle.gray)
    async def mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):       
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** замутить пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))     
        
        else:
            embed = disnake.Embed(title='Управление пользователем — Мут', description=f'{interaction.author.mention} Выберите вид **мута** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Mute(self.client, self.inter, self.member))


    @disnake.ui.button(label="Снять мут", style=ButtonStyle.gray)
    async def unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=VOICE_MUTE)
        chats = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
           
        elif role in self.member.roles:    
            embed = disnake.Embed(title='Управление пользователем — Размут', description=f'{interaction.author.mention}, Выберите **вид мута** для размута пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Razmut(self.client, self.inter, self.member))
            
        elif chats in self.member.roles:    
            embed = disnake.Embed(title='Управление пользователем — Размут', description=f'{interaction.author.mention}, Выберите **вид мута** для размута пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Razmut(self.client, self.inter, self.member))
        
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** мута ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
            
    @disnake.ui.button(label="Cменить пол", style=ButtonStyle.gray)
    async def gendera(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** изменить пол пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Cменить пол', description=f'{interaction.author.mention} Выберите **пол** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Gender(self.client, self.inter, self.member))        
        
    @disnake.ui.button(label="Замечание", style=ButtonStyle.gray)
    async def genders(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать замечание пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        role = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, у пользователя {self.member.mention} **уже есть** замечание!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention} Укажите причину **замечание** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление замечание', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.add_roles(zames)
            embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, Вы **выдали** замечание {self.member.mention}, по причине **{reason}**', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
            
            await asyncio.sleep(3600)
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.remove_roles(zames)
    
    @disnake.ui.button(label="Выдать/Снять роль", style=ButtonStyle.blurple)
    async def creativerole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
    
    @disnake.ui.button(label="Верифицировать", style=ButtonStyle.gray)
    async def verifyzalupa(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass

            
    @disnake.ui.button(label="Выдать предупреждение", style=ButtonStyle.gray)
    async def warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать предупреждение пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
       
        if  cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -2 WHERE id=?", [self.member.id])
            connection.commit()
            await self.member.edit(roles=[])
            ban_role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(ban_role)
            embed = disnake.Embed(title='Выдача Предупреждение', description=f'{self.inter.author.mention}, Пользователь получил **3** предупреждений и получил бан.', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
        
        else:
            embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите причину **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление предупреждением', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите время **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Пример: 10s/10m/10h/10d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [interaction.author.id])
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [self.member.id])
                        cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Предупреждение', reason, interaction.author.id])
                        connection.commit()

                        embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Вы **выдали** предупреждение {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                        channel = self.client.get_channel(LOG_NAKAZANIA)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Предупреждение', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Нарушитель:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Исполнитель:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed = embed_log)
                        try:
                            embed = disnake.Embed(title='Вам выдали предупреждение', color=0x2f3136)
                            embed.add_field(
                                name=f'> Исполнитель:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass
                        
                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                        return
                        

    @disnake.ui.button(label="Снять предупреждение", style=ButtonStyle.gray, row=3)
    async def unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{interaction.author.mention}, у пользователя нету предупреждение', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))  
                                
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id])
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)        
            
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id]) 
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)       
                
    @disnake.ui.button(label="История наказаний", style=ButtonStyle.blurple, row=3)
    async def history(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        mutes = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        bans = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        
        rows = cursor.execute("SELECT date, punish_view, reason, given FROM history WHERE id = ?", [self.member.id])

        embeds = []
        if mutes+bans+warn == 0:
            embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Пользователь {self.member.mention}, не получал нарушений!', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embeds.append(embed)

        else:
            for i, row in enumerate(rows):
                if i % 5 == 0:
                    embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Мутов: **{mutes}** Банов: **{bans}** Предов: **{warn}**', color=0x2f3136)
                    embed.set_thumbnail(url=self.member.display_avatar)
                    embeds.append(embed)

                embed.add_field(
                    name=f'** **',
                    value=f'`{i+1}.` [<t:{row[0]}:f>] **{row[1]}** *Причина:* {row[2]}\nModeratorатор: <@{row[3]}>',
                    inline=False
                )

        await interaction.response.edit_message(embed=embeds[0], view=Menu(self.client, self.inter, self.member, embeds))

    @disnake.ui.button(label="Отменить", style=ButtonStyle.red, row=3)
    async def delete(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()
        
class Control(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member
        
        self.ban.disabled = True
        self.unban.disabled = True
        self.verifyzalupa.disabled = True
        self.creativerole.disabled = True

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Забанить", style=ButtonStyle.gray)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
                        
    @disnake.ui.button(label="Разбанить", style=ButtonStyle.gray)
    async def unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
        
    @disnake.ui.button(label="Выдать мут", style=ButtonStyle.gray)
    async def mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** замутить пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        else:
            embed = disnake.Embed(title='Управление пользователем — Мут', description=f'{interaction.author.mention} Выберите вид **мута** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Mute(self.client, self.inter, self.member))

    @disnake.ui.button(label="Снять мут", style=ButtonStyle.gray)
    async def unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        chats = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackControl(self.client, self.inter, self.member))
            
        elif chats in self.member.roles:    
            chats = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)
            await self.member.remove_roles(cmute)     
            embed = disnake.Embed(title='Управление пользователем — Снять мут', description=f'{interaction.author.mention}, Вы размутили пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            
            await interaction.response.edit_message(embed=embed, view=BackControl(self.client, self.inter, self.member))
       
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** мута ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackControl(self.client, self.inter, self.member))
            
    @disnake.ui.button(label="Cменить пол", style=ButtonStyle.gray)
    async def gendera(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** изменить пол пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Cменить пол', description=f'{interaction.author.mention} Выберите **пол** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Gender(self.client, self.inter, self.member))        
        
    @disnake.ui.button(label="Замечание", style=ButtonStyle.gray)
    async def genders(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать замечание пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        role = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, у пользователя {self.member.mention} **уже есть** замечание!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention} Укажите причину **замечание** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление замечание', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.add_roles(zames)
            embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, Вы **выдали** замечание {self.member.mention}, по причине **{reason}**', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
            
            await asyncio.sleep(3600)
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.remove_roles(zames)
    
    @disnake.ui.button(label="Выдать/Снять роль", style=ButtonStyle.blurple)
    async def creativerole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
    
    @disnake.ui.button(label="Верифицировать", style=ButtonStyle.gray)
    async def verifyzalupa(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass

            
    @disnake.ui.button(label="Выдать предупреждение", style=ButtonStyle.gray)
    async def warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать предупреждение пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
       
        if  cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -2 WHERE id=?", [self.member.id])
            connection.commit()
            await self.member.edit(roles=[])
            ban_role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(ban_role)
            embed = disnake.Embed(title='Выдача Предупреждение', description=f'{self.inter.author.mention}, Пользователь получил **3** предупреждений и получил бан.', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
        
        else:
            embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите причину **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление предупреждением', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите время **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Пример: 10s/10m/10h/10d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [interaction.author.id])
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [self.member.id])
                        cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Предупреждение', reason, interaction.author.id])
                        connection.commit()

                        embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Вы **выдали** предупреждение {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                        channel = self.client.get_channel(LOG_NAKAZANIA)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Предупреждение', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Нарушитель:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Исполнитель:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed = embed_log)
                        try:
                            embed = disnake.Embed(title='Вам выдали предупреждение', color=0x2f3136)
                            embed.add_field(
                                name=f'> Исполнитель:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass
                        
                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=Back(self.client, self.inter, self.member))
                        return
                        

    @disnake.ui.button(label="Снять предупреждение", style=ButtonStyle.gray, row=3)
    async def unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{interaction.author.mention}, у пользователя нету предупреждение', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))  
                                
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id])
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)        
            
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id]) 
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)       
                
    @disnake.ui.button(label="История наказаний", style=ButtonStyle.blurple, row=3)
    async def history(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        mutes = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        bans = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        
        rows = cursor.execute("SELECT date, punish_view, reason, given FROM history WHERE id = ?", [self.member.id])

        embeds = []
        if mutes+bans+warn == 0:
            embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Пользователь {self.member.mention}, не получал нарушений!', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embeds.append(embed)

        else:
            for i, row in enumerate(rows):
                if i % 5 == 0:
                    embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Мутов: **{mutes}** Банов: **{bans}** Предов: **{warn}**', color=0x2f3136)
                    embed.set_thumbnail(url=self.member.display_avatar)
                    embeds.append(embed)

                embed.add_field(
                    name=f'** **',
                    value=f'`{i+1}.` [<t:{row[0]}:f>] **{row[1]}** *Причина:* {row[2]}\nModeratorатор: <@{row[3]}>',
                    inline=False
                )

        await interaction.response.edit_message(embed=embeds[0], view=Menu(self.client, self.inter, self.member, embeds))

    @disnake.ui.button(label="Отменить", style=ButtonStyle.red, row=3)
    async def delete(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()        
        
        
class Support(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

        self.ban.disabled = True
        self.unban.disabled = True
        self.mute.disabled = True
        self.unmute.disabled = True
        self.warn.disabled = True
        self.unwarn.disabled = True
        self.genders.disabled = True
        self.history.disabled = True

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Забанить", style=ButtonStyle.gray)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
                        
    @disnake.ui.button(label="Разбанить", style=ButtonStyle.gray)
    async def unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
        
    @disnake.ui.button(label="Выдать мут", style=ButtonStyle.gray)
    async def mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass


    @disnake.ui.button(label="Снять мут", style=ButtonStyle.gray)
    async def unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
        
    @disnake.ui.button(label="Замечание", style=ButtonStyle.gray)
    async def genders(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
   
    @disnake.ui.button(label="Верифицировать", style=ButtonStyle.gray)
    async def verifygender(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** верифицировать пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSupport(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Верифицировать', description=f'{interaction.author.mention} Выберите **гендерную роль** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=VerifySupport(self.client, self.inter, self.member))        

    @disnake.ui.button(label="Выдать предупреждение", style=ButtonStyle.gray)
    async def warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
    
    @disnake.ui.button(label="Снять предупреждение", style=ButtonStyle.gray)
    async def unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass

    @disnake.ui.button(label="История наказаний", style=ButtonStyle.blurple, row=3)
    async def history(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass

    @disnake.ui.button(label="Отменить", style=ButtonStyle.red, row=3)
    async def deleted(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()        
        
class Creative(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

        self.ban.disabled = True
        self.unban.disabled = True
        self.mute.disabled = True
        self.unmute.disabled = True
        self.warn.disabled = True
        self.unwarn.disabled = True
        self.genders.disabled = True
        self.verifygender.disabled = True
        self.history.disabled = True

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Забанить", style=ButtonStyle.gray, row=1)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
                        
    @disnake.ui.button(label="Разбанить", style=ButtonStyle.gray, row=1)
    async def unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
        
    @disnake.ui.button(label="Выдать мут", style=ButtonStyle.gray, row=1)
    async def mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass


    @disnake.ui.button(label="Снять мут", style=ButtonStyle.gray, row=1)
    async def unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
        
    @disnake.ui.button(label="Замечание", style=ButtonStyle.gray, row=1)
    async def genders(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
   
    @disnake.ui.button(label="Верифицировать", style=ButtonStyle.gray, row=2)
    async def verifygender(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
    
    @disnake.ui.button(label="Выдать/Снять роль", style=ButtonStyle.blurple, row=2)
    async def creativerole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** Выдать/Снять роль пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSupport(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Выдать/Снять роль', description=f'{interaction.author.mention} Выберите **взаимодействия ролью** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=CreativeRole(self.client, self.inter, self.member))        
    

    @disnake.ui.button(label="Выдать предупреждение", style=ButtonStyle.gray, row=2)
    async def warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass
    
    @disnake.ui.button(label="Снять предупреждение", style=ButtonStyle.gray, row=3)
    async def unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass

    @disnake.ui.button(label="История наказаний", style=ButtonStyle.blurple, row=3)
    async def history(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass

    @disnake.ui.button(label="Отменить", style=ButtonStyle.red, row=3)
    async def deleted(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()                

class Admin(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Забанить", style=ButtonStyle.gray)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)                
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, У пользователя уже есть бан', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))   
        
        elif self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        else:
            embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention} Укажите причину **бана** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

            def check(m: disnake.Message):
                return m.author == interaction.author and m.channel.id == interaction.channel.id 
            try:
                msg = await self.client.wait_for('message', check=check, timeout=30)
                await msg.delete()
                
            except asyncio.TimeoutError: 
                embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
            
            else:
                reason = msg.content

                if len(msg.content) > 35:
                        embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        return
                
                else:
                    embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention} Укажите время **бана** пользователя {self.member.mention}', color=0x2f3136)
                    embed.set_footer(text='Пример: 10s/10m/10h/10d')
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=None)

                    def check(m: disnake.Message):
                        return m.author == interaction.author and m.channel.id == interaction.channel.id 
                    try:
                        msg = await self.client.wait_for('message', check=check, timeout = 30)
                        await msg.delete()
                        
                    except asyncio.TimeoutError: 
                        embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        return
                    
                    else:
                        try:
                            if 's' in msg.content:
                                i = msg.content.replace("s", "")
                                times = int(i)

                                a = msg.content.replace("s", " секунд")

                            if 'm' in msg.content:
                                i = msg.content.replace("m", "")
                                times = int(i)*60

                                a = msg.content.replace("m", " минут")
                                
                            if 'h' in msg.content:
                                i = msg.content.replace("h", "")
                                times = int(i)*3600

                                a = msg.content.replace("h", " часов")

                            if 'd' in msg.content:
                                i = msg.content.replace("d", "")
                                times = int(i)*86400

                                a = msg.content.replace("d", " дней")

                            
                            cursor.execute("UPDATE users SET bans=bans+1 WHERE id=?", [self.member.id])
                            cursor.execute("UPDATE users SET bans=bans +1 WHERE id=?", [interaction.author.id])
                            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['ban', self.member.id])
                            cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Локальный бан', reason, interaction.author.id])
                            connection.commit()
    
                            
                            embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, Вы **забанили** {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))

                            channel = self.client.get_channel(LOG_NAKAZANIA)                       
                            embed_log = disnake.Embed(
                                title = 'Логи - Бан', color=0x2f3136
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Выдал:',
                                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Длительность:',
                                value = f'・{a}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Тип:',
                                value = f'・Локальный бан',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Причина:',
                                value = f'・{reason}',
                                inline=True
                            )
                            embed_log.set_thumbnail(url=interaction.author.display_avatar)
                            embed_log.timestamp = datetime.datetime.now()
                            await channel.send(embed = embed_log)
                            try:
                                embed = disnake.Embed(title='Вам был выдан бан на сервере tokame', color=0x2f3136)
                                
                                embed.add_field(
                                    name=f'> Выдал:',
                                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                                )
                                embed.add_field(
                                    name=f'> Длительность:',
                                    value=f'```{a}```'
                                )
                                embed.add_field(
                                    name=f'> Тип:',
                                    value=f'・Локальный бан'
                                )
                                embed.add_field(
                                    name=f'> Причина:',
                                    value=f'**```{reason}```**',
                                    inline=True
                                )

                                embed.set_thumbnail(url=interaction.author.display_avatar)
                                embed.timestamp = datetime.datetime.now()
                                await self.member.send(embed=embed)

                            except disnake.Forbidden:
                                pass

                            await self.member.edit(roles=[])
                            role = disnake.utils.get(self.member.guild.roles, id=BAN_ROLE)
                            await self.member.add_roles(role)
                            await asyncio.sleep(times)
                            await self.member.remove_roles(role)
                            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['unban', self.member.id])
                            connection.commit()

                        except UnboundLocalError or ValueError:
                            embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                            return
                        
    @disnake.ui.button(label="Разбанить", style=ButtonStyle.gray)
    async def unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
           
        elif role in self.member.roles:    
            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['unban', self.member.id])
            connection.commit()

            local_ban = disnake.utils.get(self.member.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(local_ban)

            embed1 = disnake.Embed(title='Управление пользователем — Разбан', description=f'{interaction.author.mention}, Вы успешно **сняли** бан у {self.member.mention}!', color=0x2f3136)
            embed1.timestamp = datetime.datetime.now()
            embed1.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed1, view=BackAdmin(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Разбанить', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли бан', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)                            
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** бана ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        
    @disnake.ui.button(label="Выдать мут", style=ButtonStyle.gray)
    async def mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** замутить пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        else:
            embed = disnake.Embed(title='Управление пользователем — Мут', description=f'{interaction.author.mention} Выберите вид **мута** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Mute(self.client, self.inter, self.member))


    @disnake.ui.button(label="Снять мут", style=ButtonStyle.gray)
    async def unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=VOICE_MUTE)
        chats = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
           
        elif role in self.member.roles:    
            embed = disnake.Embed(title='Управление пользователем — Размут', description=f'{interaction.author.mention}, Выберите **вид мута** для размута пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Razmut(self.client, self.inter, self.member))
            
        elif chats in self.member.roles:    
            embed = disnake.Embed(title='Управление пользователем — Размут', description=f'{interaction.author.mention}, Выберите **вид мута** для размута пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Razmut(self.client, self.inter, self.member))
        
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** мута ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))

   
    @disnake.ui.button(label="Замечание", style=ButtonStyle.gray)
    async def genders(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать замечание пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        role = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, у пользователя {self.member.mention} **уже есть** замечание!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention} Укажите причину **замечание** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление замечание', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                    return
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.add_roles(zames)
            embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, Вы **выдали** замечание {self.member.mention}, по причине **{reason}**', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            
            await asyncio.sleep(3600)
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.remove_roles(zames)    
        
    @disnake.ui.button(label="Верифицировать", style=ButtonStyle.gray)
    async def verifygender(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** верифицировать пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Верифицировать', description=f'{interaction.author.mention} Выберите **гендерную роль** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=VerifySupport(self.client, self.inter, self.member))
                    
    @disnake.ui.button(label="Сменить пол", style=ButtonStyle.gray)
    async def genderole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** изменить пол пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Cменить пол', description=f'{interaction.author.mention} Выберите **пол** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Gender(self.client, self.inter, self.member))                    
                    
    @disnake.ui.button(label="Выдать предупреждение", style=ButtonStyle.gray)
    async def warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать предупреждение пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
       
        if  cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -2 WHERE id=?", [self.member.id])
            connection.commit()
            await self.member.edit(roles=[])
            ban_role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(ban_role)
            embed = disnake.Embed(title='Выдача Предупреждение', description=f'{self.inter.author.mention}, Пользователь получил **3** предупреждений и получил бан.', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
        
        else:
            embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите причину **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление предупреждением', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите время **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Пример: 10s/10m/10h/10d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [interaction.author.id])
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [self.member.id])
                        cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Предупреждение', reason, interaction.author.id])
                        connection.commit()

                        embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Вы **выдали** предупреждение {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        channel = self.client.get_channel(LOG_NAKAZANIA)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Предупреждение', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Нарушитель:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Исполнитель:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed = embed_log)
                        try:
                            embed = disnake.Embed(title='Вам выдали предупреждение', color=0x2f3136)
                            embed.add_field(
                                name=f'> Исполнитель:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass
                        
                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        return
                        

    @disnake.ui.button(label="Снять предупреждение", style=ButtonStyle.gray)
    async def unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{interaction.author.mention}, у пользователя нету предупреждение', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))  
                                
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id])
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)        
            
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id]) 
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)        
            
    @disnake.ui.button(label="Выдать выговор", style=ButtonStyle.gray, row=2)
    async def vigovor(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать выговор пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        
        if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET vigovor=vigovor -2 WHERE id=?", [self.member.id])
            connection.commit()
            curator = disnake.utils.get(self.inter.guild.roles, id=CURATOR)
            moderator = disnake.utils.get(self.inter.guild.roles, id=MODER)
            support = disnake.utils.get(self.inter.guild.roles, id=SUPPORT)
            broadcaster = disnake.utils.get(self.inter.guild.roles, id=BROADCASTER)
            eventer = disnake.utils.get(self.inter.guild.roles, id=EVENTER)
            creative = disnake.utils.get(self.inter.guild.roles, id=CREATIVE)
            closemaker = disnake.utils.get(self.inter.guild.roles, id=CLOSEMAKER)
            staff = disnake.utils.get(self.inter.guild.roles, id=STAFF_ROLE)
            await self.member.remove_roles(CURATOR)
            await self.member.remove_roles(moderator)
            await self.member.remove_roles(support)
            await self.member.remove_roles(broadcaster)
            await self.member.remove_roles(eventer)
            await self.member.remove_roles(staff)
            await self.member.remove_roles(closemaker)
            await self.member.remove_roles(creative)
            
            embed = disnake.Embed(title='Выдача выговора', description=f'{self.inter.author.mention}, Вы **выдали 3 выговор** и пользователь {self.member.mention} был снят с ролей состава.', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Выговор/Снятие', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            try:
                embed = disnake.Embed(title='Вас сняли у вас 3 выговора', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                )
                embed.add_field(
                    name=f'> Причина:',
                    value=f'**```{reason}```**',
                    inline=True
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)
            
            except disnake.Forbidden:
                pass

                    
            except UnboundLocalError or ValueError:
                embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
        else:
            embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention} Укажите причину **выговора** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

            def check(m: disnake.Message):
                return m.author == interaction.author and m.channel.id == interaction.channel.id 
            try:
                msg = await self.client.wait_for('message', check=check, timeout=30)
                await msg.delete()
                
            except asyncio.TimeoutError: 
                embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                return
            
            else:
                reason = msg.content

                if len(msg.content) > 35:
                        embed = disnake.Embed(title='Управление выговором', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        return
                
                else:
                    embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention} Укажите время **выговора** пользователя {self.member.mention}', color=0x2f3136)
                    embed.set_footer(text='Пример: 10s/10m/10h/10d')
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=None)

                    def check(m: disnake.Message):
                        return m.author == interaction.author and m.channel.id == interaction.channel.id 
                    try:
                        msg = await self.client.wait_for('message', check=check, timeout = 30)
                        await msg.delete()
                        
                    except asyncio.TimeoutError: 
                        embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        return
                    
                    else:
                        try:
                            if 's' in msg.content:
                                i = msg.content.replace("s", "")
                                times = int(i)

                                a = msg.content.replace("s", " секунд")

                            if 'm' in msg.content:
                                i = msg.content.replace("m", "")
                                times = int(i)*60

                                a = msg.content.replace("m", " минут")
                                
                            if 'h' in msg.content:
                                i = msg.content.replace("h", "")
                                times = int(i)*3600

                                a = msg.content.replace("h", " часов")

                            if 'd' in msg.content:
                                i = msg.content.replace("d", "")
                                times = int(i)*86400

                                a = msg.content.replace("d", " дней")

                            

                            cursor.execute("UPDATE users SET vigovor=vigovor +1 WHERE id=?", [self.member.id])
                            connection.commit()
    
                            embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Вы **выдали** выговор {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))                                                         
                            channel = self.client.get_channel(LOG_NAKAZANIA)                       
                            embed_log = disnake.Embed(
                                title = 'Логи - Выговор', color=0x2f3136
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Исполнитель:',
                                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Длительность:',
                                value = f'・{a}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Причина:',
                                value = f'・{reason}',
                                inline=True
                            )
                            embed_log.set_thumbnail(url=interaction.author.display_avatar)
                            embed_log.timestamp = datetime.datetime.now()
                            await channel.send(embed=embed_log)
                            try:
                                embed = disnake.Embed(title='Вам выдали выговор', color=0x2f3136)
                                embed.add_field(
                                    name=f'> Исполнитель:',
                                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                                )
                                embed_log.add_field(
                                    name = '> Нарушитель:',
                                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                                )
                                embed.add_field(
                                    name=f'> Длительность:',
                                    value=f'```{a}```'
                                )
                                embed.add_field(
                                    name=f'> Причина:',
                                    value=f'**```{reason}```**',
                                    inline=True
                                )
                                embed.set_thumbnail(url=interaction.author.display_avatar)
                                embed.timestamp = datetime.datetime.now()
                                await self.member.send(embed=embed)

                            except disnake.Forbidden:
                                pass

                            await asyncio.sleep(times)
                            cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                            connection.commit()
                            
                        except UnboundLocalError or ValueError:
                            embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                            return
                        
    @disnake.ui.button(label="Снятие выговора", style=ButtonStyle.gray, row=2)
    async def vigovors(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
                
        if cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие выговора', description=f'{interaction.author.mention}, у пользователя нету выговора', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))   
                            
        elif -1 > cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]:
            embed = disnake.Embed(title='Снятие выговора', description=f'{interaction.author.mention}, у пользователя нету выговора', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.send(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
               
        else:
            if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие выговора', description=f'{self.inter.author.mention}, Вы **успешно сняли** выговор с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Выговора', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли выговор', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        
             
            if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
                cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие выговора', description=f'{self.inter.author.mention}, Вы **успешно сняли** выговор с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Выговора', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли выговор', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)         

    @disnake.ui.button(label="Выдать отпуск", style=ButtonStyle.gray, row=2)
    async def rest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Снятие отпуска', description=f'{interaction.author.mention}, у пользователя уже есть отпуск', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))   
        
        embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention} Укажите причину выдачи **отпуску** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление отпуском', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention} Укажите время на сколько выдано **отпуск** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Указывайте в днях: 1d/14d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        

                        cursor.execute("UPDATE users SET otpysk=otpysk +1 WHERE id=?", [self.member.id])
                        connection.commit()

                        embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, Вы **выдали** отпуск {self.member.mention}, причина отпуска **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))                                                         
                        channel = self.client.get_channel(LOG_OTPYSK)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Отпуск', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Получил отпуск:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Исполнитель:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность отпуска:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина отпуска:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed=embed_log)
                        try:
                            embed = disnake.Embed(title='Вы получили отпуск', color=0x2f3136)
                            embed.add_field(
                                name=f'> Исполнитель:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass

                        role = disnake.utils.get(self.member.guild.roles, id=OTPYSK_ROLE) #роль отпуска
                        await self.member.add_roles(role) 
                        
                        await asyncio.sleep(times)
                        await self.member.remove_roles(role) 
                        cursor.execute("UPDATE users SET otpysk=otpysk -1 WHERE id=?", [self.member.id])
                        connection.commit()
                        
                        
                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                        return

    @disnake.ui.button(label="Снять отпуск", style=ButtonStyle.gray, row=2)
    async def unrest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие отпуска', description=f'{interaction.author.mention}, у пользователя нету отпуска', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))   
               
        else:
            if  cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET otpysk=otpysk -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие отпуска', description=f'{self.inter.author.mention}, Вы **успешно сняли** отпуск с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_OTPYSK)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Отпуска', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Кому сняли:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли отпуск', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Сняли отпуск:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        


    @disnake.ui.button(label="Выдать/Снять роль", style=ButtonStyle.blurple, row=3)
    async def creativerole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** Выдать/Снять роль пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Выдать/Снять роль', description=f'{interaction.author.mention} Выберите **взаимодействия ролью** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=CreativeRole(self.client, self.inter, self.member))      

    @disnake.ui.button(label="Добавить в чс состава", style=ButtonStyle.gray, row=3)
    async def staffban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(title='Ошибка Прав', description=f'{interaction.author.mention}, вы **не можете** добавить в чс состава пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        if cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention}, **уже находиться** в чс состава', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention} Укажите причину **добавление в чс состава** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Добавление в чс состава', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
                    return
            cursor.execute("UPDATE users SET staffban=staffban +1 WHERE id=?", [self.member.id])
            channel = self.client.get_channel(LOG_STAFFBAN)                       
            embed_log = disnake.Embed(
                title = 'Логи - Добавление в чс состава', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Получил чс состава:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Причина добавление в чс состава:',
                value = f'・{reason}',
                inline=True
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            embed = disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention}, Вы **добавили** пользователя {self.member.mention}, в чс состава по причине **{reason}**', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))
    
    @disnake.ui.button(label="Убрать из чс состава", style=ButtonStyle.gray, row=3)
    async def staffson(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Убрать из чс состава', description=f'{interaction.author.mention}, пользователь не находиться в чс состава', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))   
               
        else:
            if  cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET staffban=staffban -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Убрать из чс состава', description=f'{self.inter.author.mention}, Вы **успешно убрали** чс состава с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Убрать из чс состава', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Кому сняли:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли чс состава', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Сняли чс состава:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        

    @disnake.ui.button(label="Выдать/Снять роль ветки", style=ButtonStyle.green, row=4)
    async def role(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Выдать/Снять роль ветки', description=f'{self.inter.author.mention}, выберите роль ветки {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        await interaction.response.edit_message(embed=embed, view=Staff(self.inter, self.client, self.member))

    @disnake.ui.button(label="Профиль Состава", style=ButtonStyle.blurple, row=4)
    async def mprofile(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.guild.get_role(ADMIN) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Администратора - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
        
        elif interaction.guild.get_role(CURATOR) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Куратора - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
            
        elif interaction.guild.get_role(MODER) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Модератора - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
        
            
        elif interaction.guild.get_role(HELPER) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Контрола - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
                value=f'```Контрол```',
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
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
            
        elif interaction.guild.get_role(SUPPORT) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Саппорта - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))     
        else:         
            embed = disnake.Embed(title='Профиль Состава', description=f'Пользователь {self.member.mention} не находится на ветке', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackAdmin(self.client, self.inter, self.member))    
            
    @disnake.ui.button(label="История наказаний", style=ButtonStyle.blurple, row=4)
    async def history(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        mutes = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        bans = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        
        rows = cursor.execute("SELECT date, punish_view, reason, given FROM history WHERE id = ?", [self.member.id])

        embeds = []
        if mutes+bans+warn == 0:
            embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Пользователь {self.member.mention}, не получал нарушений!', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embeds.append(embed)

        else:
            for i, row in enumerate(rows):
                if i % 5 == 0:
                    embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Мутов: **{mutes}** Банов: **{bans}** Предов: **{warn}**', color=0x2f3136)
                    embed.set_thumbnail(url=self.member.display_avatar)
                    embeds.append(embed)

                embed.add_field(
                    name=f'** **',
                    value=f'`{i+1}.` [<t:{row[0]}:f>] **{row[1]}** *Причина:* {row[2]}\nМодератор: <@{row[3]}>',
                    inline=False
                )

        await interaction.response.edit_message(embed=embeds[0], view=Menu(self.client, self.inter, self.member, embeds))

    @disnake.ui.button(label="Отмена", style=ButtonStyle.red, row=4)
    async def delete(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()


class Security(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Забанить", style=ButtonStyle.gray)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)                
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, У пользователя уже есть бан', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))   
        
        elif self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        else:
            embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention} Укажите причину **бана** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

            def check(m: disnake.Message):
                return m.author == interaction.author and m.channel.id == interaction.channel.id 
            try:
                msg = await self.client.wait_for('message', check=check, timeout=30)
                await msg.delete()
                
            except asyncio.TimeoutError: 
                embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
            
            else:
                reason = msg.content

                if len(msg.content) > 35:
                        embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                        return
                
                else:
                    embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention} Укажите время **бана** пользователя {self.member.mention}', color=0x2f3136)
                    embed.set_footer(text='Пример: 10s/10m/10h/10d')
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=None)

                    def check(m: disnake.Message):
                        return m.author == interaction.author and m.channel.id == interaction.channel.id 
                    try:
                        msg = await self.client.wait_for('message', check=check, timeout = 30)
                        await msg.delete()
                        
                    except asyncio.TimeoutError: 
                        embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                        return
                    
                    else:
                        try:
                            if 's' in msg.content:
                                i = msg.content.replace("s", "")
                                times = int(i)

                                a = msg.content.replace("s", " секунд")

                            if 'm' in msg.content:
                                i = msg.content.replace("m", "")
                                times = int(i)*60

                                a = msg.content.replace("m", " минут")
                                
                            if 'h' in msg.content:
                                i = msg.content.replace("h", "")
                                times = int(i)*3600

                                a = msg.content.replace("h", " часов")

                            if 'd' in msg.content:
                                i = msg.content.replace("d", "")
                                times = int(i)*86400

                                a = msg.content.replace("d", " дней")

                            
                            cursor.execute("UPDATE users SET bans=bans+1 WHERE id=?", [self.member.id])
                            cursor.execute("UPDATE users SET bans=bans +1 WHERE id=?", [interaction.author.id])
                            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['ban', self.member.id])
                            cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Локальный бан', reason, interaction.author.id])
                            connection.commit()
    
                            
                            embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, Вы **забанили** {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))

                            channel = self.client.get_channel(LOG_NAKAZANIA)                       
                            embed_log = disnake.Embed(
                                title = 'Логи - Бан', color=0x2f3136
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Выдал:',
                                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Длительность:',
                                value = f'・{a}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Тип:',
                                value = f'・Локальный бан',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Причина:',
                                value = f'・{reason}',
                                inline=True
                            )
                            embed_log.set_thumbnail(url=interaction.author.display_avatar)
                            embed_log.timestamp = datetime.datetime.now()
                            await channel.send(embed = embed_log)
                            try:
                                embed = disnake.Embed(title='Вам был выдан бан на сервере tokame', color=0x2f3136)
                                
                                embed.add_field(
                                    name=f'> Выдал:',
                                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                                )
                                embed.add_field(
                                    name=f'> Длительность:',
                                    value=f'```{a}```'
                                )
                                embed.add_field(
                                    name=f'> Тип:',
                                    value=f'・Локальный бан'
                                )
                                embed.add_field(
                                    name=f'> Причина:',
                                    value=f'**```{reason}```**',
                                    inline=True
                                )

                                embed.set_thumbnail(url=interaction.author.display_avatar)
                                embed.timestamp = datetime.datetime.now()
                                await self.member.send(embed=embed)

                            except disnake.Forbidden:
                                pass

                            await self.member.edit(roles=[])
                            role = disnake.utils.get(self.member.guild.roles, id=BAN_ROLE)
                            await self.member.add_roles(role)
                            await asyncio.sleep(times)
                            await self.member.remove_roles(role)
                            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['unban', self.member.id])
                            connection.commit()

                        except UnboundLocalError or ValueError:
                            embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                            return
                        
    @disnake.ui.button(label="Разбанить", style=ButtonStyle.gray)
    async def unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
           
        elif role in self.member.roles:    
            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['unban', self.member.id])
            connection.commit()

            local_ban = disnake.utils.get(self.member.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(local_ban)

            embed1 = disnake.Embed(title='Управление пользователем — Разбан', description=f'{interaction.author.mention}, Вы успешно **сняли** бан у {self.member.mention}!', color=0x2f3136)
            embed1.timestamp = datetime.datetime.now()
            embed1.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed1, view=BackSecurity(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Разбанить', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли бан', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)                            
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** бана ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        
    @disnake.ui.button(label="Выдать мут", style=ButtonStyle.gray)
    async def mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** замутить пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Back(self.client, self.inter, self.member))
        else:
            embed = disnake.Embed(title='Управление пользователем — Мут', description=f'{interaction.author.mention} Выберите вид **мута** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Mute(self.client, self.inter, self.member))


    @disnake.ui.button(label="Снять мут", style=ButtonStyle.gray)
    async def unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=VOICE_MUTE)
        chats = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
           
        elif role in self.member.roles:    
            embed = disnake.Embed(title='Управление пользователем — Размут', description=f'{interaction.author.mention}, Выберите **вид мута** для размута пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Razmut(self.client, self.inter, self.member))
            
        elif chats in self.member.roles:    
            embed = disnake.Embed(title='Управление пользователем — Размут', description=f'{interaction.author.mention}, Выберите **вид мута** для размута пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Razmut(self.client, self.inter, self.member))
        
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** мута ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))

   
    @disnake.ui.button(label="Замечание", style=ButtonStyle.gray)
    async def genders(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать замечание пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        role = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, у пользователя {self.member.mention} **уже есть** замечание!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention} Укажите причину **замечание** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление замечание', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                    return
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.add_roles(zames)
            embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, Вы **выдали** замечание {self.member.mention}, по причине **{reason}**', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            
            await asyncio.sleep(3600)
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.remove_roles(zames)    
        
    @disnake.ui.button(label="Верифицировать", style=ButtonStyle.gray)
    async def verifygender(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** верифицировать пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Верифицировать', description=f'{interaction.author.mention} Выберите **гендерную роль** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=VerifySupport(self.client, self.inter, self.member))
                    
    @disnake.ui.button(label="Сменить пол", style=ButtonStyle.gray)
    async def genderole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** изменить пол пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Cменить пол', description=f'{interaction.author.mention} Выберите **пол** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Gender(self.client, self.inter, self.member))                    
                    
    @disnake.ui.button(label="Выдать предупреждение", style=ButtonStyle.gray)
    async def warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать предупреждение пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
       
        if  cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -2 WHERE id=?", [self.member.id])
            connection.commit()
            await self.member.edit(roles=[])
            ban_role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(ban_role)
            embed = disnake.Embed(title='Выдача Предупреждение', description=f'{self.inter.author.mention}, Пользователь получил **3** предупреждений и получил бан.', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
        
        else:
            embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите причину **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление предупреждением', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите время **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Пример: 10s/10m/10h/10d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [interaction.author.id])
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [self.member.id])
                        cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Предупреждение', reason, interaction.author.id])
                        connection.commit()

                        embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Вы **выдали** предупреждение {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                        channel = self.client.get_channel(LOG_NAKAZANIA)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Предупреждение', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Нарушитель:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Исполнитель:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed = embed_log)
                        try:
                            embed = disnake.Embed(title='Вам выдали предупреждение', color=0x2f3136)
                            embed.add_field(
                                name=f'> Исполнитель:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass
                        
                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                        return
                        

    @disnake.ui.button(label="Снять предупреждение", style=ButtonStyle.gray)
    async def unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{interaction.author.mention}, у пользователя нету предупреждение', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))  
                                
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id])
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)        
            
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id]) 
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)        
            
    @disnake.ui.button(label="Выдать выговор", style=ButtonStyle.gray, row=2)
    async def vigovor(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать выговор пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        
        if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET vigovor=vigovor -2 WHERE id=?", [self.member.id])
            connection.commit()
            curator = disnake.utils.get(self.inter.guild.roles, id=CURATOR)
            moderator = disnake.utils.get(self.inter.guild.roles, id=MODER)
            support = disnake.utils.get(self.inter.guild.roles, id=SUPPORT)
            broadcaster = disnake.utils.get(self.inter.guild.roles, id=BROADCASTER)
            eventer = disnake.utils.get(self.inter.guild.roles, id=EVENTER)
            creative = disnake.utils.get(self.inter.guild.roles, id=CREATIVE)
            closemaker = disnake.utils.get(self.inter.guild.roles, id=CLOSEMAKER)
            staff = disnake.utils.get(self.inter.guild.roles, id=STAFF_ROLE)
            await self.member.remove_roles(CURATOR)
            await self.member.remove_roles(moderator)
            await self.member.remove_roles(support)
            await self.member.remove_roles(broadcaster)
            await self.member.remove_roles(eventer)
            await self.member.remove_roles(staff)
            await self.member.remove_roles(closemaker)
            await self.member.remove_roles(creative)
            
            embed = disnake.Embed(title='Выдача выговора', description=f'{self.inter.author.mention}, Вы **выдали 3 выговор** и пользователь {self.member.mention} был снят с ролей состава.', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Выговор/Снятие', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            try:
                embed = disnake.Embed(title='Вас сняли у вас 3 выговора', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                )
                embed.add_field(
                    name=f'> Причина:',
                    value=f'**```{reason}```**',
                    inline=True
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)
            
            except disnake.Forbidden:
                pass

                    
            except UnboundLocalError or ValueError:
                embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
        else:
            embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention} Укажите причину **выговора** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

            def check(m: disnake.Message):
                return m.author == interaction.author and m.channel.id == interaction.channel.id 
            try:
                msg = await self.client.wait_for('message', check=check, timeout=30)
                await msg.delete()
                
            except asyncio.TimeoutError: 
                embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                return
            
            else:
                reason = msg.content

                if len(msg.content) > 35:
                        embed = disnake.Embed(title='Управление выговором', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                        return
                
                else:
                    embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention} Укажите время **выговора** пользователя {self.member.mention}', color=0x2f3136)
                    embed.set_footer(text='Пример: 10s/10m/10h/10d')
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=None)

                    def check(m: disnake.Message):
                        return m.author == interaction.author and m.channel.id == interaction.channel.id 
                    try:
                        msg = await self.client.wait_for('message', check=check, timeout = 30)
                        await msg.delete()
                        
                    except asyncio.TimeoutError: 
                        embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                        return
                    
                    else:
                        try:
                            if 's' in msg.content:
                                i = msg.content.replace("s", "")
                                times = int(i)

                                a = msg.content.replace("s", " секунд")

                            if 'm' in msg.content:
                                i = msg.content.replace("m", "")
                                times = int(i)*60

                                a = msg.content.replace("m", " минут")
                                
                            if 'h' in msg.content:
                                i = msg.content.replace("h", "")
                                times = int(i)*3600

                                a = msg.content.replace("h", " часов")

                            if 'd' in msg.content:
                                i = msg.content.replace("d", "")
                                times = int(i)*86400

                                a = msg.content.replace("d", " дней")

                            

                            cursor.execute("UPDATE users SET vigovor=vigovor +1 WHERE id=?", [self.member.id])
                            connection.commit()
    
                            embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Вы **выдали** выговор {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))                                                         
                            channel = self.client.get_channel(LOG_NAKAZANIA)                       
                            embed_log = disnake.Embed(
                                title = 'Логи - Выговор', color=0x2f3136
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Исполнитель:',
                                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Длительность:',
                                value = f'・{a}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Причина:',
                                value = f'・{reason}',
                                inline=True
                            )
                            embed_log.set_thumbnail(url=interaction.author.display_avatar)
                            embed_log.timestamp = datetime.datetime.now()
                            await channel.send(embed=embed_log)
                            try:
                                embed = disnake.Embed(title='Вам выдали выговор', color=0x2f3136)
                                embed.add_field(
                                    name=f'> Исполнитель:',
                                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                                )
                                embed_log.add_field(
                                    name = '> Нарушитель:',
                                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                                )
                                embed.add_field(
                                    name=f'> Длительность:',
                                    value=f'```{a}```'
                                )
                                embed.add_field(
                                    name=f'> Причина:',
                                    value=f'**```{reason}```**',
                                    inline=True
                                )
                                embed.set_thumbnail(url=interaction.author.display_avatar)
                                embed.timestamp = datetime.datetime.now()
                                await self.member.send(embed=embed)

                            except disnake.Forbidden:
                                pass

                            await asyncio.sleep(times)
                            cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                            connection.commit()
                            
                        except UnboundLocalError or ValueError:
                            embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                            return
                        
    @disnake.ui.button(label="Снятие выговора", style=ButtonStyle.gray, row=2)
    async def vigovors(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
                
        if cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие выговора', description=f'{interaction.author.mention}, у пользователя нету выговора', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))   
                            
        elif -1 > cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]:
            embed = disnake.Embed(title='Снятие выговора', description=f'{interaction.author.mention}, у пользователя нету выговора', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.send(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
               
        else:
            if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие выговора', description=f'{self.inter.author.mention}, Вы **успешно сняли** выговор с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Выговора', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли выговор', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        
             
            if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
                cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие выговора', description=f'{self.inter.author.mention}, Вы **успешно сняли** выговор с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Выговора', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли выговор', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)         

    @disnake.ui.button(label="Выдать отпуск", style=ButtonStyle.gray, row=2)
    async def rest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Снятие отпуска', description=f'{interaction.author.mention}, у пользователя уже есть отпуск', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))   
        
        embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention} Укажите причину выдачи **отпуску** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление отпуском', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention} Укажите время на сколько выдано **отпуск** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Указывайте в днях: 1d/14d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        

                        cursor.execute("UPDATE users SET otpysk=otpysk +1 WHERE id=?", [self.member.id])
                        connection.commit()

                        embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, Вы **выдали** отпуск {self.member.mention}, причина отпуска **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))                                                         
                        channel = self.client.get_channel(LOG_OTPYSK)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Отпуск', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Получил отпуск:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Исполнитель:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность отпуска:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина отпуска:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed=embed_log)
                        try:
                            embed = disnake.Embed(title='Вы получили отпуск', color=0x2f3136)
                            embed.add_field(
                                name=f'> Исполнитель:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass

                        role = disnake.utils.get(self.member.guild.roles, id=OTPYSK_ROLE) #роль отпуска
                        await self.member.add_roles(role) 
                        
                        await asyncio.sleep(times)
                        await self.member.remove_roles(role) 
                        cursor.execute("UPDATE users SET otpysk=otpysk -1 WHERE id=?", [self.member.id])
                        connection.commit()
                        
                        
                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                        return

    @disnake.ui.button(label="Снять отпуск", style=ButtonStyle.gray, row=2)
    async def unrest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие отпуска', description=f'{interaction.author.mention}, у пользователя нету отпуска', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))   
               
        else:
            if  cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET otpysk=otpysk -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие отпуска', description=f'{self.inter.author.mention}, Вы **успешно сняли** отпуск с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_OTPYSK)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Отпуска', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Кому сняли:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли отпуск', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Сняли отпуск:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        


    @disnake.ui.button(label="Выдать/Снять роль", style=ButtonStyle.blurple, row=3)
    async def creativerole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** Выдать/Снять роль пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Выдать/Снять роль', description=f'{interaction.author.mention} Выберите **взаимодействия ролью** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=CreativeRole(self.client, self.inter, self.member))      

    @disnake.ui.button(label="Добавить в чс состава", style=ButtonStyle.gray, row=3)
    async def staffban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(title='Ошибка Прав', description=f'{interaction.author.mention}, вы **не можете** добавить в чс состава пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        if cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention}, **уже находиться** в чс состава', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention} Укажите причину **добавление в чс состава** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Добавление в чс состава', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
                    return
            cursor.execute("UPDATE users SET staffban=staffban +1 WHERE id=?", [self.member.id])
            channel = self.client.get_channel(LOG_STAFFBAN)                       
            embed_log = disnake.Embed(
                title = 'Логи - Добавление в чс состава', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Получил чс состава:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Причина добавление в чс состава:',
                value = f'・{reason}',
                inline=True
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            embed = disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention}, Вы **добавили** пользователя {self.member.mention}, в чс состава по причине **{reason}**', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))
    
    @disnake.ui.button(label="Убрать из чс состава", style=ButtonStyle.gray, row=3)
    async def staffson(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Убрать из чс состава', description=f'{interaction.author.mention}, пользователь не находиться в чс состава', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))   
               
        else:
            if  cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET staffban=staffban -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Убрать из чс состава', description=f'{self.inter.author.mention}, Вы **успешно убрали** чс состава с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Убрать из чс состава', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Кому сняли:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли чс состава', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Сняли чс состава:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        

    @disnake.ui.button(label="Выдать/Снять роль ветки", style=ButtonStyle.green, row=4)
    async def role(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Выдать/Снять роль ветки', description=f'{self.inter.author.mention}, выберите роль ветки {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        await interaction.response.edit_message(embed=embed, view=Staff(self.inter, self.client, self.member))

    @disnake.ui.button(label="Профиль Состава", style=ButtonStyle.blurple, row=4)
    async def mprofile(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.guild.get_role(ADMIN) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Администратора - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
        
        elif interaction.guild.get_role(CURATOR) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Куратора - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
            
        elif interaction.guild.get_role(MODER) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Модератора - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
        
            
        elif interaction.guild.get_role(HELPER) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Контрола - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
                value=f'```Контрол```',
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
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
            
        elif interaction.guild.get_role(SUPPORT) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Саппорта - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))     
        else:         
            embed = disnake.Embed(title='Профиль Состава', description=f'Пользователь {self.member.mention} не находится на ветке', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackSecurity(self.client, self.inter, self.member))    
            
    @disnake.ui.button(label="История наказаний", style=ButtonStyle.blurple, row=4)
    async def history(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        mutes = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        bans = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        
        rows = cursor.execute("SELECT date, punish_view, reason, given FROM history WHERE id = ?", [self.member.id])

        embeds = []
        if mutes+bans+warn == 0:
            embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Пользователь {self.member.mention}, не получал нарушений!', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embeds.append(embed)

        else:
            for i, row in enumerate(rows):
                if i % 5 == 0:
                    embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Мутов: **{mutes}** Банов: **{bans}** Предов: **{warn}**', color=0x2f3136)
                    embed.set_thumbnail(url=self.member.display_avatar)
                    embeds.append(embed)

                embed.add_field(
                    name=f'** **',
                    value=f'`{i+1}.` [<t:{row[0]}:f>] **{row[1]}** *Причина:* {row[2]}\nМодератор: <@{row[3]}>',
                    inline=False
                )

        await interaction.response.edit_message(embed=embeds[0], view=Menu(self.client, self.inter, self.member, embeds))

    @disnake.ui.button(label="Отмена", style=ButtonStyle.red, row=4)
    async def delete(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()



class Curator(disnake.ui.View):
    def __init__(self, client, inter, member):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

    async def interaction_check(self, interaction):
        if interaction.user == self.inter.author:
            return True
        else:
            await interaction.response.edit_message()

    @disnake.ui.button(label="Забанить", style=ButtonStyle.gray)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)                
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, У пользователя уже есть бан', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))  
        
        elif self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            
        else:
            embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention} Укажите причину **бана** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

            def check(m: disnake.Message):
                return m.author == interaction.author and m.channel.id == interaction.channel.id 
            try:
                msg = await self.client.wait_for('message', check=check, timeout=30)
                await msg.delete()
                
            except asyncio.TimeoutError: 
                embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
            
            else:
                reason = msg.content

                if len(msg.content) > 35:
                        embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        return
                
                else:
                    embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention} Укажите время **бана** пользователя {self.member.mention}', color=0x2f3136)
                    embed.set_footer(text='Пример: 10s/10m/10h/10d')
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=None)

                    def check(m: disnake.Message):
                        return m.author == interaction.author and m.channel.id == interaction.channel.id 
                    try:
                        msg = await self.client.wait_for('message', check=check, timeout = 30)
                        await msg.delete()
                        
                    except asyncio.TimeoutError: 
                        embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        return
                    
                    else:
                        try:
                            if 's' in msg.content:
                                i = msg.content.replace("s", "")
                                times = int(i)

                                a = msg.content.replace("s", " секунд")

                            if 'm' in msg.content:
                                i = msg.content.replace("m", "")
                                times = int(i)*60

                                a = msg.content.replace("m", " минут")
                                
                            if 'h' in msg.content:
                                i = msg.content.replace("h", "")
                                times = int(i)*3600

                                a = msg.content.replace("h", " часов")

                            if 'd' in msg.content:
                                i = msg.content.replace("d", "")
                                times = int(i)*86400

                                a = msg.content.replace("d", " дней")

                            
                            cursor.execute("UPDATE users SET bans=bans+1 WHERE id=?", [self.member.id])
                            cursor.execute("UPDATE users SET bans=bans +1 WHERE id=?", [interaction.author.id])
                            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['ban', self.member.id])
                            cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Локальный бан', reason, interaction.author.id])
                            connection.commit()
    
                            
                            embed = disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, Вы **забанили** {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))

                            channel = self.client.get_channel(LOG_NAKAZANIA)                       
                            embed_log = disnake.Embed(
                                title = 'Логи - Бан', color=0x2f3136
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Выдал:',
                                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Длительность:',
                                value = f'・{a}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Тип:',
                                value = f'・Локальный бан',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Причина:',
                                value = f'・{reason}',
                                inline=True
                            )
                            embed_log.set_thumbnail(url=interaction.author.display_avatar)
                            embed_log.timestamp = datetime.datetime.now()
                            await channel.send(embed = embed_log)
                            try:
                                embed = disnake.Embed(title='Вам был выдан бан на сервере tokame', color=0x2f3136)
                                
                                embed.add_field(
                                    name=f'> Выдал:',
                                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                                )
                                embed.add_field(
                                    name=f'> Длительность:',
                                    value=f'```{a}```'
                                )
                                embed.add_field(
                                    name=f'> Тип:',
                                    value=f'・Локальный бан'
                                )
                                embed.add_field(
                                    name=f'> Причина:',
                                    value=f'**```{reason}```**',
                                    inline=True
                                )

                                embed.set_thumbnail(url=interaction.author.display_avatar)
                                embed.timestamp = datetime.datetime.now()
                                await self.member.send(embed=embed)

                            except disnake.Forbidden:
                                pass

                            await self.member.edit(roles=[])
                            role = disnake.utils.get(self.member.guild.roles, id=BAN_ROLE)
                            await self.member.add_roles(role)
                            await asyncio.sleep(times)
                            await self.member.remove_roles(role)
                            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['unban', self.member.id])
                            connection.commit()

                        except UnboundLocalError or ValueError:
                            embed=disnake.Embed(title='Управление пользователем — Бан', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                            return
                        
    @disnake.ui.button(label="Разбанить", style=ButtonStyle.gray)
    async def unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
           
        elif role in self.member.roles:    
            cursor.execute("UPDATE users SET local_ban=? WHERE id=?", ['unban', self.member.id])
            connection.commit()

            local_ban = disnake.utils.get(self.member.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(local_ban)

            embed1 = disnake.Embed(title='Управление пользователем — Разбан', description=f'{interaction.author.mention}, Вы успешно **сняли** бан у {self.member.mention}!', color=0x2f3136)
            embed1.timestamp = datetime.datetime.now()
            embed1.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed1, view=BackCurator(self.client, self.inter, self.member))
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Разбанить', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли бан', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)                            
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** бана ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        
    @disnake.ui.button(label="Выдать мут", style=ButtonStyle.gray)
    async def mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** замутить пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        else:
            embed = disnake.Embed(title='Управление пользователем — Мут', description=f'{interaction.author.mention} Выберите вид **мута** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Mute(self.client, self.inter, self.member))


    @disnake.ui.button(label="Снять мут", style=ButtonStyle.gray)
    async def unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(self.inter.guild.roles, id=VOICE_MUTE)
        chats = disnake.utils.get(self.inter.guild.roles, id=TEXT_MUTE)
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** снять бан пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
           
        elif role in self.member.roles:    
            embed = disnake.Embed(title='Управление пользователем — Размут', description=f'{interaction.author.mention}, Выберите **вид мута** для размута пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Razmut(self.client, self.inter, self.member))
            
        elif chats in self.member.roles:    
            embed = disnake.Embed(title='Управление пользователем — Размут', description=f'{interaction.author.mention}, Выберите **вид мута** для размута пользователя {self.member.mention}!', color=0x2f3136)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=Razmut(self.client, self.inter, self.member))
        
        else:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention} **не имеет** мута ', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))

   
    @disnake.ui.button(label="Замечание", style=ButtonStyle.gray)
    async def genders(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать замечание пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        role = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
        if role in self.member.roles:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, у пользователя {self.member.mention} **уже есть** замечание!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention} Укажите причину **замечание** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление замечание', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                    return
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.add_roles(zames)
            embed = disnake.Embed(title='Управление замечание', description=f'{interaction.author.mention}, Вы **выдали** замечание {self.member.mention}, по причине **{reason}**', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            
            await asyncio.sleep(3600)
            zames = disnake.utils.get(self.inter.guild.roles, id=ROLE_ZAMEC)
            await self.member.remove_roles(zames)    

    @disnake.ui.button(label="Выдать/Снять роль", style=ButtonStyle.blurple, row=3)
    async def creativerole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** Выдать/Снять роль пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Выдать/Снять роль', description=f'{interaction.author.mention} Выберите **взаимодействия ролью** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=CreativeRole(self.client, self.inter, self.member))    
        
    @disnake.ui.button(label="Верифицировать", style=ButtonStyle.gray)
    async def verifygender(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** верифицировать пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Верифицировать', description=f'{interaction.author.mention} Выберите **гендерную роль** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=VerifySupport(self.client, self.inter, self.member))
                    
    @disnake.ui.button(label="Сменить пол", style=ButtonStyle.gray)
    async def genderole(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** изменить пол пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Управление пользователем — Cменить пол', description=f'{interaction.author.mention} Выберите **пол** для пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=Gender(self.client, self.inter, self.member))                    
                    
    @disnake.ui.button(label="Выдать предупреждение", style=ButtonStyle.gray)
    async def warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать предупреждение пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
       
        if  cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -2 WHERE id=?", [self.member.id])
            connection.commit()
            await self.member.edit(roles=[])
            ban_role = disnake.utils.get(self.inter.guild.roles, id=BAN_ROLE)
            await self.member.remove_roles(ban_role)
            embed = disnake.Embed(title='Выдача Предупреждение', description=f'{self.inter.author.mention}, Пользователь получил **3** предупреждений и получил бан.', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
        
        else:
            embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите причину **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление предупреждением', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention} Укажите время **предупреждения** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Пример: 10s/10m/10h/10d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [interaction.author.id])
                        cursor.execute("UPDATE users SET warn=warn +1 WHERE id=?", [self.member.id])
                        cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", [self.member.id, int(time.time()), 'Предупреждение', reason, interaction.author.id])
                        connection.commit()

                        embed = disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Вы **выдали** предупреждение {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        channel = self.client.get_channel(LOG_NAKAZANIA)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Предупреждение', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Нарушитель:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Исполнитель:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed = embed_log)
                        try:
                            embed = disnake.Embed(title='Вам выдали предупреждение', color=0x2f3136)
                            embed.add_field(
                                name=f'> Исполнитель:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass
                        
                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление предупреждением', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        return
                        

    @disnake.ui.button(label="Снять предупреждение", style=ButtonStyle.gray, row=1)
    async def unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{interaction.author.mention}, у пользователя нету предупреждение', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))  
                                
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id])
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)        
            
        if cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET warn=warn -1 WHERE id=?", [self.member.id]) 
            connection.commit()
            embed = disnake.Embed(title='Снятие предупреждение', description=f'{self.inter.author.mention}, Вы **успешно сняли** предупреждение с {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Снятие Предупреждение', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed = embed_log)
            embed = disnake.Embed(title='Вам сняли предупреждение', color=0x2f3136)
            embed.add_field(
                name=f'> Исполнитель:',
                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await self.member.send(embed=embed)        
            
    @disnake.ui.button(label="Выдать выговор", style=ButtonStyle.gray, row=2)
    async def vigovor(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(
                title='Ошибка Прав',
                description=f'{interaction.author.mention}, вы **не можете** выдать выговор пользователю **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        
        if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
            cursor.execute("UPDATE users SET vigovor=vigovor -2 WHERE id=?", [self.member.id])
            connection.commit()
            curator = disnake.utils.get(self.inter.guild.roles, id=CURATOR)
            moderator = disnake.utils.get(self.inter.guild.roles, id=MODER)
            support = disnake.utils.get(self.inter.guild.roles, id=SUPPORT)
            broadcaster = disnake.utils.get(self.inter.guild.roles, id=BROADCASTER)
            eventer = disnake.utils.get(self.inter.guild.roles, id=EVENTER)
            creative = disnake.utils.get(self.inter.guild.roles, id=CREATIVE)
            closemaker = disnake.utils.get(self.inter.guild.roles, id=CLOSEMAKER)
            staff = disnake.utils.get(self.inter.guild.roles, id=STAFF_ROLE)
            await self.member.remove_roles(CURATOR)
            await self.member.remove_roles(moderator)
            await self.member.remove_roles(support)
            await self.member.remove_roles(broadcaster)
            await self.member.remove_roles(eventer)
            await self.member.remove_roles(staff)
            await self.member.remove_roles(closemaker)
            await self.member.remove_roles(creative)
            
            embed = disnake.Embed(title='Выдача выговора', description=f'{self.inter.author.mention}, Вы **выдали 3 выговор** и пользователь {self.member.mention} был снят с ролей состава.', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
            channel = self.client.get_channel(LOG_NAKAZANIA)                       
            embed_log = disnake.Embed(
                title = 'Логи - Выговор/Снятие', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Нарушитель:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            try:
                embed = disnake.Embed(title='Вас сняли у вас 3 выговора', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                )
                embed.add_field(
                    name=f'> Причина:',
                    value=f'**```{reason}```**',
                    inline=True
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)
            
            except disnake.Forbidden:
                pass

                    
            except UnboundLocalError or ValueError:
                embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
        else:
            embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention} Укажите причину **выговора** пользователя {self.member.mention}', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=None)

            def check(m: disnake.Message):
                return m.author == interaction.author and m.channel.id == interaction.channel.id 
            try:
                msg = await self.client.wait_for('message', check=check, timeout=30)
                await msg.delete()
                
            except asyncio.TimeoutError: 
                embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                return
            
            else:
                reason = msg.content

                if len(msg.content) > 35:
                        embed = disnake.Embed(title='Управление выговором', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        return
                
                else:
                    embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention} Укажите время **выговора** пользователя {self.member.mention}', color=0x2f3136)
                    embed.set_footer(text='Пример: 10s/10m/10h/10d')
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=None)

                    def check(m: disnake.Message):
                        return m.author == interaction.author and m.channel.id == interaction.channel.id 
                    try:
                        msg = await self.client.wait_for('message', check=check, timeout = 30)
                        await msg.delete()
                        
                    except asyncio.TimeoutError: 
                        embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        return
                    
                    else:
                        try:
                            if 's' in msg.content:
                                i = msg.content.replace("s", "")
                                times = int(i)

                                a = msg.content.replace("s", " секунд")

                            if 'm' in msg.content:
                                i = msg.content.replace("m", "")
                                times = int(i)*60

                                a = msg.content.replace("m", " минут")
                                
                            if 'h' in msg.content:
                                i = msg.content.replace("h", "")
                                times = int(i)*3600

                                a = msg.content.replace("h", " часов")

                            if 'd' in msg.content:
                                i = msg.content.replace("d", "")
                                times = int(i)*86400

                                a = msg.content.replace("d", " дней")

                            

                            cursor.execute("UPDATE users SET vigovor=vigovor +1 WHERE id=?", [self.member.id])
                            connection.commit()
    
                            embed = disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Вы **выдали** выговор {self.member.mention}, по причине **{reason}** на **{a}**', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))                                                         
                            channel = self.client.get_channel(LOG_NAKAZANIA)                       
                            embed_log = disnake.Embed(
                                title = 'Логи - Выговор', color=0x2f3136
                            )
                            embed_log.add_field(
                                name = '> Нарушитель:',
                                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Исполнитель:',
                                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Длительность:',
                                value = f'・{a}',
                                inline=False
                            )
                            embed_log.add_field(
                                name = '> Причина:',
                                value = f'・{reason}',
                                inline=True
                            )
                            embed_log.set_thumbnail(url=interaction.author.display_avatar)
                            embed_log.timestamp = datetime.datetime.now()
                            await channel.send(embed=embed_log)
                            try:
                                embed = disnake.Embed(title='Вам выдали выговор', color=0x2f3136)
                                embed.add_field(
                                    name=f'> Исполнитель:',
                                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                                )
                                embed_log.add_field(
                                    name = '> Нарушитель:',
                                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}'
                                )
                                embed.add_field(
                                    name=f'> Длительность:',
                                    value=f'```{a}```'
                                )
                                embed.add_field(
                                    name=f'> Причина:',
                                    value=f'**```{reason}```**',
                                    inline=True
                                )
                                embed.set_thumbnail(url=interaction.author.display_avatar)
                                embed.timestamp = datetime.datetime.now()
                                await self.member.send(embed=embed)

                            except disnake.Forbidden:
                                pass

                            await asyncio.sleep(times)
                            cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                            connection.commit()
                            
                        except UnboundLocalError or ValueError:
                            embed=disnake.Embed(title='Управление выговором', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                            return
                        
    @disnake.ui.button(label="Снятие выговора", style=ButtonStyle.gray, row=2)
    async def vigovors(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
                
        if cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие выговора', description=f'{interaction.author.mention}, у пользователя нету выговора', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))   
                            
        elif -1 > cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]:
            embed = disnake.Embed(title='Снятие выговора', description=f'{interaction.author.mention}, у пользователя нету выговора', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.send(embed=embed, view=BackCurator(self.client, self.inter, self.member))
               
        else:
            if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие выговора', description=f'{self.inter.author.mention}, Вы **успешно сняли** выговор с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Выговора', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли выговор', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        
             
            if  cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 2:
                cursor.execute("UPDATE users SET vigovor=vigovor -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие выговора', description=f'{self.inter.author.mention}, Вы **успешно сняли** выговор с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Выговора', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли выговор', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Нарушитель:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)         

    @disnake.ui.button(label="Выдать отпуск", style=ButtonStyle.gray, row=2)
    async def rest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(title='Снятие отпуска', description=f'{interaction.author.mention}, у пользователя уже есть отпуск', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))   
        
        embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention} Укажите причину выдачи **отпуску** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Управление отпуском', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                    return
            
            else:
                embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention} Укажите время на сколько выдано **отпуск** пользователя {self.member.mention}', color=0x2f3136)
                embed.set_footer(text='Указывайте в днях: 1d/14d')
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.edit_original_message(embed=embed, view=None)

                def check(m: disnake.Message):
                    return m.author == interaction.author and m.channel.id == interaction.channel.id 
                try:
                    msg = await self.client.wait_for('message', check=check, timeout = 30)
                    await msg.delete()
                    
                except asyncio.TimeoutError: 
                    embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                    return
                
                else:
                    try:
                        if 's' in msg.content:
                            i = msg.content.replace("s", "")
                            times = int(i)

                            a = msg.content.replace("s", " секунд")

                        if 'm' in msg.content:
                            i = msg.content.replace("m", "")
                            times = int(i)*60

                            a = msg.content.replace("m", " минут")
                            
                        if 'h' in msg.content:
                            i = msg.content.replace("h", "")
                            times = int(i)*3600

                            a = msg.content.replace("h", " часов")

                        if 'd' in msg.content:
                            i = msg.content.replace("d", "")
                            times = int(i)*86400

                            a = msg.content.replace("d", " дней")

                        

                        cursor.execute("UPDATE users SET otpysk=otpysk +1 WHERE id=?", [self.member.id])
                        connection.commit()

                        embed = disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, Вы **выдали** отпуск {self.member.mention}, причина отпуска **{reason}** на **{a}**', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))                                                         
                        channel = self.client.get_channel(LOG_OTPYSK)                       
                        embed_log = disnake.Embed(
                            title = 'Логи - Отпуск', color=0x2f3136
                        )
                        embed_log.add_field(
                            name = '> Получил отпуск:',
                            value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Исполнитель:',
                            value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Длительность отпуска:',
                            value = f'・{a}',
                            inline=False
                        )
                        embed_log.add_field(
                            name = '> Причина отпуска:',
                            value = f'・{reason}',
                            inline=True
                        )
                        embed_log.set_thumbnail(url=interaction.author.display_avatar)
                        embed_log.timestamp = datetime.datetime.now()
                        await channel.send(embed=embed_log)
                        try:
                            embed = disnake.Embed(title='Вы получили отпуск', color=0x2f3136)
                            embed.add_field(
                                name=f'> Исполнитель:',
                                value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}'
                            )
                            embed.add_field(
                                name=f'> Длительность:',
                                value=f'```{a}```'
                            )
                            embed.add_field(
                                name=f'> Причина:',
                                value=f'**```{reason}```**',
                                inline=True
                            )
                            embed.set_thumbnail(url=interaction.author.display_avatar)
                            embed.timestamp = datetime.datetime.now()
                            await self.member.send(embed=embed)

                        except disnake.Forbidden:
                            pass

                        role = disnake.utils.get(self.member.guild.roles, id=OTPYSK_ROLE) #роль отпуска
                        await self.member.add_roles(role) 
                        
                        await asyncio.sleep(times)
                        await self.member.remove_roles(role) 
                        cursor.execute("UPDATE users SET otpysk=otpysk -1 WHERE id=?", [self.member.id])
                        connection.commit()
                        
                        
                    except UnboundLocalError or ValueError:
                        embed=disnake.Embed(title='Управление отпуском', description=f'{interaction.author.mention}, Упс... где то произошла ошибка', color=0x2f3136)
                        embed.set_thumbnail(url=interaction.author.display_avatar)
                        embed.timestamp = datetime.datetime.now()
                        await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                        return

    @disnake.ui.button(label="Снять отпуск", style=ButtonStyle.gray, row=2)
    async def unrest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Снятие отпуска', description=f'{interaction.author.mention}, у пользователя нету отпуска', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))   
               
        else:
            if  cursor.execute("SELECT otpysk FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET otpysk=otpysk -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Снятие отпуска', description=f'{self.inter.author.mention}, Вы **успешно сняли** отпуск с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Снятие Отпуска', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Кому сняли:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли отпуск', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Сняли отпуск:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        

    @disnake.ui.button(label="Добавить в чс состава", style=ButtonStyle.gray, row=3)
    async def staffban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.member.top_role.position >= interaction.author.top_role.position:
            embed = disnake.Embed(title='Ошибка Прав', description=f'{interaction.author.mention}, вы **не можете** добавить в чс состава пользователя **выше вас** по роли!', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        if cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
            embed = disnake.Embed(
                title='Ошибка',
                description=f'{interaction.author.mention}, пользователь {self.member.mention}, **уже находиться** в чс состава', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
        embed = disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention} Укажите причину **добавление в чс состава** пользователя {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed, view=None)

        def check(m: disnake.Message):
            return m.author == interaction.author and m.channel.id == interaction.channel.id 
        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
            await msg.delete()
            
        except asyncio.TimeoutError: 
            embed=disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention}, время на ответ вышло', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
            return
        
        else:
            reason = msg.content

            if len(msg.content) > 35:
                    embed = disnake.Embed(title='Добавление в чс состава', description=f'{self.member.mention}, **причина** не может привышать больше **35** символов', color=0x2f3136)
                    embed.set_thumbnail(url=interaction.author.display_avatar)
                    embed.timestamp = datetime.datetime.now()
                    await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
                    return
            cursor.execute("UPDATE users SET staffban=staffban +1 WHERE id=?", [self.member.id])
            channel = self.client.get_channel(LOG_STAFFBAN)                       
            embed_log = disnake.Embed(
                title = 'Логи - Добавление в чс состава', color=0x2f3136
            )
            embed_log.add_field(
                name = '> Получил чс состава:',
                value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Исполнитель:',
                value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                inline=False
            )
            embed_log.add_field(
                name = '> Причина добавление в чс состава:',
                value = f'・{reason}',
                inline=True
            )
            embed_log.set_thumbnail(url=interaction.author.display_avatar)
            embed_log.timestamp = datetime.datetime.now()
            await channel.send(embed=embed_log)
            embed = disnake.Embed(title='Добавление в чс состава', description=f'{interaction.author.mention}, Вы **добавили** пользователя {self.member.mention}, в чс состава по причине **{reason}**', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.edit_original_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))
    
    @disnake.ui.button(label="Убрать из чс состава", style=ButtonStyle.gray, row=3)
    async def staffson(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 0:
            embed = disnake.Embed(title='Убрать из чс состава', description=f'{interaction.author.mention}, пользователь не находиться в чс состава', color=disnake.Color.red())
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))   
               
        else:
            if  cursor.execute("SELECT staffban FROM users WHERE id = ?", [self.member.id]).fetchone()[0] == 1:
                cursor.execute("UPDATE users SET staffban=staffban -1 WHERE id=?", [self.member.id])
                connection.commit()
                embed = disnake.Embed(title='Убрать из чс состава', description=f'{self.inter.author.mention}, Вы **успешно убрали** чс состава с {self.member.mention}', color=0x2f3136)
                embed.set_thumbnail(url=self.member.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
                channel = self.client.get_channel(LOG_NAKAZANIA)                       
                embed_log = disnake.Embed(
                    title = 'Логи - Убрать из чс состава', color=0x2f3136
                )
                embed_log.add_field(
                    name = '> Кому сняли:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Исполнитель:',
                    value = f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.set_thumbnail(url=interaction.author.display_avatar)
                embed_log.timestamp = datetime.datetime.now()
                await channel.send(embed = embed_log)
                embed = disnake.Embed(title='Вам сняли чс состава', color=0x2f3136)
                embed.add_field(
                    name=f'> Исполнитель:',
                    value=f'・{interaction.author.mention}\n・{interaction.author}\n・{interaction.author.id}',
                    inline=False
                )
                embed_log.add_field(
                    name = '> Сняли чс состава:',
                    value = f'・{self.member.mention}\n・{self.member}\n・{self.member.id}',
                    inline=False
                )
                embed.set_thumbnail(url=interaction.author.display_avatar)
                embed.timestamp = datetime.datetime.now()
                await self.member.send(embed=embed)        

    @disnake.ui.button(label="Выдать/Снять роль ветки", style=ButtonStyle.green, row=4)
    async def role(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(title='Выдать/Снять роль ветки', description=f'{self.inter.author.mention}, выберите роль ветки {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=interaction.author.display_avatar)
        await interaction.response.edit_message(embed=embed, view=Staff(self.inter, self.client, self.member))


    @disnake.ui.button(label="Профиль Состава", style=ButtonStyle.blurple, row=4)
    async def mprofile(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.guild.get_role(ADMIN) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Администратора - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
        
        elif interaction.guild.get_role(CURATOR) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Куратора - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
            
        elif interaction.guild.get_role(MODER) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Модератора - {self.member}**',color=0x2f3136)
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
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
        
            
        elif interaction.guild.get_role(HELPER) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Контрола - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
                value=f'```Контрол```',
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
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))      
            
        elif interaction.guild.get_role(SUPPORT) in self.member.roles:
            mute = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            ban = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            veref = cursor.execute("SELECT verify FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            vigovors = cursor.execute("SELECT vigovor FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            author_online = cursor.execute("SELECT voice_time FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
            connection.commit

            embed = disnake.Embed(description=f'**Профиль Саппорта - {self.member}**',color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            
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
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))         
        else:         
            embed = disnake.Embed(title='Профиль Состава', description=f'Пользователь {self.member.mention} не находится на ветке, или же у него нет стафф профиля ветки', color=0x2f3136)
            embed.set_thumbnail(url=interaction.author.display_avatar)
            await interaction.response.edit_message(embed=embed, view=BackCurator(self.client, self.inter, self.member))    
 
    @disnake.ui.button(label="История наказаний", style=ButtonStyle.blurple, row=4)
    async def history(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        warn = cursor.execute("SELECT warn FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        mutes = cursor.execute("SELECT mutes FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        bans = cursor.execute("SELECT bans FROM users WHERE id = ?", [self.member.id]).fetchone()[0]
        
        rows = cursor.execute("SELECT date, punish_view, reason, given FROM history WHERE id = ?", [self.member.id])

        embeds = []
        if mutes+bans+warn == 0:
            embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Пользователь {self.member.mention}, не получал нарушений!', color=0x2f3136)
            embed.set_thumbnail(url=self.member.display_avatar)
            embeds.append(embed)

        else:
            for i, row in enumerate(rows):
                if i % 5 == 0:
                    embed = disnake.Embed(title=f'История нарушений — {self.member}', description=f'Мутов: **{mutes}** Банов: **{bans}** Предов: **{warn}**', color=0x2f3136)
                    embed.set_thumbnail(url=self.member.display_avatar)
                    embeds.append(embed)

                embed.add_field(
                    name=f'** **',
                    value=f'`{i+1}.` [<t:{row[0]}:f>] **{row[1]}** *Причина:* {row[2]}\nModeratorатор: <@{row[3]}>',
                    inline=False
                )

        await interaction.response.edit_message(embed=embeds[0], view=Menu(self.client, self.inter, self.member, embeds))    
    
    @disnake.ui.button(label="Отмена", style=ButtonStyle.red, row=4)
    async def delete(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message()
        await interaction.delete_original_message()


class Menu(disnake.ui.View):
    def __init__(self, client, inter, member, embeds: List[disnake.Embed]):
        super().__init__(timeout=None)
        self.client = client
        self.inter = inter
        self.member = member

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

    @disnake.ui.button(emoji="◀", style=disnake.ButtonStyle.gray)
    async def prev_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count -= 1
        embed = self.embeds[self.embed_count]

        self.next_page.disabled = False

        if self.embed_count == 0:
            self.prev_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    @disnake.ui.button(label="Назад", style=ButtonStyle.blurple)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.guild.get_role(ADMIN) in interaction.author.roles: #роль admin
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Admin(self.client, self.inter, self.member))
            return
        
        elif interaction.guild.get_role(CURATOR) in interaction.author.roles: #роль куратора
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Curator(self.client, self.inter, self.member))       
            return
        
        elif interaction.guild.get_role(HELPER) in interaction.author.roles: #роль control
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Control(self.client, self.inter, self.member))
            return
        
        elif interaction.guild.get_role(MODER) in interaction.author.roles: #роль modera
            embed = disnake.Embed(title='Управление пользователем', description=f'{interaction.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}!', color=0x2f3136)
            embed.set_thumbnail(url=self.inter.author.display_avatar)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=Moderations(self.client, self.inter, self.member))
            return

    @disnake.ui.button(emoji="▶", style=disnake.ButtonStyle.gray)
    async def next_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count += 1
        embed = self.embeds[self.embed_count]

        self.prev_page.disabled = False
        
        if self.embed_count == len(self.embeds) - 1:
            self.next_page.disabled = True

        await interaction.response.edit_message(embed=embed, view=self)




class Action(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.inter = iter
            
    @commands.slash_command(name='action', description='Установить наказание пользователю')
    @commands.has_any_role(ADMIN, CURATOR, MODER, HELPER, SUPPORT, CREATIVE, SECURITY)
    async def action(self, inter, member: disnake.Member = commands.Param(name="пользовaтель")):
        self.member = member
        embed = disnake.Embed(title='Управление пользователем', description=f'{inter.author.mention} **Выберите** операцию для **взаимодействия** с {self.member.mention}', color=0x2f3136)
        embed.set_thumbnail(url=inter.author.display_avatar)
        embed.timestamp = datetime.datetime.now()
        if member == inter.author:
            embed = disnake.Embed(
                title='Управление пользователем', description=f'{inter.author.mention}, **Вы** не можете **взаимодействовать** с **самим собой**', color=0x2f3136)
            embed.set_thumbnail(url=inter.author.display_avatar)
            await inter.send(embed=embed, ephemeral=True)

        elif  inter.guild.get_role(ADMIN) in inter.author.roles: #ADMIN
            await inter.send(embed=embed, view=Admin(self.client, inter, member))
            
        elif inter.guild.get_role(SECURITY) in inter.author.roles: #SECURITY
            await inter.send(embed=embed, view=Security(self.client, inter, member))
                
        elif inter.guild.get_role(CURATOR) in inter.author.roles: # CURATOR
            await inter.send(embed=embed, view=Curator(self.client, inter, member))
        
        elif inter.guild.get_role(MODER) in inter.author.roles: #MODER
            await inter.send(embed=embed, view=Moderations(self.client, inter, member))    
        
        elif inter.guild.get_role(HELPER) in inter.author.roles: #CONTROL
            await inter.send(embed=embed, view=Control(self.client, inter, member))
                
        elif inter.guild.get_role(SUPPORT) in inter.author.roles: #SUPPORT
            await inter.send(embed=embed, view=Support(self.client, inter, member))    
        
        elif inter.guild.get_role(CREATIVE) in inter.author.roles: #Creative
            await inter.send(embed=embed, view=Creative(self.client, inter, member))
    

    
def setup(client):
    client.add_cog(Action(client))