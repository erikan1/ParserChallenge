from html.parser import HTMLParser

class HeadParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] in ['href', 'src', 'content']:
                print('{0}: {1}'.format(tag, attr[1]))


website = open("./head.html").read()
HeadParser().feed(website)
