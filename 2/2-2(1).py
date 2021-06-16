from thinkdsp import Sinusoid
from thinkdsp import normalize,unbias
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
class SawtoothSignal(Sinusoid):
    def evaluate(self, ts):
        cycles = self.freq *ts + self.offset/np.pi/2
        frac,_=np.modf(cycles)
        ys=normalize(unbias(frac),self.amp)
        return ys

Signal = SawtoothSignal(200)
duration = Signal.period*3
segment = Signal.make_wave(duration,framerate=40000)
segment.plot()
decorate(xlabel='Time(s)')
plt.show()

plt.show()
wave = Signal.make_wave(duration = 0.5,framerate=40000)
wave.apodize()
wave.make_audio()
wave.write(filename='2-3.wav')

Spectrum = wave.make_spectrum()
Spectrum.plot()
decorate(xlabel='频谱(Hz)')
plt.show()


sawtooth =SawtoothSignal().make_wave(duration=0.5,framerate=40000)
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency(Hz)')
sawtooth.make_spectrum().plot(color='blue')
#方波对比
square =SquareSignal(amp=0.5).make_wave(duration=0.5,framerate=40000)
square.make_spectrum().plot()
#三角波对比
#triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5,framerate=40000)
#triangle.make_spectrum().plot()
plt.show()