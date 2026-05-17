import os

DIR = 'f:/26年4月/kb01/pages/en/concepts/'

CATEGORIES = [
    {
        "name": "🔮 Ontology",
        "items": [
            {"slug": "self", "title": "Self (Atman)", "desc": "The eternal, unchanging reality"},
            {"slug": "brahman", "title": "Brahman", "desc": "The Absolute Reality"},
            {"slug": "heart", "title": "Heart (Hrdaya)", "desc": "The seat of the Self"},
            {"slug": "maya", "title": "Maya", "desc": "The power of illusion"},
            {"slug": "satchidananda", "title": "Satchidananda", "desc": "Nature of Brahman"},
            {"slug": "advaita", "title": "Advaita", "desc": "Non-duality"},
            {"slug": "satya", "title": "Satya", "desc": "The Truth"}
        ]
    },
    {
        "name": "🧠 Mind and Ego",
        "items": [
            {"slug": "mind", "title": "Mind (Citta)", "desc": "The instrument of thought"},
            {"slug": "ego", "title": "Ego (Ahamkara)", "desc": "False identification"},
            {"slug": "aham-vritti", "title": "Aham-vritti", "desc": "The root I-thought"},
            {"slug": "vasanas", "title": "Vasanas", "desc": "Latent tendencies"},
            {"slug": "samskara", "title": "Samskara", "desc": "Subconscious imprints"},
            {"slug": "avidya", "title": "Avidya", "desc": "Ignorance"},
            {"slug": "chit-jada-granthi", "title": "Knot of Matter", "desc": "The bond of ego"},
            {"slug": "awareness", "title": "Awareness", "desc": "Pure observation"}
        ]
    },
    {
        "name": "🛤️ Practice Methods",
        "items": [
            {"slug": "self-inquiry", "title": "Self-Inquiry", "desc": "The direct path"},
            {"slug": "sadhana", "title": "Sadhana", "desc": "Spiritual practice"},
            {"slug": "bhakti", "title": "Bhakti", "desc": "Path of devotion"},
            {"slug": "samadhi", "title": "Samadhi", "desc": "Advanced meditation"},
            {"slug": "surrender", "title": "Surrender", "desc": "Letting go"},
            {"slug": "japa", "title": "Japa", "desc": "Repetition of names"},
            {"slug": "silence", "title": "Silence", "desc": "The highest teaching"},
            {"slug": "vichara", "title": "Vichara", "desc": "Deep investigation"}
        ]
    },
    {
        "name": "☸️ Karma and Reincarnation",
        "items": [
            {"slug": "karma", "title": "Karma", "desc": "Action and reaction"},
            {"slug": "prarabdha", "title": "Prarabdha", "desc": "Destined karma"},
            {"slug": "samsara", "title": "Samsara", "desc": "Cycle of rebirth"},
            {"slug": "jiva", "title": "Jiva", "desc": "Individual soul"},
            {"slug": "fate", "title": "Fate", "desc": "The law of destiny"},
            {"slug": "freewill", "title": "Free Will", "desc": "Beyond karma"}
        ]
    },
    {
        "name": "🕊️ Liberation and States",
        "items": [
            {"slug": "moksha", "title": "Moksha", "desc": "Final liberation"},
            {"slug": "jivanmukti", "title": "Jivanmukti", "desc": "Liberated while living"},
            {"slug": "jnani", "title": "Jnani", "desc": "The realized sage"},
            {"slug": "enlightenment", "title": "Enlightenment", "desc": "Self-Realization"},
            {"slug": "sahaja", "title": "Sahaja", "desc": "The natural state"},
            {"slug": "peace", "title": "Peace (Shanti)", "desc": "Inner tranquility"},
            {"slug": "nishtha", "title": "Nishtha", "desc": "Steady abidance"},
            {"slug": "moksha-path", "title": "Path to Moksha", "desc": "The journey to freedom"}
        ]
    },
    {
        "name": "✨ Guru and Grace",
        "items": [
            {"slug": "guru", "title": "Guru", "desc": "The spiritual guide"},
            {"slug": "grace", "title": "Grace (Anugraha)", "desc": "The power of awakening"},
            {"slug": "antaryamin", "title": "Inner Guide", "desc": "The Guru within"},
            {"slug": "upadesha", "title": "Upadesha", "desc": "Instruction"},
            {"slug": "satsang", "title": "Satsang", "desc": "Holy association"},
            {"slug": "darshana", "title": "Darshana", "desc": "Auspicious sight"},
            {"slug": "sharanagati", "title": "Sharanagati", "desc": "Total surrender"}
        ]
    },
    {
        "name": "🌀 Consciousness and Yoga",
        "items": [
            {"slug": "turiya", "title": "Turiya", "desc": "The fourth state"},
            {"slug": "kundalini", "title": "Kundalini", "desc": "Primordial energy"},
            {"slug": "yoga", "title": "Yoga", "desc": "Path of union"},
            {"slug": "tapas", "title": "Tapas", "desc": "Spiritual austerity"},
            {"slug": "mantra", "title": "Mantra", "desc": "Sacred sound"},
            {"slug": "shakti", "title": "Shakti", "desc": "Divine power"}
        ]
    },
    {
        "name": "⚖️ Laws and Ethics",
        "items": [
            {"slug": "dharma", "title": "Dharma", "desc": "Righteousness"},
            {"slug": "isvara", "title": "Isvara", "desc": "The Personal God"},
            {"slug": "klesha", "title": "Klesha", "desc": "Mental afflictions"},
            {"slug": "smriti", "title": "Smriti", "desc": "Remembrance"},
            {"slug": "viveka", "title": "Viveka", "desc": "Discrimination"},
            {"slug": "vairagya", "title": "Vairagya", "desc": "Dispassion"},
            {"slug": "svasthya", "title": "Svasthya", "desc": "Self-abidance"},
            {"slug": "santosha", "title": "Santosha", "desc": "Contentment"}
        ]
    },
    {
        "name": "🌱 Other Concepts",
        "items": [
            {"slug": "abhyasa", "title": "Abhyasa", "desc": "Persistent practice"},
            {"slug": "anubhava", "title": "Anubhava", "desc": "Direct experience"},
            {"slug": "awareness", "title": "Awareness", "desc": "Pure consciousness"},
            {"slug": "body", "title": "The Body", "desc": "Physical sheath"},
            {"slug": "buddhi", "title": "Buddhi", "desc": "Higher intellect"},
            {"slug": "dhyana", "title": "Dhyana", "desc": "Meditation"},
            {"slug": "lakshya", "title": "Lakshya", "desc": "Point of focus"},
            {"slug": "mano", "title": "Mano", "desc": "Lower mind"},
            {"slug": "prana", "title": "Prana", "desc": "Life force"}
        ]
    }
]

