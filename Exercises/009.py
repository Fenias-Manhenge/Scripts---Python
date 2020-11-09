import speech_recognition as sr
import pyaudio as audio

recognizer = sr.Recognizer()
# recognizer.energy_threshold = 300

with sr.Microphone() as source:
    print('Say something: \nlistening...')
    audio = recognizer.listen(source)

    print('\nYou said: ')
    print(recognizer.recognize_google(audio))

'''
words = input("Say something").lower()

if "Hi xi!" in words:
    print('Hi, sir how are you?')
elif 'I am fine, and you?':
    print('I am fine too!')
else:
    print('Hum?')
'''