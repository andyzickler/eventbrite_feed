import operator
import requests

from cachetools import TTLCache, cachedmethod
from eventbritefeed.feed import EventbriteFeedGenerator


class EventbriteClient(object):
    url_template = 'https://www.eventbrite.com/org/{}/showmore/?type=future&page={}'

    def __init__(self):
        self.session = requests.Session()
        self.cache = TTLCache(maxsize=20, ttl=600)

    @cachedmethod(operator.attrgetter('cache'))
    def _get_all_events(self, org):
        events = []
        page_num = 1
        url = self._get_url(org, page_num)
        result = self.session.get(url)
        data = result.json()['data']
        events.extend(data['events'])

        while data.get('has_next_page') is True:
            page_num += 1
            url = self._get_url(org, page_num)
            result = self.session.get(url)
            data = result.json()['data']
            events.extend(data['events'])

        return events

    def _get_url(self, org, page):
        return self.url_template.format(org, page)

    def get_feed(self, org):
        events = self._get_all_events(org)

        ebf = EventbriteFeedGenerator(events)
        return ebf.atom_str(pretty=True)
