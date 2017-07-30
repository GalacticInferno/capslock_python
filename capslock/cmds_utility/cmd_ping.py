

def ex(invoke, args, message, client):
    yield from client.send_message(message.channel, "Pong!")
    return
