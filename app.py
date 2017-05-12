# -*- coding: utf-8 -*-
import os
import random

from pypugjs.ext.tornado import patch_tornado

import tornado.httpserver
import tornado.ioloop
from tornado import template
import tornado.web
import tornado.websocket
from tornado.web import url

patch_tornado()

from janome.tokenizer import Tokenizer
import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.pug")


class TokenizeHandler(tornado.websocket.WebSocketHandler):

    users = set()
    messages = []

    def open(self):
        self.users.add(self)
        print('Session opened by {}'.format(self.request.remote_ip))
        for message in self.messages:
            self.write_message(message)

    def on_message(self, message):
        message = json.loads(message)
        if message["text"]:
            t = Tokenizer()
            tokens = t.tokenize(message["text"])
            message["text"] = ""
            for token in tokens:
                message["text"] += "{} ".format(token.surface)
            for user in self.users:
                user.write_message(message)
            self.messages.append(message)
            while len(self.messages) > 20:
                self.messages = self.messages[1:-1]

    def on_close(self):
        self.users.remove(self)
        print('Session closed by {}'.format(self.request.remote_ip))

class Application(tornado.web.Application):
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        handlers = [
            url(r'/', IndexHandler, name='index'),
            url(r'/tokenize', TokenizeHandler, name='tokenize'),
        ]
        settings = dict(
            template_path=os.path.join(BASE_DIR, 'templates'),
            static_path=os.path.join(BASE_DIR, 'static'),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
