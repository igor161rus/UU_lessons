from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        # for attr in attrs:
        #     print('->', attr[0], '>', attr[1])

    def handle_endtag(self, tag):
        print(tag)

    def handle_data(self, data):
        print(data.strip())


parser = MyHTMLParser()
parser.feed('''
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Parse me!</h1>
    </body>
</html>
''')
