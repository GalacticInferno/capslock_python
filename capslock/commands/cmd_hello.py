import random


def ex(invoke, args, message, client):
    line = random.choice(open('commands\hello.txt').readlines())
    print(line)
    yield from client.send_message(message.channel, line.format(message.author))
