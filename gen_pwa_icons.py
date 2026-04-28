"""Generate PWA icons from user-provided ramana photo.
Source: pages/icons/ramana-source.jpg (749x1000, portrait)
Maskable: content in center 80%, 10% padding, dark background
Any: circular crop of the face area
"""
from PIL import Image, ImageDraw, ImageFilter
import os

ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages', 'icons')
SOURCE = os.path.join(ICON_DIR, 'ramana-source.jpg')

img = Image.open(SOURCE).convert('RGBA')
print(f'Source: {img.size}, {img.mode}')

# --- 1. Maskable icons (square with padding) ---
# For maskable: content must be in center 80%. We'll crop center square,
# resize to 80% of icon, and fill remaining with background color.
# Get background color from the image edges
bg_color = (13, 17, 23, 255)  # Match theme: #0d1117

for px in [192, 512]:
    # Crop center square from source (portrait -> square, take center-top area for face)
    w, h = img.size
    # For portrait photo, center crop horizontally, bias toward top for face
    crop_w = min(w, h)
    left = (w - crop_w) // 2
    top = 0  # Take from top to capture face
    if top + crop_w > h:
        top = (h - crop_w) // 2
    cropped = img.crop((left, top, left + crop_w, top + crop_w))
    
    # Resize to 80% of target (maskable safe zone)
    content_size = int(px * 0.8)
    content_img = cropped.resize((content_size, content_size), Image.LANCZOS)
    
    # Create canvas with dark background
    canvas = Image.new('RGBA', (px, px), bg_color)
    offset = (px - content_size) // 2
    canvas.paste(content_img, (offset, offset))
    
    out = os.path.join(ICON_DIR, f'icon-{px}.png')
    canvas.save(out, 'PNG')
    print(f'[maskable] {out} ({os.path.getsize(out)} bytes)')

# --- 2. Any-purpose icons (circular crop) ---
for px in [192, 512]:
    w, h = img.size
    crop_size = min(w, h)
    left = (w - crop_size) // 2
    top = 0
    if top + crop_size > h:
        top = (h - crop_size) // 2
    cropped = img.crop((left, top, left + crop_size, top + crop_size)).resize((px, px), Image.LANCZOS)
    
    # Create circular mask with slight feathering
    mask = Image.new('L', (px, px), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse([0, 0, px - 1, px - 1], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(1))
    
    circular = cropped.copy()
    circular.putalpha(mask)
    
    out = os.path.join(ICON_DIR, f'icon-{px}-any.png')
    circular.save(out, 'PNG')
    print(f'[any] {out} ({os.path.getsize(out)} bytes)')

# --- 3. Generate apple-touch-icon (180x180, no mask) ---
w, h = img.size
crop_size = min(w, h)
left = (w - crop_size) // 2
top = 0
if top + crop_size > h:
    top = (h - crop_size) // 2
cropped = img.crop((left, top, left + crop_size, top + crop_size)).resize((180, 180), Image.LANCZOS)
mask = Image.new('L', (180, 180), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse([0, 0, 179, 179], fill=255)
apple_icon = cropped.copy()
apple_icon.putalpha(mask)
out = os.path.join(ICON_DIR, 'apple-touch-icon.png')
apple_icon.save(out, 'PNG')
print(f'[apple] {out} ({os.path.getsize(out)} bytes)')

# --- 4. Generate favicon (32x32) ---
favicon = cropped.resize((32, 32), Image.LANCZOS)
mask32 = Image.new('L', (32, 32), 0)
draw32 = ImageDraw.Draw(mask32)
draw32.ellipse([0, 0, 31, 31], fill=255)
favicon.putalpha(mask32)
out = os.path.join(ICON_DIR, 'favicon-32.png')
favicon.save(out, 'PNG')
print(f'[favicon] {out} ({os.path.getsize(out)} bytes)')

print('\nAll icons generated!')
