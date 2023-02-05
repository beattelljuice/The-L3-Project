from scipy.io.wavfile import write
class receive:
    def __init__(self):
        pass
    
    def converttowav(self,input,freq=44100,target="output.wav"):
        write(target, freq, input)