import numpy as np
x = [1, 2, 3, 4]
h = [1, 0, -1]  # 卷积核（右减左）

y_full = np.convolve(x, h, mode='full')
y_same = np.convolve(x, h, mode='same')
y_valid = np.convolve(x, h, mode='valid')

print("Full:", y_full)
print("Same:", y_same)
print("Valid:", y_valid)


