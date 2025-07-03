import numpy as np
import matplotlib.pyplot as plt

# 构造一个简单信号：混合两种频率
t = np.linspace(0, 1, 500)
x = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# 使用FFT求频谱
X = np.fft.fft(x)
freq = np.fft.fftfreq(len(t), d=(t[1] - t[0]))  # 频率坐标

# 只取前半段（对称）
half = len(X)//2
plt.figure(figsize=(10,4))
plt.plot(freq[:half], np.abs(X[:half]) / half)
plt.title("Magnitude Spectrum")
plt.xlabel("frequency (Hz)")
plt.ylabel("extent")
plt.grid(True)
plt.tight_layout()
plt.show()