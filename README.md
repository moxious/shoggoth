# Shoggoth

## What is this?

A quick demo showing ChatGPT auto-tagging of posts on discourse.

This simple demo:

1. Loads the latest post from Discourse
2. Cuts it down to title/content only
3. Feeds it into ChatGPT with a **prime directive** to read the post
and categorize it according to common topics and product lines.

## Setup

```
pip3 install openai 
pip install fluent-discourse
```

- Set up API keys and customize contents of `.env` (requires paid OpenAI API key & discourse key)

```
cp .env.template .env
```

## Run

```
python index.py
```

## Next Steps (Hypothetically)

1. The **prime directive** is not good, it's basic and naive, and could really use some work.
2. Test that we trust the output
3. (Eventually) wire it to a bot account on discourse that modifies 
posts with suggested tags _when the user hasn't tagged it themselves_.
