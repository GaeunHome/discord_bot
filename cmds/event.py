import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, datetime

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['channel']))
        await channel.send(f'{member} 加入裴家軍！')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['裴秀珉', '秀珉']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('SWITH你好！')
        if self.bot.user.mentioned_in(msg):
            content = msg.content
            parts = content.split(' ', 1)
            if len(parts) > 1:
                text = parts[1]
            await msg.channel.send(f'{msg.author.mention} SWITH你好！{reply}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("你缺少參數喔！")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("並沒有這個指令！")
        else:
            await ctx.send("發生錯誤了呀！")

async def setup(bot):
    await bot.add_cog(Event(bot))