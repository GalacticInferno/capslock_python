

def ex(invoke, args, message, client):
    member = message.mentions[0]
    days = int(args[1].__str__()[0:len(args[1])].replace("'", ""))

    if len(args) > 0:
        yield from client.ban(member, days)
        if len(args) > 2:
            reason = args[2].__str__()[0:len(args)].replace("'", "")
            yield from client.send_message(message.channel,
                '%s was banned for reason: %s for %s days'
                % (member, reason, days))
        else:
            yield from client.send_message(message.channel,
            '%s the ban hammer has spoken!' % (member))
    else:
        yield from client.send_message(message.author,
            '%s is missing args!' % (invoke))
    return
