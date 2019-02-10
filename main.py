#Vanilla Python Modules~
import smtplib
#Not Python Vanilla Modules~
import speech_recognition as sr
import ctypes
import comtypes
#My Modules~
from bot import *
#from audio_control import *
from user_check import *
from comandos import *

#init shiro
isRunning = True
shiro = Bot()


def listen_me(msg=""):
    
    r = sr.Recognizer()

    with sr.Microphone() as mic:
        shiro.shiro_voice(msg)
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
    
    try:
        comando = r.recognize_google(audio, language='pt-br')
    except:
        print('restarting listen_me()')
        main(listen_me())

    return comando.lower()

def main(comando):
    
    print(comando)
    if 'shiro acorde' in comando:
        ordem = listen_me('{}, por favor, diga o comando.'.format(readUser()))
        ativar_comando(ordem)

    shiro.shiro_voice('Tarefa realizada.')
    main(listen_me())

if __name__ == '__main__':
    user = "indefinido"
    if not checkUser():
        user = readUser()
        shiro.shiro_voice('Bem vindo {}, Estou pronta para atendê-lo.'.format(user))
        while isRunning:
            shiro.shiro_voice('Caso precise de mim diga "shiro acorde!"')
            main(listen_me())
    else:
        shiro.shiro_voice('Bem vindo, {}. Meu nome é {} e a partir de hoje serei sua assistente pessoal. Espero me dar bem com você'.format(user, shiro.nome))
        shiro.shiro_voice('Atualmente encontro-me na versão de software {}, portanto, caso haja quaisquer bugs ou sugestões, por favor, sinta-se a vontade para entrar em contato com meus desenvolvedores. Minhas informações de uso encontram-se na pasta "README".'.format(shiro.version))
        shiro.shiro_voice('Há um arquivo nesta mesma pasta com uma lista de comandos disponíveis. Bom, Antes de começarmos...')
        registerUser(listen_me("Qual seu nome?"))
        main(listen_me('Prazer em conhecê-lo, {}. Mestre... Caso precise de mim diga "shiro acorde!"'.format(readUser())))
