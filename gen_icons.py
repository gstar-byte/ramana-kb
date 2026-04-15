from PIL import Image, ImageDraw
import os

sizes = [72, 96, 128, 144, 152, 192, 384, 512]
out_dir = 'c:/Users/willp/WorkBuddy/20260410104230/pages/icons'

for size in sizes:
    # Create gradient background
    img = Image.new('RGBA', (size, size), (26, 26, 78, 255))
    draw = ImageDraw.Draw(img)
    
    # Gradient overlay
    for y in range(size):
        ratio = y / size
        r = int(26 + ratio * (100 - 26))
        g = int(26 + ratio * (60 - 26))
        b = int(78 + ratio * (140 - 78))
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))
    
    # Draw Om-like circle (sacred symbol)
    cx, cy = size // 2, size // 2
    outer_r = int(size * 0.38)
    inner_r = int(size * 0.28)
    
    # Outer circle
    draw.ellipse([cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r],
                 outline=(255, 215, 0, 255), width=max(2, size // 64))
    
    # Inner smaller circle
    inner = int(size * 0.15)
    draw.ellipse([cx - inner, cy - inner, cx + inner, cy + inner],
                 fill=(255, 215, 0, 255))
    
    # Three dots symbol (Om representation)
    dot_r = max(2, size // 32)
    dot_positions = [
        (cx, cy - int(size * 0.2)),
        (cx - int(size * 0.15), cy - int(size * 0.05)),
        (cx + int(size * 0.15), cy - int(size * 0.05)),
    ]
    for px, py in dot_positions:
        draw.ellipse([px - dot_r, py - dot_r, px + dot_r, py + dot_r],
                     fill=(255, 215, 0, 255))
    
    # Save as PNG
    filename = os.path.join(out_dir, f'icon-{size}.png')
    img.save(filename, 'PNG')
    print(f'Created: icon-{size}.png')

# Also create main 192 and 512 icons referenced in manifest
for base_size, name in [(192, 'icon-192'), (512, 'icon-512')]:
    src = os.path.join(out_dir, f'icon-{base_size}.png')
    dst = os.path.join(out_dir, f'{name}.png')
    if os.path.exists(src) and not os.path.exists(dst):
        Image.open(src).save(dst, 'PNG')
        print(f'Copied: {name}.png')

print('All icons created!')
