from thinkdsp import SquareSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt

square = SquareSignal(1100).make_wave(duration=0.5,framerate=20000)
square.make_spectrum().plot()
decorate(xlabel='Frequency(Hz)')
plt.show()