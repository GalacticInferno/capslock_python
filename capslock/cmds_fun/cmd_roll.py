from random import randrange


def ex(invoke, args, message, client):
    if len(args) > 3:
        yield from client.send_message(message.channel, "Too many arguments!")
    elif len(args) > 0:
        die = args[0].__str__()[0:].replace("'", "")
        dice_mod = 0
        total_roll = 0
        if len(args) > 1:
            dice_mod = int(args[2].__str__()[0:].replace("'", ""))
        dice_amount = die.split("d", 1)[0]
        dice_type = int(die.split("d", 2)[1])
        print("Amount: %s\nType: %s" % (dice_amount, dice_type))
        for x in range(1, (int(dice_amount) + 1)):
            print("Rolling...")
            roll = randrange(1, (dice_type) + 1)
            print("Roll: %s" % (roll))
            total_roll = (roll + int(dice_mod) + total_roll)
            print("Current total: %s" % (total_roll))
        yield from client.send_message(message.channel,
            "Roll: %s" % (total_roll))
    else:
        yield from client.send_message(message.author,
            '%s is missing args!' % (invoke))
    return
