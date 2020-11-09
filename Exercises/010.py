import speech_recognition as sr

fl = "speech.wav"
recognizer = sr.Recognizer()

with sr.AudioFile(fl) as source:
    audio = recognizer.record(source)
    print(recognizer.recognize_google(audio))

"""
vr = float(input('Digite o valor contido na carteira: '))
print('voce pode comprar {:.2f}$'.format(vr / 72.83))
"""
