import os, sys, json, random, argparse
from dotenv import load_dotenv
from shoggoth import Shoggoth, ShoggothReponse
from discourse import CommunitySupport, Topic

# Take what's in .env -> os.environ
load_dotenv()

argParser = argparse.ArgumentParser()
argParser.add_argument("-t", "--topic", help="Discourse topic link")

args = argParser.parse_args()
print("args=%s" % args)

cs = CommunitySupport()

if args.topic:
    bits = cs.parse_link(args.topic)
    print(bits)
    sys.exit(0)
else:
    topics = cs.latest_topics_no_replies()
    topic = topics[0]
    print(topic.get_head_content())
    print(topic.get_link())

shoggy = Shoggoth()
print(shoggy.run(Shoggoth.TAG_JSON, topic.get_head_content()))

