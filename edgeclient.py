# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

class edge:
    def __init__(self):
        pass
    def record(self,duration,SamplingFrequency=44100):
        recording = sd.rec(int(duration * SamplingFrequency), 
                   samplerate=SamplingFrequency, channels=2,dtype='int32')
        sd.wait()
        print(recording)
        return recording
