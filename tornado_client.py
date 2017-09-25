import tornado.gen
import tornado.httpclient
import tornado.ioloop
import tornado.web
import sys
import urlparse

from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding('utf-8')


class News:
    def __init__(self, link, text):
        self.link = link
        self.text = text

    def __str__(self):
        return '{} ({})'.format(self.text, self.link)


class YandexNewsParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.news = []
        self.news_url = 'news.yandex.ru'

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        href = d.get('href')
        label = d.get('aria-label')
        if href and label and tag == 'a' and self.news_url in href:
            link = urlparse.urlparse(href)
            query = dict([x.split('=') for x in link.query.split('&')])
            data = list(urlparse.urlparse(query['cl4url']))
            if not data[0]:
                data[0] = 'http'
            url = urlparse.urlunparse(data)
            self.news.append(News(url, label))

    # def news(self):
    #     return self.news


@tornado.gen.coroutine
def main():
    yandex_url = 'http://yandex.ru'
    response = yield tornado.httpclient.AsyncHTTPClient().fetch(yandex_url)
    html = response.body if isinstance(response.body, str) \
        else response.body.decode()
    parser = YandexNewsParser()
    parser.feed(html)
    for news in parser.news:
        print news

if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().run_sync(main)
