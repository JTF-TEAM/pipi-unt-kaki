import nextcord
from nextcord.ext import commands
import requests
import os
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO



class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def Create(self, username, avatar, level, rank, current_xp, custom_background, xp_color, next_level_xp):
        img = Image.new('RGB', (934, 282), color = custom_background) 
        response = requests.get(avatar)
        img_avatar = Image.open(BytesIO(response.content)).convert("RGBA")
        bigsize = (img_avatar.size[0] * 3, img_avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(img_avatar.size)
        img_avatar.putalpha(mask)
        img_avatar = img_avatar.resize((170, 170))
        img.paste(img_avatar, (50, 50))
        d = ImageDraw.Draw(img)
        d = self.Poloska(d, 260, 180, 575, 40, current_xp/next_level_xp, bg="#484B4E", fg = xp_color)
        font = ImageFont.truetype(font=f"cogs/fonts/regular.ttf", size=50)
        font2 = ImageFont.truetype(font=f"cogs/fonts/regular.ttf", size=25)
        d.text((260, 100),username,(255,255,255), font=font)
        d.text((740, 130),f"{current_xp}/{next_level_xp} XP",(255,255,255), font=font2)
        d.text((630, 50),f"Уровень {level}",xp_color, font=font)
        d.text((260, 50),f"Ранг #{rank}",(255,255,255), font=font2)
        img.save(f"{os.getcwd()}\\cogs\\pics\\out.jpg")
        return f"{os.getcwd()}\\cogs\\pics\\out.jpg"

    def Poloska(self, poloska, x, y, w, h, progress, bg="black", fg="red"):
        poloska.ellipse((x+w, y, x+h+w, y+h), fill=bg)
        poloska.ellipse((x, y, x+h, y+h), fill=bg)
        poloska.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)
        w *= progress
        poloska.ellipse((x+w, y, x+h+w, y+h),fill=fg)
        poloska.ellipse((x, y, x+h, y+h),fill=fg)
        poloska.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=fg)

        return poloska

    
    @nextcord.slash_command(name='rank', description='hueta')
    async def rank(self, interaction: nextcord.Interaction):
        # тут надо просписать высасывание даты из монги
        user_stats = [10, 5, 800, 1600]
        card = self.Create(
                    username=interaction.user.name,
                    avatar= interaction.user.avatar,
                    level=user_stats[0], # user level
                    rank=user_stats[1], # user rank
                    current_xp=user_stats[2], # user xp
                    custom_background= "#000000", # background colour
                    xp_color="#FF7A7A", # Foreground colour
                    next_level_xp=user_stats[3]) # Next level xp
        A = nextcord.File(card)
        await interaction.response.send_message(content="s", file=A)

    

def setup(bot):
    bot.add_cog(Rank(bot))