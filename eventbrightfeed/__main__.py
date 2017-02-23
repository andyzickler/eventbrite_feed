from http.server import HTTPServer

from eventbrightfeed.server import EventBrightFeedRequestHandler

def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 3000)
    httpd = HTTPServer(server_address, EventBrightFeedRequestHandler)
    print('running server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()