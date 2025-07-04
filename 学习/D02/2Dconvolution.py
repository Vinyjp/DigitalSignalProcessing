import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from scipy.misc import face  # 小测试图像

# 载入图像（灰度）
img = face(gray=True)[::4, ::4]  # 降采样更快

# 定义卷积核（边缘检测）
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# 执行卷积
filtered = convolve2d(img, kernel, mode='same', boundary='symm')

# 展示图像
plt.figure(figsize=(10,4))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered, cmap='gray')
plt.title("result(edge detection)")
plt.axis('off')
plt.tight_layout()
plt.show()