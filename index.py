import openai
import os
from dotenv import load_dotenv
from shoggoth import Shoggoth, ShoggothReponse
from fluent_discourse import Discourse

# Take what's in .env -> os.environ
load_dotenv()

client = Discourse.from_env(raise_for_rate_limit=False)
latest = client.posts.json.get()

post = latest['latest_posts'][0]

# Don't need all of the meta information about the post, just title/content.
# The robot doesn't need the user's ID and avatar to tag a post
filtered = { key: post[key] for key in post.keys() & {'topic_html_title', 'cooked'} }

# OpenAI wants text prompts, so careful to coerce JSON -> str.
shoggy = Shoggoth()
print(shoggy.run(Shoggoth.TAG_JSON, str(filtered)))

