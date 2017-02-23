import os
from eventbritefeed.server import EventbriteFeedHTTPServer

def run():
    port = os.getenv('EBF_PORT', 3011)
    address = os.getenv('EBF_ADDRESS', '127.0.0.1')
    print('starting server... Listening on {}:{}'.format(address, port))
    httpd = EventbriteFeedHTTPServer((address, port))
    print('running server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
