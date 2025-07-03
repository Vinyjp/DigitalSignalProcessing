"""试验下采样和量化"""
import numpy as np
import matplotlib.pyplot as plt

# 连续时间信号
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 5 * t)

# 采样：每隔0.05s取一个
n = np.arange(0, 1, 0.05)
x_sampled = np.sin(2 * np.pi * 5 * n)

# 量化：8-bit灰度（映射到0~255再回映）
x_quantized = np.round((x_sampled + 1) * 127.5)  # shift到0~255
x_quantized = x_quantized / 127.5 - 1  # 还原到-1~1

plt.figure(figsize=(10,4))
plt.plot(t, x, label='continue signal x(t)')
plt.stem(n, x_quantized, linefmt='r-', markerfmt='ro', basefmt='r-', label='sampling+quantifying signal')
plt.title('sampling + quantifying present')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()