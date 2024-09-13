import discord
from discord.ext import commands
import json, os, asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

# 建立 Intents 實例並啟用所需的意圖
intents = discord.Intents.default()
# 啟用 message_content 意圖
intents.message_content = True
# 建立 Bot 實例並傳遞 intents
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(">> 裴秀珉來啦！！ <<")
    game = discord.Game("老婆機器人！！")

async def load_extensions():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'載入 {extension}.py 完成')

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'卸載 {extension}.py 完成')

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'動態更新 {extension}.py 完成')

async def start_bot():
    await load_extensions()
    await bot.start(jdata['TOKEN'])

if __name__ == "__main__":
    asyncio.run(start_bot())