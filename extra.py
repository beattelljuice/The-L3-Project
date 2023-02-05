import speech_recognition as sr

def listen_for_keyword():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
        if "wake up droid" in text:
            print("Keyword detected! Triggering event...")
            # Trigger the event here
        else:
            print("Keyword not detected.")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))

if __name__ == '__main__':
    while True:
        listen_for_keyword()
