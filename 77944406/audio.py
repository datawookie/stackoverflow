import wave
import sys

import pyaudio

CHUNK = 1024

with wave.open('StarWars3.wav', 'rb') as wf:
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    while len(data := wf.readframes(CHUNK)):
        stream.write(data)

    stream.close()

    p.terminate()
