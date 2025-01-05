import cv2
import numpy as np

# 读取彩色图像
img = cv2.imread('/home/ycren/python/UW/DATA/Test/test/Snipaste_2025-01-04_22-50-54.jpg')

# 计算平均亮度
average_blue = np.mean(img[:,:,1])
average_green = np.mean(img[:,:,2])
average_red = np.mean(img[:,:,0])

# 计算权重因子
w_blue = 1.0 / average_blue * average_green
w_green = 1.0 / average_green * average_red
w_red = 1.0 / average_red * average_blue

# 应用权重因子进行白平衡校正
img_corrected = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换为RGB格式以便处理
img_corrected[:,:,0] = w_blue * img[:,:,0] + (1 - w_blue) * img[:,:,2]  # 蓝色通道校正
img_corrected[:,:,1] = w_green * img[:,:,1]                             # 绿色通道保持不变
img_corrected[:,:,2] = w_red * img[:,:,2] + (1 - w_red) * img[:,:,0]   # 红色通道校正
img_corrected = cv2.cvtColor(img_corrected, cv2.COLOR_RGB2BGR)  # 转回BGR格式以便显示和保存
cv2.imwrite('wb.jpg', img_corrected)

