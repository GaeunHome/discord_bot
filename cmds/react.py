import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def photo(self, ctx):
        await ctx.message.delete()
        chosen_image_path = random.choice(jdata['Pic'])
        pic = discord.File(chosen_image_path)
        await ctx.send(file=pic)

async def setup(bot):
    await bot.add_cog(React(bot))