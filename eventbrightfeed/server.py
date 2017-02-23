#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler
import requests

from .feed import EventBrightFeedGenerator


# HTTPRequestHandler class
class EventBrightFeedRequestHandler(BaseHTTPRequestHandler):

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

        ebf = EventBrightFeedGenerator(events)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'application/atom+xml')
        self.end_headers()

        # Write content as utf-8 data
        # self.wfile.write(bytes(message, "utf8"))
        self.wfile.write(ebf.atom_str(pretty=True))
        return


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
