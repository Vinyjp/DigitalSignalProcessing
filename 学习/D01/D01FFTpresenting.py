import numpy as np
import time

N = 2**14
x = np.random.randn(N)

# 手动做DFT（非常慢）
def dft_naive(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# 测试FFT时间
start = time.time()
X_fft = np.fft.fft(x)
print("FFT用时：", time.time() - start)

# 测试DFT时间（非常慢，可以注释）
# start = time.time()
# X_dft = dft_naive(x)
# print("DFT用时：", time.time() - start)