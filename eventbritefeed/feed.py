from feedgen.feed import FeedGenerator, FeedEntry


class EventbriteFeedGenerator(FeedGenerator):
    """
    Class that takes a converts a list of events and generates a feed
    """

    def __init__(self, events):
        super(EventbriteFeedGenerator, self).__init__()
        self.events = events
        self.id(events[0]['organizer']['id'])
        self.title("Eventbrite: {}".format(events[0]['organizer']['name']))
        self.logo(events[0]['organizer']['logo']['url'])
        self.author(name=events[0]['organizer']['name'])
        self.link(href=events[0]['organizer']['url'], rel='via')

        for event in events:
            self.add_entry(EventbriteFeedEntry(event))


class EventbriteFeedEntry(FeedEntry):
    """
    Builds a FeedEntry from an Event
    """
    def __init__(self, event):
        super(EventbriteFeedEntry, self).__init__()
        self.id(event['url'])
        self.title(event['name']['text'])
        self.content(EventbriteFeedEntry._event_html(event), type='html')
        self.link(href=event['url'], rel='via')
        self.published(event['start']['utc'])
        self.updated(event['start']['utc'])

    @staticmethod
    def _event_html(event):
        """Return event html with the logo prepended"""
        img_html = u'<img src="{}"></img>'.format(event['logo']['url'])
        event_html = u'{}\n{}'.format(img_html, event['description']['html'])
        return event_html

