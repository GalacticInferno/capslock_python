# Search Command
from urllib.parse import urlencode


def serach_dictonary(message, args, client):
    url = ("http://www.dictionary.com/browse/{}".format(urlencode({'q':
           ' '.join(args[1:len(args)])})))
    yield from client.send_message(message.channel, url)
    return


def search_github(message, args, client):
    url = ("https://github.com/search?utf8=%E2%9C%93&{}"
           "&ref=simplesearch".format(urlencode({'q':
           ' '.join(args[1:len(args)])})))
    yield from client.send_message(message.channel, url)
    return


def search_python(message, args, client):
    url = ("https://docs.python.org/3/search.html?{}"
           "&check_keywords=yes&area=default".format(urlencode({'q':
           ' '.join(args[1:len(args)])})))
    yield from client.send_message(message.channel, url)
    return


def search_msdm(message, args, client):
    url = ("https://social.msdn.microsoft.com/Search/en-US?q=if"
           "&pgArea=header&emptyWatermark=true&query={}&ac=2"
           .format(urlencode({'q': ' '.join(args[1:len(args)])})))
    yield from client.send_message(message.channel, url)
    return


search_list = {
    'dic': serach_dictonary,
    'github': search_github,
    'python': search_python,
    'msdm': search_msdm
}


def ex(invoke, args, message, client):
    if len(args) > 0:
        sub_invoke = args[0].__str__()[0:].replace("'", "")
        print(sub_invoke, ' ', args)
        if search_list.__contains__(sub_invoke):
            yield from search_list.get(sub_invoke)(message, args, client)
        else:
            yield from client.send_message(message.channel,
                "I've yet to read that myself!")
            yield from client.send_message(message.channel,
                "Why dont you try looking at %s" % ('http://devdocs.io/'))
    else:
        yield from client.send_message(message.author,
            '%s is missing args!' % (invoke))
    return
