import pyttsx3
class speech:
    def __init__(self):
        pass

    def speak(self,tosay):
        synthesizer = pyttsx3.init()
        synthesizer.say(tosay)
        synthesizer.runAndWait()
        synthesizer.stop()