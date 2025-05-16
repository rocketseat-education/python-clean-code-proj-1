class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        self._verify_if_song_already_registered()
        self._verify_songs_infos()
        self._insert_song()
        self._format_response()

    def _verify_if_song_already_registered(new_song_informations: dict) -> None:
        pass

    def _verify_songs_infos(new_song_informations: dict) -> None:
        pass

    def _insert_song() -> None:
        pass

    def _format_response() -> None:
        pass
