"""Extract chapter content from surpassing_love.txt for chapters 1-8 (chapters 9-10 not in PDF)"""
import re, json

with open('pdf_content/surpassing_love.txt', 'r', encoding='utf-8') as f:
    content = f.read()

def clean_garbled(text):
    return re.sub(r'(.)\1{4,}', r'\1', text)

parts = content.split('--- 第')
pages = {}
for part in parts[1:]:
    m = re.match(r'(\d+)页 ---(.*)', part, re.DOTALL)
    if m:
        pages[int(m.group(1))] = m.group(2)

# Manual PDF page mapping based on analysis
# Each chapter: (start_pdf_page, end_pdf_page_exclusive, title)
chapters_map = {
    1: (11, 24, 'Reminiscences-I — Viswanatha Swami'),
    2: (24, 29, 'From Early Days'),
    3: (29, 40, "Scenes from Ramana's Life — B.V. Narasimha Swami"),
    4: (40, 65, 'How Bhagavan Came to Me'),
    5: (65, 70, 'Incidents Connected with the Life of Sri Bhagavan — M.V. Krishnan'),
    6: (70, 72, "Lessons from Bhagavan's Life — K.R.K. Murthy"),
    7: (72, 75, 'Loving Devotion — T.P.R.'),
    8: (75, 81, 'Memorable Days with the Sage of Arunachala'),
}

chapters = {}
for ch_num, (start, end, title) in sorted(chapters_map.items()):
    parts_list = []
    for pn in range(start, end):
        if pn in pages:
            cleaned = clean_garbled(pages[pn])
            # Remove literal \n remnants
            cleaned = cleaned.replace('\\n', ' ')
            # Remove leading \n
            cleaned = cleaned.lstrip('\r\n')
            parts_list.append(cleaned)
    
    full_text = '\r\n\r\n'.join(parts_list)
    # Remove standalone book page numbers at start of sections
    full_text = re.sub(r'^\d{1,3}\r\n', '', full_text, flags=re.MULTILINE)
    # Clean up whitespace
    full_text = re.sub(r'\r\n{3,}', '\r\n\r\n', full_text)
    full_text = full_text.strip()
    
    chapters[ch_num] = {
        'title': title,
        'content': full_text,
        'chars': len(full_text),
    }

for ch_num, data in sorted(chapters.items()):
    print(f"Ch {ch_num} ({data['title']}): {data['chars']} chars")
    print(f"  Preview: {data['content'][:200]}...")

with open('chapters_sl_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(chapters)} chapters to chapters_sl_extracted.json")
print("Note: Chapters 9-10 are not covered in the PDF (only 80 pages scanned, book ends at page ~296)")
