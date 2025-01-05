import cv2

# 读取彩色图像
img = cv2.imread('/home/ycren/python/UW/DATA/Test/test/Snipaste_2025-01-04_22-50-54.jpg')

# 将彩色图像分解为单独的颜色通道
b, g, r = cv2.split(img)

# 对每个颜色通道进行直方图均衡化
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)

# 合并均衡化后的颜色通道
result = cv2.merge((b_eq, g_eq, r_eq))


cv2.imwrite('he.jpg', result)