import nextcord
from nextcord.ext import commands
import random
import motor.motor_asyncio as mator
MONGO = ""
class ref(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.databasa = mator.AsyncIOMotorClient(MONGO)

    
    @nextcord.slash_command(name='create_referal')
    async def asd(self, interaction: nextcord.Interaction, description:str):
        bukvi = 'qweasdzxcvbnfghrtyuiojklmp0123456789PLOKMIJNUHBYGVTFCRDXESZWAQ'
        dlinna = len(bukvi)-1
        ssilka = ''
        for i in range(11):
            ssilka += bukvi[random.randint(0, dlinna)]
        self.databasa.insert_one(
            {
                'guild_id':interaction.guild, 
                'ssilka':ssilka,
                'creator_id':interaction.user.id,
                'uses': 0,
                'active': True,
                'description': description,
                'users':[]
            }
        )

        await interaction.response.send_message(f'ВАШ РЕФЕРАЛЪ {ssilka}')
        return
    
    @nextcord.slash_command(name='use_referal')
    async def asd(self, interaction: nextcord.Interaction, ssilka:str):
        est = self.databasa.find_one({'guild':interaction.guild, 'ssilka':ssilka})
        if est != None:
            if est['active'] == True:
                if interaction.user.id in est['users']:
                    await interaction.response.send_message('вы уже использовали эту ссылку')
                else:
                    new_uses = est['uses']+1
                    new_users = est['users'].copy()
                    self.databasa.update_one({'ssilka': ssilka}, {'$set': {'uses':new_uses, 'users':new_users.append(interaction.user.id)}})
                    nihuya = est['description']
                    await interaction.response.send_message(f'поздравляем вы успешно активировали ссылку и получили {nihuya}')
            else:
                await interaction.response.send_message(f'Ссылка в данный момент не активна')
        else:
            await interaction.response.send_message(f'таких ссыылок нет')
        return

    @nextcord.slash_command(name='edit_referal')
    async def asd(self, interaction: nextcord.Interaction, ssilka:str,  mode:str):
        est = self.databasa.find_one({'guild':interaction.guild, 'ssilka':ssilka})
        if est != None:
            if mode == 'activate':
                self.databasa.update_one({'ssilka': ssilka}, {'$set': {'active':True}})
                await interaction.response.send_message('ссылка активирована')
            elif mode == 'deactive':
                self.databasa.update_one({'ssilka': ssilka}, {'$set': {'active':False}})
                await interaction.response.send_message('ссылка дизактивирована')
            else:
                await interaction.response.send_message(f'данная команда используется по примеру - ssilka(vasha ssilka), mode(active/deactive)')
        else:
            await interaction.response.send_message('такой ссылки нету')
    
    @nextcord.slash_command(name='referal_info')
    async def asd(self, interaction: nextcord.Interaction, ssilka:str):
        est = self.databasa.find_one({'guild':interaction.guild, 'ssilka':ssilka})
        if est != None:
            users = ''
            for aidi in est['users']:
                users += f"<@{aidi}>\n"
            await interaction.response.send_message(
                embed=nextcord.Embed(
                    title='fer info',
                    description=f"автор: <@{est['creator_id']}>\nиспользований {est['uses']}\nstatus {est['active']}\nmembers: {users}"
                )
            )
        else:
            await interaction.response.send_message('такой ссылки нету')

def setup(bot):
    bot.add_cog(ref(bot))