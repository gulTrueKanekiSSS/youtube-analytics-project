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