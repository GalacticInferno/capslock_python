sub_invoke = 'null'


def ex(invoke, args, message, client):
    if len(args) > 0:
        global sub_invoke
        sub_invoke = args[0].__str__()[0:].replace("'", "")
        amount = int(args[1].replace("'", ""))
        print(sub_invoke, ' ', args)

        if sub_invoke in ('bot'):
            deleted = yield from client.purge_from(message.channel, limit=amount, check=is_bot)
            yield from client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
        else:
            deleted = yield from client.purge_from(message.channel, limit=amount, check=is_user)
            yield from client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
    else:
        yield from client.send_message(message.author, '%s is missing args!' % (invoke))


def is_bot(message):
    print(message.author)
    return message.author.__str__() in ('CAPS LOCK#4714')


def is_user(message):
    print(message.author)
    return message.author.__str__() == sub_invoke
