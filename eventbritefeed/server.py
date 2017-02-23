#!/usr/bin/env python
import posixpath
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

from eventbritefeed.client import EventbriteClient


# HTTPRequestHandler class
class EventbriteFeedRequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        org = self._get_org_id()
        client = EventbriteClient()
        result = client.get_feed(org)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'application/atom+xml')
        self.end_headers()

        # Write content as utf-8 data
        # self.wfile.write(bytes('hello!', 'utf-8'))
        self.wfile.write(result)
        return

    def _get_org_id(self):
        return self.path_array[0]

    @property
    def path_array(self):
        head = posixpath.normpath(urlparse(self.path).path)
        result = []
        while head != "/":
            (head, tail) = posixpath.split(head)
            result.insert(0, tail)
        return result


class EventbriteFeedHTTPServer(HTTPServer):
    def __init__(self, server_address):
        super(EventbriteFeedHTTPServer, self).__init__(server_address, EventbriteFeedRequestHandler)

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
