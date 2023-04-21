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
    
    print("Got %d topics" % len(topics))

    shoggy = Shoggoth()
    
    for topic in topics:
        print ("```\n%s\n```\n\n" % json.dumps(topic.get_head_content(), indent=2))
        print(shoggy.run(Shoggoth.TAG_JSON, topic.get_head_content()))

