# Discord.py Youtube Bot

## Setup

#### Requirements
* Google Developer Account
* A Google Project
* Google Youtube API 
* Python

#### Required Python Modules
* [discord.py]("https://discordpy.readthedocs.io/en/stable/")
* [discord_slash]("https://discord-py-slash-command.readthedocs.io/en/latest/quickstart.html")
* [urllib.parse]("https://docs.python.org/3/library/urllib.parse.html")
* [googleapiclient]("https://cloud.google.com/ai-platform/prediction/docs/python-client-library")

## Instructions

#### To run this project you will need to access google developer console.
#### In the google developer console find the api section then add the Youtube Api.
#### Once you have added the api take care of any nessassary credential or api management. Be sure to get a api to your project.
#### Open Up the project files and search for references of the api_key variable, then replace the api_key variable with your api key.

## Using Google API Example

#### Example
```python
from googleapiclient.discovery import build

API_KEY = 'YOUR API KEY HERE'

def build(name, version, key):
    api = build(name, version, developer_key=key)
    return build
build('youtube', 'v3', API_KEY)

```
