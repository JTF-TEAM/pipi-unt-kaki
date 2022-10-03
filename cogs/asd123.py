import nextcord
from nextcord.ext import commands
from nextcord import  SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ui import Button, View
import datetime, time
import json
import random


class asd123(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guilds = [guild.id for guild in bot.guilds]

    
    @nextcord.slash_command()
    async def asd(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f'owner is {interaction.guild.owner.mention}', ephemeral=1)
        return

    @nextcord.slash_command()
    async def asd123(self, interaction: nextcord.Interaction):
        await interaction.response.send_message('HI, MARS~!', ephemeral=1)
        return
    
    @nextcord.slash_command()
    async def kabooki(self, interaction: nextcord.Interaction, question: str):
        await interaction.response.send_message(
            content=f"{question} is {random.choice((' true', ' false'))}",
            ephemeral=1
        )

def setup(bot):
    bot.add_cog(asd123(bot))