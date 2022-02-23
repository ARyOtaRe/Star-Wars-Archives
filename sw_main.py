#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord 
from discord.ext import commands
from datetime import datetime
import os
import json
import requests

"""
https://github.com/Aiita/StarWarsElphebat/blob/25d927227fd71b117c44bf03c4e2a2cfa4f27dac/SWPlanets.json"""




class Archives(commands.Bot):
    async def on_ready(self):
        '''connecting'''
        general=client.get_channel(823948756705083433)
        await general.send ('I am a bold one.')
        await client.change_presence(activity = discord.Activity(name = "me boot up...", type = discord.ActivityType.watching)) # Simplistic help

        await client.change_presence(activity = discord.Activity(name ="with the devs\' nerves", type = discord.ActivityType.playing)) # Simplistic help


        print("Ich bin der bold one")

    async def on_message(self, message):
        if message.author == client.user:
            return 
        
        if "colander" in message.content:
            await message.channel.send(' https://tenor.com/view/nigel-ng-uncle-roger-failure-uncle-roger-failure-fail-gif-17897119')
            print('failure')
        
        if message.content.startswith('I am the Senate'):
            await message.channel.send(' https://tenor.com/view/not-yet-mace-windu-star-wars-gif-9797353')
            print('not yet')
            
        if message.content.startswith('https://tenor.com/view/hello-there-hi-there-greetings-gif-944266'):
            await message.channel.send('https://tenor.com/view/grievous-general-kenobi-star-wars-gif-11406339')
            print('General Kenobi')

        return await client.process_commands(message)
        

    
client= Archives(command_prefix=commands.when_mentioned_or('arch!'))

client.remove_command('help')

@client.command()
@commands.is_owner()
async def ping(ctx):
    await ctx.send(f'My ping is currently of `{client.latency:,.2f}` seconds.')

@client.command(description='Gives you invitation links to add it to your server',aliases=['inv','invitation'])
async def invite(ctx):
    embed=discord.Embed(title="Here's how to invite me!", description="You will need to manage the server you want it to be in", color=0xE20088) \
    .add_field(name="Administrator invite:", value="https://discord.com/api/oauth2/authorize?client_id=825795403135975504&permissions=8&scope=bot", inline=False) \
    .add_field(name="Normal invite:",value="https://discord.com/api/oauth2/authorize?client_id=825795403135975504&permissions=4294967287&scope=bot", inline=False) \
    .set_footer(text="Star Wars Archives | Developed by ARyOtaRe#8215 and Killian#8237") \
    .set_author(name="Thanks for inviting me!")\
    .set_thumbnail(url="https://cdn.discordapp.com/emojis/750050623055200306.png?v=1")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed) 


@client.command(aslaises=['dbreload','dbr',])
@commands.is_owner()
async def databasereload(ctx):
    url='https://raw.githubusercontent.com/ARyOtaRe/Star-Wars-Archives/main/SWPlanets.json?token=ARM2OK3PR5L5IBJDK67GBITBT2P4K'
    r=requests.get(url)
    with open('swplanets.json', 'wb') as output:
        output.write(r.content)


@client.command(description='Gives you a list of the planets currently available in our database', aliases=['lst'])
async def list(ctx):
    folder='/home/aryotare/star_wars_archives'
    with open(os.path.join(os.path.abspath(folder),'swplanets.json'),'r') as jsonfile:
        data = json.loads(jsonfile.read())
    Description = "\n".join(data["planets"].keys())
    embed=discord.Embed(title=f"Here's the list of all the planets you can search for! We currently have {len(data['planets'].keys())} of them. ", description=Description, color=0xE20088)\
    .set_footer(text="Star Wars Archives | Developed by ARyOtaRe#8215 and Killian#8237")\
    .set_thumbnail(url ="https://static.wikia.nocookie.net/frstarwars/images/2/2e/Holocron-TSWB.png/revision/latest?cb=20201021063046")\
    .set_author(name="Here's the planet you were looking for:")
    embed.timestamp=datetime.now()

    await ctx.send(embed=embed)

data=json.loads(open(os.path.join(os.path.abspath('/home/pi/starwarsarchives'),'swplanets.json'),'r').read())

@client.command(description=f'Tells you facts about any Star Wars planet, we currently have {len(data["planets"].keys())} of them.', aliases=['info', 'plt','plnt'])
async def planet(ctx,*,args):
    folder='/home/aryotare/star_wars_archives'
    with open(os.path.join(os.path.abspath(folder),'swplanets.json'),'r') as json_file:
        data = json.loads(json_file.read())
    embed=discord.Embed(title=f"The planet you were looking for is {args}", description="If you want more info, ask the staff or write a suggestion!", color=0xE20088)\
    .add_field(name="**Rotation period:**", value=f'{int(data["planets"][args]["rotation_period"]):,.0f}', inline=False)\
    .add_field(name="**Orbital period:**",value=f'{int(data["planets"][args]["orbital_period"]):,.0f}', inline=False)\
    .add_field(name="**Diameter:**",value=f'{int(data["planets"][args]["diameter"]):,.0f}', inline=False)\
    .add_field(name="**Climate:**",value=data["planets"][args]["climate"], inline=False)\
    .add_field(name='**Gravity:**', value=data["planets"][args]["gravity"],inline=False)\
    .add_field(name='**Terrain:**', value=data["planets"][args]["terrain"],inline=False)\
    .add_field(name='**Surface water:**', value=f'{data["planets"][args]["surface_water"]}%',inline=False)\
    .add_field(name='**Population:**', value=f'{int(data["planets"][args]["population"]):,.0f}',inline=False)\
    .set_footer(text="Star Wars Archives | Developed by ARyOtaRe#8215 and Killian#8237")\
    .set_thumbnail(url = data["planets"][args]["photo"])\
    .set_author(name="Here's the planet you were looking for:")
    embed.timestamp=datetime.now()

    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed=discord.Embed(title="This is the list of the commands you can do", description="This is the current updated list, more to come.", color=0xE20088)\
    .add_field(name="**list**",value="Gives you infos about the planets the bot can give you informations on.", inline=False)\
    .add_field(name="**planet**", value="Gives you informations about the planet you chose (from the Star Wars universe).", inline=False)\
    .add_field(name="**help**",value="Gives you this message.", inline=False)\
    .set_footer(text="Star Wars Archives | Developed by ARyOtaRe#8215 and Killian#8237")
    embed.timestamp=datetime.now()

    await ctx.send(embed=embed)




client.run('ODI1Nzk1NDAzMTM1OTc1NTA0.YGDH5g.odpB4tmIlD7aNpY_xaKQg2GaEOI')



