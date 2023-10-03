
from src.imp import pjson, youtube, object_to_dict


class Video:
    __youtube_api = youtube

    def __init__(self, video_id):
        self.__video_id = video_id
        self._video = self.get_service().videos().list(id=self.get_video_id, part='snippet,statistics').execute()

    def __get_items(self):
        return self.print_info().get("items")[0]
    def __get_snippet(self):
        return self.__get_items().get("snippet")

    def __get_statistics(self):
        return self.__get_items().get("statistics")

    @property
    def title(self):
        return self.__get_snippet().get("title")

    def url(self):
        return f"https://www.youtube.com/channel/{self.get_video_id}"

    @property
    def amount_views(self):
        return self.__get_statistics().get("viewCount")

    @property
    def likes(self):
        return self.__get_statistics().get("likeCount")

    @property
    def get_video_id(self):
        return self.__video_id

    @classmethod
    def get_service(cls):
        return cls.__youtube_api



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pjson(self._video)
        return self._video

    def to_json(self, channel_name):
        """ Записывает информацию в файл.json """
        with open(channel_name, 'w', encoding='utf-8') as file:
            object_to_dict(self._video, file)

    def __str__(self):
        return f"{self.title()}"


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id

    @property
    def get_playlist_id(self):
        return self.__playlist_id

    def __repr__(self):
        return f"{self.__class__.__name__}({self.get_video_id}, {self.get_playlist_id}, {self.title()}, {self.url()}, {self.amount_views()}, {self.likes()}"