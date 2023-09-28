from typing import Optional, Dict

from src.imp import pjson, youtube, object_to_dict


class Channel:
    """Класс для ютуб-канала"""

    __youtube_api = youtube

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self._channel = youtube.channels().list(id=self.get_channel_id, part='snippet,statistics').execute()

    def __get_items(self) -> Optional[Dict]:
        return self.print_info().get("items")[0]

    def __get_snippet(self) -> Optional[Dict]:
        return self.__get_items().get("snippet")

    def __get_statistics(self) -> Optional[Dict]:
        return self.__get_items().get("statistics")
    @property
    def get_channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__get_snippet().get("title")

    @property
    def get_description_chanel(self):
        return self.__get_snippet().get("description")

    @property
    def url(self):
        return f"https://www.youtube.com/channel/{self.get_channel_id}"

    @property
    def get_amount_subs(self):
        return self.__get_statistics().get("subscriberCount")

    @property
    def video_count(self):
        return self.__get_statistics().get("videoCount")

    @property
    def get_amount_views(self):
        return self.__get_statistics().get("viewCount")

    @classmethod
    def get_service(cls):
        return cls.__youtube_api

    def to_json(self, channel_name):
        with open(channel_name, 'w', encoding='utf-8') as file:
            object_to_dict(self._channel, file)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pjson(self._channel)
        return self._channel
