import os

DIR = 'f:/26年4月/kb01/pages/en/concepts/'
BASE = '../'

def make_page(slug, title, emoji, subtitle, tags, html_content):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Ramana Maharshi Knowledge Base</title>
    <meta name="description" content="{title} - Core concepts of Sri Ramana Maharshi's spiritual teachings.">
    <link rel="stylesheet" href="../styles.min.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🙏%3C/text%3E%3C/svg%3E">
    <style>
        .content-wrapper {{ margin-top: 60px !important; }}
        .concept-section {{ margin-bottom: 2rem; }}
    </style>
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 Ramana Knowledge Base</a>
                <button class="sidebar-close-btn" title="Close sidebar">◀</button>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 Core Index</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item">📖 Books <span class="count">18</span></a>
                    <a href="index.html" class="sidebar-item active">🔮 Concepts <span class="count">50+</span></a>
                    <a href="../methods/index.html" class="sidebar-item">🛤️ Methods <span class="count">12</span></a>
                    <a href="../qa/index.html" class="sidebar-item">💬 Q&A <span class="count">600</span></a>
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
                    <span class="topbar-title">🔮 Core Concepts</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">Home</a>
                    <a href="../books/index.html">Books</a>
                    <a href="index.html" class="active">Concepts</a>
                    <a href="../methods/index.html">Methods</a>
                    <a href="../qa/index.html">Q&A</a>
                    <a href="../persons/index.html">Persons</a>
                    <a href="../graph.html">Graph</a>
                    <div class="lang-dropdown">
                        <button class="lang-dropdown-btn">EN ▾</button>
                        <div class="lang-dropdown-menu">
                            <a href="../../concepts/{slug}.html">简体中文</a>
                            <a href="../../zh-TW/concepts/{slug}.html">繁體中文</a>
                        </div>
                    </div>
                </nav>
            </header>

            <div class="content-wrapper">
                <nav class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Concepts</a> / <span>{title}</span></nav>
                
                <header class="page-header">
                    <h1>{emoji} {title}</h1>
                    <p class="subtitle">{subtitle}</p>
                </header>

                {html_content}

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">🔗 Related Concepts</h2>
                    <div class="concept-tags">
                        {tags}
                    </div>
                </div>
            </div>

            <footer class="site-footer">
                <p>© 2026 Ramana Maharshi Knowledge Base | Heritage of Arunachala</p>
            </footer>
        </main>
    </div>
    <script src="../bundle.min.js" defer></script>
    <script>
        function toggleSidebar() {{
            document.getElementById('sidebar').classList.toggle('open');
        }}
    </script>
