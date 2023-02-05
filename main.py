import processorserver
import edgeclient
import mp3totext
import speech_recognition as sr



def record_to_text():
    # Make the objects
    edgobj = edgeclient.edge()
    receiveobj = processorserver.receive()
    speakobj = mp3totext.speak()

    # Start the recording process
    print("Starting the record process")
    recording = edgobj.record(5)
    print("Finished the record process")
    print("The data collected was ")
    print(recording)
    print('Datatype:', recording.dtype)


    # --- This part can be placed on an external server if nessiscary for processing power

    print("Starting the conversion process")
    receiveobj.converttowav(recording)
    print("Finished the conversion process")

    # Convert the wav file to text (speechtotext)
    textfromspeech = speakobj.file_to_text("output.wav",5)
    print(textfromspeech)
    return textfromspeech

def listen_for_keyword():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=2) # Set timeout to 2 seconds
        except sr.WaitTimeoutError:
            # Timeout error, ignore it and continue to the next iteration
            print("Timeout threshold reached")
            return
    try:
        text = r.recognize_google(audio)
        print(text)
        if "wake up droid" in text:
            print("Keyword detected! Triggering event...")
            record_to_text()
        else:
            print("Keyword not detected.")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))


if __name__ == '__main__':
    while True:
        listen_for_keyword()