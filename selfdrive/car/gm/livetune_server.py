#!/usr/bin/env python3
import threading
from wsgiref.simple_server import WSGIServer, make_server
#import json

# POC / example web service for live tuning
# TODO: auth, use an existing restful library
# TODO: make the code not suck

exampleResp = b"{\"minEnableSpeed\": 0, \"steerRatio\": 15.2}"

started = False
httpd : WSGIServer
th : threading.Thread

def app(environ, start_response):
    # if environ['REQUEST_METHOD'] == 'POST':
    #     start_response('200 OK', [('Content-Type', 'text/json')])
    #     return [b'']
    start_response('200 OK', [('Content-Type', 'text/json')])
    return [exampleResp]

def launch_listener_async():
    if (started):
        return
    th = threading.Thread(target=_launch_listener)
    th.start()

def _launch_listener():
    #TODO: error handling, etc
    httpd = make_server('', 8282, app)
    httpd.serve_forever()



# if __name__ == '__main__':
#     try:        
#         launch_listener()
#         print('Serving on port 8282...')
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         print('Goodbye.')
