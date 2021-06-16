from thinkdsp import Spectrum, decorate
from thinkdsp import TriangleSignal
from thinkdsp import SquareSignal
import matplotlib.pyplot as plt
def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

wave = SquareSignal(freq= 440).make_wave(duration=0.5)
Spectrum = wave.make_spectrum()
Spectrum.plot(high=10000,color='blue')
filter_spectrum(Spectrum)
Spectrum.scale(440)
Spectrum.plot(high=10000)
decorate(xlabel='Frequency(Hz)')
plt.show()
