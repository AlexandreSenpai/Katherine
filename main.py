#Vanilla Python Modules~
import smtplib
#Not Python Vanilla Modules~
import speech_recognition as sr
from playsound import playsound
import ctypes
import comtypes
#My Modules~
from shiro import *
from audio_control import *
from user_check import *

#Global Vars
#init shiro
shiro = Shiro('Shiro', 'Branca', 'Branco', '1.53', 'Brasil')
isRunning = True

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
        shiro_voice('Bem vindo {}, Estou pronta para atendê-lo.'.format(user))
        while isRunning:
            shiro_voice('Diga o comando!')
            main(listen_me())
    else:
        shiro_voice('Bem vindo, {}. Meu nome é {} e a partir de hoje serei sua assistente pessoal. Espero me dar bem com você'.format(user, shiro.nome))
        shiro_voice('Atualmente encontro-me na versão de software {}, portanto, caso haja quaisquer bugs ou sugestões, por favor, sinta-se a vontade para entrar em contato com meus desenvolvedores. Minhas informações de uso encontram-se na pasta "README".'.format(shiro.version))
        shiro_voice('Há um arquivo nesta mesma pasta com uma lista de comandos disponíveis. Bom, Antes de começarmos...')
        registerUser(listen_me("Qual seu nome?"))
        main(listen_me('Prazer em conhecê-lo, {}. Mestre... Diga o comando.'.format(readUser())))
