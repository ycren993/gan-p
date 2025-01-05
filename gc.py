import cv2
import numpy as np

# 读取彩色图像
img = cv2.imread('/home/ycren/python/UW/DATA/Test/test/Snipaste_2025-01-04_22-50-54.jpg')
gamma = 0.5  # 可以根据需要调整gamma值，gamma<1会使图像变亮，gamma>1会使图像变暗
lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in range(256)]).astype("uint8")
gamma_corrected = cv2.LUT(img, lookup_table)  # 应用伽马校正后的查找表进行校正处理后的图像显示和保存。
cv2.imwrite('gc.jpg', gamma_corrected)