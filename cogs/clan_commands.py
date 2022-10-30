import nextcord
from nextcord.ext import commands
import random
import motor.motor_asyncio as mator

MONGO = "" # ssilka na mongu
connection = mator.AsyncIOMotorClient(MONGO)
mogo = connection['disco-disco-go-go']

class CCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(name='clan_create', description='создание клана на сервербе')
    async def create_clan(self, interaction: nextcord.Interaction, clan_name: str, description: str = ''):
        clan_id = random.randint(1000000,99999999)
        clan_role = await interaction.guild.create_role(clan_name)
        clanboss_data = await mogo.infousers.find_one({'member_id':interaction.user.id})
        if clanboss_data != None:
            if clanboss_data['money'] > 1:
                await mogo.clans.insert_one( {
                        'guild_id': interaction.guild.id,
                        'owner_id': interaction.user.id,
                        'clan_id': clan_id,
                        'member:': [],
                        'cash_clan':0,
                        'clan_icon':'url',
                        'clan_role': clan_role.id,
                        'clan_shop':[],
                        'clan_name':clan_name,
                        'clan_bio': description
                        }           
                    )
                new_money = clanboss_data['money'] - 1
                await mogo.infousers.update_one({'money':new_money})
                await interaction.response.send_message(f'Клан создан. Клан айди {clan_id}')
            else:
                await interaction.response.send_message(f'Malo denyak dlya etogo{clan_id}')
        await interaction.response.send_message(f'Что то пошло не так')

    @nextcord.slash_command(name='clan_delete', description='Удоление клана на сервербе')
    async def delete_clan(self, interaction: nextcord.Interaction, clan_id: int):
        await mogo.clans.delete_one( {'clan_id': clan_id})
        await interaction.response.send_message('Клан удолен')
        pass


    @nextcord.slash_command(name='add_member', description='добавление микрочелика в клан')
    async def add_member(self, interaction: nextcord.Interaction, member: nextcord.Member, clan_id: int):
        clan = await mogo.clans.find_one({'clan_id':clan_id})
        if clan != None:
            new_data = clan.copy()
            new_data['members'].append(member.id)
            await mogo.clans.update_one(clan, {'$set': new_data})
            await interaction.response.send_message(f'Добавлен пользователь')
        else:
            await interaction.response.send_message("Что то пошло не так... ")


    @nextcord.slash_command(name='remove_member', description='кик сикрочелика')
    async def remove_member(self, interaction: nextcord.Interaction, member: nextcord.Member, clan_id: int):
        clan = await mogo.clans.find_one({'clan_id':clan_id})
        if clan != None:
            new_data = clan.copy()
            new_data['members'].delete(member.id)
            await mogo.clans.update_one(clan, {'$set': new_data})
            await interaction.response.send_message(f'Пользователь уадлен')
        else:
            await interaction.response.send_message("Что то пошло не так... ")
    

    @nextcord.slash_command(name='set_bio', description='задать описание клана')
    async def set_bio(self, interaction: nextcord.Interaction, new_bio: str, clan_id: int):
        clan = await mogo.clans.find_one({'clan_id':clan_id})
        if clan != None:
            new_data = clan.copy()
            new_data['clan_bio'] = new_bio
            await mogo.clans.update_one(clan, {'$set': new_data})
            await interaction.response.send_message(f'Готово')
        else:
            await interaction.response.send_message("Что то пошло не так... ")
    
    @nextcord.slash_command(name='set_pic', description='сменить картинку клана')
    async def set_bio(self, interaction: nextcord.Interaction, new_pic_url: str, clan_id: int):
        clan = await mogo.clans.find_one({'clan_id':clan_id})
        if clan != None:
            new_data = clan.copy()
            new_data['clan_icon'] = new_pic_url
            await mogo.clans.update_one(clan, {'$set': new_data})
            await interaction.response.send_message(f'Готово')
        else:
            await interaction.response.send_message("Что то пошло не так... ")
    
    @nextcord.slash_command(name='send_money', description='закинуть деняк в клан')
    async def send_money(self, interaction: nextcord.Interaction, a: str, clan_id: int):
        # if u chela est dengi
        clan = await mogo.clans.find_one({'clan_id':clan_id})
        if clan != None:
            new_data = clan.copy()
            new_data['cash_clan'] += a
            await mogo.clans.update_one(clan, {'$set': new_data})
            await interaction.response.send_message(f'Готово')
        else:
            await interaction.response.send_message("Что то пошло не так... ")
    
    @nextcord.slash_command(name='clan_shop', description='magaz klana')
    async def clan_shop(self, interaction: nextcord.Interaction, clan_id: int):
        clan = await mogo.clans.find_one({'clan_id':clan_id})
        if clan != None:
            await interaction.response.send_message(
                embed=nextcord.Embed(
                    title='MAGAZ',
                    description= str(role+'\n' for role in clan['clan_shop'])
                )
            )
        else:
            await interaction.response.send_message("Что то пошло не так... ")
    

    @nextcord.slash_command(name='clan_info', description='инфа про клан')
    async def clan_info(self, interaction: nextcord.Interaction, clan_id: int):
        clan = await mogo.clans.find_one({'clan_id':clan_id})
        if clan != None:
            E = nextcord.Embed(
                title = f"{clan['clan_name']} clan",
                description=f"владелец: <@{clan['owner_id']}>\nкэшъ: {clan['cash_clan']}\nчелов в клаане: {len(clan['member'])}"
            )
            E.set_image(clan['clan_icon'])
            await interaction.response.send_message(embed=E)
        else:
            await interaction.response.send_message("Что то пошло не так... ")
        
    
    @nextcord.slash_command(name='request_to_join', description='запрос на вступление в клан')
    async def clan_info(self, interaction: nextcord.Interaction, clan_id: int):
        clan = await mogo.clans.find_one({'clan_id':clan_id})
        if clan != None:
            owner = interaction.guild.get_member(clan['owner_id'])
            await owner.send(f"Микрочелик {interaction.user.mention} хочет вступить в ваш говноклан")
            await interaction.response.send_message(f"Заявка отправлена")
        else:
            await interaction.response.send_message("Что то пошло не так... ")

            

def setup(bot):
    bot.add_cog(CCommands(bot))