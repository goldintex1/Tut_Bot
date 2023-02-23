import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents = intents)


@bot.event
async def  on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_voice_state_update(member, before, after):
    channel = bot.get_channel(1078302505110347856)
    if before.channel != None:
        if after.channel != None:
            await channel.send(f"{member.name}已離開{before.channel}頻道")
            await channel.send(f"{member.name}已加入{after.channel}頻道")
        else:
            await channel.send(f"{member.name}已離開{before.channel}頻道")
    else:
        if before.channel == None:
            await channel.send(f"{member.name}已加入{after.channel}頻道")
    

        

bot.run("MTA3ODIyODkzNzY4MDg5MTk5NQ.GkUk_C.pfKqYIMqL1K_uj9s5OFgtgYtkQLk8jz8zWhCZ4")