

def ex(invoke, args, message, client):
    member = message.mentions[0]

    if len(args) > 0:
        yield from client.kick(member)
        if len(args) > 1:
            reason = args[1].__str__()[0:len(args)].replace("'", "")
            yield from client.send_message(message.channel, '%s was kicked for reason: %s' % (member, reason))
        else:
            yield from client.send_message(message.channel, '%s has been booted!' % (member))
