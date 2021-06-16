
from thinkdsp import Spectrum, decorate
from thinkdsp import TriangleSignal
import matplotlib.pyplot as plt

def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0
wave = TriangleSignal(freq=440).make_wave(duration=1.5)
Spectrum = wave.make_spectrum()
Spectrum.plot(high=10000,color='blue')
filter_spectrum(Spectrum)
Spectrum.scale(400)
Spectrum.plot(high=10000)
decorate(xlabel='Frequency(Hz)')
plt.show()