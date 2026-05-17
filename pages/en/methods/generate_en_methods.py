import os

DIR = 'f:/26年4月/kb01/pages/en/methods/'

def make_method_page(slug, title, emoji, path_tag, summary, steps, tips):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Practice Method | Ramana Maharshi</title>
    <link rel="stylesheet" href="../styles.min.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🙏%3C/text%3E%3C/svg%3E">
    <style>
        .method-hero {{ background: rgba(100, 200, 255, 0.05); padding: 40px; border-radius: 20px; margin-bottom: 30px; border: 1px solid rgba(100, 200, 255, 0.1); }}
        .method-emoji {{ font-size: 3em; margin-bottom: 15px; }}
        .path-badge {{ display: inline-block; padding: 4px 12px; border-radius: 12px; font-size: 0.85em; margin-bottom: 15px; background: rgba(100, 200, 255, 0.2); color: #64c8ff; }}
        .section-title {{ color: #64c8ff; border-left: 4px solid #64c8ff; padding-left: 15px; margin: 30px 0 20px 0; }}
        .practice-step {{ background: rgba(255, 255, 255, 0.03); padding: 20px; border-radius: 10px; margin-bottom: 15px; border-left: 3px solid rgba(100, 200, 255, 0.3); }}
        .step-num {{ font-weight: bold; color: #64c8ff; margin-right: 10px; }}
        .tip-box {{ background: rgba(255, 165, 0, 0.05); border: 1px dashed rgba(255, 165, 0, 0.3); padding: 20px; border-radius: 10px; margin-top: 30px; }}
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
                    <a href="../index.html" class="sidebar-item">🏛️ Home</a>
                    <a href="../books/index.html" class="sidebar-item">📖 Books</a>
                    <a href="../concepts/index.html" class="sidebar-item">🔮 Concepts <span class="count">85+</span></a>
                    <a href="index.html" class="sidebar-item active">🛤️ Methods <span class="count">12</span></a>
                    <a href="../qa/index.html" class="sidebar-item">💬 Q&A <span class="count">15</span></a>
                </div>
            </div>
        </aside>

        <main class="content">
            <div class="language-switcher">
                <a href="https://ramanamaharshi.space/methods/{slug.replace('-detail', '')}.html">简体</a>
                <a href="https://ramanamaharshi.space/zh-TW/methods/{slug.replace('-detail', '')}.html">繁體</a>
                <a href="https://ramanamaharshi.space/en/methods/{slug}.html" class="active">EN</a>
            </div>

            <div class="main-content">
                <nav class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Methods</a> / <span>{title}</span></nav>
                
                <div class="method-hero">
                    <div class="method-emoji">{emoji}</div>
                    <span class="path-badge">{path_tag}</span>
                    <h1>{title}</h1>
                    <p>{summary}</p>
                </div>

                <h2 class="section-title">How to Practice</h2>
                <div class="steps-container">
                    {steps}
                </div>

                <div class="tip-box">
                    <h3 style="color:#ffcc66;margin-top:0;">💡 Practical Tips</h3>
                    {tips}
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
    
    with open(os.path.join(DIR, f"{slug}.html"), 'w', encoding='utf-8') as f:
        f.write(html)

METHODS = [
    {
        "slug": "self-inquiry-detail",
        "title": "Self-Inquiry (Atma Vichara)",
        "emoji": "🔍",
        "path_tag": "Jnana Yoga",
        "summary": "The most direct method to realize the Self by investigating the source of the 'I'-thought.",
        "steps": '''
            <div class="practice-step"><span class="step-num">01.</span> When a thought arises, do not follow it. Ask: "To whom does this thought arise?"</div>
            <div class="practice-step"><span class="step-num">02.</span> The answer will be "To me." Then ask: "Who am I?"</div>
            <div class="practice-step"><span class="step-num">03.</span> Keep the mind fixed on the source of the "I", avoiding all other thoughts.</div>
        ''',
        "tips": "<p>Consistency is key. Do not worry about progress; just keep returning to the question 'Who am I?'</p>"
    },
    {
        "slug": "surrender-detail",
        "title": "Surrender (Saranagati)",
        "emoji": "🙏",
        "path_tag": "Bhakti Yoga",
        "summary": "Giving up the individual ego to the Divine or the Guru.",
        "steps": '''
            <div class="practice-step"><span class="step-num">01.</span> Recognize that a higher power governs everything.</div>
            <div class="practice-step"><span class="step-num">02.</span> Hand over all your burdens and worries to that power.</div>
            <div class="practice-step"><span class="step-num">03.</span> Accept whatever happens as the will of the Divine.</div>
        ''',
        "tips": "<p>True surrender means having no personal will other than the Divine will.</p>"
    },
    {
        "slug": "devotion-detail",
        "title": "Devotion (Bhakti)",
        "emoji": "💝",
        "path_tag": "Bhakti Yoga",
        "summary": "The path of love and devotion towards the Divine.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Cultivate love for a chosen form of God or the Guru.</div><div class="practice-step"><span class="step-num">02.</span> Sing praises, offer prayers, and think of the Divine constantly.</div>',
        "tips": "<p>Bhakti and Jnana are not different; they meet in the Heart.</p>"
    },
    {
        "slug": "mantra-detail",
        "title": "Mantra and Japa",
        "emoji": "📿",
        "path_tag": "Mantra Yoga",
        "summary": "Repetition of sacred names or sounds to steady the mind.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Choose a mantra given by a Guru or one you have faith in.</div><div class="practice-step"><span class="step-num">02.</span> Repeat it with focus, either aloud or mentally.</div>',
        "tips": "<p>Mental Japa is more powerful than vocal Japa.</p>"
    },
    {
        "slug": "meditation-detail",
        "title": "Meditation (Dhyana)",
        "emoji": "🧘",
        "path_tag": "Raja Yoga",
        "summary": "Achieving one-pointedness of mind through sustained focus.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Sit in a comfortable posture.</div><div class="practice-step"><span class="step-num">02.</span> Focus on a single object, breath, or the sense of "I".</div>',
        "tips": "<p>The goal of meditation is to reach the state beyond meditation.</p>"
    },
    {
        "slug": "grace-detail",
        "title": "Guru's Grace",
        "emoji": "✨",
        "path_tag": "Grace",
        "summary": "The subtle influence of the Guru that leads to awakening.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Be open and receptive to the Guru\'s presence.</div><div class="practice-step"><span class="step-num">02.</span> Abide in the silence taught by the Guru.</div>',
        "tips": "<p>Grace is always available; we only need to turn towards it.</p>"
    },
    {
        "slug": "arunachala-detail",
        "title": "Arunachala Practice",
        "emoji": "⛰️",
        "path_tag": "Arunachala",
        "summary": "Connecting with the spiritual energy of the sacred hill.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Perform Girivalam (circumambulation) around the hill.</div><div class="practice-step"><span class="step-num">02.</span> Meditate with the hill as the physical symbol of the Self.</div>',
        "tips": "<p>Arunachala is the silent Guru in the form of a mountain.</p>"
    },
    {
        "slug": "scripture-detail",
        "title": "Scripture Study",
        "emoji": "📖",
        "path_tag": "Sravana",
        "summary": "Reading and contemplating the teachings of the Sages.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Read core texts like "Talks with Sri Ramana Maharshi".</div><div class="practice-step"><span class="step-num">02.</span> Reflect deeply on the meaning of the teachings.</div>',
        "tips": "<p>Study should lead to practice, not just intellectual accumulation.</p>"
    },
    {
        "slug": "silence-detail",
        "title": "Silence (Mauna)",
        "emoji": "🤫",
        "path_tag": "Direct Path",
        "summary": "The practice of remaining in silent awareness.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Observe periods of external silence.</div><div class="practice-step"><span class="step-num">02.</span> Cultivate internal silence by stilling the mind.</div>',
        "tips": "<p>True silence is the state of the Self, beyond speech and thought.</p>"
    },
    {
        "slug": "sleep-detail",
        "title": "Sleep Practice",
        "emoji": "🌙",
        "path_tag": "Yoga Nidra",
        "summary": "Maintaining awareness through the states of waking, dreaming, and deep sleep.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Remain aware of the "I" as you fall asleep.</div><div class="practice-step"><span class="step-num">02.</span> Recognize the continuity of awareness during sleep.</div>',
        "tips": "<p>Deep sleep is a glimpse of the Self, minus the ego.</p>"
    },
    {
        "slug": "knower-detail",
        "title": "Knower of the Body",
        "emoji": "👁️",
        "path_tag": "Kshetrajna",
        "summary": "The practice of identifying as the witness of the body.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Observe the body as an object separate from the Self.</div><div class="practice-step"><span class="step-num">02.</span> Inquire: "Who is the knower of this body?"</div>',
        "tips": "<p>You are not the body; you are the awareness in which it appears.</p>"
    },
    {
        "slug": "seva-detail",
        "title": "Selfless Service (Seva)",
        "emoji": "🤝",
        "path_tag": "Karma Yoga",
        "summary": "Performing actions without desire for personal gain.",
        "steps": '<div class="practice-step"><span class="step-num">01.</span> Perform your duties with the attitude of service.</div><div class="practice-step"><span class="step-num">02.</span> Offer the fruits of your actions to the Divine.</div>',
        "tips": "<p>Seva purifies the mind and prepares it for Jnana.</p>"
    }
]

for m in METHODS:
    make_method_page(m['slug'], m['title'], m['emoji'], m['path_tag'], m['summary'], m['steps'], m['tips'])
