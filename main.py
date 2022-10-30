#!/usr/bin/env python3
import os
from typing import Collection
import nextcord
from nextcord.ext import application_checks, commands
#from nextcord_logging import Discord_Handler

intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


####################### geting cock ##################################
guilds = [786255515570667541]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=nextcord.Activity(name=f'-', type=nextcord.ActivityType.listening))


@bot.slash_command(guild_ids=guilds)
async def pukpuk(interaction: nextcord.Interaction, модуль: str):
    await interaction.send(f'😎 BAVOVNA ', ephemeral=True)



@bot.slash_command(guild_ids=guilds)
@application_checks.is_owner()
async def load(interaction: nextcord.Interaction, модуль: str):
    bot.load_extension(f"cogs.{модуль}")
    await interaction.send(f'✅ Загружен модуль {модуль}', ephemeral=True)


@bot.slash_command(guild_ids=guilds)
@application_checks.is_owner()
async def reload(interaction: nextcord.Interaction, модуль: str):
    bot.reload_extension(f"cogs.{модуль}")
    await interaction.send(f'✅ Рестарт модуль {модуль} перезагружен', ephemeral=True)


@bot.slash_command(guild_ids=guilds)
@application_checks.is_owner()
async def unload(interaction: nextcord.Interaction, модуль: str):
    bot.unload_extension(f"cogs.{модуль}")
    await interaction.send(f'✅ Модуль **{модуль}** выгружен', ephemeral=True)

TOKEN = '' # ssilka na tokuen
bot.run(TOKEN)