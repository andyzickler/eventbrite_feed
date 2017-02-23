#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler

from eventbritefeed.client import EventbriteClient


# HTTPRequestHandler class
class EventbriteFeedRequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        client = EventbriteClient()
        result = client.get_feed()

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'application/atom+xml')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(result)
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