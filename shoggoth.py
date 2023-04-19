import openai
import os

"""
Just a wrapper object so the caller doesn't have to deal
with OpenAI response formats for now.
"""
class ShoggothReponse:
    def __init__(self, obj):
        self.response = obj
    
    def __str__(self):
        return self.response.choices[0].message.content

DEFAULT_MODEL = 'gpt-3.5-turbo'

"""
Core object that wraps OpenAPI API and makes it easy to
just give a Discourse post, and return a tag set.
"""
class Shoggoth:    
    TAG_JSON = {
        "system_messages": [
            {
                "role": "system",
                "content": """
                    You will tag a user input that is expressed in JSON format.
                    The post will relate to the Grafana software platform, which
                    contains the following products, which each relate to an 
                    area of functionality.  Each term is a tag, what is in the
                    parentheses describes what that tag covers.

                    - Grafana (dashboarding)
                    - Loki (logging)
                    - Mimir (prometheus and metrics)
                    - OnCall (incident response monitoring, or IRM)
                    - K6 (software load testing, browser testing)
                    - Pyroscope (continuous profiling of code)
                    - Phlare (continuous profiling of code)

                    Additional common topics include:

                    - dashboards (which include common panels and visualization types)
                    - plugins
                    - datasource (connections to remote data sources)
                    - transformations
                    - Auth (Authentication and authorization issues)
                    - Any of the 3 cloud providers (Azure, GCP, and AWS)
                    - Infrastructure (infra observability)
                    - App (application observability)

                    Tag the input according to the list above, if the question or issue
                    is primarily about that topic.  Do not tag it to a topic if
                    the topic in question is just mentioned in passing, such as 
                    in an example.  The "Grafana" tag is very broad, so do not use it unless
                    the post is about core dashboarding and Grafana functionality.

                    You may assign up to 3 tags.  Emit your response as a python list.
                """
            }
        ]
    }

    SENTIMENT_JSON = {
        "system_messages": [
            {
                "role": "system",
                "content": """
                    You will classify the emotional sentiment of a post formatted
                    in JSON.  Input text within the JSON may contain HTML, and
                    you are expected to understand its format and meaning.

                    You may answer positive, negative, or neutral.

                    Provide reasons for your judgements, cite examples.
                """
            }
        ]
    }

    def __init__(self):
        openai.api_key = os.environ['OPENAI_API_KEY']

    def run(self, command, input, model=DEFAULT_MODEL):
        response = openai.ChatCompletion.create(
            model=model,
            messages=command['system_messages'] + [
                { "role": "user", "content": input }
            ])
        
        return ShoggothReponse(response)



