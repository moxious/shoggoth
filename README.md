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
pip install pydiscourse
```

- Set up API keys and customize contents of `.env` (requires paid OpenAI API key & discourse key)

```
cp .env.template .env
```

## Run

```
python index.py
```

## Sample Output

```
$ python3 index.py 
https://community.grafana.com/t/merging-results-of-multiple-queries-into-table-use-label-values-as-columns/85986

{'topic_html_title': 'Merging results of multiple queries into table (Use label values as columns)', 'cooked': '<p>I managed to resolve it myself.</p>\n<p>Starting point<br>\nTable panel with 2 queries that have identical set of labels.  1 label contains values that you want to have as columns (env = dev / qa / …)</p>\n<p>Add transformations</p>\n<p>Merge Transformation : all the actual values are stored as Value <span class="hashtag">#A</span>, <span class="hashtag">#B</span>, …<br>\nAdd field from calculation : Reduce Row … Select the Value#A <span class="hashtag">#B</span> fields and calculate the Total<br>\nGrouping to Matrix : Column = env, Row= <strong>name</strong> Cell Value = Total</p>'}

['Grafana', 'dashboards', 'transformations']
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
