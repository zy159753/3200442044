import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


t=np.arange(-1,11,1)
ty=np.arange(-1,22,1)



def u(t):
    return np.where(t>=0,1.0,0.0)
x=u(t)-u(t-2)+u(t-4)-u(t-12)
h=u(t-1)-u(t-3)+u(t-6)-u(t-10)
y1=signal.convolve(x,h)
ws,h0=signal.freqz(y1,whole=True)
ws,h1=signal.freqz(x,whole=True)
ws,h2=signal.freqz(h,whole=True)
h=h1*h2


plt.subplot(211)
plt.plot(ws,h0)
plt.title("时域卷积")
plt.subplot(212)
plt.plot(ws,h)
plt.title('频域相乘')
plt.show()