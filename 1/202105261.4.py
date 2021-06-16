import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
import time

def strech(wave, fact):
    wave.ts *= fact
    wave.framerate /= fact
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False# 负号'-'显示为方块的问题

wave = thinkdsp.read_wave('100475__iluppai__saxophone-weep.wav')# 导入音频
wave.normalize()
play("100475__iluppai__saxophone-weep.wav", flags=8)
plt.subplot(311)
plt.title("原音频")
wave.plot()
time.sleep(2)

strech(wave, 0.5)
plt.subplot(312)
plt.title("2倍速")
plt.xlim(0, 20)
wave.plot()
wave.write("2倍速.wav")
play("2倍速.wav", flags=8)
time.sleep(2)

strech(wave, 8)
wave.write("0.5倍速.wav")
play("0.5倍速.wav", flags=18)
plt.subplot(313)
plt.title("0.5倍速")
plt.xlim(0, 20)
wave.plot()
time.sleep(1)
plt.show()
