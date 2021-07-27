import discord
from discord import member
from discord.ext import commands
from discord.ext.commands import has_permissions
import datetime
import asyncio

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'{client.user}로 로그인 완료 ({client.user.id})')
    
@client.command()
async def dm(ctx, *, msg):
    await ctx.send('서버 모두에게 DM을 전송합니다.')
    sent = 0
    fail = 0
    for user in ctx.guild.members:
        try:
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.add_field(name=f'{ctx.message.guild.name} 서버에서 DM이 전송되었습니다.', value=msg)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            if user == client.user:
                pass
            else:
                await user.send(embed=embed)
                await ctx.send(f":white_check_mark: {user.mention}에게 DM을 전송했습니다.")
                await asyncio.sleep(1)
                sent += 1
        except:
            await ctx.send(f':no_entry: {user.mention}에게 DM 전송을 실패했습니다.')
            fail += 1
    embed = discord.Embed(title='전체DM 결과', description=f':white_check_mark: 성공 : **{sent}** 회 \n:no_entry: 실패 : **{fail}** 회', colour=discord.Colour.blue())
    await ctx.send(embed=embed) 
   
   
