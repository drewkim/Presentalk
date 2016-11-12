#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

# Graham Hughes Nov 11, 2016

import speech_recognition as sr
import os


# obtain audio from the microphone
r = sr.Recognizer()
r.pause_threshold = 0.5
r.energy_threshold = 1000 # Adjust to ambient noise (this is high, requires personal mic)

def send_words():
    with sr.Microphone() as source:
        print(">>>")
        try:
            audio = r.listen(source, timeout = 3)
        except:
            return None

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        words = r.recognize_google(audio)
        return words
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # recognize speech using IBM Speech to Text
    IBM_USERNAME = "11702311-ff64-438e-98d5-c911a38d826d" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = "PXss8FokhHZ4" # IBM Speech to Text passwords are mixed-case alphanumeric strings
    try:
        words = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
        return words
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))