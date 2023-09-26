import os
import json
from dotenv import load_dotenv
from googleapiclient.discovery import build


load_dotenv()

api_key = os.getenv('YOUTUBE_API_KEY')
print(api_key)
youtube = build('youtube', 'v3', developerKey=api_key)


def pjson(data: dict) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))

def object_to_dict(object):
    fields = dict()
    fields.update(object.__class__.__dict__)
    fields.update(object.__dict__)

    fields = dict(filter(lambda x: not x[0].startswith('_'), fields.items()))

    new_fields = dict()
    for k, v in fields.items():
        if hasattr(v, '__dict__'):
            v = object_to_dict(v)

        new_fields[k] = v

    return new_fields
