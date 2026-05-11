#!/usr/bin/env python3
"""
精确处理图标：裁剪白边 + 去除水印
"""

from PIL import Image, ImageDraw
import numpy as np
import os

def trim_white_border(img):
    """裁剪白色边框，但保留真实内容"""
    arr = np.array(img)
    h, w = arr.shape[:2]

    # 检测每一行/列是否有白色像素占比过高
    # 白边判定：整行/列的平均亮度 > 240

    # 上边：从上往下找第一行不是纯白的
    top = 0
    for y in range(h):
        row = arr[y, :, :3]
        brightness = row.mean(axis=1).mean()
        if brightness < 240:
            top = y
            break

    # 下边：从下往上找第一行不是纯白的
    bottom = h
    for y in range(h - 1, -1, -1):
        row = arr[y, :, :3]
        brightness = row.mean(axis=1).mean()
        if brightness < 240:
            bottom = y + 1
            break

    # 左边：从左往右找第一列不是纯白的
    left = 0
    for x in range(w):
        col = arr[:, x, :3]
        brightness = col.mean(axis=1).mean()
        if brightness < 240:
            left = x
            break

    # 右边：从右往左找第一列不是纯白的
    right = w
    for x in range(w - 1, -1, -1):
        col = arr[:, x, :3]
        brightness = col.mean(axis=1).mean()
        if brightness < 240:
            right = x + 1
            break

    print(f"  裁剪区域: ({left}, {top}) 到 ({right}, {bottom})")
    print(f"  裁剪后尺寸: {right-left} x {bottom-top}")

    # 裁剪
    cropped = img.crop((left, top, right, bottom))
    return cropped

def remove_watermark_simple(img):
    """简单去除水印：只替换右下角浅色区域"""
    arr = np.array(img)
    h, w = arr.shape[:2]

    # 水印区域：右下角约15%宽度，底部10%高度
    wm_width = int(w * 0.18)
    wm_height = int(h * 0.10)

    wm_x = w - wm_width
    wm_y = h - wm_height

    # 参考区域：水印上方和左侧的交接处
    ref_region = arr[wm_y:wm_y+wm_height//2, wm_x-wm_width//3:wm_x, :3]

    # 计算背景色（使用中位数，避免极端值）
    bg_color = np.median(ref_region.reshape(-1, 3), axis=0)

    # 在水印区域内，检测浅色像素并替换
    wm_area = arr[wm_y:h, wm_x:w, :3]

    # 浅色阈值：比背景色亮很多的可能是水印
    brightness = wm_area.astype(float).mean(axis=2)
    ref_brightness = float(bg_color.mean())

    # 替换比参考亮度高30%以上的像素
    mask = brightness > (ref_brightness + 30)
    wm_area[mask] = bg_color

    arr[wm_y:h, wm_x:w, :3] = wm_area

    return Image.fromarray(arr)

def process_icon(input_path, output_path):
    """处理单个图标"""
    print(f"处理: {os.path.basename(input_path)}")

    # 读取
    img = Image.open(input_path).convert('RGBA')
    original_w, original_h = img.size
    print(f"  原始尺寸: {original_w}x{original_h}")

    # 1. 裁剪白边
    trimmed = trim_white_border(img)

    # 2. 去除水印
    result = remove_watermark_simple(trimmed)

    # 3. 恢复到原始尺寸
    result = result.resize((original_w, original_h), Image.LANCZOS)

    # 保存
    result.save(output_path, 'PNG', optimize=True)
    print(f"  已保存: {output_path}")
    print()

# 处理
icons_dir = "pages/icons"

for filename in ["icon-192.png", "icon-512.png"]:
    bak_path = os.path.join(icons_dir, filename + ".bak")
    out_path = os.path.join(icons_dir, filename)

    if os.path.exists(bak_path):
        process_icon(bak_path, out_path)
    else:
        print(f"备份不存在: {bak_path}")

print("完成!")
