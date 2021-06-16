import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False# 负号'-'显示为方块的问题
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')

#创建sin和cos函数
sin = thinkdsp.SinSignal(freq=500, amp=1.0,offset=0)
cos = thinkdsp.CosSignal(freq=900, amp=0.5,offset=0)

Mix = cos+sin
plt.subplot(1,2,1)
plt.title("复合信号")
Mix.plot()

wave = Mix.make_wave(duration=0.5)
spectrum = wave.make_spectrum()
plt.subplot(1,2,2)
plt.title("复合信号频谱")
spectrum.plot()

wave.write("复合信号.wav")
play("复合信号.wav", flags=1)
plt.show()
