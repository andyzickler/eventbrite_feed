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
        if org is None:
            # TODO: We need better error handling
            self.send_response(404)
            return
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
        if len(self.path_array) is not 2:
            return None
        org, org_id = self.path_array[:2]
        if org == 'org' and org_id is not None:
            return org_id
        return None

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
