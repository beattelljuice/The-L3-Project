import speech_recognition as SR

class speak:
    def __init__(self):
        self.speechobject = SR.Recognizer()

    def file_to_text(self,FileLocation,SeccondsToAnalyse):
        info = SR.AudioFile(FileLocation)
        with info as source:
            self.speechobject.adjust_for_ambient_noise(source)
            audio_data = self.speechobject.record(source,duration=SeccondsToAnalyse)
        data = self.speechobject.recognize_google(audio_data)
        return data
