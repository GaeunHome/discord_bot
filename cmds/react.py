import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def photo(self, ctx):
        await ctx.message.delete()
        pic = discord.File(jdata['pic']) # 檔案路徑
        await ctx.send(file=pic)

async def setup(bot):
    await bot.add_cog(React(bot))