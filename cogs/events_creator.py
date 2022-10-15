import nextcord
from nextcord.ext import commands
from nextcord import  SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ui import Button, View
import datetime, time


class eventcreator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guilds = [guild.id for guild in bot.guilds]
        # set before deploy
        self.event_channel_id = 0 
        self.event_role_id = 0

    
    @nextcord.slash_command()
    async def create_event(self, interaction: nextcord.Interaction, event_name: str, event_description: str, event_cash: int, date:str, time:str):
        event_channel = interaction.guild.get_channel(self.event_channel_id)
        event_role = interaction.guild.get_role(self.event_role_id)
        if event_role != None and event_channel != None:
            E = nextcord.Embed(
                title=f"{event_name} ивент",
                description=f"{event_description}\nДеняк за эвент: {event_cash} $\nвремя проведения: {date} {time}"
            )

            await interaction.response.send_message(contern = event_role.mention ,embed=E)
        else:
            await interaction.response.send_message('что то пошло не так')

    

def setup(bot):
    bot.add_cog(eventcreator(bot))