import tornado.ioloop
import tornado.web
import tornado.gen

import os.path


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.database = db

    def get(self):
        items = ['item1', 'item2', 'item3']
        self.render('index.html', title='my server', items=items)


class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        raise tornado.web.HTTPError(403)

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

app = tornado.web.Application([
    (r"/", MainHandler, dict(db='mysql')),
    (r"/admin", AdminHandler),
], **settings)

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
