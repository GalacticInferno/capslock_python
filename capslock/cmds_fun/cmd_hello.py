import os
import random

script_dir = os.path.dirname(__file__)
rel_path = "data_fun/hello_response.txt"
abs_file_path = os.path.join(script_dir, rel_path)


def ex(invoke, args, message, client):
    if os.path.isfile(abs_file_path):
        with open(abs_file_path) as f:
            lines = f.readlines()
            rand_line = is_comment(lines)
            print(rand_line)
            yield from client.send_message(message.channel,
                rand_line.format(message.author))
    else:
        print('No such file or directory [Errno 2]')
    return


def is_comment(_lines):
    while True:
        rand_line = random.choice(_lines)
        if not rand_line.startswith('#'):
            break
    return rand_line
