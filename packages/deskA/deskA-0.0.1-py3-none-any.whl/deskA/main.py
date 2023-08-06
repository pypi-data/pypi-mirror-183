import datetime
import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess


def speak(text):
    tts = gTTS(text=text, lang="en")
    i = 0
    while os.path.exists("voice%s.mp3" % i):
        i += 1

    filename = "voice%s.mp3" % i
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(str(e))
            print("Say that again please")

    return said.lower()


def note(text):
    date = datetime.datetime.now()
    save_path = 'C:/Users/Ewelyn/PycharmProjects/GoogleAssistant/Notes'
    file_name = str(date).replace(":", "-") + "-note.txt"
    complete_path = os.path.join(save_path, file_name)
    with open(complete_path, "w") as f:
        f.write(text)

        subprocess.Popen(["notepad.exe", complete_path])


print("Start")
text = get_audio()
note_strings = ["make a note", "write this down", "remember this"]
bye_strings = ["bye", "goodbye", "bye-bye", "see ya", "see ya later", "later"]
wake = "wake up"
while True:
    print("Listening...")
    text = get_audio()
    if text.count(wake) > 0:
        speak("Yes?")
        text = get_audio()
        if "hello" in text:
            speak("hello, how are you?")
            continue
        elif "what is your name" in text:
            speak("My name is Quiera")
            continue
        else:
            speak("I don't understand")
        for phrase in note_strings:
            if phrase in text:
                speak("What would you like me to write down?")
                note_text = get_audio().lower()
                note(note_text)
                speak("I've made a note of that!")
                continue
            else:
                speak("I don't understand")
                continue
        for phrase in bye_strings:
            if phrase in text:
                speak("Goodbye! See ya later")
                exit()
            else:
                speak("I don't understand")
                continue
