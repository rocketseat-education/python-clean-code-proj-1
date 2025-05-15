def introduction_page() -> str:
    message = '''

    Sistema Musical

    * Cadastrar Musica - 1
    * Criar Playlist - 2
    * Sair - 5

    '''

    print(message)
    command = input("Commando: ")

    return command
