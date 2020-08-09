import discord
from discord.ext import commands
from classes import classes
from class_list import class_list

client = commands.Bot(command_prefix = '!')

@client.command()
async def cb(ctx, *, course):
    clss = str(course)
    if clss in class_list:
        data = classes[clss]
        await ctx.send(clss + '\n' + data['n'] + '\n' + 'Instructor: ' + data['i'] + '\n' + data['d'] + '\n' + 'Lecture: ' + ', '.join(data['lr']) + '\n' + 'Recitations: ' + ', '.join(data['rr']))
    else:
        await ctx.send('Please enter a valid class number.')

client.run('NzQyMTExMDMyNTkxMjUzNjE2.XzBWwQ.QdXhXw72VeqM7V6w_3QyPafuhOU')