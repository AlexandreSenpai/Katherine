import random
import webbrowser
import os
import pyttsx3
#import win32com
from playsound import playsound

class Bot:
    def __init__(self):
        self.nome = 'Shiro'
        self.cor = 'Branca'
        self.cabelo = 'Branco'
        self.altura = 1.30
        self.pais = 'Brasil'
        self.version = '0.0.1'
        self.jokes = ['Por que o 007 não sai da cola dos bandidos quando vira super herói?... Porque ele vira o Bond, Super Bond.', 'O que é Cl-Cl-Cl-Cl-Cl-Cl?... Cloro-fila.']

    def shiro_voice(self, voice):
        try:
            engine = pyttsx3.init()
            engine.say(voice)
            engine.runAndWait()
            t = voice.split()
            t = t[0]
            title = ""
            for i in t:
                if i in 'íóúáéìòèàù!@#$%':
                    i = i.replace(i, "")
                title += i
                '''
                sound = gTTS(voice, lang="pt-br")
                sound.save('{}.mp3'.format(title))
                playsound('{}.mp3'.format(title))
                '''
        except:
            print('não há informação o suficiente.')

    def TellJoke():
        joke = random.choice(shiro.jokes)
        return joke

    def openUrl(path):
        webbrowser.open('https://' + path)

    def runFile(path):
        os.startfile(path)

    def searchThing(path):
        webbrowser.open('https://www.google.com.br/search?q=' + path)

