import random
import webbrowser
import os
import getpass
from xml.dom import NotFoundErr

import dotenv
from gtts import gTTS
from playsound import playsound

from .lib.youtube import Youtube

class Bot:
    def __init__(self, quiet: bool = False):
        self.nome = 'Katherine'
        self.nome_pronuncia = 'Quéferin'
        self.cor = 'Branca'
        self.cabelo = 'Branco'
        self.altura = 1.60
        self.pais = 'Brasil'
        self.version = '0.0.1'
        self.quiet = quiet

        self.running(quiet=self.quiet)
        dotenv.load_dotenv()

    def voice(self, to_speech: str):
        if isinstance(to_speech, str):
            voice_path = './resources/tmp/v.mp3'
            gTTS(text=to_speech, lang='pt-br').save(voice_path)
            playsound(voice_path)
            os.remove(voice_path)

    def running(self, quiet: bool = False):
        if quiet is False:
            self.voice(f'Olá! Meu nome é {self.nome_pronuncia} e estou pronta para lhe servir.')
            self.voice(f'Caso precise de mim, diga: {self.nome_pronuncia}, Ueikãpi!')
            self.voice('Como está se sentindo hoje?')

    def tell_joke(self):
        jokes = [
            'Por que o 007 não sai da cola dos bandidos quando vira super herói?... Porque ele vira o Bond, Super Bond.', 
            'O que é Cl-Cl-Cl-Cl-Cl-Cl?... Cloro-fila.'
        ]
        joke = random.choice(jokes)
        self.voice(joke)

    def open_url(self, path: str):
        if '.' not in path:
            path = f'{path}.com'
        webbrowser.open('https://' + path)

    def run_file(self, term):
        def look_for_file(root: str):
            root_path = os.walk(root)
            for path in root_path:
                for folder in path:
                    if isinstance(folder, list):
                        for item in folder:
                            if term in item.lower() and '.lnk' in item.lower(): 
                                return f'{path[0]}\\{item}'
        
        startup_paths = [
            r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs',
            r'C:\Users\alexa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs',
        ]

        for path in startup_paths:
            windows_path = look_for_file(path)
            if windows_path is not None:
                os.startfile(windows_path)
                return
        else:
            raise NotFoundErr
                
    def search(self, to_search: str):
        webbrowser.open('https://www.google.com.br/search?q=' + to_search)
    
    def execute(self, command: str):
        if 'navegar para' in command:
            url = command.split()[2:]
            self.voice(f'Abrindo {url}.')
            self.open_url(path=''.join(url))

        if 'executar' in command:
            executable = command.split()[1:]
            self.voice("Executando {}".format(executable))
            try:
                self.run_file(term=' '.join(executable))
            except NotFoundErr:
                self.voice('Infelizmente não foi encontrado nenhum caminho para a requisição solicitada.')

        if 'pesquisar' in command:
            searchable = command.replace('pesquisar', '')
            self.voice("Pesquisando {}".format(searchable))
            self.search(to_search=searchable)

        if 'me conte uma piada' in command or 'contar piada' in command:
            self.tell_joke()
        
        if 'reproduzir no' in command:
            local_to_reproduce = command.split()[2]
            if local_to_reproduce == 'youtube':
                url = Youtube(token=os.getenv('YT_TOKEN')).most_viewed(query=' '.join(command.split()[3:]))
                if url is not None:
                    self.voice(f'Reproduzindo em {command.split()[2]} {" ".join(command.split()[3:])}')
                    self.open_url(path=url)
                else:
                    self.voice(f'Nenhum resultado encontrado para: {" ".join(command.split()[3:])}')
            else:
                self.voice(f'Infelizmente {local_to_reproduce} ainda não está disponível.')
        
        if 'desligar computador' in command:
            self.voice('Desligando o computador... Boa noite, mestre!')
            os.system('shutdown -s')

        # if 'volume' in x:
        #     audio_controller = AudioController('firefox.exe')
        #     audio_controller.set_volume(float(path)/100)

        playsound.playsound('./resources/sfx/sleep.mp3')


if __name__ == '__main__':
    katherine = Bot(quiet=True)
    print(getpass.getuser())
