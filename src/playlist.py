import operator

from src.video import Video
from src.imp import youtube, pjson
from datetime import timedelta

class PlayList:
    __youtube_api = youtube

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self._playlist_of_video = self.get_service().playlistItems().list(playlistId=self.playlist_id, part='contentDetails',
                                                                 maxResults=50).execute()
        self._playlist = self.get_service().playlists().list(id=self.playlist_id, part='snippet').execute()
        self.title = self.__get_snippet_pl().get("title")
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.durations = self.durations()

    def __get_items(self):
        return self.print_info().get("items")[0]

    def __get_snippet(self):
        return self.__get_items().get("snippet")

    def __get_items_pl(self):
        return self.print_info_pl().get("items")[0]

    def __get_snippet_pl(self):
        return self.__get_items_pl().get("snippet")

    def get_videos_id(self):
        res = []
        for dict in self.print_info().get("items"):
            res.append(dict.get("contentDetails").get("videoId"))
        return res

    def get_durations(self):
        durations = []
        for id in self.get_videos_id():
            object = Video(id)
            durations.append(object.get_info()[0].get("contentDetails").get("duration"))
        return durations

    def durations(self):
        import isodate
        res = []
        for duration in self.get_durations():
            res.append(isodate.parse_duration(duration).total_seconds())
        return res

    def parse_seconds(self):
        sec = sum(self.durations)
        sec = sec % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60
        return ("%2d:%02d:%02d" % (hour, min, sec)).lstrip()

    def __contentDetails(self):
        return self.__get_items().get("contentDetails")

    @property
    def playlist_id(self):
        return self.__playlist_id

    @classmethod
    def get_service(cls):
        return cls.__youtube_api

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pjson(self._playlist_of_video)

        return self._playlist_of_video

    def print_info_pl(self):
        pjson(self._playlist)
        return self._playlist

    def __str__(self):
        return f"{self.parse_hours_min_sec()}"

    def show_best_video(self):
        res = {}
        for dict in self.print_info().get("items"):
            res[dict.get("contentDetails").get("videoId")] = Video(dict.get("contentDetails").get("videoId")).likes

        x = max(res.items(), key=operator.itemgetter(1))
        return f"https://youtu.be/{x[0]}"


