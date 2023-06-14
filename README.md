# Shoggoth

## What is this?

A CLI tool for auto-tagging and categorization of community posts on [discourse](https://community.grafana.com/)

This simple demo:

1. Loads the latest post from Discourse
2. Cuts it down to title/content only
3. Feeds it into OpenAI with a **prime directive** to read the post
and categorize it according to common topics and product lines.

## Setup

```
pip3 install openai 
pip3 install pydiscourse
pip3 install pandas
```

- Set up API keys and customize contents of `.env` (requires paid OpenAI API key & discourse key)

```
cp .env.template .env
```

## Run

`python index.py --help` for information.

### Latest Posts

In the simplest run mode it will check for the latest posts that are untagged with no replies, and process them.

```
python index.py
```

### A specific post

Provide a full link

```
python index.py --topic https://community.grafana.com/t/trying-to-setup-a-grafana-deployment-in-kubernetes-cluster/86306
```

### A Search Term

```
python index.py --search Exception 
```

## Sample Output

```
## Recommendations: Trying to setup a grafana deployment in kubernetes cluster

- URL: https://community.grafana.com/t/trying-to-setup-a-grafana-deployment-in-kubernetes-cluster/86306
- Tags: kubernetes, deployment, liveness-probe, readiness-probe, container, monitoring
- Summary: The user is trying to deploy Grafana on a Kubernetes cluster, but is having issues with liveness probe, and readiness probe errors.
- Friendly: Yes
- Concern: No
- Notes: The deployment and service YAML files seem fine as per the official Grafana documentation. Since there are errors in the livenessProbe and readinessProbe section, review the configuration related to these probes, especially the TCP socket's port. It looks like a port issue since the connection is refused on port 3000. Also, ask the
```

## Wait What?  How does this work?

* With the OpenAI API, the "prompt" you give it is JSON of the post, much like ChatGPT.
* But the API lets you give "system level prompts" before the "user level prompts"
* These system level prompts are what I'm calling 'the prime directive'.
* Check the static variables in `shoggoth.py` for "how to tell the robot what to do".

What the OpenAI API sees, is something like this:

```
{ 
    "messages": [
        { "role": "system", "message": "Give me joke answers only, always with ;)" },
        { "role": "user", "message": "What's 2+2?" }
    ]
}
```

The API would probably respond to this with something like, 

> "It's pi, lol ;)"

We use these system directives to give it a mini-tutorial about our domain, so that it "knows how to read the post".

## Next Steps (Hypothetically)

1. The **prime directive** is not good, it's basic and naive, and could really use some work.
2. Test that we trust the output
3. (Eventually) wire it to a bot account on discourse that modifies 
posts with suggested tags _when the user hasn't tagged it themselves_.
