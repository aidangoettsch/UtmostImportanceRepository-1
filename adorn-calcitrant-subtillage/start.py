import pyaudio

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

# print(p.get_default_output_device_info())

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=False,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)

print("* done")

stream.stop_stream()
stream.close()

p.terminate()