from thinkdsp import Spectrum, TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
triangle = TriangleSignal().make_wave(duration=0.01)
#triangle.plot()
#decorate(xlabel='Time(s)')
#plt.show()
Spectrum = triangle.make_spectrum()

Spectrum.hs[0] = 100
triangle.plot(color='blue')
Spectrum.make_wave().plot()
plt.show()