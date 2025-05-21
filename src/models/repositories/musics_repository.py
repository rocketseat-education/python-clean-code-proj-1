from src.models.entities.music import Music


class __MusicsRepository:
    def __init__(self):
        self.__music_list = []

    def insert_music(self, music: Music) -> None:
        self.__music_list.append(music)

    def find_music(self, title: str) -> Music:
        for music in self.__music_list:
            if music.title == title:
                return music

        return None

    def get_all_songs(self) -> list[Music]:
        return self.__music_list


# Singleton - Design Pattern
musics_repository = __MusicsRepository()
