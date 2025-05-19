import os


class SongRegisterView:
    def registry_song_initial(self) -> dict:
        self.__clear()
        print("Implementar Nova Musica \n\n")

        title = input("Determine o nome da musica: ")
        artist = input("Determine o nome do artista: ")
        year = input("Determine o ano de publicacao: ")

        new_song_informations = {
            "title": title, "artist": artist, "year": year
        }

        return new_song_informations

    def __clear(self):
        os.system("cls||clear")

    def registry_song_success(self, controller_response: dict) -> None:
        message = '''

        Musica cadastrada com sucesso!

        * Título: {}
        * Quantidade: {}
        '''. format(
            controller_response["attributes"]["title"],
            controller_response["count"]
        )
        print(message)

    def registry_song_fail(self, controller_response: dict) -> None:
        self.__clear()

        message = '''
        Falha ao cadastrar a musica

        * Erro: {}
        '''.format(
            controller_response["error"],
        )
        print(message)
