from scipy.signal import firwin, lfilter
import numpy as np
import matplotlib.pyplot as plt

# 采样参数
fs = 1000  # 采样频率 1000Hz
nyq = fs / 2  # 奈奎斯特频率

# 设计一个截止频率 100Hz 的低通滤波器（FIR）
numtaps = 101  # 滤波器系数数量（越多越精准）
cutoff = 100 / nyq
b = firwin(numtaps, cutoff)

# 构造信号（混合50Hz和300Hz）
t = np.linspace(0, 1, fs)
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*300*t)

# 滤波（应用FIR滤波器）
y = lfilter(b, 1.0, x)

# 画图
plt.figure(figsize=(10,4))
plt.plot(t, x, label="original")
plt.plot(t, y, label="after", linewidth=2)
plt.legend()
plt.grid()
plt.title("FIRresult")
plt.tight_layout()
plt.show()