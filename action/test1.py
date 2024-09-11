import cv2
import numpy as np

# 读取大图和小图（模板）
large_image = cv2.imread('large_image.jpg', 0)
template = cv2.imread('template_image.jpg', 0)
template_height, template_width = template.shape

# 使用归一化互相关进行模板匹配
result = cv2.matchTemplate(large_image, template, cv2.TM_CCOEFF_NORMED)

# 获取最大匹配位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 如果是归一化互相关方法，使用 max_loc
top_left = max_loc
bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

# 在大图上标出匹配的区域
cv2.rectangle(large_image, top_left, bottom_right, 255, 2)

# 显示结果
cv2.imshow('Matched Image', large_image)
cv2.waitKey(0)
cv2.destroyAllWindows()