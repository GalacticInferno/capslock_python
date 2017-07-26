import discord
import logging
import asyncio
import datetime

import secrets
from commands import cmd_ban, cmd_clean, cmd_echo, cmd_hello, cmd_help
from commands import cmd_highfive, cmd_info, cmd_kick, cmd_ping, cmd_search, cmd_unban, STATICS

client = discord.Client()

command = {
    "ban": cmd_ban,
    "clean": cmd_clean,
    "echo": cmd_echo,
    "hello": cmd_hello,
    "help": cmd_help,
    "highfive": cmd_highfive,
    "info": cmd_info,
    "kick": cmd_kick,
    "ping": cmd_ping,
    "search": cmd_search,
    "unban": cmd_unban
}

# Logging
dLogger = logging.getLogger('discord')
dLogger.setLevel(logging.DEBUG)

dHandler = logging.FileHandler(filename='discordDEBUG.log', encoding='utf-8', mode='w')
dHandler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

dLogger.addHandler(dHandler)


# Bot Events
@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in')
    print('-------------------')
    print(client.user.name)
    print(client.user.id)
    print('-------------------')


@client.event
@asyncio.coroutine
def on_member_join(member: discord.Member):
    currentTime = datetime.datetime.now()
    print(currentTime, ': {0.name} joined the server'.format(member))


@client.event
@asyncio.coroutine
def on_member_remove(member: discord.Member):
    currentTime = datetime.datetime.now()
    print(currentTime, ': {0.name} left the server'.format(member))


@client.event
@asyncio.coroutine
def on_member_leave(member: discord.Member):
    currentTime = datetime.datetime.now()
    print(currentTime, ': {0.name} left the server'.format(member))


@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(STATICS.PREFIX):
        currentTime = datetime.datetime.now()
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        print("TIME: %s\nUSER: %s\nINVOKE: %s\nARGS: %s" %
              (currentTime, message.author.name, invoke, args.__str__()[1:-1].replace("'", "")))
        print('-------------------')

        if command.keys().__contains__(invoke):
            yield from command.get(invoke).ex(invoke, args, message, client)
        else:
            yield from client.send_message(message.author, '%s is an invaild command!' % (invoke))
            print('WARNING: Invaild command: %s' % (invoke))


client.run(secrets.BOT_TOKEN)
