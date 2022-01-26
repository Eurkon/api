# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/15 11:31

from api.index import Handler
from http.server import HTTPServer

if __name__ == '__main__':
    try:
        server = HTTPServer(('localhost', 8888), Handler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()
