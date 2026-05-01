#!/usr/bin/env python3
import os

# Read the karma.html as base template
with open('/workspace/pages/concepts/karma.html', 'r', encoding='utf-8') as f:
    template = f.read()

concepts = [
    ('ahamkara.html', '我慢 / Ahamkara', '💀', '自我执着 · 个体身份的根源'),
    ('antahkarana.html', '内具 / Antahkarana', '🧩', '心意四身 · 内在感知的工具'),
    ('buddhi.html', '觉 / Buddhi', '🧠', '分辨的智 · 内在的智慧'),
    ('asat.html', '非存在 / Asat', '❌', '虚幻的显现 · 与真相对的非实'),
    ('anubhava.html', '亲证 / Anubhava', '💫', '直接体验 · 超越文字的证悟'),
    ('paramatma.html', '超灵 / Paramatma', '🔆', '最高我 · 宇宙的自我'),
    ('prakriti.html', '自性 / Prakriti', '🌱', '原质 · 物质世界的源头'),
    ('purusha.html', '神我 / Purusha', '👁️', '原人 · 纯粹的觉知'),
    ('nirguna.html', '无德 / Nirguna', '🌌', '无属性 · 超越一切描述的梵'),
    ('saguna.html', '有德 / Saguna', '👑', '有属性 · 人格化的梵'),
    ('guna.html', '三德 / Guna', '⚖️', '属性 · 构成自然的三种特质'),
    ('vikalpa.html', '分别 / Vikalpa', '🔀', '妄想 · 制造二元的思维'),
]

print(f"Will create {len(concepts)} concept pages...")

# For this test, let's just create 3 important ones
selected = concepts[:5]

for filename, title, icon, subtitle in selected:
    # Create a simple version based on karma.html structure
    html = template
    html = html.replace('☸️ 业力 / Karma', f'{icon} {title}')
    html = html.replace('业力/Karma', title)
    html = html.replace('因果法则 · 行为的反作用力', subtitle)
    html = html.replace('karma.html', filename)
    
    # Write file
    filepath = f'/workspace/pages/concepts/{filename}'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created: {filepath}')

print(f'\nSuccessfully created {len(selected)} concept pages!')
