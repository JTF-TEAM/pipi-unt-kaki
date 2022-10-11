import collections
import nextcord
from nextcord.ext import commands
import pymongo
import random
collector = pymongo.MongoClient('')

class CCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(name='clan_create', description='создание клана на сервербе')
    async def create_clan(self, interaction: nextcord.Interaction, clan_name: str):
        await interaction.response.send_message('clan created')
        collector.clans.insert_one( {
                'guild_id': interaction.guild.id,
                'owner_id': interaction.user.id,
                'clan_id': random.randint(1000000,99999999),
                'member:': [],
                'cash_clan':0,
                'clan_icon':'url',
                'clan_role': 0,
                'clan_shop':[],
                'clan_name':clan_name,
                'clan_bio': ''
            }           
        )
    
    @nextcord.slash_command(name='add_member', description='создание клана на сервербе')
    async def add_member(self, interaction: nextcord.Interaction, member: nextcord.Member):
        await interaction.response.send_message('member added')
        # get collections
        # add member
        # edit collection

    

        

    

def setup(bot):
    bot.add_cog(CCommands(bot))