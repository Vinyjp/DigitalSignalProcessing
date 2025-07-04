import numpy as np
import matplotlib.pyplot as plt

# 采样参数
fs = 1000
t = np.linspace(0, 1, fs)

# 构造一个混合信号（5Hz + 50Hz + 200Hz）
x = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t) + 0.4 * np.sin(2 * np.pi * 200 * t)

# DFT（FFT）变换
X = np.fft.fft(x)
freq = np.fft.fftfreq(len(x), d=1/fs)

# 只看正频率
half = len(x) // 2
plt.plot(freq[:half], np.abs(X[:half]) / half)
plt.title("frequency domain representation of the signal")
plt.xlabel("frequency (Hz)")
plt.ylabel("extend")
plt.grid()
plt.tight_layout()
plt.show()