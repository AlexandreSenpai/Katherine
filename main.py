import playsound
import speech_recognition as sr

import katherine

def listen_me():

    r = sr.Recognizer()

    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        print('running')
        while True:
            audio = r.listen(mic)
            try:
                comando = r.recognize_google(audio_data=audio).lower()
                if 'atherine wake up' in comando[1:]:
                    playsound.playsound('./resources/sfx/wake.mp3')
                    print('roda o comando')
                    try:
                        comando = r.recognize_google(audio_data=r.listen(mic), language='pt-br').lower()
                        yield comando
                    except sr.UnknownValueError:
                        playsound.playsound('./resources/sfx/sleep.mp3')
            except sr.UnknownValueError:
                pass
    
if __name__ == '__main__':

    katherine = katherine.Bot(quiet=True)
    for comando in listen_me():
        katherine.execute(command=comando)
