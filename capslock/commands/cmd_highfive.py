

def ex(invoke, args, message, client):
    msg = yield from client.send_message(message.channel, ':hand_splayed:')
    message = yield from client.wait_for_reaction(':hand_splayed:', message=msg)
    yield from client.send_message(message.channel, 'Hell ya!')
