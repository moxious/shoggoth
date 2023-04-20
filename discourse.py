import os
from pydiscourse import DiscourseClient

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

    def latest_topics_no_replies(self):
        response = self.client.latest_topics()        
        topics = topics_with_single_post(response['topic_list']['topics'])
        return [
            Topic(self.client.topic(topic_id=topic['id'], slug=topic['slug']))
            for topic in topics
            if topic['posts_count'] == 1
        ]
