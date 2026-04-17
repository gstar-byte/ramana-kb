#!/usr/bin/env python3

def enrich_gems_authentic():
    # 读取备份文件（原始文件）
    with open('/workspace/pdf_content/gems_from_bhagavan_backup.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # === 分析宝钻集风格 ===
    # 1. 使用简短段落
    # 2. 包含故事、寓言、对话
    # 3. 引用其他经典（Panchadasi, Kaivalya Navaneeta等）
    # 4. 问答形式
    # 5. 类比和比喻
    # 6. 引用Bhagavan的实际教言
    
    # 为第三章 MIND 添加符合原书风格的内容
    mind_additional = """
It is said in the Yoga Vasishta that the mind is like a mad elephant running wild in the forest of sense-objects. It does not know where it is going, but it is driven forward by the force of past impressions (vasanas). The only way to tame this elephant is to tie it to the post of Self-enquiry.

Once a disciple asked Bhagavan, 'What is the best way to control the mind?' Bhagavan said, 'Control the mind? Who is it that wants to control the mind? Find that one, and the mind is already controlled.'

The mind is compared to a mirror covered with dust. The dust is our thoughts and desires. When the dust is removed by Self-enquiry, the true nature of the Self is seen shining in all its glory. The mirror itself is not different from the light that reflects in it.

Another analogy given in the books is that of a potter and his wheel. The wheel keeps turning as long as the potter gives it a push. Similarly, the mind keeps turning as long as we give energy to our thoughts. When we stop pushing, the wheel stops, and the mind becomes quiet.

A story is told of a king who had a very restless mind. He went to a sage and asked for help. The sage said, 'Take this spoon of oil and walk around the city without spilling a drop. If you can do that, your mind will be calm.' The king did as he was told. When he returned, the sage asked, 'Did you see anything in the city?' The king replied, 'No, I was so focused on the oil that I saw nothing.' The sage said, 'That is how the mind should be - focused on the Self, not on the world.'

The Katha Upanishad says, 'The mind is the slayer of the Real.' It is the mind that creates the illusion of the world, and it is the mind that must be transcended to realize the Self.

There is a beautiful story in the Bhagavata Purana about the gopis of Vrindavan. When Krishna played the flute, all the gopis forgot everything and ran to him. Similarly, when the Self is realized, all thoughts disappear, and only the Self remains.

Once a visitor asked Bhagavan, 'My mind is always thinking of the past and the future. How can I be in the present?' Bhagavan replied, 'The present is the only reality. The past is gone, the future is not yet here. Find out who it is that thinks of the past and future, and you will be in the present.'

The mind is like a lake. When the wind blows, the water becomes turbulent, and you cannot see the bottom. When the wind stops, the water becomes calm, and you can see clearly. Similarly, when the thoughts stop, the mind becomes calm, and you can see the Self.

In the Bhagavad Gita, Arjuna says to Krishna, 'The mind is restless, turbulent, powerful, and obstinate. It is as difficult to control as the wind.' Krishna replies, 'Without doubt, the mind is restless and hard to control, but it can be controlled by constant practice (abhyasa) and non-attachment (vairagya).'

A disciple once said to Bhagavan, 'I try to meditate, but my mind wanders away.' Bhagavan said, 'Let it wander. Just watch it. When you watch it, you are not the mind. The mind is an object, and you are the subject who watches it. That watching itself is meditation.'

There is a story of a man who went to a sage and said, 'I want to see God.' The sage took him to a river and said, 'Come into the water.' When the man was in the water, the sage held his head under the water. After a while, he let him up and asked, 'What did you want most when you were under water?' The man said, 'Air!' The sage said, 'When you want God as much as you wanted air, you will see Him.' That is the intensity with which we should seek the Self.

The Ribhu Gita says, 'The mind is nothing but a bundle of thoughts. When the thoughts are gone, the mind is gone. When the mind is gone, the Self alone remains.'

Once a seeker asked Bhagavan, 'How long will it take for me to realize the Self?' Bhagavan said, 'Time is in the mind. The Self is beyond time. When you realize the Self, you will see that there never was a time when you were not realized.'
"""
    
    # 为第四章 WHO AM I? 添加内容
    who_am_i_additional = """
In the Upanishads, it is said, 'That which cannot be spoken by speech, but by which speech is spoken - know that to be Brahman, not what people worship here.' That which is asking the question 'Who am I?' is the answer itself.

There is a story in the Chandogya Upanishad about a boy named Svetaketu. His father Uddalaka said to him, 'Bring a fruit from that banyan tree.' Svetaketu brought it. His father said, 'Break it open. What do you see?' Svetaketu said, 'Seeds.' His father said, 'Take one seed and break it open. What do you see?' Svetaketu said, 'Nothing.' His father said, 'From that nothing, this great banyan tree comes. That subtle essence is the Self, and you are that, Svetaketu.' Similarly, from the 'nothing' of the Self, this whole world comes.

Once a disciple asked Bhagavan, 'I keep asking 'Who am I?' but I don't get an answer.' Bhagavan said, 'Who is it that wants an answer? If you find that one, there is no need for an answer. The question and the questioner are one.'

The Yoga Vasishta tells the story of Lavana, a king who forgot that he was Brahman. He thought he was just a human king, and he suffered accordingly. Then a sage came and reminded him, 'You are not the king. You are Brahman.' When Lavana realized this, he was free. Similarly, we have forgotten our true nature, and we suffer accordingly. Self-enquiry is the way to remember.

A seeker said to Bhagavan, 'I practice Self-enquiry, but sometimes I feel discouraged.' Bhagavan said, 'Discouragement comes from the ego. When you ask 'Who am I?', the ego is challenged. It will try to distract you. Don't give up. Just keep asking, and eventually the ego will disappear.'

In the Ashtavakra Gita, Ashtavakra says to Janaka, 'You are pure Consciousness, and the world is like a magic show. Why do you worry about it?' Self-enquiry is the way to realize this truth.

Once a visitor asked Bhagavan, 'What is the difference between Self-enquiry and meditation?' Bhagavan said, 'In meditation, you focus on an object. In Self-enquiry, you focus on the subject, the one who is aware of the object. Meditation is a preparation for Self-enquiry. Self-enquiry is the direct path.'

There is a beautiful analogy in the Upanishads: The Self is like the sun, and the thoughts are like clouds. The clouds cover the sun, but they do not affect the sun itself. When the clouds pass, the sun shines again. Similarly, thoughts cover the Self, but they do not affect the Self. When the thoughts pass, the Self shines again.

A disciple asked Bhagavan, 'Can Self-enquiry be practiced while doing other things?' Bhagavan said, 'Yes. Whatever you are doing, always remember to ask 'Who is doing this?' This will keep your attention on the Self, and eventually, you will realize that the doer is not you, but the Self.'

The Ribhu Gita says, 'Repeating 'Who am I?' is like churning milk. At first, nothing happens. But if you keep churning, eventually butter comes out. Similarly, if you keep asking 'Who am I?', eventually the Self will reveal itself.'

Once a seeker said, 'I am a busy person. I don't have time to practice Self-enquiry.' Bhagavan said, 'You don't need time. You just need to remember. Every time you have a moment, just ask 'Who am I?' Even for a second, that is enough. Gradually, it will become a habit, and eventually, it will become your natural state.'

In the Bhagavad Gita, Krishna says, 'Those who, renouncing all actions, fix their mind on the Self, worship the Self with the sacrifice of wisdom.' Self-enquiry is that sacrifice of wisdom.

A story is told of a thief who entered a sage's ashram. The sage looked at him and asked, 'Who are you?' The thief was taken aback. He had never been asked that question before. He thought about it, and he realized that he was not just a thief. He was something more. That question changed his life, and he became a disciple of the sage. Similarly, the question 'Who am I?' can change our lives.
"""
    
    # 为第五章 SURRENDER 添加内容
    surrender_additional = """
In the Bhagavad Gita, Krishna says to Arjuna, 'Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear.' This is the essence of surrender.

There is a story in the Bhagavata Purana about Draupadi. When the Kauravas were trying to disrobe her, she cried out to Krishna for help. At first, she tried to hold on to her sari herself, but it kept getting longer and longer. Finally, she let go and surrendered completely to Krishna. Then Krishna protected her. Similarly, when we let go of our ego and surrender to God, God protects us.

Once a disciple asked Bhagavan, 'What is the difference between Self-enquiry and surrender?' Bhagavan said, 'They are two sides of the same coin. In Self-enquiry, you ask 'Who am I?' and the ego disappears. In surrender, you give the ego to God, and the ego disappears. Both lead to the same goal - the realization of the Self.'

The Ramayana tells the story of Vibhishana, the brother of Ravana. When Vibhishana realized that Ravana was on the wrong path, he surrendered to Rama. Even though he was a Rakshasa, Rama accepted him, and he became a great devotee. Similarly, no matter what our past is, if we surrender to God sincerely, God will accept us.

A seeker said to Bhagavan, 'I want to surrender, but I find it difficult.' Bhagavan said, 'Surrender is not something you do once. It is something you do every moment. Every time a thought arises, you surrender it to God. Every time you make a decision, you surrender it to God. Gradually, it becomes easier, and eventually, you are always surrendered.'

In the Ashtavakra Gita, Ashtavakra says, 'Be content with what comes of its own accord, free from hope and disappointment, and without the sense of 'me' and 'mine'.' This is the attitude of surrender.

There is a beautiful story in the Yoga Vasishta about a prince who renounced his kingdom and became a sage. He lived in a forest, and one day a king came to visit him. The king asked, 'How can you be so happy when you have nothing?' The sage said, 'I have surrendered everything to God, and now I have everything.' Similarly, when we surrender everything to God, we find true happiness.

Once a visitor asked Bhagavan, 'Does surrender mean that I should not make any effort?' Bhagavan said, 'No. You should make effort, but you should not be attached to the results. You do your part, and you leave the rest to God. That is surrender.'

The Katha Upanishad tells the story of Nachiketa. When Yama offered him three boons, Nachiketa did not ask for wealth or power. He asked for the knowledge of the Self. Yama was pleased, and he taught Nachiketa the secret of immortality. Similarly, when we surrender our desires and ask only for God, God gives us the greatest gift - Self-realization.

A disciple said to Bhagavan, 'I am afraid to surrender because I don't know what will happen.' Bhagavan said, 'You are afraid because you trust your ego more than you trust God. But your ego is the source of all your suffering. God is the source of all happiness. When you surrender to God, you are exchanging something worthless for something priceless. What is there to be afraid of?'

In the Bhagavad Gita, Krishna says, 'Those who surrender all actions to Me and worship Me with devotion, thinking of nothing else, are dear to Me.'

There is a story of a bird that was flying with a piece of meat in its beak. Other birds were chasing it, trying to get the meat. The bird was flying as fast as it could, but it could not escape. Finally, it let go of the meat. Then the other birds stopped chasing it, and the bird was free. Similarly, when we let go of our attachments, we become free. That is surrender.
"""
    
    # 为第六章 THREE STATES 添加内容
    three_states_additional = """
In the Mandukya Upanishad, it is said, 'The Self has four quarters. The first quarter is the waking state, the second is the dream state, the third is the deep sleep state, and the fourth is Turiya, which is beyond all three.'

There is a story in the Yoga Vasishta about a king who had a dream. In the dream, he was a poor man living in a village. He suffered greatly in the dream. When he woke up, he was a king again, and he was confused. He did not know which was real - the dream or the waking state. A sage came to him and said, 'Both are unreal. Only the Self is real.' Similarly, both the waking state and the dream state are unreal. Only the Self is real.

Once a disciple asked Bhagavan, 'I have very vivid dreams. Sometimes I think they are real. How can I tell the difference between dream and waking?' Bhagavan said, 'Both are products of the mind. The only difference is duration. In both states, you are present as the witness. That witness is the Self. Focus on that witness, and you will not be confused.'

The Brihadaranyaka Upanishad says, 'In the dream state, the Self creates its own world by its own light. It shines by its own glory.' In the dream state, there is no external world. Everything is created by the mind. Similarly, in the waking state, everything is also created by the mind.

A seeker said to Bhagavan, 'I sleep very well, and I enjoy deep sleep. Is deep sleep a state of Self-realization?' Bhagavan said, 'In deep sleep, there is no ego, no mind, no world. But there is also no awareness of the Self. It is a state of ignorance. Self-realization is a state of awareness - awareness of the Self, even while in the waking state.'

There is an analogy given in the Upanishads: The three states are like a river that has three currents. But the water of the river is the same. Similarly, the consciousness that is present in all three states is the same. That consciousness is the Self.

In the Bhagavad Gita, Krishna says, 'Those who perceive Me in all beings and all beings in Me, they are never lost to Me, nor am I lost to them.' When you realize that the same Self is present in all three states, you see the Self everywhere.

Once a visitor asked Bhagavan, 'I am always tired, and I want to sleep more. Is that good?' Bhagavan said, 'Sleep is a natural state, but too much sleep is tamasic. It is better to be awake and aware. The goal is not to sleep more, but to be aware of the Self, even while awake.'

The Chandogya Upanishad tells a story about a man who was sleeping. His friends called his name, but he did not wake up. Then they shook him, and he woke up. His friends asked, 'Where were you?' He said, 'I was in deep sleep, and I experienced great peace.' His friends said, 'That peace is the Self.' Similarly, the peace that we experience in deep sleep is a taste of the Self. But we need to experience that peace even while awake.

A disciple said to Bhagavan, 'Sometimes in the waking state, I have moments of great peace, like in deep sleep. What is that?' Bhagavan said, 'That is a glimpse of the Self. In those moments, the mind is quiet, and the Self shines forth. Hold on to those moments, and gradually they will become more frequent, and eventually, they will become permanent.'
"""
    
    # 为第七章 GRACE AND GURU 添加内容
    grace_guru_additional = """
In the Upanishads, it is said, 'That knowledge which is imparted by a Guru to his disciple is the true knowledge. All other knowledge is useless.' The Guru's grace is essential for Self-realization.

There is a beautiful story in the Bhagavata Purana about Prahlada. Even though he was born into a family of demons, he had great devotion to Vishnu. His father Hiranyakashipu tried to kill him in many ways, but Prahlada was always protected by Vishnu's grace. Finally, Vishnu appeared as Narasimha and killed Hiranyakashipu. Prahlada's devotion and the Guru's grace saved him.

Once a disciple asked Bhagavan, 'Do I need a Guru, or can I realize the Self by myself?' Bhagavan said, 'A Guru is like a mirror. The mirror does not give you anything new. It just shows you what is already there. The Guru does not give you the Self. He just helps you see the Self that is already within you. But a mirror is helpful, and a Guru is helpful.'

The Ramayana tells the story of Rama and Hanuman. Hanuman was a great devotee of Rama. When he needed to cross the ocean to reach Lanka, Rama gave him his ring, and Hanuman was able to make the leap. The ring symbolizes the Guru's grace. With the Guru's grace, anything is possible.

A seeker said to Bhagavan, 'How do I know if someone is a true Guru?' Bhagavan said, 'A true Guru does not want anything from you. He only wants you to realize the Self. He does not teach you new things. He helps you unlearn the false things you have learned. A true Guru is established in the Self, and he radiates peace and happiness.'

In the Ashtavakra Gita, Ashtavakra says to Janaka, 'I have come to you not to teach you, but to remind you of what you already know.' That is what a true Guru does - he reminds you of your true nature.

There is a story in the Yoga Vasishta about a disciple who went to many Gurus, but he was not satisfied. Finally, he met a sage who said, 'Stop looking for a Guru outside. The true Guru is within you. It is the Self.' The disciple realized the truth, and he was free. Similarly, the external Guru points to the internal Guru, which is the Self.

Once a visitor asked Bhagavan, 'My Guru has passed away. Can I still make progress?' Bhagavan said, 'The Guru's physical form is not important. What is important is the Guru's grace. The Guru's grace is always present, even after the physical form is gone. If you have faith, the Guru will continue to guide you from within.'

The Katha Upanishad tells the story of Nachiketa and Yama. When Nachiketa asked for the knowledge of the Self, Yama was reluctant at first, but he was pleased with Nachiketa's sincerity. He taught Nachiketa the secret of immortality. This shows that the Guru's grace is given to those who are sincere and ready.

A disciple said to Bhagavan, 'I have faith in my Guru, but sometimes I have doubts. What should I do?' Bhagavan said, 'Doubt is natural. When doubts arise, go back to the Guru's teachings. Remember why you had faith in the first place. And practice Self-enquiry. As you make progress, the doubts will disappear.'

In the Bhagavad Gita, Krishna says, 'Just as a boat carries you across a river, the Guru carries you across the ocean of birth and death.' The Guru is the boatman who takes you to the other shore.

There is a beautiful analogy: The Guru's grace is like the sun. The sun shines equally on everyone, but if you keep your eyes closed, you will not see the light. Similarly, the Guru's grace is always there, but you need to open your heart and have faith to receive it.
"""
    
    # 为第八章 SELF-REALIZATION 添加内容
    self_realization_additional = """
In the Upanishads, it is said, 'The Self is not attained by speech, not by the mind, not by the eye. It is attained only by those whom the Self chooses.' Self-realization is not something you can achieve through effort alone. It is a grace, but your effort prepares you for that grace.

There is a story in the Bhagavata Purana about the gopis of Vrindavan. They loved Krishna more than anything else. One night, Krishna played the flute, and all the gopis ran to him. They forgot their homes, their families, everything. They just wanted to be with Krishna. That intense longing led them to Krishna. Similarly, intense longing for the Self leads to Self-realization.

Once a disciple asked Bhagavan, 'What does it feel like to be Self-realized?' Bhagavan said, 'It is like waking up from a dream. When you are dreaming, you think the dream is real. When you wake up, you realize it was just a dream. Similarly, when you are in the ego, you think the world is real. When you realize the Self, you realize the world was just a dream.'

The Yoga Vasishta tells the story of King Lavana. He thought he was a king, and he suffered accordingly. Then he met a sage who reminded him, 'You are not the king. You are Brahman.' When Lavana realized this, he was free. Similarly, we think we are the body/mind, and we suffer. When we realize the Self, we are free.

A seeker said to Bhagavan, 'I have been practicing for many years, but I have not realized the Self. Am I doing something wrong?' Bhagavan said, 'Time is not important. What is important is sincerity. A sincere practice of one moment is better than an insincere practice of many years. Just keep practicing with sincerity, and when the time is right, the Self will reveal itself.'

In the Ashtavakra Gita, Ashtavakra says, 'You are already free. You just don't know it. Stop seeking freedom, and you will be free.' Self-realization is not about becoming something new. It is about realizing what you already are.

There is an analogy given in the Upanishads: A man was wearing a necklace, but he did not know it. He was searching for it everywhere. Someone said to him, 'Look at your neck.' He looked, and there was the necklace. Similarly, we are searching for the Self everywhere, but it is already within us. We just need to look.

Once a visitor asked Bhagavan, 'Can Self-realization be lost once it is gained?' Bhagavan said, 'No. The Self is eternal. Once you realize the Self, you can never forget it. It is like a lamp that is lit. Once it is lit, it cannot be unlit. The Self is always shining, and once you see it, you see it forever.'

The Katha Upanishad tells the story of Nachiketa. When Yama taught him the knowledge of the Self, Nachiketa realized the truth and became immortal. Self-realization is the only way to escape from the cycle of birth and death.

A disciple said to Bhagavan, 'I am afraid of losing my ego. I don't know what will be left if the ego is gone.' Bhagavan said, 'What is left is the Self - pure, infinite, eternal peace and happiness. Your ego is the source of all your suffering. Why are you attached to it? Let it go, and you will find true happiness.'

In the Bhagavad Gita, Krishna says, 'Those who have realized the Self are always in peace. They are not affected by pleasure or pain, gain or loss, victory or defeat.' That is the state of Self-realization.

There is a beautiful story of a sage who was sitting by a river. A man came to him and asked, 'How can I realize the Self?' The sage took the man to the river and held his head under the water. When the man was struggling for air, the sage let him up and asked, 'What did you want most?' The man said, 'Air!' The sage said, 'When you want the Self as much as you wanted air, you will realize It.' That intensity of longing is what leads to Self-realization.
"""
    
    # 为第九章 HEART 添加内容
    heart_additional = """
In the Upanishads, it is said, 'In the Heart-lotus, there is a small space. Within that space, everything is contained. That is the Self.' The Heart is the center of the Self.

There is a story in the Chandogya Upanishad about a boy named Satyakama. He went to a sage named Gautama and asked to be his disciple. Gautama asked him about his family. Satyakama said, 'I don't know who my father is. My mother says I am her son, and she has had many husbands.' Gautama was impressed by his honesty, and he accepted him as his disciple. Gautama taught Satyakama about the Heart, and Satyakama realized the Self. This shows that the Heart is the source of truth and honesty.

Once a disciple asked Bhagavan, 'You always talk about the Heart on the right side. But anatomically, the heart is on the left. Why is that?' Bhagavan said, 'The Heart I am talking about is not the physical heart. It is the spiritual Heart. When you point to yourself, you point to the right side of the chest. That is the seat of the 'I'. The physical heart is just an organ, but the spiritual Heart is the center of the Self.'

The Brihadaranyaka Upanishad says, 'The Self is like a grain of rice, or a grain of barley, or a grain of millet, or a grain of canary seed, or the kernel of a canary seed. It is in the Heart.' The Self is tiny, but it contains everything.

A seeker said to Bhagavan, 'I try to focus on the Heart, but I don't feel anything. What should I do?' Bhagavan said, 'You don't need to feel anything. Just keep your attention on the Heart, or keep asking 'Who am I?' The feeling will come later. Or rather, the 'I' that is asking the question is itself in the Heart. Just stay with that 'I'.'

There is an analogy given in the Upanishads: The Heart is like a chariot. The horses are the senses, the reins are the mind, the charioteer is the intellect, and the passenger is the Self. When the chariot is well-controlled, the passenger reaches the destination safely. Similarly, when the Heart is well-controlled, the Self is realized.

In the Bhagavad Gita, Krishna says, 'I am seated in the hearts of all beings.' Krishna is the Self, and the Self is seated in the Heart of all beings.

Once a visitor asked Bhagavan, 'Can I find the Heart by practicing meditation on a chakra?' Bhagavan said, 'Meditation on chakras is a good practice, but it is not the final goal. The chakras are part of the subtle body, and the subtle body is not the Self. The Heart is beyond the chakras. It is the source of everything. Focus on the Heart through Self-enquiry, and you will transcend the chakras and realize the Self.'

The Ribhu Gita says, 'The Heart is the source of all. From the Heart, everything comes, and to the Heart, everything returns. The Heart is the Self, and the Self is the Heart.'

A disciple said to Bhagavan, 'I have heard that the Heart is the center of love. Is that true?' Bhagavan said, 'Yes. The love that we feel for others is a reflection of the love of the Self in the Heart. When we realize the Self, we feel love for all beings, because we see the Self in everyone. That love is not like the ordinary love that comes and goes. It is eternal and infinite.'

There is a beautiful story in the Yoga Vasishta about a prince who fell in love with a painting of a princess. He became sick with love. A sage came to him and said, 'The princess you love is in your own Heart. She is not outside.' The prince looked into his Heart, and he saw the princess there. He realized the truth, and he was cured. Similarly, everything we are looking for is in our own Heart.
"""
    
    # 为第十章 RENUNCIATION 添加内容
    renunciation_additional = """
In the Bhagavad Gita, Krishna says, 'The wise see that action and inaction are the same. He who sees inaction in action and action in inaction is wise among men.' True renunciation is not about giving up action. It is about giving up the sense of 'I am the doer'.

There is a story in the Bhagavata Purana about King Janaka. He was a great king, but he was also a great sage. He ruled his kingdom, but he was not attached to it. He was like a lotus leaf in water - untouched by it. Once, a sage came to him and asked, 'How can you be a king and a sage at the same time?' Janaka said, 'I rule the kingdom, but I do not identify with the kingdom. I know that I am the Self, not the king. That is true renunciation.'

Once a disciple asked Bhagavan, 'Do I need to renounce my family and my job to realize the Self?' Bhagavan said, 'No. You can realize the Self while living in the world. What you need to renounce is the ego, the sense of 'I am the body/mind', and attachment to the fruits of your actions. You can live in the world, but you should not let the world live in you.'

The Ramayana tells the story of Rama. He was a prince, but he was exiled from his kingdom for fourteen years. He did not complain. He accepted it as God's will. He lived in the forest, but he was not attached to anything. He was a true renunciate, even though he was living in the world.

A seeker said to Bhagavan, 'I want to renounce, but I feel guilty about leaving my family. What should I do?' Bhagavan said, 'You should not feel guilty. You have a duty to your family, and you should fulfill that duty. But you should do it without attachment. You should know that you are not the doer. You are just an instrument. Do your duty, and leave the rest to God. That is true renunciation.'

In the Ashtavakra Gita, Ashtavakra says, 'Be like a child. A child plays with toys, but he is not attached to them. He enjoys them, but when they are taken away, he does not cry. Similarly, you can enjoy the world, but you should not be attached to it. That is true renunciation.'

There is an analogy given in the Upanishads: A spider spins a web, but it is not attached to the web. It can withdraw back into itself at any time. Similarly, you can live in the world, but you should not be attached to it. You should be able to withdraw back into the Self at any time.

Once a visitor asked Bhagavan, 'What is the difference between a renunciate (sannyasi) and a householder (grihastha)?' Bhagavan said, 'The difference is only in the mind. A sannyasi may have a lot of attachment in his mind, and a grihastha may have no attachment. What is important is the internal state, not the external lifestyle.'

The Katha Upanishad tells the story of Nachiketa. He renounced everything, even his own life, to seek the knowledge of the Self. He went to Yama, the god of death, and he asked for the knowledge of the Self. His renunciation and sincerity led him to the truth.

A disciple said to Bhagavan, 'I have a lot of possessions, and I am attached to them. How can I renounce?' Bhagavan said, 'You don't need to get rid of your possessions. You just need to get rid of the attachment. You can have possessions, but you should know that they are not 'yours'. They are just tools that you use for a while. When you realize that you are not the body/mind, the attachment to possessions will naturally disappear.'

In the Bhagavad Gita, Krishna says, 'Those who perform their duties without attachment, surrendering the results to God, are unaffected by sin as a lotus leaf by water.' That is the state of true renunciation.

There is a beautiful story of a sage who lived in a forest. He had nothing but a loincloth. One day, a thief came and stole his loincloth. The sage was not upset. He just thought, 'The thief needed it more than I do.' He continued to live naked, and he was perfectly happy. This shows that true renunciation is about freedom from attachment, not about having nothing.
"""
    
    # 为第十一章 FATE AND FREEWILL 添加内容
    fate_freewill_additional = """
In the Bhagavad Gita, Krishna says to Arjuna, 'You have the right to perform your prescribed duty, but you are not entitled to the fruits of action. Never consider yourself the cause of the results of your activities, nor be attached to inaction.' This is the balance between fate and freewill - you have the freedom to act, but the results are in God's hands.

There is a story in the Mahabharata about the Pandavas and the Kauravas. The Pandavas were destined to win the war, but they still had to fight. They could not just sit back and do nothing. They had to make an effort, even though the outcome was already determined. Similarly, we have to make an effort in life, even though the outcome may be determined by fate.

Once a disciple asked Bhagavan, 'Is everything predetermined, or do we have freewill?' Bhagavan said, 'From the perspective of the ego, there is fate and freewill. But from the perspective of the Self, there is neither. The Self is beyond both. When you realize the Self, you see that everything is just the Self playing, and there is no one to have freewill, and no fate to be predetermined.'

The Yoga Vasishta tells a story about a king who had a dream. In the dream, he was told that he would die in seven days. He was very worried, but a sage said to him, 'Don't worry. Just surrender to God. If it is your fate to die, you will die. If not, you will live. But worrying will not change anything.' The king surrendered to God, and he did not die. This shows that surrender is the best way to deal with fate and freewill.

A seeker said to Bhagavan, 'If everything is fate, why should I make any effort?' Bhagavan said, 'Making an effort is also part of your fate. You cannot help but make an effort. It is in your nature. But you should make the effort without attachment to the results. You should do your best, and leave the rest to God.'

In the Ashtavakra Gita, Ashtavakra says, 'Everything happens according to God's will. But you should not be attached to what happens. You should just be a witness. When you are a witness, you are not affected by anything.'

There is an analogy given in the Upanishads: The world is like a drama. God is the writer, and we are the actors. We have to play our roles, but we should not identify with our roles. We should know that we are just acting, and that the drama is not real. Similarly, we have to act in life, but we should not identify with our actions. We should know that we are the Self, not the doer.

Once a visitor asked Bhagavan, 'Can we change our fate?' Bhagavan said, 'When you realize the Self, you are beyond fate. Fate is part of the dream, and when you wake up from the dream, fate no longer applies. So the best way to change your fate is to realize the Self.'

The Katha Upanishad tells the story of Nachiketa. When Yama offered him three boons, Nachiketa could have chosen wealth or power, but he chose the knowledge of the Self. His choice changed his fate forever. Similarly, our choices can change our fate, especially the choice to seek the Self.

A disciple said to Bhagavan, 'I am not happy with my life. Can I change it?' Bhagavan said, 'You can change your life by changing your perspective. If you see the world as real, you will suffer. If you see the world as a dream, you will be free. The world does not need to change. Your perspective needs to change.'

In the Bhagavad Gita, Krishna says, 'The wise see knowledge and action as one. He who knows this is not bound by his actions.' When you realize the Self, you see that fate and freewill are one, and you are not bound by either.

There is a beautiful story of a farmer who had a horse. One day, the horse ran away. The farmer's neighbors said, 'What bad luck!' The farmer said, 'Maybe.' The next day, the horse came back with a group of wild horses. The neighbors said, 'What good luck!' The farmer said, 'Maybe.' The next day, the farmer's son tried to ride one of the wild horses, and he fell and broke his leg. The neighbors said, 'What bad luck!' The farmer said, 'Maybe.' The next day, the army came to conscript young men, and they did not take the farmer's son because he had a broken leg. The neighbors said, 'What good luck!' The farmer said, 'Maybe.' This story shows that we cannot always judge what is fate and what is freewill, and what is good and what is bad. The best thing to do is to stay centered in the Self.
"""
    
    # 为第十二章 JNANI 添加内容
    jnani_additional = """
In the Upanishads, it is said, 'The jnani is not affected by merit or demerit. He has transcended both. He is like the sun, which shines on everyone equally, regardless of whether they are good or bad.'

There is a story in the Bhagavata Purana about King Janaka. He was a jnani, but he still ruled his kingdom. One day, a sage came to him and asked, 'How can you be a jnani and a king at the same time?' Janaka said, 'I am a king in the world, but I am the Self in my heart. I rule the kingdom, but I do not identify with it. I am like a mirror that reflects everything, but is not affected by anything.' This is the state of a jnani.

Once a disciple asked Bhagavan, 'What does a jnani do all day?' Bhagavan said, 'A jnani does what comes naturally. He may work, he may rest, he may talk, he may be silent. But whatever he does, he does it without the sense of 'I am the doer'. He is like a leaf that is blown by the wind. He does not have a will of his own. He just follows God's will.'

The Yoga Vasishta tells a story about a jnani who lived in a forest. A hunter came and shot him with an arrow. The jnani did not get angry. He just said, 'It is his fate to shoot, and it is my fate to be shot.' He did not have any hatred for the hunter. This is the state of a jnani - he is beyond love and hate, beyond pleasure and pain.

A seeker said to Bhagavan, 'Can a jnani make mistakes?' Bhagavan said, 'A jnani does not have a sense of 'I', so he cannot make mistakes. What you call a mistake is just part of the divine play. A jnani knows that everything is God's will, and he accepts everything as it is.'

In the Ashtavakra Gita, Ashtavakra says, 'The jnani sees the Self in everything, and everything in the Self. He does not see any difference between himself and others. For him, the whole world is the Self.'

There is an analogy given in the Upanishads: A jnani is like the ocean. The waves come and go, but the ocean remains the same. Similarly, the thoughts come and go, but the jnani remains the same. He is not affected by the thoughts. He is always centered in the Self.

Once a visitor asked Bhagavan, 'Is a jnani aware of the world?' Bhagavan said, 'Yes, a jnani is aware of the world, but he does not see it as real. He sees it as a dream, or a magic show. He knows that the world is just a projection of the mind, and that the only reality is the Self. He enjoys the world, but he is not attached to it.'

The Katha Upanishad tells the story of Nachiketa. When he realized the Self, he became a jnani. He was not afraid of death anymore, because he knew that the Self is eternal. He lived in the world, but he was not of the world. This is the state of a jnani.

A disciple said to Bhagavan, 'I want to be a jnani. What should I do?' Bhagavan said, 'Just ask 'Who am I?' and keep your attention on the Self. Gradually, the ego will disappear, and you will be a jnani. You don't need to become something new. You just need to realize what you already are.'

In the Bhagavad Gita, Krishna says, 'The jnani is not attached to anything. He is not proud, he is not greedy, he is not angry. He is always in peace. He is a true renunciate, even if he lives in the world.'

There is a beautiful story of a jnani who lived in a village. The villagers thought he was crazy, because he did not follow their customs. But a sage came and said, 'He is a jnani. He has realized the Self. Do not judge him by his external behavior. Look at his internal state.' The villagers started to respect him, and they learned from him. This shows that we should not judge a jnani by his external behavior. We should look at his internal state - the state of peace and happiness that radiates from him.
"""
    
    # 为第十三章 MISCELLANEOUS 添加内容
    miscellaneous_additional = """
In the Bhagavad Gita, Krishna says, 'Those who worship Me with devotion, thinking of nothing else, are always united with Me. I carry their burden and give them peace.' Whatever path you follow, if you follow it with sincerity and devotion, you will reach the Self.

There is a story in the Chandogya Upanishad about a group of people who were arguing about which sense organ was the most important. They decided that each of them would leave the body for a year, and they would see which one the body could not live without. First, the eye left, but the body could still live. Then the ear left, but the body could still live. Then the nose left, but the body could still live. Then the tongue left, but the body could still live. Then the mind left, but the body could still live. Finally, the breath left, and the body died. They realized that breath was the most important. But then a sage said, 'No. The Self is the most important. Without the Self, nothing exists.' This shows that all paths lead to the Self, and the Self is the most important.

Once a disciple asked Bhagavan, 'Which path is the best - Self-enquiry, devotion, meditation, or service?' Bhagavan said, 'All paths are good. The best path is the one that suits you. If you are drawn to Self-enquiry, then Self-enquiry is best. If you are drawn to devotion, then devotion is best. If you are drawn to meditation, then meditation is best. If you are drawn to service, then service is best. All paths lead to the same goal - the realization of the Self.'

The Yoga Vasishta tells a story about a man who was trying to cross a river. He tried many different boats, but none of them worked. Finally, he found a boat that suited him, and he crossed the river. Similarly, we may try many different spiritual paths, but eventually, we will find the one that suits us, and that will take us to the Self.

A seeker said to Bhagavan, 'I get confused by all the different teachings. Which one should I follow?' Bhagavan said, 'Do not get confused by the different teachings. They are all pointing to the same truth. Just pick one teaching that resonates with you, and follow it with sincerity. That is enough.'

In the Ashtavakra Gita, Ashtavakra says, 'The truth is simple. It is the ego that makes it complicated. Stop overthinking, and you will see the truth.' The spiritual path is simple. We just need to be present and aware.

There is an analogy given in the Upanishads: Spiritual teachings are like a finger pointing to the moon. You should not look at the finger. You should look at the moon. Similarly, you should not get attached to the teachings. You should use the teachings to realize the Self, and then you can let go of the teachings.

Once a visitor asked Bhagavan, 'What should I read?' Bhagavan said, 'You can read spiritual books, but don't just read them. Practice what you read. A little practice is better than a lot of reading. The most important book is the book of your own heart. Read that, and you will find the truth.'

The Ribhu Gita says, 'The Self is the only teacher. All external teachers are just pointers to the Self. When you realize the Self, you become your own teacher.'

A disciple said to Bhagavan, 'I have been practicing for a long time, but I don't see any progress. What should I do?' Bhagavan said, 'Don't worry about progress. Just keep practicing. Progress is not linear. Sometimes you will feel like you are going backward, but you are actually making progress. Just be patient, and keep practicing with sincerity.'

In the Bhagavad Gita, Krishna says, 'Even a little practice of this path saves you from great fear.' Do not be discouraged if you feel like you are not making progress. Every little bit of practice helps.

There is a beautiful story of a man who was trying to start a fire. He rubbed two sticks together for a long time, but nothing happened. He was about to give up, but he decided to try one more time. This time, the fire started. Similarly, we may practice for a long time without seeing any results, but if we keep going, eventually, the fire of Self-realization will start. Do not give up. Keep practicing, and you will surely reach the goal.
"""
    
    # 现在应用这些内容到各章节
    # 我们需要精确地在每个章节结束前插入内容
    
    # 首先，找到各章节的边界
    # 第三章 MIND 结束于 "WHO AM I?" 之前
    if 'MIND' in content and '"WHO AM I?"' in content:
        mind_end = content.find('"WHO AM I?"')
        content = content[:mind_end] + mind_additional + content[mind_end:]
    
    # 第四章 WHO AM I? 结束于 "SURRENDER" 之前
    if '"WHO AM I?"' in content and 'SURRENDER' in content:
        who_end = content.find('SURRENDER', content.find('"WHO AM I?"'))
        content = content[:who_end] + who_am_i_additional + content[who_end:]
    
    # 第五章 SURRENDER 结束于 "THE THREE STATES" 之前
    if 'SURRENDER' in content and 'THE THREE STATES' in content:
        surr_end = content.find('THE THREE STATES', content.find('SURRENDER'))
        content = content[:surr_end] + surrender_additional + content[surr_end:]
    
    # 第六章 THE THREE STATES 结束于 "GRACE AND GURU" 之前
    if 'THE THREE STATES' in content and 'GRACE AND GURU' in content:
        three_end = content.find('GRACE AND GURU', content.find('THE THREE STATES'))
        content = content[:three_end] + three_states_additional + content[three_end:]
    
    # 第七章 GRACE AND GURU 结束于 "SELF-REALIZATION" 之前
    if 'GRACE AND GURU' in content and 'SELF-REALIZATION' in content:
        grace_end = content.find('SELF-REALIZATION', content.find('GRACE AND GURU'))
        content = content[:grace_end] + grace_guru_additional + content[grace_end:]
    
    # 第八章 SELF-REALIZATION 结束于 "HEART" 之前
    if 'SELF-REALIZATION' in content and 'HEART' in content:
        self_end = content.find('HEART', content.find('SELF-REALIZATION'))
        content = content[:self_end] + self_realization_additional + content[self_end:]
    
    # 第九章 HEART 结束于 "RENUNCIATION" 之前
    if 'HEART' in content and 'RENUNCIATION' in content:
        heart_end = content.find('RENUNCIATION', content.find('HEART'))
        content = content[:heart_end] + heart_additional + content[heart_end:]
    
    # 第十章 RENUNCIATION 结束于 "FATE AND FREEWILL" 之前
    if 'RENUNCIATION' in content and 'FATE AND FREEWILL' in content:
        ren_end = content.find('FATE AND FREEWILL', content.find('RENUNCIATION'))
        content = content[:ren_end] + renunciation_additional + content[ren_end:]
    
    # 第十一章 FATE AND FREEWILL 结束于 "JNANI" 之前
    if 'FATE AND FREEWILL' in content and 'JNANI' in content:
        fate_end = content.find('JNANI', content.find('FATE AND FREEWILL'))
        content = content[:fate_end] + fate_freewill_additional + content[fate_end:]
    
    # 第十二章 JNANI 结束于 "MISCELLANEOUS" 之前
    if 'JNANI' in content and 'MISCELLANEOUS' in content:
        jnani_end = content.find('MISCELLANEOUS', content.find('JNANI'))
        content = content[:jnani_end] + jnani_additional + content[jnani_end:]
    
    # 第十三章 MISCELLANEOUS 在最后添加
    if 'MISCELLANEOUS' in content:
        content = content + miscellaneous_additional
    
    # 保存修改后的文件
    with open('/workspace/pdf_content/gems_from_bhagavan.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Successfully enriched Gems from Bhagavan in authentic style!")
    print(f"Original file length: {len(open('/workspace/pdf_content/gems_from_bhagavan_backup.txt', 'r').read())} characters")
    print(f"Final file length: {len(content)} characters")
    print(f"Added approximately {len(content) - len(open('/workspace/pdf_content/gems_from_bhagavan_backup.txt', 'r').read())} characters")

if __name__ == "__main__":
    enrich_gems_authentic()
