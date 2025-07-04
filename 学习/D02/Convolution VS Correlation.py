x = [1, 2, 3, 4]
h = [1, 0, -1]  # 检测斜率的卷积核

import numpy as np

y_conv = np.convolve(x, h, mode='full')
y_corr = np.correlate(x, h, mode='full')

print("卷积输出:", y_conv)
print("相关输出:", y_corr)


