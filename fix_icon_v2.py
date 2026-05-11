#!/usr/bin/env python3
"""
智能裁剪图标：检测内容边界，居中放大到目标尺寸
"""

from PIL import Image
import numpy as np
import os

def smart_crop_and_resize(img_path, output_path, target_size):
    """智能裁剪并调整尺寸"""
    img = Image.open(img_path).convert('RGBA')
    arr = np.array(img)
    h, w = arr.shape[:2]

    print(f"处理: {os.path.basename(img_path)}")
    print(f"  原始尺寸: {w}x{h}")

    # 检测接近白色的像素 (所有通道 > 245)
    near_white = (arr[:,:,0] > 245) & (arr[:,:,1] > 245) & (arr[:,:,2] > 245)

    # 找内容边界（白色比例<5%的位置）
    # 上边
    top = 0
    for y in range(h):
        if near_white[y, :].mean() * 100 < 5:
            top = y
            break

    # 下边
    bottom = h
    for y in range(h-1, -1, -1):
        if near_white[y, :].mean() * 100 < 5:
            bottom = y
            break

    # 左边
    left = 0
    for x in range(w):
        if near_white[:, x].mean() * 100 < 5:
            left = x
            break

    # 右边
    right = w
    for x in range(w-1, -1, -1):
        if near_white[:, x].mean() * 100 < 5:
            right = x
            break

    print(f"  内容边界: ({left}, {top}) 到 ({right}, {bottom})")
    print(f"  内容尺寸: {right-left} x {bottom-top}")

    # 裁剪内容区域
    content = img.crop((left, top, right+1, bottom+1))
    content_w, content_h = content.size

    # 创建目标尺寸的透明背景
    result = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))

    # 计算缩放比例，使内容居中填充
    scale = min(target_size / content_w, target_size / content_h)
    new_w = int(content_w * scale)
    new_h = int(content_h * scale)

    # 缩放内容
    content = content.resize((new_w, new_h), Image.LANCZOS)

    # 居中粘贴
    paste_x = (target_size - new_w) // 2
    paste_y = (target_size - new_h) // 2
    result.paste(content, (paste_x, paste_y))

    print(f"  缩放后: {new_w} x {new_h}")
    print(f"  居中位置: ({paste_x}, {paste_y})")

    # 保存
    result.save(output_path, 'PNG', optimize=True)
    print(f"  已保存: {output_path}")
    print()

# 处理
icons_dir = "pages/icons"

files = [
    ("icon-192.png.bak", "icon-192.png", 192),
    ("icon-512.png.bak", "icon-512.png", 512),
]

for bak_name, out_name, size in files:
    bak_path = os.path.join(icons_dir, bak_name)
    out_path = os.path.join(icons_dir, out_name)

    if os.path.exists(bak_path):
        smart_crop_and_resize(bak_path, out_path, size)
    else:
        print(f"备份不存在: {bak_path}")

print("完成!")
