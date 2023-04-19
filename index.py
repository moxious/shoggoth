import openai
import os
import random
import json
from dotenv import load_dotenv
from shoggoth import Shoggoth, ShoggothReponse
from fluent_discourse import Discourse

# Take what's in .env -> os.environ
load_dotenv()

client = Discourse.from_env(raise_for_rate_limit=False)
response = client.posts.json.get()

# Filter posts, only top level, no replies.
posts = [ x for x in response['latest_posts'] if not 'reply_to_user' in x ]

# Save latest batch for inspection
with open(".latest_posts.json", "w") as f:
    f.write(json.dumps(posts, indent = 4))

# Select a random post
post = posts[random.randint(0, len(posts))]

link = os.environ['DISCOURSE_URL'] + 't/%s/%s' % (post['topic_slug'], post['topic_id'])
print(link)

# Don't need all of the meta information about the post, just title/content.
# The robot doesn't need the user's ID and avatar to tag a post
filtered = { key: post[key] for key in post.keys() & {'topic_html_title', 'cooked'} }

print(str(filtered))

# OpenAI wants text prompts, so careful to coerce JSON -> str.
shoggy = Shoggoth()
print(shoggy.run(Shoggoth.TAG_JSON, str(filtered)))

