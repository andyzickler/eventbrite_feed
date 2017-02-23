from feedgen.feed import FeedGenerator
# import dateutil.parser


class EventBrightFeed(object):
    """
    Class that takes a converts a list of events and generates a feed
    """

    def __init__(self, events):
        self.events = events
        self.feed_generator = FeedGenerator()
        self.feed_generator.id(events[0]['organizer']['id'])
        self.feed_generator.title("Eventbrite: {}".format(events[0]['organizer']['name']))
        self.feed_generator.logo(events[0]['organizer']['logo']['url'])
        self.feed_generator.author(name=events[0]['organizer']['name'])
        self.feed_generator.link(href=events[0]['organizer']['url'], rel='via')

        for event in events:
            feed_entry = self.feed_generator.add_entry()
            feed_entry.id(event['url'])
            feed_entry.title(event['name']['text'])
            feed_entry.content(EventBrightFeed._event_html(event), type='html')
            feed_entry.link(href=event['url'], rel='via')
            feed_entry.published(event['start']['utc'])
            feed_entry.updated(event['start']['utc'])
            # feed_entry.published(dateutil.parser.parse(event['start']['utc']))

    def get_atom(self):
        return self.feed_generator.atom_str(pretty=True)

    @staticmethod
    def _event_html(event):
        """Return event html with the logo prepended"""
        img_html = u'<img src="{}"></img>'.format(event['logo']['url'])
        event_html = u'{}\n{}'.format(img_html, event['description']['html'])
        return event_html
