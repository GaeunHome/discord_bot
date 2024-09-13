import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hi(self, ctx):
        uid = ctx.author.id
        await ctx.send(f'<@{uid}> 裴家軍！')

# discord embed
# https://cog-creators.github.io/discord-embed-sandbox/

    @commands.command()
    async def info(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="裴秀珉的生活日常", url="https://www.instagram.com/baesuminiee?igsh=MXh6NWMzaGgwdnh5bA==", description="呀呀呀呀", color=0x45cacd, timestamp=datetime.datetime.now())
        embed.set_author(name="🐰裴秀珉 🤍배수민")
        embed.set_thumbnail(url="https://kpopping.com/documents/75/3/1536/230226-STAYC-Sumin-documents-1.jpeg?v=95233")
        embed.add_field(name="Birth", value="2001.03.13", inline=True)
        embed.add_field(name="age", value="23", inline=True)
        embed.set_footer(text="裴家軍代表")
        await ctx.send(embed=embed)

    @commands.command()
    async def notice(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)
    
    @commands.group()
    async def about(self, ctx):
        await ctx.message.delete()
        pass
    
    @about.command()
    async def youtube_channel(self, ctx):
        await ctx.send("官方Youtube頻道已經更新影片啦！\nhttps://www.youtube.com/@STAYC")
    
    @about.command()
    async def naver(self, ctx):
        await ctx.send("官方幕後照更新啦！\nhttps://post.naver.com/my.naver?memberNo=39382404")

async def setup(bot):
    await bot.add_cog(Main(bot))