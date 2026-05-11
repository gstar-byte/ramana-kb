#!/usr/bin/env python3
"""
去除图标右下角AI水印
使用更精确的方法：只处理水印区域，用周围背景色平滑填充
"""

from PIL import Image, ImageFilter
import numpy as np
import os

def remove_watermark(input_path, output_path, target_size=None):
    """去除水印并调整尺寸"""

    # 打开图像
    img = Image.open(input_path).convert('RGBA')
    arr = np.array(img)
    h, w = arr.shape[:2]

    print(f"处理: {os.path.basename(input_path)}")
    print(f"  原始尺寸: {w}x{h}")

    # 根据图像尺寸确定水印区域
    # 水印通常在右下角，占图像底部约5-10%，右侧约20-30%

    # 定义水印区域（右下角）
    # 对于192x192的图标，水印大约在底部10-20像素，右侧40-50像素
    wm_height = int(h * 0.08)  # 水印高度约占8%
    wm_width = int(w * 0.25)   # 水印宽度约占25%

    wm_y_start = h - wm_height
    wm_x_start = w - wm_width

    print(f"  水印区域: x={wm_x_start}-{w}, y={wm_y_start}-{h}")

    # 获取参考背景色（水印上方区域）
    ref_y_start = max(0, wm_y_start - wm_height)
    ref_region = arr[ref_y_start:wm_y_start, wm_x_start:w, :3]

    # 计算背景色的中位数（比均值更鲁棒）
    bg_color = np.median(ref_region, axis=(0, 1)).astype(np.uint8)
    print(f"  背景色 (中位数): RGB({bg_color[0]}, {bg_color[1]}, {bg_color[2]})")

    # 创建水印区域的mask（识别哪些像素是水印）
    wm_region = arr[wm_y_start:h, wm_x_start:w, :3]

    # 计算每个像素与背景色的差异
    diff = np.abs(wm_region.astype(float) - bg_color.astype(float))
    diff_score = diff.sum(axis=2)

    # 差异大的像素是水印（阈值根据经验调整）
    threshold = 80  # RGB差异总和阈值
    mask = diff_score > threshold

    print(f"  水印像素占比: {mask.mean()*100:.1f}%")

    # 创建修复后的区域
    fixed_region = wm_region.copy()

    # 对于水印像素，使用背景色
    fixed_region[mask] = bg_color

    # 对于非水印像素，保持原样（可能是图像内容）
    # 但进行轻微模糊以平滑过渡

    # 将修复后的区域放回原图
    arr[wm_y_start:h, wm_x_start:w, :3] = fixed_region

    # 对整个水印区域应用轻微高斯模糊，让过渡更自然
    # 提取水印区域并模糊
    wm_area = arr[wm_y_start:h, :, :]
    wm_pil = Image.fromarray(wm_area)
    wm_blurred = wm_pil.filter(ImageFilter.GaussianBlur(radius=0.5))
    arr[wm_y_start:h, :, :] = np.array(wm_blurred)

    # 创建新图像
    result = Image.fromarray(arr)

    # 调整尺寸（如果需要）
    if target_size and (w != target_size or h != target_size):
        result = result.resize((target_size, target_size), Image.LANCZOS)
        print(f"  调整尺寸至: {target_size}x{target_size}")

    # 保存
    result.save(output_path, 'PNG', optimize=True)
    print(f"  已保存: {output_path}")
    print()

# 处理文件
icons_dir = "pages/icons"

# 定义需要处理的文件和目标尺寸
files_to_process = [
    ("icon-192.png", 192),
    ("icon-512.png", 512),
]

for filename, target_size in files_to_process:
    input_path = os.path.join(icons_dir, filename)
    output_path = os.path.join(icons_dir, filename)

    if os.path.exists(input_path):
        remove_watermark(input_path, output_path, target_size)
    else:
        print(f"文件不存在: {input_path}")

print("处理完成!")
