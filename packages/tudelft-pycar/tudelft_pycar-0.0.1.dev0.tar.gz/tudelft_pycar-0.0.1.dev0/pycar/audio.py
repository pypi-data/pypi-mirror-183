import pyaudio

isInit = False;
p = None;

def init():
    """
    Initializes PyAudio, but only if it hasn't been initialized yet.
    """
    global p
    if p == None:
        p = pyaudio.PyAudio();


def get_devices():
    """
    Get the available audio devices.

    Returns a tuple of the device index and its info.

    This function is a generator, so you can use it like
    ```
    for _,dev in get_devices():
        print(dev.name)
    ```
    """
    global p
    init()
    count = p.get_device_count()
    i=0
    while i < count:
        yield (i,p.get_device_info_by_index(i))
        i+=1

def open(dev, **kwargs):
    """
    Opens an audio device as input.

    `dev` should be the device index.
    Returns a PyAudio `Stream` object.
    """
    global p
    init()
    return p.open(input_device_index=dev, input=True, **kwargs)

fmt = pyaudio.paInt16
rate = 44100
chunk = 2048
xdata,ydata = [], []
line = None
ax = None
xmax = 20

import wave
import numpy as np
def main():
    """Example: listing audio devices and plotting one channel"""
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    global line,ax,xmax;

    for i,dev in get_devices():
        print(f"Index: {i}")
        name = dev["name"]
        print(f"Name: {name}")
        chans = dev["maxInputChannels"]
        print(f"Max inputs: {chans}")
        print()

    chan = int(input("Select device index: "))

    stream = open(chan,format=fmt,channels=1,rate=rate,frames_per_buffer=chunk)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0,xmax)
    ax.set_ylim(0,1)
    line, = ax.plot(xdata, ydata)

    ani = animation.FuncAnimation(fig, update, fargs=(stream,), interval=100)
    plt.show()

def update(frame, stream):
    global xmax
    data = stream.read(chunk, exception_on_overflow=False)
    waveData = wave.struct.unpack("%dh"%(chunk), data)
    npArray = np.array(waveData)
    power = np.mean(npArray**2)/chunk/40
    newx = len(xdata)+1
    xdata.append(newx)
    ydata.append(power)
    if newx > xmax:
        xmax += 20
        ax.set_xlim(xmax-40,xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line,

if __name__ == "__main__":
    main()
