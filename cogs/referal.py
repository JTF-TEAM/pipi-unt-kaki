import nextcord
from nextcord.ext import commands
import random

class ref(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.databasa = motor('ssilka')

    
    @nextcord.slash_command(name='create_referal')
    async def asd(self, interaction: nextcord.Interaction):
        bukvi = 'qweasdzxcvbnfghrtyuiojklmp0123456789PLOKMIJNUHBYGVTFCRDXESZWAQ'
        dlinna = len(bukvi)-1
        ssilka = ''
        for i in range(11):
            ssilka += bukvi[random.randint(0, dlinna)]
        self.databasa.insert_one({'guild':interaction.guild, 'ssilka':ssilka})

        await interaction.response.send_message(f'ВАШ РЕФЕРАЛЪ {ssilka}')
        return
    
    @nextcord.slash_command(name='use_referal')
    async def asd(self, interaction: nextcord.Interaction, ssilka:str):
        est = self.databasa.find_one({'guild':interaction.guild, 'ssilka':ssilka})
        if est != None:
            self.databasa.delete_one({'guild':interaction.guild, 'ssilka':ssilka})
            nihuya = 'много недег'
            await interaction.response.send_message(f'поздравляем вы успешно активировали ссылку и получили {nihuya}')
        else:
            await interaction.response.send_message(f'таких ссыылок нет')
        return


def setup(bot):
    bot.add_cog(ref(bot))