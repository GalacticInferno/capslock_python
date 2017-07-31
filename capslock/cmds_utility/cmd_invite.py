from cmds_utility.data_utility import STATICS, alias_utility


def ex(invoke, args, message, client):
    if len(args) > 0:
        sub_invoke = args[0].__str__()[0:].replace("'", "")
        print(sub_invoke, ' ', args)
        if sub_invoke in alias_utility.bot_alias:
            yield from client.send_message(message.author,
                STATICS.INVITE_BOT)
        elif sub_invoke in alias_utility.server_alias:
            yield from client.send_message(message.author,
                STATICS.INVITE_SERVER)
        else:
            yield from client.send_message(message.author,
                '%s is an invaild argument' % (sub_invoke))
    else:
        yield from client.send_message(message.author,
            '%s is missing args!' % (invoke))
    return
