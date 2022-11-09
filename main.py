#! /usr/bin/python3
# coding: utf-8
# Created by: ARyOtaRe
# Created on: Wed 26 May 2021 09:38:04
# Last modified by: ARyOtaRe
# Last modified on: 08/06/2022 14:21

import discord
from discord.ext import commands
from datetime import datetime
from time import sleep
import os
import json
import requests

with open('tokens.json', 'r') as token_file:
    Tokens = json.loads(token_file.read())


class Archives(commands.Bot):
    async def on_ready(self):
        '''Connecting bot to the Discord group.'''
        general = client.get_channel(823948756705083433)
        await general.send('I am a bold one.')
        # Simplistic help
        msg_boot = "myself booting up..."
        await client.change_presence(activity=discord.Activity(name=msg_boot,
                                    type=discord.ActivityType.watching))
        sleep(5)
        # Simplistic help
        msg_play = "with the devs\' nerves"
        await client.change_presence(activity=discord.Activity(name=msg_play,
                                    type=discord.ActivityType.playing))
        print("Ich bin der bold one")

    async def on_message(self, message):
        '''Handling messages requests sent to bot.'''
        if message.author == client.user:
            # ??? Return What ???
            return

        elif "colander" in message.content:
            await message.channel.send(' https://tenor.com/view/\
nigel-ng-uncle-roger-failure-uncle-roger-failure-fail-gif-17897119')
            print('failure')

        elif message.content.startswith('I am the Senate'):
            await message.channel.send(' https://tenor.com/view/\
not-yet-mace-windu-star-wars-gif-9797353')
            print('not yet')

        elif any(element in message.content.lower() for element
                in ['hello there', 'hi there', 'hello-there',
                'hi-there', 'greetings']):
            await message.channel.send('https://tenor.com/view/hello-there-hi-\
                there-greetings-gif-9442662')
            print('General Kenobi')
        else:
            await message.channel.send('https://www.gearfuse.com/wp-content/\
uploads/2013/07/Han.gif')
            print('What now?')

        return await client.process_commands(message)


client = Archives(command_prefix=commands.when_mentioned_or('ach!'))

client.remove_command('help')


@client.command()
@commands.is_owner()
async def dbreload(ctx):
    '''????Database Reload?????'''
    url = 'https://raw.githubusercontent.com/ARyOtaRe/Star-Wars-Archives/main/\
SWPlanets.json'
    r = requests.get(url)
    with open(os.path.join(os.getcwd(), 'swat.json'), 'wb') as output:
        output.write(r.content)


@client.command()
async def invite(ctx):
    '''Invite SW bot to a discord group'''
    embed = discord.Embed(title="Here's how to invite me!",
                        description="You will need to manage the server \
you want it to be in",
                        color=0xE20088) \
        .add_field(name="Administrator invite:",
                    value="https://discord.com/api/oauth2/authorize?\
client_id=825795403135975504&permissions=8&scope=bot",
                    inline=False) \
        .add_field(name="Normal invite:",
                    value="https://discord.com/api/oauth2/authorize?client_id=\
825795403135975504&permissions=4294967287&scope=bot",
                    inline=False) \
        .set_footer(text="Star Wars Archives | Developed by \
ARyOtaRe#8215 and Killian#8237") \
        .set_author(name="Thanks for inviting me!")\
        .set_thumbnail(url="https://cdn.discordapp.com/emojis/\
750050623055200306.png?v=1")
    embed.timestamp = datetime.now()
    await ctx.send(embed=embed)

# Description = "\n".join(planet_dict["planets"].keys())


@client.command()
async def list(ctx):
    '''Listing all available planets'''
    with open(os.path.join(os.getcwd(), 'SWPlanets.json'), 'r') as json_file:
        planet_dict = json.loads(json_file.read())
    Description = "\n".join(planet_dict["planets"].keys())

    embed = discord.Embed(title="Here's the list of all the planets \
you can search for:",
                        description=Description, color=0xE20088)\
        .set_footer(text="Star Wars Archives | Developed by ARyOtaRe#8215 \
and Killian#8237")\
        .set_thumbnail(url="https://static.wikia.nocookie.net/frstarwars/images/\
2/2e/Holocron-TSWB.png/revision/latest?cb=20201021063046")\
        .set_author(name="Here's the planet you were looking for:")
    embed.timestamp = datetime.now()

    await ctx.send(embed=embed)


@client.command()
async def planet(ctx, arg: str):
    """Display planet's info"""
    with open(os.path.join(os.getcwd(), 'SWPlanets.json'), 'r') as json_file:
        planet_dict = json.loads(json_file.read())

    target_planet = planet_dict["planets"][arg.title()]

    embed = discord.Embed(title=f"Your planet is {arg.title()}",
                        description="If you want more info, \
ask the staff or leave a suggestion!",
                        color=0xE20088)\
        .add_field(name="**Rotation period:**",
                    value=f'{int(["rotation_period"]):,.0f}',
                    inline=False)\
        .add_field(name="**Orbital period:**",
                    value=f'{int(target_planet["orbital_period"]):,.0f}',
                    inline=False)\
        .add_field(name="**Diameter:**",
                    value=f'{int(target_planet["diameter"]):,.0f}',
                    inline=False)\
        .add_field(name="**Climate:**",
                    value=target_planet["climate"],
                    inline=False)\
        .add_field(name='**Gravity:**',
                    value=target_planet["gravity"],
                    inline=False)\
        .add_field(name='**Terrain:**',
                    value=target_planet["terrain"],
                    inline=False)\
        .add_field(name='**Surface water:**',
                    value=f'{target_planet["surface_water"]}%',
                    inline=False)\
        .add_field(name='**Population:**',
                    value=f'{int(target_planet["population"]):,.0f}',
                    inline=False)\
        .set_footer(text="Star Wars Archives | \
Developed by ARyOtaRe#8215 and Killian#8237")\
        .set_thumbnail(url=target_planet["photo"])\
        .set_author(name="Here's the planet you were looking for:")
    embed.timestamp = datetime.now()

    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    '''Display Help'''
    embed = discord.Embed(title="This is the list of the commands you can do",
                        description="This is the current updated list, \
more to come.",
                        color=0xE20088)\
        .add_field(name="**list**",
                    value="Gives you infos about the planets the bot can \
give you informations on.",
                    inline=False)\
        .add_field(name="**planet**",
                    value="Gives you informations about the planet \
you chose (from the Star Wars universe).",
                    inline=False)\
        .add_field(name="**help**",
                    value="Gives you this message.",
                    inline=False)\
        .set_footer(text="Star Wars Archives | \
Developed by ARyOtaRe#8215 and Killian#8237")
    embed.timestamp = datetime.now()

    await ctx.send(embed=embed)


@client.event
async def on_disconnect():
    general = client.get_channel(823948756705083433)
    await general.send('Completing the archives, I will be right back.')


client.run(Tokens["bot_token"]["token"])
