import tornado.gen
import tornado.httpclient
import tornado.ioloop
import tornado.web
import sys

from HTMLParser import HTMLParser

base_url = 'http://yandex.ru'

reload(sys)
sys.setdefaultencoding('utf-8')


@tornado.gen.coroutine
def main():
    class NewsParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            d = dict(attrs)
            href = d.get('href')
            label = d.get('aria-label')
            if href and label and tag == 'a' and 'news.yandex.ru' in href:
                print label + " - " + href

    response = yield tornado.httpclient.AsyncHTTPClient().fetch(base_url)
    html = response.body if isinstance(response.body, str) \
        else response.body.decode()
    parser = NewsParser()
    parser.feed(html)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().run_sync(main)
