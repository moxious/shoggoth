import os
from pydiscourse import DiscourseClient
from datetime import date, timedelta

def topics_with_single_post(topics):
    return [
        topic for topic in topics
        if topic['posts_count'] == 1
    ]

class Topic:
    def __init__(self, data):
        self.data = data
    
    def get_link(self):
        return os.environ['DISCOURSE_URL'] + 't/%s/%s' % (self.data['slug'], self.data['id'])

    def get_head_content(self):
        top_post = self.get_posts()[0]
        return {
            "url": self.get_link(),
            "id": self.data['id'],
            "slug": self.data['slug'],
            "title": self.data['title'],
            "content": top_post['cooked'],
        }

    def __dict__(self):
        return self.data

    def tags(self): 
        return self.data['tags']

    def is_tagged(self): 
        return len(self.tags()) > 0

    def has_replies(self):
        return self.data['posts_count'] > 1

    def get_posts(self):
        return self.data['post_stream']['posts']

class CommunitySupport():
    def __init__(self):
        # https://discourse.readthedocs.io/en/latest/
        # Bad bad bad docs though.
        self.client = DiscourseClient(
            os.environ['DISCOURSE_URL'],
            api_username=os.environ['DISCOURSE_USERNAME'],
            api_key=os.environ['DISCOURSE_API_KEY'])
        
    """Naive method to extract a slug and ID from a web link"""
    def parse_link(self, link):
        from urllib.parse import urlparse
        url = urlparse(link)
        # https://community.grafana.com/t/i-would-like-to-use-the-status-history-feature-but-the-results-are-overlapping/86154
        path = url.path
        
        if not path.startswith('/t/'):
            raise Exception('Invalid link')
        
        [slug, id] = path[3:].split('/')
        return { "slug": slug, "id": id }

    def get_topic_for_link(self, link):
        bits = self.parse_link(link)
        return Topic(self.client.topic(slug=bits['slug'], topic_id=bits['id']))

    """Search for posts that match a particular string"""
    def search(self, q='', page=1, recent_only=True, no_replies=True):
        search_string = q
        if no_replies:
            search_string = search_string + " min_posts:1 max_posts:1"
        if recent_only:
            search_string = search_string + " after:%s" % str(date.today() - timedelta(days=4))

        # https://community.grafana.com/search?q=after%3A2023-04-20%20min_posts%3A1%20max_posts%3A1&page=1
        response = self.client.search(term='', q=search_string, page=page)
        return self.post_generator(response['posts'])        

    def post_generator(self, list):
        """Async calls to client.post take time so we implement this as a generator"""
        idx = 0
        while idx < len(list):
            current = list[idx]
            ks = sorted(current.keys())
            
            print(ks)
            yield Topic(self.client.post(post_id=current['id'], topic_id=current['topic_id']))
            idx += 1

    def topic_generator(self, list):
        """Async calls to client.post take time so we implement this as a generator"""
        idx = 0
        while idx < len(list):
            current = list[idx]
            yield Topic(self.client.topic(topic_id=current['id'], slug=current['slug']))
            idx += 1

    def latest_topics(self):
        response = self.client.latest_topics()
        return self.topic_generator(response['topic_list']['topics'])