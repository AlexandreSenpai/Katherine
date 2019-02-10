from bot import *
#from audio_control import *

def ativar_comando(x):
    croped = x.split()
    first_word = 1
    last_word = len(croped)
    get_path = croped[first_word:last_word]
    path = ''.join(get_path)
    #Method to search things~
    croped2 = x.replace('pesquisar', '')

    if 'abrir' in x:
        shiro_voice("Abrindo {}".format(croped[1]))
        openUrl(path)

    if 'executar' in x:
        shiro_voice("Executando {}".format(path))
        try:
            runFile(paths[path])
        except:
            shiro_voice('{}, infelizmente não foi encontrado nenhum caminho para a requisição solicitada.'.format(user))

    if 'pesquisar' in x:
        shiro_voice("Pesquisando {}".format(croped2))
        searchThing(croped2)

    if 'volume' in x:
        audio_controller = AudioController('firefox.exe')
        audio_controller.set_volume(float(path)/100)
