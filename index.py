import openai
import os
import random
import json
from dotenv import load_dotenv
from shoggoth import Shoggoth, ShoggothReponse
from fluent_discourse import Discourse
from discourse import top_level_posts, link_for_post, content_only

# Take what's in .env -> os.environ
load_dotenv()

client = Discourse.from_env(raise_for_rate_limit=False)
response = client.posts.json.get()

# No replies, they tend to be partial and missing context.
posts = top_level_posts(response['latest_posts'])

# Save latest batch for inspection
with open(".latest_posts.json", "w") as f:
    f.write(json.dumps(posts, indent = 4))

# Select a random post
post = posts[random.randint(0, len(posts))]

print(link_for_post(post))

# Don't need all of the meta information about the post, just title/content.
# The robot doesn't need the user's ID and avatar to tag a post
filtered = { key: post[key] for key in post.keys() & {'topic_html_title', 'cooked'} }

print(str(content_only(post)))

shoggy = Shoggoth()
print(shoggy.run(Shoggoth.TAG_JSON, content_only(post)))

