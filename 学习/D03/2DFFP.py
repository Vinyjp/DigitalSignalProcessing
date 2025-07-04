import numpy as np
import matplotlib.pyplot as plt
import cv2

# 读取图像（灰度 MRI 或任意图像）
img = cv2.imread('/Users/shihaosen/Desktop/AI/文件夹/数字信号/data/1.jpg', cv2.IMREAD_GRAYSCALE)

# 做二维FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)  # 把低频移到中间（可视化用）

# 计算频谱（取复数模长 + 对数变换增强对比）
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

# 可视化
plt.figure(figsize=(10,4))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("Magnitude Spectrum")
plt.axis('off')

plt.tight_layout()
plt.show()