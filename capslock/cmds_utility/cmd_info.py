from cmds_utility.data_utility import STATICS

# Bot Info
name = STATICS.NAME
version = STATICS.VERSION
description = 'The Python version of the CSA discord bot'
creator = STATICS.AUTHOR

botInfo = 'Name: {0}\nVersion: {1}\nDesc: {2}\nAuthor: {3}'.format(
    name, version, description, creator)


def ex(invoke, args, message, client):
    if len(args) > 0:
        sub_invoke = args[0].__str__()[0:].replace("'", "")
        print(sub_invoke, ' ', args)
        if sub_invoke in ('CAPSLOCK', 'capslock'):
            yield from client.send_message(message.author, botInfo)
    else:
        yield from client.send_message(message.author, '%s is missing args!'
            % (invoke))
    return
