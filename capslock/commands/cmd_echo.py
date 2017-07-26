

def ex(invoke, args, message, client):
    yield from client.send_message(message.channel, ':trumpet: %s :trumpet:' % (args.__str__()[1:-1].replace("'", "")))
    yield from client.delete_message(message)
