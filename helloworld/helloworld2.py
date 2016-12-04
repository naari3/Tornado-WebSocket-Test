# -*- coding: utf-8 -*-
import os
import time

from pypugjs.ext.tornado import patch_tornado

import tornado.ioloop
import tornado.web

from tornado import template

patch_tornado()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.pug", nowtime=time.time())


application = tornado.web.Application([
    (r"/", MainHandler),
    ],
    template_path=os.path.join(os.getcwd(), "templates"),
    static_path=os.path.join(os.getcwd(), "static"),
)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
