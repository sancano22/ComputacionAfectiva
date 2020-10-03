#brew install portaudio
#pip3 install pyaudio
#pip3 install wave
import pyaudio
import wave

#definiciones parametros
FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
duracion=4
archivo="grabacion.wav"
audio=pyaudio.PyAudio()
stream=audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
print ("grabando..")
frames=[]
for i in range(0,int(RATE/CHUNK*duracion)):
	data=stream.read(CHUNK)
	frames.append(data)
print("grabacion terminada")
#detenemos la grabación
stream.stop_stream()
stream.close()
audio.terminate()

#creamos /guardamos archivo
waveFile=wave.open(archivo,'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()