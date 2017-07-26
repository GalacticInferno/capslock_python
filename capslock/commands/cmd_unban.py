

def ex(invoke, args, message, client):
    member = message.mentions[0]

    if len(args) > 0:
        yield from client.unban(message.server, member)
        yield from client.send_message(message.channel, '%s was unbanned' % (member))
