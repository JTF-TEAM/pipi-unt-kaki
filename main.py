#!/usr/bin/env python3
import os
from typing import Collection
import nextcord
from configs import pymonger
from configs import mainconf
from nextcord.ext import application_checks, commands
#from nextcord_logging import Discord_Handler

TOKEN = mainconf.poken
intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


####################### geting cock ##################################
batadase = pymonger.Monga()
guilds = [guild.id for guild in bot.guilds]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=nextcord.Activity(name=f'test', type=nextcord.ActivityType.listening))
    # log_all_members_test(bot)


@bot.event
async def on_message(message):
    batadase.increase_int_value(message.author.id, 'message count')

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


bot.run(TOKEN)