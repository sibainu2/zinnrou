import discord
from discord import channel
from discord import guild
from discord.ext import commands
from discord.role import R
from discord_buttons_plugin import *
import random
from time import sleep


bot = commands.Bot(command_prefix = "m!")
buttons = ButtonsClient(bot)

########################宣言#############################
times=0#0：開始前　1：朝　2：昼　3：夕方 4:夜　
player={
    "p1":{"id":0,"name":"","potion":"村人","life":1},
    "p2":{"id":0,"name":"","potion":"村人","life":1},
    "p3":{"id":0,"name":"","potion":"村人","life":1},
    "p4":{"id":0,"name":"","potion":"村人","life":1},
    "p5":{"id":0,"name":"","potion":"村人","life":1},
    "p6":{"id":0,"name":"","potion":"村人","life":1},
    "p7":{"id":0,"name":"","potion":"村人","life":1},
    "p8":{"id":0,"name":"","potion":"村人","life":1},
    "p9":{"id":0,"name":"","potion":"村人","life":1}
    }

def timecheck():
    global times
    return times



@bot.command()
async def ready(ctx):
#    times=0
#    for i in range(1,10):
#        await ctx.guild.create_role(f"player{i+1}")

    
    #チャンネル作成
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        autorize_role: discord.PermissionOverwrite(read_messages=True)
        }
    Category = await ctx.guild.create_category("部屋")
    mainch = await ctx.guild.create_text_channel("集会場")
    log = await ctx.guild.create_text_PartialInviteChannel("log")
    wch = await ctx.guild.create_text_PartialInviteChannel("人狼チャット")
    uch = await ctx.guild.create_text_PartialInviteChannel("占い師")
    rch = await ctx.guild.create_text_PartialInviteChannel("霊能")
    kch = await ctx.guild.create_text_PartialInviteChannel("騎士")
    await mainch.edit(category = Category)
    await log.edit(category = Category)
    await wch.edit(category = Category)
    await uch.edit(category = Category)
    await rch.edit(category = Category)
    await kch.edit(category = Category)
    embed=discord.Embed(title="参加者の皆さんへ",color=0x00ffff)



bot.run("ODY2NjMyODI0OTg2NDAyODM3.YPVYtg.9rbiRwtxwhGqm4ToJ5G1fekwo9s")