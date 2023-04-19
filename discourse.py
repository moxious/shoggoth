import os

"""Filter posts to only those that are not replies"""
def top_level_posts(posts):
    return [ 
        post for post in posts
        if (not 'reply_to_user' in post) and
           (post['post_number'] == 1)
    ]

"""Return the full link for a given post object."""
def link_for_post(post):
    return os.environ['DISCOURSE_URL'] + 't/%s/%s' % (post['topic_slug'], post['topic_id'])

"""Return a cut-down dict with topic & content only"""
def content_only(post):
    return {
        "title": post['topic_html_title'],
        "content": post['cooked']
    }
