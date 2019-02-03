import random
import webbrowser
import os
import pyttsx3
import win32com


class Shiro:
    def __init__(self, nome, cor, cabelo, altura, pais):
        self.nome = nome
        self.cor = cor
        self.cabelo = cabelo
        self.altura = altura
        self.pais = pais
        self.version = '0.0.1'
        self.jokes = ['Por que o 007 não sai da cola dos bandidos quando vira super herói?... Porque ele vira o Bond, Super Bond.', 'O que é Cl-Cl-Cl-Cl-Cl-Cl?... Cloro-fila.']

paths = {
    "leagueoflegends": "E:\Arquivos de programas (x86)\League of Legends\LeagueClient.exe",
    "visualstudiocode": "E:\Arquivos de programas (x86)\Microsoft VS Code\Code.exe",
    "photoshop": "E:\Program files (x86)\Adobe\Adobe Photoshop CC 2018\Photoshop.exe"
}

def shiro_voice(voice=""):
        engine = pyttsx3.init()
        engine.say(voice)
        engine.runAndWait()

def TellJoke():
    joke = random.choice(shiro.jokes)
    return joke

def openUrl(path):
    webbrowser.open('https://' + path)

def runFile(path):
    os.startfile(path)

def searchThing(path):
    webbrowser.open('https://www.google.com.br/search?q=' + path)

