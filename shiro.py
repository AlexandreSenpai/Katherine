#Vanilla Python Modules~
import os
import webbrowser
import smtplib
import win32com
#Not Python Vanilla Modules~
import speech_recognition as sr
from playsound import playsound
import ctypes
import comtypes
import pyttsx3
from pycaw.pycaw import AudioUtilities

#Global Vars
isRunning = True
file = "name.txt"
paths = {
    "leagueoflegends": "E:\Arquivos de programas (x86)\League of Legends\LeagueClient.exe",
    "visualstudiocode": "E:\Arquivos de programas (x86)\Microsoft VS Code\Code.exe",
    "photoshop": "E:\Program files (x86)\Adobe\Adobe Photoshop CC 2018\Photoshop.exe"
}

def registerUser(user):
    with open(file, 'w') as f:
        f.write(user)
    f.close()

def checkUser():
    if os.path.getsize(file) <= 0:
        return True

def readUser():
    user_name = ""
    if not checkUser():
        with open(file, 'r') as f:
            for line in f:
                user_name = line
    return user_name

def openUrl(path):
    webbrowser.open('https://' + path)
def runFile(path):
    os.startfile(path)
def searchThing(path):
    webbrowser.open('https://www.google.com.br/search?q=' + path)

class AudioController(object):
    def __init__(self, process_name):
        self.process_name = process_name
        self.volume = self.process_volume()

    def process_volume(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                return interface.GetMasterVolume()

    def set_volume(self, decibels):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                self.volume = min(1.0, max(0.0, decibels))
                interface.SetMasterVolume(self.volume, None)
                shiro_voice('Volume set to', self.volume)

def shiro_voice(voice):
    engine = pyttsx3.init()
    engine.say(voice)
    engine.runAndWait()

def listen_me(msg=""):
    
    r = sr.Recognizer()

    with sr.Microphone() as mic:
        shiro_voice(msg)
        r.adjust_for_ambient_noise(mic, duration=1)
        audio = r.listen(mic)
    
    try:
        comando = r.recognize_google(audio, language='pt-br')
    except:
        main(listen_me())

    return comando.lower()

def main(comando):
    #Method to open sites and run softwares~
    croped = comando.split()
    first_word = 1
    last_word = len(croped)
    get_path = croped[first_word:last_word]
    path = ''.join(get_path)
    #Method to search things~
    croped2 = comando.replace('pesquisar', '')

    if 'abrir' in comando:
        shiro_voice("Abrindo {}".format(croped[1]))
        openUrl(path)

    if 'executar' in comando:
        shiro_voice("Executando {}".format(path))
        try:
            runFile(paths[path])
        except:
            shiro_voice('{}, infelizmente não foi encontrado nenhum caminho para a requisição solicitada.'.format(user))

    if 'pesquisar' in comando:
        shiro_voice("Pesquisando {}".format(croped2))
        searchThing(croped2)

    if 'volume' in comando:
        audio_controller = AudioController('firefox.exe')
        audio_controller.set_volume(float(path)/100)

    main(listen_me())

if __name__ == '__main__':
    user = "indefinido"
    if not checkUser():
        user = readUser()
        shiro_voice('Bem vindo, {}.'.format(user))
        while isRunning:
            shiro_voice("Estou pronta para atendê-lo, diga o comando.")
            main(listen_me())
    else:
        shiro_voice('Bem vindo, {}.'.format(user))
        registerUser(listen_me("Qual seu nome?"))
        main(listen_me())
