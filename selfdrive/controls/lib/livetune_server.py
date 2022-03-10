#!/usr/bin/env python3
import threading
from wsgiref.simple_server import WSGIServer, make_server

#from cereal import car
import json

# POC / example web service for live tuning
# TODO: auth, use an existing restful library
# TODO: make the code not suck
# TODO: not using a class here makes me feel kinda sick...

httpd : WSGIServer
th : threading.Thread
global _CP
# TODO: May need to do this the right way and create a service with events to be reacted to...

def app(environ, start_response):
    global _CP
    if _CP is None:
        start_response('200 OK', [('Content-Type', 'text/json')])
        return [b"Whoopsie no _CP"]
    # if environ['REQUEST_METHOD'] == 'POST':
    #     start_response('200 OK', [('Content-Type', 'text/json')])
    #     return [b'']
    data = json.dumps(_CP)
    start_response('200 OK', [('Content-Type', 'text/json')])
    return [data.encode()]

def launch_listener_async(CP):
    global _CP
    #if (httpd is not None):
    #    return
    #started = True
    _CP = CP
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