def generate_index():
    grid_html = ""
    for cat in CATEGORIES:
        links_html = ""
        for item in cat['items']:
            links_html += f'                        <a href="{item["slug"]}.html">{item["title"]} — {item["desc"]}</a>\n'
        
        grid_html += f'''
                    <div class="concept-category">
                        <h3>{cat['name']}</h3>
{links_html}                    </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Core Concepts | Ramana Maharshi Knowledge Base</title>
    <link rel="stylesheet" href="../styles.min.css">
    <style>
        .concept-categories {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 30px; }}
        .concept-category {{ background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 25px; }}
        .concept-category h3 {{ color: #64c8ff; margin-bottom: 15px; border-bottom: 1px solid rgba(100, 200, 255, 0.2); padding-bottom: 10px; }}
        .concept-category a {{ display: block; color: rgba(255, 255, 255, 0.8); text-decoration: none; margin-bottom: 8px; font-size: 0.9em; }}
        .concept-category a:hover {{ color: #64c8ff; }}
        @media (max-width: 768px) {{ .concept-categories {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 Sri Ramana KB</a>
                <button class="sidebar-close-btn">◀</button>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 Navigation</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item">📖 Books</a>
                    <a href="index.html" class="sidebar-item active">🔮 Concepts</a>
                    <a href="../methods/index.html" class="sidebar-item">🛤️ Methods</a>
                    <a href="../qa/index.html" class="sidebar-item">💬 Q&A</a>
                </div>
            </div>
        </aside>

        <main class="content">
            <div class="language-switcher">
                <a href="/concepts/index.html">简体</a>
                <a href="/zh-TW/concepts/index.html">繁體</a>
                <a href="/en/concepts/index.html" class="active">EN</a>
            </div>

            <div class="main-content">
                <nav class="breadcrumb"><a href="../index.html">Home</a> / <span>Concepts</span></nav>
                <header class="page-header">
                    <h1>🔮 Core Concepts</h1>
                    <p class="subtitle">80+ Core Concepts · Key Insights for Self-Realization</p>
                </header>

                <div class="concept-categories">
                    {grid_html}
                </div>
            </div>
        </main>
    </div>
    <script src="../bundle.min.js"></script>
    <script>
        function toggleSidebar() {{
            document.getElementById('sidebar').classList.toggle('open');
            document.getElementById('sidebarOverlay').classList.toggle('active');
        }}
    </script>
</body>
</html>'''

    with open(os.path.join(DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    generate_index()
