#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

# Graham Hughes Nov 11, 2016

import speech_recognition as sr
import os


# obtain audio from the microphone
r = sr.Recognizer()
cmd_next = """
osascript -e 'tell application "System Events" to keystroke "next"'
"""

cmd_last = """
osascript -e 'tell application "System Events" to keystroke "last"'
"""

while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        words = r.recognize_google(audio)
        print(words)
        if "next" in words:
            os.system(cmd_next)
        elif "last" in words or "previous" in words:
            os.system(cmd_last)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
