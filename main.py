
import asyncio
import os
import logging

import nextcord
from configs import mainconf
from nextcord.ext import application_checks, commands
#from nextcord_logging import Discord_Handler


TOKEN = mainconf.poken
intents = nextcord.Intents.all()
#?
# intents.members = True
# intents.message_content = True

bot = commands.Bot(intents=intents)



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=nextcord.Activity(name=f'test', type=nextcord.ActivityType.listening))


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


# @bot.event
# async def on_application_command_error(interaction: nextcord.Interaction, error):
#     if isinstance(error, ApplicationError):
#         await interaction.response.send_message(f"{error}", ephemeral=True)
#         return

# # @bot.slash_command(guild_ids=guilds)
# # @application_checks.is_owner()
# # async def load(interaction: nextcord.Interaction, модуль: str):
# #     bot.load_extension(f"cogs.{модуль}")
# #     await interaction.send(f'✅ Загружен модуль {модуль}', ephemeral=True)


# # @bot.slash_command(guild_ids=guilds)
# # @application_checks.is_owner()
# # async def reload(interaction: nextcord.Interaction, модуль: str):
# #     bot.reload_extension(f"cogs.{модуль}")
# #     await interaction.send(f'✅ Рестарт модуль {модуль} перезагружен', ephemeral=True)


# # @bot.slash_command(guild_ids=guilds)
# # @application_checks.is_owner()
# # async def unload(interaction: nextcord.Interaction, модуль: str):
# #     bot.unload_extension(f"cogs.{модуль}")
# #     await interaction.send(f'✅ Модуль **{модуль}** выгружен', ephemeral=True)


bot.run(TOKEN)