</body>
</html>'''


PAGES = [
    {
        "slug": "maya",
        "title": "Maya (Illusion)",
        "emoji": "🌊",
        "subtitle": "The Power of Illusion that Veils the Reality",
        "tags": '<a href="brahman.html" class="tag">Brahman</a><a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>What is Maya?</h2><p>Maya is the mysterious power that makes the One Reality appear as a manifold world. It is a "creative illusion" with no independent existence.</p></div>'
    },
    {
        "slug": "brahman",
        "title": "Brahman (The Absolute)",
        "emoji": "🌀",
        "subtitle": "The Ultimate Reality - One Without a Second",
        "tags": '<a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>The Absolute</h2><p>Brahman is the Sanskrit name for the Ultimate Reality. In the experience of the Jnani, Brahman is all that exists.</p></div>'
    },
    {
        "slug": "karma",
        "title": "Karma and Fate",
        "emoji": "⚖️",
        "subtitle": "Destiny and the Path Beyond Both",
        "tags": '<a href="surrender.html" class="tag">Surrender</a>',
        "content": '<div class="concept-section"><h2>The Law of Karma</h2><p>As long as one identifies with the body, one is bound by the laws of action and reaction (Karma).</p></div>'
    },
    {
        "slug": "samadhi",
        "title": "Samadhi (Absorption)",
        "emoji": "🧘",
        "subtitle": "The State of Absorption in the Self",
        "tags": '<a href="peace.html" class="tag">Peace</a>',
        "content": '<div class="concept-section"><h2>Stillness</h2><p>Samadhi is the state where the mind becomes still and merges into its source, the Self.</p></div>'
    },
    {
        "slug": "jnana",
        "title": "Jnana (Knowledge)",
        "emoji": "🛤️",
        "subtitle": "The Path of Direct Knowledge",
        "tags": '<a href="self-inquiry.html" class="tag">Self-Inquiry</a>',
        "content": '<div class="concept-section"><h2>True Wisdom</h2><p>Jnana is not intellectual learning; it is the direct experience of the Self.</p></div>'
    },
    {
        "slug": "heart",
        "title": "The Heart (Hridaya)",
        "emoji": "💖",
        "subtitle": "The Spiritual Center of Being",
        "tags": '<a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>The Source</h2><p>The Heart is the center of Consciousness, the source of the "I".</p></div>'
    },
    {
        "slug": "silence",
        "title": "Silence (Mauna)",
        "emoji": "🤫",
        "subtitle": "The Highest Form of Teaching",
        "tags": '<a href="guru.html" class="tag">Guru</a>',
        "content": '<div class="concept-section"><h2>Eloquence</h2><p>Silence is the only language that can truly describe the Self.</p></div>'
    },
    {
        "slug": "moksha",
        "title": "Moksha (Liberation)",
        "emoji": "🕊️",
        "subtitle": "Freedom from the Illusion of Bondage",
        "tags": '<a href="enlightenment.html" class="tag">Enlightenment</a>',
        "content": '<div class="concept-section"><h2>Recognition</h2><p>Moksha is the recognition of your ever-present freedom.</p></div>'
    },
    {
        "slug": "advaita",
        "title": "Advaita (Non-duality)",
        "emoji": "🌀",
        "subtitle": "The Philosophy of Non-dual Reality",
        "tags": '<a href="brahman.html" class="tag">Brahman</a>',
        "content": '<div class="concept-section"><h2>Not Two</h2><p>Advaita teaches that the individual soul and the Absolute are identical.</p></div>'
    },
    {
        "slug": "vasanas",
        "title": "Vasanas (Tendencies)",
        "emoji": "🌪️",
        "subtitle": "Latent Tendencies of the Mind",
        "tags": '<a href="mind.html" class="tag">Mind</a>',
        "content": '<div class="concept-section"><h2>Seeds of Thought</h2><p>Vasanas are the latent impressions that cause thoughts and desires to arise.</p></div>'
    },
    {
        "slug": "turiya",
        "title": "Turiya (The Fourth State)",
        "emoji": "🌟",
        "subtitle": "Pure Consciousness Beyond All States",
        "tags": '<a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>The Substratum</h2><p>Turiya is the reality that underlies waking, dream, and sleep states.</p></div>'
    },
    {
        "slug": "bhakti",
        "title": "Bhakti (Devotion)",
        "emoji": "💝",
        "subtitle": "The Path of Love",
        "tags": '<a href="surrender.html" class="tag">Surrender</a>',
        "content": '<div class="concept-section"><h2>Divine Love</h2><p>Bhakti is the path of surrender to God or the Guru.</p></div>'
    },
    {
        "slug": "guru",
        "title": "The Guru",
        "emoji": "🌟",
        "subtitle": "The Inner Guide",
        "tags": '<a href="grace.html" class="tag">Grace</a>',
        "content": '<div class="concept-section"><h2>The Guide</h2><p>The Guru is the Self in human form, leading the seeker back to the source.</p></div>'
    },
    {
        "slug": "sadhana",
        "title": "Sadhana (Practice)",
        "emoji": "🕯️",
        "subtitle": "The Path of Spiritual Effort",
        "tags": '<a href="self-inquiry.html" class="tag">Self-Inquiry</a>',
        "content": '<div class="concept-section"><h2>Effort</h2><p>Sadhana is the effort required to remove obstacles to Realization.</p></div>'
    },
    {
        "slug": "vichara",
        "title": "Vichara (Enquiry)",
        "emoji": "🔍",
        "subtitle": "The Quest for the Self",
        "tags": '<a href="self-inquiry.html" class="tag">Self-Inquiry</a>',
        "content": '<div class="concept-section"><h2>The Quest</h2><p>Vichara is tracing the "I"-thought back to its source.</p></div>'
    },
    {
        "slug": "peace",
        "title": "Peace (Shanti)",
        "emoji": "🧘‍♂️",
        "subtitle": "Your Inherent Nature",
        "tags": '<a href="silence.html" class="tag">Silence</a>',
        "content": '<div class="concept-section"><h2>Innateness</h2><p>Peace is not acquired; it is revealed when the mind is quiet.</p></div>'
    },
    {
        "slug": "world",
        "title": "The World (Jagat)",
        "emoji": "🌍",
        "subtitle": "Appearance and Reality",
        "tags": '<a href="maya.html" class="tag">Maya</a>',
        "content": '<div class="concept-section"><h2>Observation</h2><p>The world is real as the Self, but unreal as an independent entity.</p></div>'
    },
    {
        "slug": "jnani",
        "title": "The Jnani (Sage)",
        "emoji": "🧙‍♂️",
        "subtitle": "The Realized One",
        "tags": '<a href="enlightenment.html" class="tag">Enlightenment</a>',
        "content": '<div class="concept-section"><h2>Abidance</h2><p>A Jnani abides in the Self while performing actions without doership.</p></div>'
    },
    {
        "slug": "shakti",
        "title": "Shakti (Power)",
        "emoji": "⚡",
        "subtitle": "Dynamic Aspect of Being",
        "tags": '<a href="brahman.html" class="tag">Brahman</a>',
        "content": '<div class="concept-section"><h2>Energy</h2><p>Shakti is the dynamic aspect of the silent Consciousness.</p></div>'
    },
    {
        "slug": "prarabdha",
        "title": "Prarabdha (Destiny)",
        "emoji": "🏹",
        "subtitle": "The Fruit of Past Actions",
        "tags": '<a href="karma.html" class="tag">Karma</a>',
        "content": '<div class="concept-section"><h2>Destiny</h2><p>Prarabdha is the karma destined to be worked out in this life.</p></div>'
    },
    {
        "slug": "scripture-study",
        "title": "Scripture Study",
        "emoji": "✍️",
        "subtitle": "The Role of Sacred Texts",
        "tags": '<a href="jnana.html" class="tag">Jnana</a>',
        "content": '<div class="concept-section"><h2>Purpose of Study</h2><p>Bhagavan taught that scriptures are useful to point the way, but they must eventually be transcended for direct experience.</p></div>'
    },
    {
        "slug": "sleep-practice",
        "title": "Sleep Practice",
        "emoji": "💤",
        "subtitle": "Awareness in the Transition to Sleep",
        "tags": '<a href="turiya.html" class="tag">Turiya</a>',
        "content": '<div class="concept-section"><h2>Beyond Dreams</h2><p>Practice being aware at the moment of falling asleep to recognize the state of pure awareness that persists even in deep sleep.</p></div>'
    },
    {
        "slug": "knower-of-body",
        "title": "Knower of the Body",
        "emoji": "⚡",
        "subtitle": "Investigating the Subject",
        "tags": '<a href="self-inquiry.html" class="tag">Self-Inquiry</a>',
        "content": '<div class="concept-section"><h2>Who Knows?</h2><p>Investigate who is the knower of the body and its sensations. This leads back to the Self.</p></div>'
    },
    {
        "slug": "arunachala",
        "title": "Arunachala",
        "emoji": "⛰️",
        "subtitle": "The Holy Mountain of Fire",
        "tags": '<a href="guru.html" class="tag">Guru</a>',
        "content": '<div class="concept-section"><h2>The Hill of Grace</h2><p>Arunachala is the Self in the form of a hill. Girivalam (circumambulation) is a powerful practice for destroying the ego.</p></div>'
    },
    {
        "slug": "mantra",
        "title": "Mantra (Japa)",
        "emoji": "📿",
        "subtitle": "Sacred Sound and Repetition",
        "tags": '<a href="bhakti.html" class="tag">Bhakti</a>',
        "content": '<div class="concept-section"><h2>Repetition</h2><p>Constant repetition of a mantra helps to steady the mind and prepare it for Self-enquiry.</p></div>'
    },
    {
        "slug": "meditation",
        "title": "Meditation",
        "emoji": "🧘",
        "subtitle": "Concentration of the Mind",
        "tags": '<a href="samadhi.html" class="tag">Samadhi</a>',
        "content": '<div class="concept-section"><h2>Steadying the Mind</h2><p>Meditation is the practice of keeping the mind focused on a single object to achieve stillness.</p></div>'
    },
    {
        "slug": "devotion",
        "title": "Devotion",
        "emoji": "💝",
        "subtitle": "The Path of the Heart",
        "tags": '<a href="bhakti.html" class="tag">Bhakti</a>',
        "content": '<div class="concept-section"><h2>Love for the Divine</h2><p>Devotion and surrender are the same. When love for the Divine becomes total, the ego disappears.</p></div>'
    },
    {
        "slug": "abhyasa",
        "title": "Abhyasa",
        "emoji": "🔄",
        "subtitle": "Constant and Determined Practice",
        "tags": '<a href="sadhana.html" class="tag">Sadhana</a>',
        "content": '<div class="concept-section"><h2>The Need for Abhyasa</h2><p>Abhyasa is the constant effort to remain in the state of the Self. Without persistent practice, the mind tends to wander back into worldliness.</p></div>'
    },
    {
        "slug": "ananda",
        "title": "Ananda (Bliss)",
        "emoji": "🌈",
        "subtitle": "The Inherent Bliss of the Self",
        "tags": '<a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>True Bliss</h2><p>Ananda is not a pleasure derived from objects; it is the very nature of the Self. When the mind is quiet, Bliss is naturally felt.</p></div>'
    },
    {
        "slug": "aham-vritti",
        "title": "Aham-vritti",
        "emoji": "🆔",
        "subtitle": "The 'I'-thought and its Source",
        "tags": '<a href="self-inquiry.html" class="tag">Self-Inquiry</a>',
        "content": '<div class="concept-section"><h2>The Root Thought</h2><p>Aham-vritti is the first-person thought. By investigating the source of this "I"-thought, it vanishes into the Heart.</p></div>'
    },
    {
        "slug": "anubhava",
        "title": "Anubhava",
        "emoji": "👁️",
        "subtitle": "Direct Experience of Reality",
        "tags": '<a href="jnana.html" class="tag">Jnana</a>',
        "content": '<div class="concept-section"><h2>Beyond Theory</h2><p>Anubhava is the direct, non-dual experience of the Self, which transcends all intellectual understanding.</p></div>'
    },
    {
        "slug": "chit",
        "title": "Chit (Pure Consciousness)",
        "emoji": "🔆",
        "subtitle": "The Light of Awareness",
        "tags": '<a href="brahman.html" class="tag">Brahman</a>',
        "content": '<div class="concept-section"><h2>The Knower</h2><p>Chit is the pure awareness that illuminates all thoughts and perceptions, yet remains unaffected by them.</p></div>'
    },
    {
        "slug": "jivanmukti",
        "title": "Jivanmukti",
        "emoji": "🔓",
        "subtitle": "Liberation While Living",
        "tags": '<a href="moksha.html" class="tag">Moksha</a>',
        "content": '<div class="concept-section"><h2>The Liberated Life</h2><p>Jivanmukti is the state of a sage who is liberated from the illusion of bondage even while the body persists.</p></div>'
    },
    {
        "slug": "manonasha",
        "title": "Manonasha",
        "emoji": "🌬️",
        "subtitle": "Destruction of the Mind",
        "tags": '<a href="samadhi.html" class="tag">Samadhi</a>',
        "content": '<div class="concept-section"><h2>Final Stillness</h2><p>Manonasha is not the loss of intelligence, but the permanent extinction of the ego-mind in the Self.</p></div>'
    },
    {
        "slug": "vairagya",
        "title": "Vairagya",
        "emoji": "🍂",
        "subtitle": "Dispassion and Non-attachment",
        "tags": '<a href="viveka.html" class="tag">Viveka</a>',
        "content": '<div class="concept-section"><h2>Letting Go</h2><p>Vairagya is the absence of desire for worldly objects, arising from the realization of their ephemeral nature.</p></div>'
    },
    {
        "slug": "viveka",
        "title": "Viveka",
        "emoji": "⚖️",
        "subtitle": "Discrimination Between Real and Unreal",
        "tags": '<a href="vairagya.html" class="tag">Vairagya</a>',
        "content": '<div class="concept-section"><h2>The Power to Discern</h2><p>Viveka is the intellectual clarity that distinguishes the eternal Self from the transient world and body.</p></div>'
    },
    {
        "slug": "satsang",
        "title": "Satsang",
        "emoji": "🤝",
        "subtitle": "Association with the Truth",
        "tags": '<a href="guru.html" class="tag">Guru</a>',
        "content": '<div class="concept-section"><h2>Holy Company</h2><p>Satsang is being in the presence of a Sage or the Self. It is the most powerful aid for a seeker.</p></div>'
    },
    {
        "slug": "isvara",
        "title": "Isvara (God)",
        "emoji": "🔱",
        "subtitle": "The Personal God and Creator",
        "tags": '<a href="brahman.html" class="tag">Brahman</a>',
        "content": '<div class="concept-section"><h2>The Role of Isvara</h2><p>Isvara is the manifestation of Brahman as the creator and sustainer of the world. Devotion to Isvara leads to the purification of the mind.</p></div>'
    },
    {
        "slug": "jiva",
        "title": "Jiva (Individual Soul)",
        "emoji": "👤",
        "subtitle": "The Individualized Consciousness",
        "tags": '<a href="ego.html" class="tag">Ego</a>',
        "content": '<div class="concept-section"><h2>The Illusion of Separation</h2><p>The Jiva is the Self identifying with the body and mind. When this identification ceases, the Jiva is realized to be Brahman.</p></div>'
    },
    {
        "slug": "kundalini",
        "title": "Kundalini",
        "emoji": "🐍",
        "subtitle": "The Primordial Energy",
        "tags": '<a href="shakti.html" class="tag">Shakti</a>',
        "content": '<div class="concept-section"><h2>The Serpent Power</h2><p>Kundalini is the spiritual energy latent in the body. Bhagavan taught that the rising of Kundalini is natural when the mind is turned inward.</p></div>'
    },
    {
        "slug": "dharma",
        "title": "Dharma",
        "emoji": "📜",
        "subtitle": "Righteousness and Cosmic Order",
        "tags": '<a href="karma.html" class="tag">Karma</a>',
        "content": '<div class="concept-section"><h2>Living in Truth</h2><p>Dharma is the way of life that is in harmony with the Self. The highest Dharma is to abide in the Self.</p></div>'
    },
    {
        "slug": "fate",
        "title": "Fate and Destiny",
        "emoji": "🌌",
        "subtitle": "The Law of Prarabdha",
        "tags": '<a href="prarabdha.html" class="tag">Prarabdha</a>',
        "content": '<div class="concept-section"><h2>Facing Destiny</h2><p>Fate is the result of past actions. One can transcend fate only by realizing the Self which is beyond all actions.</p></div>'
    },
    {
        "slug": "freewill",
        "title": "Free Will",
        "emoji": "🕊️",
        "subtitle": "Choice and Responsibility",
        "tags": '<a href="fate.html" class="tag">Fate</a>',
        "content": '<div class="concept-section"><h2>The Power of Choice</h2><p>Free will exists as long as there is an ego. The best use of free will is to turn inward and find its source.</p></div>'
    },
    {
        "slug": "yoga",
        "title": "Yoga",
        "emoji": "🧘‍♂️",
        "subtitle": "Union with the Divine",
        "tags": '<a href="sadhana.html" class="tag">Sadhana</a>',
        "content": '<div class="concept-section"><h2>Paths of Union</h2><p>Yoga is the process of uniting the individual with the Absolute. Bhagavan taught that Jnana is the ultimate Yoga.</p></div>'
    },
    {
        "slug": "tapas",
        "title": "Tapas",
        "emoji": "🔥",
        "subtitle": "Spiritual Austerity",
        "tags": '<a href="sadhana.html" class="tag">Sadhana</a>',
        "content": '<div class="concept-section"><h2>The Fire of Practice</h2><p>Tapas is the intense effort to reach the goal. The highest Tapas is to remain in the Heart without any thoughts.</p></div>'
    },
    {
        "slug": "samsara",
        "title": "Samsara",
        "emoji": "🎡",
        "subtitle": "The Cycle of Birth and Death",
        "tags": '<a href="maya.html" class="tag">Maya</a>',
        "content": '<div class="concept-section"><h2>The Wheel of Existence</h2><p>Samsara is the state of identification with the transient world. Realization of the Self is the end of Samsara.</p></div>'
    },
    {
        "slug": "japa",
        "title": "Japa",
        "emoji": "📿",
        "subtitle": "Repetition of Sacred Names",
        "tags": '<a href="mantra.html" class="tag">Mantra</a>',
        "content": '<div class="concept-section"><h2>Steadying the Mind</h2><p>Japa is the repetition of God\'s name or a mantra. It purifies the mind and leads to meditation.</p></div>'
    },
    {
        "slug": "awareness",
        "title": "Awareness",
        "emoji": "🕯️",
        "subtitle": "Pure Consciousness Without Object",
        "tags": '<a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>Being Aware</h2><p>Pure Awareness is your true nature. It is the background against which all experiences occur.</p></div>'
    },
    {
        "slug": "body",
        "title": "The Body",
        "emoji": "🧘‍♂️",
        "subtitle": "The Physical Sheath",
        "tags": '<a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>I am not the Body</h2><p>Bhagavan taught that the root of all suffering is the identification with the body. You are the Self, not the mortal frame.</p></div>'
    },
    {
        "slug": "buddhi",
        "title": "Buddhi (Intellect)",
        "emoji": "🧠",
        "subtitle": "The Discriminating Faculty",
        "tags": '<a href="viveka.html" class="tag">Viveka</a>',
        "content": '<div class="concept-section"><h2>Role of Intellect</h2><p>Buddhi is the higher mind that discriminates between the real and the unreal. When purified, it leads to the Self.</p></div>'
    },
    {
        "slug": "dhyana",
        "title": "Dhyana (Meditation)",
        "emoji": "🧘",
        "subtitle": "One-pointedness of Mind",
        "tags": '<a href="samadhi.html" class="tag">Samadhi</a>',
        "content": '<div class="concept-section"><h2>Focus on the Source</h2><p>Dhyana is the practice of keeping the mind fixed on the Self or a sacred object to achieve stillness.</p></div>'
    },
    {
        "slug": "enlightenment",
        "title": "Enlightenment",
        "emoji": "✨",
        "subtitle": "Realization of the Self",
        "tags": '<a href="moksha.html" class="tag">Moksha</a>',
        "content": '<div class="concept-section"><h2>The Great Awakening</h2><p>Enlightenment is the permanent realization of your true nature as the Absolute, ending the illusion of separation.</p></div>'
    },
    {
        "slug": "klesha",
        "title": "Klesha",
        "emoji": "⛈️",
        "subtitle": "The Afflictions of the Mind",
        "tags": '<a href="ego.html" class="tag">Ego</a>',
        "content": '<div class="concept-section"><h2>Overcoming Obstacles</h2><p>Kleshas are the mental afflictions like ignorance and attachment that cause suffering. They are removed through Jnana.</p></div>'
    },
    {
        "slug": "lakshya",
        "title": "Lakshya",
        "emoji": "🎯",
        "subtitle": "The Target of Meditation",
        "tags": '<a href="dhyana.html" class="tag">Dhyana</a>',
        "content": '<div class="concept-section"><h2>Finding the Goal</h2><p>Lakshya is the point of focus in spiritual practice. The ultimate Lakshya is the Self within.</p></div>'
    },
    {
        "slug": "mano",
        "title": "Mano (The Mind)",
        "emoji": "🌬️",
        "subtitle": "The Instrument of Thought",
        "tags": '<a href="mind.html" class="tag">Mind</a>',
        "content": '<div class="concept-section"><h2>Nature of Mind</h2><p>Mano is the lower mind, the bundle of thoughts. Its stillness is the gateway to the Self.</p></div>'
    },
    {
        "slug": "nishtha",
        "title": "Nishtha",
        "emoji": "🏛️",
        "subtitle": "Steady Abidance in the Self",
        "tags": '<a href="sahaja.html" class="tag">Sahaja</a>',
        "content": '<div class="concept-section"><h2>Unyielding Awareness</h2><p>Nishtha is the state of being firmly established in the Self, unaffected by external circumstances.</p></div>'
    },
    {
        "slug": "prana",
        "title": "Prana",
        "emoji": "💨",
        "subtitle": "The Vital Life Force",
        "tags": '<a href="mind.html" class="tag">Mind</a>',
        "content": '<div class="concept-section"><h2>Breath and Mind</h2><p>Prana and Mind are like two branches of the same tree. Control of breath leads to control of the mind.</p></div>'
    },
    {
        "slug": "sahaja",
        "title": "Sahaja Samadhi",
        "emoji": "🌊",
        "subtitle": "The Natural State",
        "tags": '<a href="samadhi.html" class="tag">Samadhi</a>',
        "content": '<div class="concept-section"><h2>Spontaneous Realization</h2><p>Sahaja is the state of natural abidance in the Self while functioning in the world, without any effort.</p></div>'
    },
    {
        "slug": "ahamkara",
        "title": "Ahamkara",
        "emoji": "🎭",
        "subtitle": "The Ego-Sense",
        "tags": '<a href="ego.html" class="tag">Ego</a>',
        "content": '<div class="concept-section"><h2>The False \'I\'</h2><p>Ahamkara is the ego-sense that identifies with the body and says "I am this". It is the source of all separation.</p></div>'
    },
    {
        "slug": "anatma",
        "title": "Anatma",
        "emoji": "🚫",
        "subtitle": "Non-Self",
        "tags": '<a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>The Not-Self</h2><p>Anatma refers to everything that is not the Self—the body, mind, and world. Realization involves detaching from the Anatma.</p></div>'
    },
    {
        "slug": "anityata",
        "title": "Anityata",
        "emoji": "⏳",
        "subtitle": "Impermanence",
        "tags": '<a href="maya.html" class="tag">Maya</a>',
        "content": '<div class="concept-section"><h2>Transient Nature</h2><p>Anityata is the quality of impermanence in all worldly things. Recognizing this leads to dispassion (Vairagya).</p></div>'
    },
    {
        "slug": "antahkarana",
        "title": "Antahkarana",
        "emoji": "🏛️",
        "subtitle": "The Inner Instrument",
        "tags": '<a href="mind.html" class="tag">Mind</a>',
        "content": '<div class="concept-section"><h2>The Mental Complex</h2><p>Antahkarana consists of the mind, intellect, ego, and memory. It is the internal tool for experiencing the world.</p></div>'
    },
    {
        "slug": "antaryamin",
        "title": "Antaryamin",
        "emoji": "💖",
        "subtitle": "The Inner Guide",
        "tags": '<a href="guru.html" class="tag">Guru</a>',
        "content": '<div class="concept-section"><h2>The Dweller Within</h2><p>Antaryamin is the Self acting as the inner ruler and guide in the hearts of all beings.</p></div>'
    },
    {
        "slug": "asat",
        "title": "Asat",
        "emoji": "🌫️",
        "subtitle": "The Unreal",
        "tags": '<a href="satya.html" class="tag">Satya</a>',
        "content": '<div class="concept-section"><h2>Illusion</h2><p>Asat is that which has no permanent existence. The world as perceived by the ego is Asat; the Self alone is Sat (Real).</p></div>'
    },
    {
        "slug": "avidya",
        "title": "Avidya",
        "emoji": "🌑",
        "subtitle": "Ignorance",
        "tags": '<a href="maya.html" class="tag">Maya</a>',
        "content": '<div class="concept-section"><h2>Root of Bondage</h2><p>Avidya is the spiritual ignorance of one\'s true nature. It is the veil that hides the light of the Self.</p></div>'
    },
    {
        "slug": "chit-jada-granthi",
        "title": "Chit-jada-granthi",
        "emoji": "🔗",
        "subtitle": "The Knot of Consciousness and Matter",
        "tags": '<a href="ego.html" class="tag">Ego</a>',
        "content": '<div class="concept-section"><h2>The Essential Bond</h2><p>This is the "knot" that binds pure consciousness to the inert body, creating the illusion of a personal "I".</p></div>'
    },
    {
        "slug": "darshana",
        "title": "Darshana",
        "emoji": "👁️",
        "subtitle": "Vision of the Divine",
        "tags": '<a href="guru.html" class="tag">Guru</a>',
        "content": '<div class="concept-section"><h2>Auspicious Sight</h2><p>Darshana is the act of seeing or being seen by a Sage or a Deity, which confers great spiritual benefit.</p></div>'
    },
    {
        "slug": "dharmata",
        "title": "Dharmata",
        "emoji": "⚖️",
        "subtitle": "The Essence of Things",
        "tags": '<a href="dharma.html" class="tag">Dharma</a>',
        "content": '<div class="concept-section"><h2>Intrinsic Nature</h2><p>Dharmata is the true nature or essence of reality, beyond all conceptual labels.</p></div>'
    },
    {
        "slug": "moksha-path",
        "title": "Path to Moksha",
        "emoji": "🕊️",
        "subtitle": "The Journey to Liberation",
        "tags": '<a href="moksha.html" class="tag">Moksha</a>',
        "content": '<div class="concept-section"><h2>Direct and Indirect Paths</h2><p>While there are many paths, Bhagavan emphasized Self-Inquiry as the most direct route to Moksha.</p></div>'
    },
    {
        "slug": "samskara",
        "title": "Samskara",
        "emoji": "🧠",
        "subtitle": "Subconscious Impressions",
        "tags": '<a href="vasanas.html" class="tag">Vasanas</a>',
        "content": '<div class="concept-section"><h2>Mental Imprints</h2><p>Samskaras are the latent impressions left by past thoughts and actions, which shape our present tendencies.</p></div>'
    },
    {
        "slug": "santosha",
        "title": "Santosha",
        "emoji": "☮️",
        "subtitle": "Contentment",
        "tags": '<a href="peace.html" class="tag">Peace</a>',
        "content": '<div class="concept-section"><h2>Inner Satisfaction</h2><p>Santosha is the state of being satisfied with whatever comes, recognizing it as the will of the Divine.</p></div>'
    },
    {
        "slug": "satchidananda",
        "title": "Satchidananda",
        "emoji": "✨",
        "subtitle": "Existence-Consciousness-Bliss",
        "tags": '<a href="brahman.html" class="tag">Brahman</a>',
        "content": '<div class="concept-section"><h2>The Nature of Reality</h2><p>This is the description of the Absolute: Sat (Eternal Existence), Chit (Pure Consciousness), and Ananda (Infinite Bliss).</p></div>'
    },
    {
        "slug": "satya",
        "title": "Satya",
        "emoji": "💎",
        "subtitle": "Truth",
        "tags": '<a href="self.html" class="tag">Self</a>',
        "content": '<div class="concept-section"><h2>The Absolute Truth</h2><p>Satya is that which is eternal and unchanging. The Self alone is the Truth; the world is a relative appearance.</p></div>'
    },
    {
        "slug": "sharanagati",
        "title": "Sharanagati",
        "emoji": "🙏",
        "subtitle": "Total Surrender",
        "tags": '<a href="surrender.html" class="tag">Surrender</a>',
        "content": '<div class="concept-section"><h2>Final Refuge</h2><p>Sharanagati is the complete and final surrender of the ego to the Guru or God.</p></div>'
    },
    {
        "slug": "shraddha",
        "title": "Shraddha",
        "emoji": "🙏",
        "subtitle": "Faith and Earnestness",
        "tags": '<a href="sadhana.html" class="tag">Sadhana</a>',
        "content": '<div class="concept-section"><h2>The Power of Faith</h2><p>Shraddha is the unwavering faith in the words of the Guru and the scriptures, which is essential for success.</p></div>'
    },
    {
        "slug": "siddhi",
        "title": "Siddhi",
        "emoji": "✨",
        "subtitle": "Supernatural Powers",
        "tags": '<a href="maya.html" class="tag">Maya</a>',
        "content": '<div class="concept-section"><h2>Distractions on the Path</h2><p>Siddhis are occult powers that may arise during practice. Bhagavan warned that they are obstacles to Self-realization.</p></div>'
    },
    {
        "slug": "smriti",
        "title": "Smriti",
        "emoji": "💭",
        "subtitle": "Remembrance",
        "tags": '<a href="mind.html" class="tag">Mind</a>',
        "content": '<div class="concept-section"><h2>Mindfulness of the Self</h2><p>Smriti is the constant remembrance of one\'s true nature or the Guru\'s presence.</p></div>'
    },
    {
        "slug": "sukha",
        "title": "Sukha",
        "emoji": "☀️",
        "subtitle": "Happiness",
        "tags": '<a href="ananda.html" class="tag">Ananda</a>',
        "content": '<div class="concept-section"><h2>Relative Joy</h2><p>Sukha is worldly happiness, which is transient. It is but a reflection of the eternal Bliss (Ananda) of the Self.</p></div>'
    },
    {
        "slug": "svasthya",
        "title": "Svasthya",
        "emoji": "🌿",
        "subtitle": "Established in the Self",
        "tags": '<a href="peace.html" class="tag">Peace</a>',
        "content": '<div class="concept-section"><h2>True Health</h2><p>Svasthya literally means "being established in one\'s own Self." It is the state of perfect health and balance.</p></div>'
    },
    {
        "slug": "upadesha",
        "title": "Upadesha",
        "emoji": "📜",
        "subtitle": "Spiritual Instruction",
        "tags": '<a href="guru.html" class="tag">Guru</a>',
        "content": '<div class="concept-section"><h2>The Guru\'s Guidance</h2><p>Upadesha is the teaching or guidance given by the Guru to the disciple to lead them to realization.</p></div>'
    }
]

for page in PAGES:
    html = make_page(page['slug'], page['title'], page['emoji'], page['subtitle'], page['tags'], page['content'])
    filename = f"{page['slug']}.html"
    filepath = os.path.join(DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {filepath}")
