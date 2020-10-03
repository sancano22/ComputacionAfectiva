#brew install portaudio
#pip3 install pyaudio
#pip3 install wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from IPython.display import Audio
from numpy.fft import fft,ifft

Fs,data=read("grabacion.wav")
print("frecuencia", Fs)
plt.figure()
fourier=np.fft.fft(data[:])
#plt.plot(data)
plt.plot(np.abs(fourier))
plt.xlabel("muestras")
plt.ylabel("amplitud")
plt.title("forma de la onda de audio")
plt.show()
#estructura del audio
#print(data.shape)
