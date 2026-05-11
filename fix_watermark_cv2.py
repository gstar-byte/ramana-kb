#!/usr/bin/env python3
"""
使用OpenCV inpainting去除水印
"""

import cv2
import numpy as np
from PIL import Image
import os

def remove_watermark_cv2(input_path, output_path, target_size=None):
    """使用OpenCV inpainting去除水印"""

    # 读取图像
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"无法读取: {input_path}")
        return

    h, w = img.shape[:2]
    print(f"处理: {os.path.basename(input_path)}")
    print(f"  原始尺寸: {w}x{h}")

    # 分离alpha通道（如果有）
    if img.shape[2] == 4:
        bgr = img[:, :, :3]
        alpha = img[:, :, 3]
    else:
        bgr = img
        alpha = None

    # 创建水印mask
    # 水印在右下角，我们需要创建一个mask来标记水印区域
    mask = np.zeros((h, w), dtype=np.uint8)

    # 定义水印区域（根据图像尺寸调整）
    # 水印通常在右下角，宽度约占25-30%，高度约占8-12%
    wm_width = int(w * 0.30)
    wm_height = int(h * 0.12)

    wm_x_start = w - wm_width
    wm_y_start = h - wm_height

    # 在水印区域，我们需要识别哪些像素是水印
    # 通过颜色差异来识别
    wm_region = bgr[wm_y_start:h, wm_x_start:w]

    # 计算水印区域上方参考区域的背景色
    ref_y_start = max(0, wm_y_start - wm_height)
    ref_region = bgr[ref_y_start:wm_y_start, wm_x_start:w]
    bg_color = np.median(ref_region, axis=(0, 1))
    print(f"  背景色参考: B={bg_color[0]:.1f}, G={bg_color[1]:.1f}, R={bg_color[2]:.1f}")

    # 创建mask：与背景色差异大的像素是水印
    diff = np.abs(wm_region.astype(float) - bg_color.astype(float))
    diff_score = diff.sum(axis=2)

    # 阈值：差异大于这个值认为是水印
    threshold = 100
    wm_mask = (diff_score > threshold).astype(np.uint8) * 255

    # 将mask放回原图位置
    mask[wm_y_start:h, wm_x_start:w] = wm_mask

    # 扩展mask一点点，确保覆盖完整
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    print(f"  水印区域: x={wm_x_start}-{w}, y={wm_y_start}-{h}")
    print(f"  水印像素占比: {np.sum(mask > 0) / (h * w) * 100:.2f}%")

    # 使用inpainting去除水印
    # INPAINT_NS = Navier-Stokes based method
    # INPAINT_TELEA = Fast Marching Method
    inpainted = cv2.inpaint(bgr, mask, 3, cv2.INPAINT_TELEA)

    # 合并alpha通道
    if alpha is not None:
        result = np.dstack([inpainted, alpha])
    else:
        result = inpainted

    # 调整尺寸
    if target_size and (w != target_size or h != target_size):
        result = cv2.resize(result, (target_size, target_size), interpolation=cv2.INTER_LANCZOS4)
        print(f"  调整尺寸至: {target_size}x{target_size}")

    # 保存
    cv2.imwrite(output_path, result)
    print(f"  已保存: {output_path}")
    print()

# 处理文件
icons_dir = "pages/icons"

files_to_process = [
    ("icon-192.png", 192),
    ("icon-512.png", 512),
]

for filename, target_size in files_to_process:
    input_path = os.path.join(icons_dir, filename)
    output_path = os.path.join(icons_dir, filename)

    if os.path.exists(input_path):
        remove_watermark_cv2(input_path, output_path, target_size)
    else:
        print(f"文件不存在: {input_path}")

print("处理完成!")
