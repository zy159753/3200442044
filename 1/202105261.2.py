import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
import time

def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False#显示负号

wave = thinkdsp.read_wave('100475__iluppai__saxophone-weep.wav')#导入音频
plt.subplot(2,3,1)
plt.title("原始音频")
wave.plot()
wave.write(filename='输出1-2.wav')

segment = wave.segment(start=1.1, duration=0.5)# 截取一段持续0.5s的音频
plt.subplot(2,3,2)
plt.title("截取的0.5s的音频")
segment.plot()

# 绘制频谱
spectrum = segment.make_spectrum()
plt.subplot(2,3,3)
plt.title("所截取的音频频谱")
#plt.ylim(0, 1000)
spectrum.plot(high=7000)

# 低通
spectrum.low_pass(cutoff=600,factor=0.01)
wave_lp = spectrum.make_wave()
wave_lp.write(filename='低通.wav')
plt.subplot(234)
plt.title("低通滤波后的音频")
plt.ylim(0, 1000)
spectrum.plot(high=6000)
play('低通.wav', flags=1)
time.sleep(5)# 等待5s运行下一条语句

#高通
spectrum = segment.make_spectrum()
spectrum.high_pass(4000)
wave_hp = spectrum.make_wave()
wave_hp.write(filename='高通.wav')
plt.subplot(235)
plt.title("高通滤波音频")
plt.ylim(0, 1000)
spectrum.plot(high=8000)
play('高通.wav', flags=1)
time.sleep(5)# 等待5s运行下一条语句

#带通
spectrum = segment.make_spectrum()
spectrum.band_stop(low_cutoff=1000 ,high_cutoff=4000)
wave_bp = spectrum.make_wave()
wave_bp.write(filename='带通.wav')
plt.subplot(236)
plt.title("带阻滤波音频")
plt.ylim(0, 1000)
spectrum.plot(high=7000)
play('带通.wav', flags=1)
plt.show()