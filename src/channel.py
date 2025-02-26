import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    API_KEY: str = os.getenv("API_KEY")
    youtube = build("youtube", "v3", developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part="snippet,statistics").execute()

    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        # return json.dumps(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute())
        return json.dumps(
            self.youtube.channels().list(id=self.channel_id, part="snippet,statistics").execute(),
            indent=2,
            ensure_ascii=False,
        )
