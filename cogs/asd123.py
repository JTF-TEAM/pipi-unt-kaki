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

    @nextcord.slash_command()
    async def meth(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(
            embed=nextcord.Embed(
                title='O_O'
            ).set_image(
                url="https://i.ytimg.com/vi/Z3llc7h-gdw/maxresdefault.jpg"
            ),
            ephemeral=1
        )

    @nextcord.slash_command(name='am_i_gay?',description="bot say truth about your sexuality")
    async def yes(self, interaction: nextcord.Interaction):
        await interaction.response.send_message('yes')
    

    
    @nextcord.slash_command(name='sts',description="olko dlya stasov")
    async def stas(self, interaction: nextcord.Interaction):
        await interaction.response.send_message('ti stas')

def setup(bot):
    bot.add_cog(asd123(bot))