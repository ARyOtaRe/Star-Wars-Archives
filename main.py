import discord 
from discord.ext import commands
from datetime import datetime
import os
import json





folder="C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Star-Wars-Archives"
with open(os.path.join(os.path.abspath(folder),'Star_Wars_planets.json'),'r') as json_file:
    data = json.loads(json_file.read())


class Archives(commands.Bot):
    async def on_ready(self):
        '''connecting'''
        general=client.get_channel(823948756705083433)
        await general.send ('I am a bold one.')
        await client.change_presence(activity = discord.Activity(name = f"me boot up...", type = discord.ActivityType.watching)) # Simplistic help

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


@client.command()
async def invite(ctx):
    embed=discord.Embed(title="Here's how to invite me!", description="You will need to manage the server you want it to be in", color=0xE20088) \
    .add_field(name="Administrator invite:", value="https://discord.com/api/oauth2/authorize?client_id=825795403135975504&permissions=8&scope=bot", inline=False) \
    .add_field(name="Normal invite:",value="https://discord.com/api/oauth2/authorize?client_id=825795403135975504&permissions=4294967287&scope=bot", inline=False) \
    .set_footer(text="Star Wars Archives | Developped by BRΣ1ZH#8215,Killian#8237 and Aiita#6303") \
    .set_author(name="Thanks for inviting me!")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed) 

@client.command()
async def planet(ctx, arg):
    embed=discord.Embed(title=f"Your planet is {arg}", description="If you want more info, ask the staff or put a suggestion!", color=0xE20088)\
    .add_field(name="Rotation period:", value=f'{int(data["planets"][arg]["rotation_period"]):,.0f}', inline=False)\
    .add_field(name="Orbital period:",value=f'{int(data["planets"][arg]["orbital_period"]):,.0f}', inline=False)\
    .add_field(name="Diameter:",value=f'{int(data["planets"][arg]["diameter"]):,.0f}', inline=False)\
    .add_field(name="Climate:",value=data["planets"][arg]["climate"], inline=False)\
    .add_field(name='Gravity:', value=data["planets"][arg]["gravity"],inline=False)\
    .add_field(name='Terrain:', value=data["planets"][arg]["terrain"],inline=False)\
    .add_field(name='Surface water:', value=f'{data["planets"][arg]["surface_water"]}%',inline=False)\
    .add_field(name='Population:', value=f'{int(data["planets"][arg]["population"]):,.0f}',inline=False)\
    .set_footer(text="Star Wars Archives | Developped by BRΣ1ZH#8215,Killian#8237 and Aiita#6303")\
    .set_thumbnail(url = data["planets"][arg]["photo"])\
    .set_author(name="Here's the planet you were looking for:")
    embed.timestamp=datetime.now()

    await ctx.send(embed=embed)



client.run('ODI1Nzk1NDAzMTM1OTc1NTA0.YGDH5g.odpB4tmIlD7aNpY_xaKQg2GaEOI')



