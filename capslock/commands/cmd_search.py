# Search Command
from urllib.parse import urlencode


def ex(invoke, args, message, client):
    if len(args) > 0:
        sub_invoke = args[0].__str__()[0:].replace("'", "")
        print(sub_invoke, ' ', args)
        # Search on the Python Docs
        if sub_invoke in ('python', 'pyh'):
            url = ("https://docs.python.org/3/search.html?{}"
                   "&check_keywords=yes&area=default".format(urlencode({'q': ' '.join(args[1:len(args)])})))
            yield from client.send_message(message.channel, url)
        elif sub_invoke in ('msdm', 'microsoft'):
            url = ("https://social.msdn.microsoft.com/Search/en-US?q=if"
                   "&pgArea=header&emptyWatermark=true&query={}&ac=2".format(urlencode({'q': ' '.join(args[1:len(args)])})))
            yield from client.send_message(message.channel, url)
    else:
        yield from client.send_message(message.author, '%s is missing args!' % (invoke))
