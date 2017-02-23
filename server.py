#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from event_bright_feed import EventBrightFeed
import requests


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        session = requests.Session()

        events = []

        first_url = 'https://www.eventbrite.com/org/:orgID/showmore/?type=future&page=1'
        second_url = 'https://www.eventbrite.com/org/:orgID/showmore/?type=future&page=2'
        r = session.get(first_url)
        first_data = r.json()['data']
        r = session.get(second_url)
        second_data = r.json()['data']

        # soup = BeautifulSoup(data, 'html.parser')

        events.extend(first_data['events'])
        events.extend(second_data['events'])

        ebf = EventBrightFeed(events)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'application/atom+xml')
        self.end_headers()

        # Write content as utf-8 data
        # self.wfile.write(bytes(message, "utf8"))
        self.wfile.write(ebf.get_atom())
        return


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 3000)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()

# HTTPRequestHandler only deals with HTTP and the EvenBrightFeelController
# EventBrightClient 
# - dif updates of cache
# EvenBrightFeedController -> returns 
# 
# 
# class EventbriteEvent
# class EventBriteFeed 
# class EventBriteClient - queries event brite, returns EventBriteFeed
# class resourceController(EventBriteClient) returns strings (xml, json, etc)
# class RequestHandler(resourceController)
# class server(options, requestHandler)
# 
# 