import requests

from eventbritefeed.feed import EventbriteFeedGenerator


class EventbriteClient(object):


    def get_feed(self):
        session = requests.Session()

        events = []

        first_url = 'https://www.eventbrite.com/org/:orgID/showmore/?type=future&page=1'
        second_url = 'https://www.eventbrite.com/org/:orgID/showmore/?type=future&page=2'
        r = session.get(first_url)
        first_data = r.json()['data']
        r = session.get(second_url)
        second_data = r.json()['data']

        events.extend(first_data['events'])
        events.extend(second_data['events'])

        ebf = EventbriteFeedGenerator(events)
        return ebf.atom_str(pretty=True)
