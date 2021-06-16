from thinkdsp import Spectrum, TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
triangle = TriangleSignal().make_wave(duration=0.01)
#triangle.plot()
#decorate(xlabel='Time(s)')
#plt.show()
Spectrum = triangle.make_spectrum()
print(Spectrum.hs[0])