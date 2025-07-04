import numpy as np
from matplotlib import pyplot as plt
import cv2

# 读取图像（灰度 MRI 或任意图像）
img= cv2.imread('/Users/shihaosen/Desktop/AI/文件夹/数字信号/data/1.jpg', cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# 获取图像的尺寸
rows, cols = img.shape
crow, ccol = rows//2, cols//2

# 计算频谱（取复数模长 + 对数变换增强对比）
# 创建一个与图像大小一样的掩膜
mask = np.zeros((rows, cols), np.uint8)
# 创建一个低通滤波器掩膜
# 半径为 R 的圆心区域为 1（白），表示保留
R = 50  # 你可以调大调小试试看
cv2.circle(mask, (ccol, crow), R, 1, thickness=-1)

#频域滤波
f_filtered = fshift * mask

#还原图像
f_ishift = np.fft.ifftshift(f_filtered)
img_filtered = np.fft.ifft2(f_ishift)
img_filtered = np.abs(img_filtered)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("original image")

plt.subplot(1,3,2)
plt.imshow(mask * 255, cmap='gray')
plt.title("low-pass filter")

plt.subplot(1,3,3)
plt.imshow(img_filtered, cmap='gray')
plt.title("result")

plt.tight_layout()
plt.show()


