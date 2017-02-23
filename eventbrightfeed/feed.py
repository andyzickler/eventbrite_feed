from feedgen.feed import FeedGenerator
# import dateutil.parser


class EventBrightFeedGenerator(FeedGenerator):
    """
    Class that takes a converts a list of events and generates a feed
    """

    def __init__(self, events):
        super(EventBrightFeedGenerator, self).__init__()
        self.events = events
        self.id(events[0]['organizer']['id'])
        self.title("Eventbrite: {}".format(events[0]['organizer']['name']))
        self.logo(events[0]['organizer']['logo']['url'])
        self.author(name=events[0]['organizer']['name'])
        self.link(href=events[0]['organizer']['url'], rel='via')

        for event in events:
            feed_entry = self.add_entry()
            feed_entry.id(event['url'])
            feed_entry.title(event['name']['text'])
            feed_entry.content(EventBrightFeedGenerator._event_html(event), type='html')
            feed_entry.link(href=event['url'], rel='via')
            feed_entry.published(event['start']['utc'])
            feed_entry.updated(event['start']['utc'])
            # feed_entry.published(dateutil.parser.parse(event['start']['utc']))

    @staticmethod
    def _event_html(event):
        """Return event html with the logo prepended"""
        img_html = u'<img src="{}"></img>'.format(event['logo']['url'])
        event_html = u'{}\n{}'.format(img_html, event['description']['html'])
        return event_html
