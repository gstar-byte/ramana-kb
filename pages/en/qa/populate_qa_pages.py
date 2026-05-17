import os

# Base directory for English QA pages
DIR = 'f:/26年4月/kb01/pages/en/qa/'

def make_qa_page(filename, title, description, category, count, qa_items):
    items_html = ""
    for item in qa_items:
        items_html += f'''
                        <div class="qa-item">
                            <h3 class="qa-q">❓ {item['q']}</h3>
                            <div class="qa-a">{item['a']}{f'<div class="quote-box">{item["quote"]}<div class="source">— Sri Ramana Maharshi</div></div>' if 'quote' in item else ""}</div>
                        </div>'''

    page_num = int(filename.split('-')[1].split('.')[0])
    prev_link = f"qa-{page_num-1}.html" if page_num > 1 else "index.html"
    next_link = f"qa-{page_num+1}.html" if page_num < 15 else "index.html"
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Ramana Maharshi Q&A</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../styles.min.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🙏%3C/text%3E%3C/svg%3E">
    <style>
        /* Fix for fixed topbar overlapping content */
        .content-wrapper {{
            margin-top: 60px !important;
        }}
    </style>
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 Sri Ramana KB</a>
                <button class="sidebar-close-btn" title="Close sidebar">◀</button>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 Navigation</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item">📖 Books <span class="count">17</span></a>
                    <a href="../concepts/index.html" class="sidebar-item">🔮 Concepts <span class="count">85+</span></a>
                    <a href="../methods/index.html" class="sidebar-item">🛤️ Methods <span class="count">12</span></a>
                    <a href="index.html" class="sidebar-item active">💬 Q&A <span class="count">15</span></a>
                    <a href="../persons/index.html" class="sidebar-item">👤 Persons <span class="count">3</span></a>
                    <a href="../graph.html" class="sidebar-item">🕸️ Knowledge Graph</a>
                </div>
            </div>
        </aside>

        <main class="main-content">
            <header class="topbar">
                <button class="sidebar-open-btn" title="Open sidebar">▶</button>
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">💬 Q&A</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">Home</a>
                    <a href="../books/index.html">Books</a>
                    <a href="../concepts/index.html">Concepts</a>
                    <a href="../methods/index.html">Methods</a>
                    <a href="index.html" class="active">Q&A</a>
                    <a href="../persons/index.html">Persons</a>
                    <a href="../graph.html">Graph</a>
                    <div class="lang-dropdown"><button class="lang-dropdown-btn">EN ▾</button><div class="lang-dropdown-menu"><a href="../../qa/{filename}">简体中文</a></div></div>
                </nav>
            </header>

            <div class="content-wrapper">
                <nav class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Q&A</a> / <span>{category}</span></nav>
                <div class="page-header">
                    <h1>💬 {title}</h1>
                    <p class="subtitle">{description}</p>
                </div>
                <div class="qa-container">
                    {items_html}
                </div>
                <div class="pagination">
                    <a href="{prev_link}" class="page-link">Previous</a>
                    <a href="index.html" class="page-link">Index</a>
                    <a href="{next_link}" class="page-link">Next</a>
                </div>
            </div>
        </main>
    </div>
    <script src="../bundle.min.js"></script>
    <script>
    function toggleSidebar() {{
        var s=document.getElementById('sidebar'),o=document.getElementById('sidebarOverlay');
        if(!s)return;
        var open=s.classList.toggle('open');
        if(o)o.classList.toggle('active',open);
    }}
    </script>
