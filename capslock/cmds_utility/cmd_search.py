# Search Command
from urllib.parse import urlencode

python_alias = {
    "python",
    "pyh"
}

msdm_alias = {
    "msdm",
    "microsoft"
}


def ex(invoke, args, message, client):
    if len(args) > 0:
        sub_invoke = args[0].__str__()[0:].replace("'", "")
        print(sub_invoke, ' ', args)
        if sub_invoke in python_alias:
            url = ("https://docs.python.org/3/search.html?{}"
                   "&check_keywords=yes&area=default".format(urlencode({'q':
                   ' '.join(args[1:len(args)])})))
            yield from client.send_message(message.channel, url)
        elif sub_invoke in msdm_alias:
            url = ("https://social.msdn.microsoft.com/Search/en-US?q=if"
                   "&pgArea=header&emptyWatermark=true&query={}&ac=2"
                   .format(urlencode({'q': ' '.join(args[1:len(args)])})))
            yield from client.send_message(message.channel, url)
        else:
            yield from client.send_message(message.channel,
                "I've yet to read that myself!")
            yield from client.send_message(message.channel,
                "Why dont you try looking at %s" % ('http://devdocs.io/'))
    else:
        yield from client.send_message(message.author,
            '%s is missing args!' % (invoke))
    return
