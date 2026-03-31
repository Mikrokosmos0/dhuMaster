import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 加载图像并进行 FFT
# 请确保 tree_spatial_domain.jpg 在路径下，或修改为你的文件名
img_path = 'patient001_01_slice000.jpg'
img = cv2.imread(img_path, 0)

if img is None:
    # 如果没找到图，生成一个带网格的随机图作为演示
    img = np.zeros((300, 300), dtype="uint8")
    cv2.putText(img, "TREE", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, 255, 5)
    img = cv2.GaussianBlur(img, (5, 5), 0)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

# 执行 FFT 并移到中心
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# 2. 定义滤波器半径
r_low = 30        # 低通和高通的阈值
r_in, r_out = 30, 80 # 带通的内圆和外圆半径

# 3. 创建掩膜 (Masks)
mask_lpf = np.zeros((rows, cols), np.uint8)
cv2.circle(mask_lpf, (ccol, crow), r_low, 1, -1)

mask_hpf = 1 - mask_lpf

mask_bpf = np.zeros((rows, cols), np.uint8)
cv2.circle(mask_bpf, (ccol, crow), r_out, 1, -1)
cv2.circle(mask_bpf, (ccol, crow), r_in, 0, -1)

# 4. 应用滤波并逆变换 (IFFT)
def apply_filter(shift_data, mask):
    f_filtered = shift_data * mask
    f_ishift = np.fft.ifftshift(f_filtered)
    img_back = np.fft.ifft2(f_ishift)
    return np.abs(img_back)

img_lpf = apply_filter(fshift, mask_lpf)
img_hpf = apply_filter(fshift, mask_hpf)
img_bpf = apply_filter(fshift, mask_bpf)

# 5. 可视化输出 (2x2 布局)
# 设置中文字体为楷体_GB2312，英文字体为Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'KaiTi_GB2312', '楷体_GB2312']
plt.rcParams['axes.unicode_minus'] = False
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# a) 原始图像
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].axis('off')
axes[0, 0].set_title('\n\na) 原始图像 (Original)', y=-0.2)

# b) 低通滤波
axes[0, 1].imshow(img_lpf, cmap='gray')
axes[0, 1].axis('off')
axes[0, 1].set_title('\n\nb) 低通滤波 (Low-Pass)', y=-0.2)

# c) 高通滤波
axes[1, 0].imshow(img_hpf, cmap='gray')
axes[1, 0].axis('off')
axes[1, 0].set_title('\n\nc) 高通滤波 (High-Pass)', y=-0.2)

# d) 带通滤波
axes[1, 1].imshow(img_bpf, cmap='gray')
axes[1, 1].axis('off')
axes[1, 1].set_title('\n\nd) 带通滤波 (Band-Pass)', y=-0.2)

plt.tight_layout()
plt.show()