</body>
</html>'''

QA_DATA = [
    {
        "filename": "qa-1.html",
        "title": "Self and Ego",
        "description": "Fundamental questions on the difference between the true Self and the false ego.",
        "category": "Self-Inquiry",
        "items": [
            {"q": "What is the Self?", "a": "The Self is the 'I am' - the pure consciousness that is the witness of all experience. It is not within time or space, nor does it depend on any external conditions. It is your deepest essence."},
            {"q": "What is the difference between Self and ego?", "a": "The Self is eternal existence, pure 'I am'. The ego is a false identification with the body, name, and role. Ego is a product of ignorance; the Self is Reality itself."},
            {"q": "How to recognize the Self?", "a": "By inquiring 'Who am I?'. When other thoughts arise, let them go and keep asking. This redirects attention inward until only the pure 'I am' remains."},
            {"q": "Where is the Self located in the body?", "a": "The Maharshi pointed to the 'Heart' (Hridaya) on the right side of the chest. This is not the physical heart but the spiritual center from which the 'I' arises."},
            {"q": "Is the mind an obstacle?", "a": "The mind is the only obstacle. It is nothing but a bundle of thoughts. When the mind is quieted through inquiry, the Self reveals itself spontaneously."}
        ]
    },
    {
        "filename": "qa-2.html",
        "title": "Practice of Self-Inquiry",
        "description": "Practical guidance on how to perform Atma-Vichara in daily life.",
        "category": "Practice",
        "items": [
            {"q": "How to start Self-Inquiry?", "a": "Whenever a thought arises, ask: 'To whom has this thought arisen?'. The answer will be 'To me'. Then ask: 'Who am I?'. This brings the mind back to its source."},
            {"q": "Can I practice while working?", "a": "Yes. Let the body do the work while the mind remains anchored in the Self. It is like an actor playing a role while knowing his true identity."},
            {"q": "What if I can't concentrate?", "a": "Concentration is not necessary. What is required is to turn the attention inward. Every time the mind wanders, bring it back by asking 'To whom did this thought occur?'."},
            {"q": "Is a Guru necessary?", "a": "The Guru is the Self. Externally, the Guru pushes you inward; internally, the Self pulls you in. They are one and the same."}
        ]
    },
    {
        "filename": "qa-3.html",
        "title": "Silence and Teaching",
        "description": "Why the Maharshi taught in silence and the power of silent presence.",
        "category": "Teaching",
        "items": [
            {"q": "Why is silence the highest teaching?", "a": "Words are only pointers to the Truth. Truth itself is beyond words. Silence is the perfect instruction because it directly transmits the state of the Self."},
            {"q": "How does silent presence work?", "a": "In the presence of a Sage, the mind of the seeker naturally becomes still. This is the power of Grace acting through silence."},
            {"q": "Did the Maharshi ever talk?", "a": "He answered questions with great patience for those who could not understand his silence. But he always said that his silent teaching was more potent."}
        ]
    }
]

# Adding more data for pages 4-15 with translated content themes
themes = [
    ("Surrender", "The path of devotion and letting go of personal will."),
    ("Grace", "The ever-present blessing that guides the seeker."),
    ("Samadhi", "The state of absorption in the Self."),
    ("Dream and Reality", "Comparing the waking state to the dream state."),
    ("Karma and Fate", "Understanding destiny and free will."),
    ("The Guru", "The role of the external and internal Master."),
    ("World and Illusion", "The nature of the manifested universe as Maya."),
    ("Liberation (Moksha)", "The final freedom from the cycle of birth and death."),
    ("Daily Conduct", "How a seeker should live and interact in the world."),
    ("Diet and Health", "The impact of food on the mind and practice."),
    ("Meditation vs. Inquiry", "Clarifying the difference between Dhyana and Vichara."),
    ("Final Realization", "The state of the Jivanmukta (liberated while alive).")
]

for i, (topic, desc) in enumerate(themes, 4):
    QA_DATA.append({
        "filename": f"qa-{i}.html",
        "title": topic,
        "description": desc,
        "category": "Philosophy",
        "items": [
            {"q": f"What is the essence of {topic}?", "a": f"In the Maharshi's teaching, {topic.lower()} is fundamentally about returning to the source. It is not about gaining something new, but about removing the ignorance that veils the truth."},
            {"q": f"How should a seeker approach {topic}?", "a": "By remaining as one is, without the interference of the ego. This is the simplest and most direct way to realize the truth of any spiritual concept."}
        ]
    })

# Generate the pages
for page in QA_DATA:
    html = make_qa_page(page['filename'], page['title'], page['description'], page['category'], len(page['items']), page['items'])
    with open(os.path.join(DIR, page['filename']), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {page['filename']}")
