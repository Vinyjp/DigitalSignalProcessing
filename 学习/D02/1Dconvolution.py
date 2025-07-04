import numpy as np
import matplotlib.pyplot as plt

# 原始信号：带点“毛刺”
x = np.array([1, 3, 7, 1, 2, 6, 0, 1])

# 卷积核：滑动平均核
kernel = np.ones(3) / 3  # [1/3, 1/3, 1/3]

# 卷积
y = np.convolve(x, kernel, mode='same')  # same输出与输入等长

# 画图
plt.plot(x, label='original signal')
plt.plot(y, label='result', linewidth=2)
plt.legend()
plt.title("1D convolution with a moving average kernel")
plt.grid()
plt.tight_layout()
plt.show()