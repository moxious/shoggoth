import os, sys, json, random, argparse
from dotenv import load_dotenv
from shoggoth import Shoggoth, ShoggothReponse
from discourse import CommunitySupport, Topic

# Take what's in .env -> os.environ
load_dotenv()

argParser = argparse.ArgumentParser()
argParser.add_argument("-t", "--topic", help="Discourse topic link")
argParser.add_argument("-s", "--search", help="Search term")
argParser.add_argument("-l", "--replies", help="Whether or not to process topics with replies (defaults false)", default=False, action=argparse.BooleanOptionalAction)
argParser.add_argument("-u", "--tags", help="Whether or not to process topics with tags (defaults false)", default=False, action=argparse.BooleanOptionalAction)
argParser.add_argument("-e", "--embeddings", help="Use embeddings mode", action=argparse.BooleanOptionalAction)

args = argParser.parse_args()
print(args)
cs = CommunitySupport()

# Run mode is responsible for setting a set of topics in an array
# [].  The shoggoth will then process the array.
if args.topic:
    topic = cs.get_topic_for_link(args.topic)
    # This flag overrides the others
    args.tags = True
    args.replies = True
    topics = [topic]
elif args.search:
    topics = cs.search(args.search)
else:
    topics = cs.latest_topics()

shoggy = Shoggoth()
    
processed = 0
for topic in topics:
    # Evaluate filters of whether or not we should process this post.
    if not args.replies and topic.has_replies():
        # Skip those with replies.
        print("Skipping for replies")
        continue

    if not args.tags and topic.is_tagged():
        print("Skipping for tags")
        continue

    processed += 1 

    if args.embeddings:
        resp = shoggy.get_embedding(topic.get_fulltext())
        print(json.dumps(resp.response, indent=2))
    else:
        print(shoggy.run(Shoggoth.TAG_JSON, topic.get_head_content()))
        print("\n\n```\n%s\n```\n\n" % json.dumps(topic.get_head_content(), indent=2))

print("Total processed: %d" % processed)
