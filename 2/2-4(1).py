from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
triangle = TriangleSignal().make_wave(duration=0.01)
triangle.plot()
decorate(xlabel='Time(s)')
plt.show()