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

    
    @nextcord.slash_command()
    async def create_event(self, interaction: nextcord.Interaction, event_name: str, event_description: str):
        # await interaction.guild.create_scheduled_event(
        #     name=event_name, 
        #     description=event_description,
        #     end_time= datetime.datetime.now(),
        #     start_time=datetime.datetime.now(),
        #     entity_type= nextcord.ScheduledEventEntityType.external
        #     )
        return

    @nextcord.slash_command()
    async def set_event_pic(self, interaction: nextcord.Interaction, event_name: str, event_description: str):
        return
    

def setup(bot):
    bot.add_cog(eventcreator(bot))