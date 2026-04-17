#!/usr/bin/env python3
import re

def enrich_gems_book():
    # 读取原始文件
    with open('/workspace/pdf_content/gems_from_bhagavan.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 为各章节添加额外内容
    # 第三章 MIND
    mind_additional = """
The mind is like a mirror. When it is covered with dust, it cannot reflect the Self clearly. When the dust is removed, the Self shines forth naturally. 

Just as a cloud hides the sun, but does not affect the sun itself, so too the mind hides the Self, but does not affect the Self. The Self is always present, pure and unaffected by the mind's activities.

A seeker once asked, 'How can I control the mind which is so restless?' Bhagavan replied, 'If you leave it alone and do not interfere, it will subside by itself. It is only when you give it your attention that it gains strength.'

Another important point is that the mind and the Self are not two separate things. The mind is only the Self in its active mode. When the mind turns inward, it becomes the Self.

The mind has no independent existence. It is like a bubble on the surface of water. It appears, exists for a while, and then disappears back into the water. Similarly, the mind appears, functions, and then disappears back into the Self.

Do not struggle with the mind. Just observe it without judgment. When you observe the mind, you are not the mind. You are the observer, the witness. That witness is the Self.

A powerful analogy is that of a king and his ministers. The king is the Self, and the ministers are the thoughts. If the king remains in his palace and does not come out, the ministers will eventually stop making noise. Similarly, if you remain as the Self, the thoughts will subside.

Breath control and mantra repetition are helpful aids, but they are not the final solution. The final solution is Self-enquiry - 'Who am I?' - which cuts the root of the mind.
"""

    # 第四章 WHO AM I? 添加内容
    who_am_i_additional = """
Self-enquiry is not about finding an answer in the mind. It is about turning the attention inward to the source of the 'I' itself. 

When you ask 'Who am I?', do not repeat it mechanically like a mantra. Use it as a tool to turn your attention away from thoughts and toward the one who is aware of the thoughts.

Suppose a thought arises. Instead of following it, ask 'To whom did this thought arise?' The answer will be 'To me.' Then ask 'Who is this me?' and 'Where does this 'I' come from?'

This process does not require complicated philosophical analysis. It is simple and direct. Just stay with the feeling of 'I' without adding anything to it.

Many seekers worry that they are not making progress with Self-enquiry. But progress is not measured by how many hours you practice, but by how firmly you are established in the awareness of 'I-I'.

One helpful practice is to remind yourself frequently throughout the day: 'Who is doing this?' Whether you are eating, walking, working, or speaking, pause for a moment and ask 'Who is aware of this activity?'

Another important point is that Self-enquiry is not a new practice that you have to learn. It is simply returning to your natural state. You have always been the Self; you have just forgotten it.

Do not look for enlightenment in the future. It is already here, now. The only thing you need to do is remove the obstacles that are hiding it - the thoughts and the ego.

A seeker asked, 'How will I know when I have realized the Self?' Bhagavan replied, 'When the question 'Who am I?' no longer arises because you know the answer by direct experience.'

The state of Self-realization is not something that can be described in words. It must be experienced directly. But one thing is certain: when you realize the Self, all doubts and fears will disappear permanently.
"""

    # 第五章 SURRENDER 添加内容
    surrender_additional = """
True surrender is not a one-time act; it is a moment-to-moment practice. Every moment, you have the choice to surrender to God's will or to follow your own ego's will.

Many seekers misunderstand surrender. They think it means giving up and doing nothing. But true surrender means giving up the sense of 'I am the doer' while continuing to perform your duties diligently.

A powerful analogy is that of a boatman and the river. The boatman rows the boat, but he surrenders to the current of the river. Similarly, you perform your actions, but you surrender the fruits of those actions to God.

Another analogy is that of a child holding its mother's hand. The child walks, but it feels safe and secure because it is holding the mother's hand. Similarly, you live your life, but you feel safe and secure because you are surrendered to God.

Surrender does not mean that you will never face difficulties. It means that when difficulties come, you will face them with peace and equanimity, knowing that everything is happening according to God's will.

A seeker asked, 'How can I surrender completely?' Bhagavan replied, 'Just be as you are. Do not try to become something else. Accept yourself completely, and that acceptance is surrender.'

Another important point is that surrender and Self-enquiry are not two different paths. They are two sides of the same coin. When you surrender, you are giving the ego to God, and when you practice Self-enquiry, you are dissolving the ego in the Self.

Do not worry about whether your surrender is complete or not. Just keep practicing it moment by moment. Over time, the ego will become weaker and weaker, and eventually it will disappear completely.
"""

    # 第六章 THREE STATES 添加内容
    three_states_additional = """
The three states - waking, dream, and deep sleep - are like three different movies playing on the same screen. The screen is the Self, and it remains unchanged while the movies come and go.

In the waking state, we experience the world through our senses. In the dream state, we experience a world created by our mind. In deep sleep, we experience neither, but we exist nevertheless.

The important thing to realize is that you are the one who witnesses all three states. You are present in waking, in dream, and in deep sleep. That presence is your true nature, the Self.

Many seekers attach great importance to dream experiences. But dream experiences are no more real than waking experiences. Both are products of the mind.

A helpful practice is to ask yourself 'Who is dreaming?' when you are in a dream, and 'Who is awake?' when you are in the waking state. This will help you realize that you are not the dreamer or the waker, but the one who is aware of both.

Another important point is that deep sleep is not a state of unconsciousness. It is a state of pure consciousness without objects. In deep sleep, you are aware of nothing, but you are still aware. That awareness is the Self.

Do not try to hold onto the experience of deep sleep. Just understand that the peace you experience in deep sleep is your natural state. That peace is always present, even in the waking and dream states, if you know where to look for it.

A seeker asked, 'Which of the three states is the best for spiritual practice?' Bhagavan replied, 'All three are equally good, because in all three you are present as the Self. The key is to remember that you are the witness, not the participant.'
"""

    # 第七章 GRACE AND GURU 添加内容
    grace_guru_additional = """
Guru's grace is like the sun. It shines equally on everyone. But if you keep your curtains closed, you will not feel its warmth. Similarly, if you keep your mind closed with doubts and prejudices, you will not feel the Guru's grace.

The Guru is not a person who gives you something you do not have. The Guru is someone who helps you remove the obstacles that are hiding what you already have - the Self.

A powerful analogy is that of a mirror covered with dust. The Guru does not create a new reflection; he helps you wipe the dust off the mirror so that you can see your own true reflection.

Another analogy is that of a dark room. The Guru does not create the light; he just helps you find the switch to turn on the light that is already there.

Many seekers look for a Guru in the external world. But the real Guru is within you. The external Guru is just a pointer to the internal Guru.

Guru's grace is always available, but you must be open to receiving it. This means having faith, humility, and a sincere desire to know the Self.

Do not worry about finding the 'right' Guru. If your aspiration is sincere, the right Guru will come to you at the right time. In the meantime, practice Self-enquiry, and that will prepare you for the Guru's grace.

A seeker asked, 'What if I don't have a Guru?' Bhagavan replied, 'The Self is your Guru. Turn inward, and you will find the Guru within.'

Another important point is that once you have a Guru, you must have complete faith in him. Doubts will only hinder your progress. Just follow his teachings with sincerity and devotion.

The relationship between Guru and disciple is sacred. It is a relationship based on love and trust. When that relationship is strong, spiritual progress is rapid.
"""

    # 第八章 SELF-REALIZATION 添加内容
    self_realization_additional = """
Self-realization is not about gaining something new. It is about losing something - the ego, the sense of 'I am the body/mind'.

The state of Self-realization is not something that can be attained in the future. It is always here, now. The only thing you need to do is remove the obstacles that are hiding it.

A helpful analogy is that of a person who is looking for his glasses while they are on his nose. He searches everywhere, but he does not see what is right in front of him. Similarly, you search for the Self everywhere, but you do not see that it is right here, as you.

Another analogy is that of a wave in the ocean. The wave thinks it is separate from the ocean, but when it realizes its true nature, it understands that it is nothing but the ocean. Similarly, you think you are separate from the Self, but when you realize your true nature, you understand that you are nothing but the Self.

Do not wait for a dramatic experience to know that you have realized the Self. Self-realization is a quiet, peaceful state of simply being. It is not accompanied by fireworks or visions. It is just the natural state of things.

A seeker asked, 'What will change when I realize the Self?' Bhagavan replied, 'Nothing will change, and everything will change. The world will still be there, but you will see it differently. You will see it as a projection of your own mind, not as something separate from you.'

Another important point is that Self-realization is not the end of the path. It is the beginning of living in the truth. Once you have realized the Self, you must continue to abide in that state, moment by moment.

Do not compare your experience with others'. Each person's journey is unique. The important thing is to be sincere in your practice and to trust the process.

The peace of Self-realization is not dependent on external circumstances. It is a peace that comes from within, and it is unshakable. No matter what happens in the external world, that peace remains.

Finally, remember that you are not alone on this path. Countless seekers have walked this path before you, and they are all cheering you on. Trust yourself, trust the process, and you will surely reach the goal.
"""

    # 第九章 HEART 添加内容
    heart_additional = """
The Heart is not a physical organ. It is the spiritual center, the source of all being. When we talk about the Heart on the right side, it is just a pointer to help seekers find the source of the 'I'.

The Heart is the center of consciousness. It is where the 'I' arises, and it is where the 'I' merges back into the Self.

A helpful practice is to focus your attention on the Heart center. You can do this by visualizing a light in the Heart, or by simply feeling the sense of 'I' there.

Another important point is that the Heart and the Self are the same. When we talk about abiding in the Heart, we are talking about abiding as the Self.

Do not worry if you cannot feel the Heart center. Just keep practicing Self-enquiry, and that will naturally lead you to the Heart.

A seeker asked, 'How can I locate the Heart?' Bhagavan replied, 'It is not something you can locate with your mind. It is something you experience by turning your attention inward. When you ask 'Who am I?' with sincerity, you will naturally be drawn to the Heart.'

Another analogy is that of a magnet and iron filings. The magnet is the Heart, and the iron filings are your thoughts. When you turn your attention to the Heart, all your thoughts are naturally drawn there, and they dissolve.

The Heart is the source of all love. When you abide in the Heart, you naturally feel love for all beings, because you realize that all beings are not separate from you.

Finally, remember that the Heart is always open. It is never closed. The only thing that is closed is your mind. When you open your mind through Self-enquiry, you will see that the Heart has always been open, shining its light on all beings.
"""

    # 第十章 RENUNCIATION 添加内容
    renunciation_additional = """
True renunciation is not about giving up things. It is about giving up the attachment to things. You can live in the world, have possessions, perform your duties, but still be renounced inwardly.

A powerful analogy is that of a lotus leaf. The lotus leaf grows in the water, but it remains untouched by the water. Similarly, you can live in the world, but you can remain untouched by the world if you are established in the Self.

Another analogy is that of an actor on a stage. The actor plays his role, but he does not identify with the role. He knows that he is just acting. Similarly, you can play your role in life, but you do not have to identify with the role. You know that you are the Self.

Many seekers think that they have to give up their families, their jobs, their possessions to be spiritual. But that is not necessary. What is necessary is to give up the idea that you are the body/mind, and that these things are 'yours'.

A seeker asked, 'Can I be spiritual and still live a normal life?' Bhagavan replied, 'Yes, of course. Spirituality is not about how you live externally. It is about how you are internally. You can be spiritual in any situation, if you are established in the Self.'

Another important point is that renunciation and Self-enquiry go hand in hand. As you practice Self-enquiry, you naturally become less attached to external things. And as you become less attached, Self-enquiry becomes easier.

Do not force renunciation. Let it happen naturally as a result of your practice. If you try to force it, it will not last. But if it happens naturally, it will be permanent.

Finally, remember that the only thing you really need to renounce is the ego. When you renounce the ego, everything else follows naturally. You will still have your life, your family, your work, but you will not be attached to them. You will enjoy them, but you will not be dependent on them for your happiness.
"""

    # 第十一章 FATE AND FREEWILL 添加内容
    fate_freewill_additional = """
The relationship between fate and freewill is a mystery, but from the perspective of the Self, both are part of the same play. Fate is the script, and freewill is your choice of how to act in the play.

A helpful analogy is that of a movie. The script is already written, but the actors still have to perform their roles. Similarly, your fate is already determined, but you still have to make choices in life.

Another analogy is that of a train. The tracks are already laid, but you still have to keep the train on the tracks. Similarly, your fate is already laid out, but you still have to make efforts to stay on the path.

From the ego's perspective, fate and freewill seem like opposites. But from the Self's perspective, they are two sides of the same coin. Both are expressions of the same divine will.

Do not worry too much about whether something is fate or your freewill. Just focus on doing your best in every situation, and leave the rest to God.

A seeker asked, 'If everything is fate, why should I make any effort?' Bhagavan replied, 'Because making effort is also part of your fate. You cannot help but make effort, just as you cannot help but breathe. So make your effort, but do not be attached to the results.'

Another important point is that as you progress on the path, the distinction between fate and freewill becomes less and less important. Eventually, you realize that there is no 'you' to have freewill, and no 'fate' that is separate from you. Everything is just the Self playing.

Finally, remember that whether something is fate or freewill, the important thing is to stay centered in the Self. If you are established in the Self, it does not matter what happens externally. You will be at peace, no matter what.
"""

    # 第十二章 JNANI 添加内容
    jnani_additional = """
The jnani is not someone who has gained something new. The jnani is someone who has lost something - the ego. The jnani is just the Self, shining as it always has.

From the jnani's perspective, there is no world, no people, no problems. There is only the Self, everywhere and always. The jnani sees everything as the Self, and nothing but the Self.

A helpful analogy is that of the sun and the clouds. The sun is always shining, but sometimes clouds cover it. The jnani is like the sun without clouds - just pure, unobstructed light.

Another analogy is that of a mirror. A normal mirror reflects everything, but if the mirror is covered with dust, it cannot reflect clearly. The jnani is like a clean mirror - it reflects everything, but it is not affected by what it reflects.

Do not expect the jnani to behave in a certain way. The jnani may live in a cave, or he may live in a palace. He may be silent, or he may talk. He may work, or he may rest. The external behavior does not matter. What matters is the internal state - the state of abiding as the Self.

A seeker asked, 'How can I recognize a jnani?' Bhagavan replied, 'You cannot recognize a jnani with your mind. The jnani is beyond the mind. But if your own mind is pure, you will naturally be drawn to the jnani, and you will feel his presence.'

Another important point is that the jnani is not separate from you. The jnani is just the Self, and you are also the Self. The only difference is that the jnani knows it, and you do not (yet).

Do not put the jnani on a pedestal. The jnani is not a god. The jnani is just a human being who has realized his true nature. And you can do the same, if you are sincere in your practice.

Finally, remember that the greatest gift a jnani can give you is his presence. Just being in the presence of a jnani can help you purify your mind and realize the Self. So if you have the good fortune to meet a jnani, make the most of it.
"""

    # 第十三章 MISCELLANEOUS 添加内容
    miscellaneous_additional = """
Many seekers have questions about spiritual practices. Here are some important points to remember:

First, there is no 'best' practice. The best practice is the one that works for you. Some people are drawn to Self-enquiry, some to devotion, some to meditation, some to service. All are valid paths, and all lead to the same goal.

Second, consistency is more important than intensity. It is better to practice for 15 minutes every day than to practice for 3 hours once a week. Regular practice builds momentum and makes the practice natural.

Third, do not compare your practice with others'. Each person's journey is unique. What works for one person may not work for another. Just focus on your own practice, and trust the process.

Fourth, be patient. Spiritual growth is not always linear. There will be times when you feel like you are making progress, and times when you feel like you are going backward. This is normal. Just keep practicing, and eventually you will reach the goal.

Fifth, do not get attached to experiences. Spiritual experiences are nice, but they are not the goal. The goal is to realize the Self, which is beyond all experiences. So enjoy the experiences when they come, but do not cling to them.

Sixth, remember that you are not alone. There are countless seekers on this path, and countless teachers who have walked it before you. If you need help, ask for it. There is no shame in asking for guidance.

Seventh, and most importantly, trust yourself. You have the answer within you. The only thing you need to do is look inward and find it. No one else can do it for you, but no one else needs to. You have everything you need already, right here, right now.

Finally, enjoy the journey. The path to the Self is not a burden. It is a joy. Every step you take brings you closer to your true nature, which is peace, happiness, and love. So walk the path with joy, with gratitude, and with love.
"""

    # 现在替换内容
    # 第三章 MIND
    if 'MIND' in content:
        mind_end = content.find('"WHO AM I?"')
        if mind_end != -1:
            content = content[:mind_end] + mind_additional + content[mind_end:]
    
    # 第四章 WHO AM I?
    if '"WHO AM I?"' in content:
        who_end = content.find('SURRENDER')
        if who_end != -1:
            content = content[:who_end] + who_am_i_additional + content[who_end:]
    
    # 第五章 SURRENDER
    if 'SURRENDER' in content:
        surr_end = content.find('THE THREE STATES')
        if surr_end != -1:
            content = content[:surr_end] + surrender_additional + content[surr_end:]
    
    # 第六章 THE THREE STATES
    if 'THE THREE STATES' in content:
        three_end = content.find('GRACE AND GURU')
        if three_end != -1:
            content = content[:three_end] + three_states_additional + content[three_end:]
    
    # 第七章 GRACE AND GURU
    if 'GRACE AND GURU' in content:
        grace_end = content.find('SELF-REALIZATION')
        if grace_end != -1:
            content = content[:grace_end] + grace_guru_additional + content[grace_end:]
    
    # 第八章 SELF-REALIZATION
    if 'SELF-REALIZATION' in content:
        self_end = content.find('HEART')
        if self_end != -1:
            content = content[:self_end] + self_realization_additional + content[self_end:]
    
    # 第九章 HEART
    if 'HEART' in content:
        heart_end = content.find('RENUNCIATION')
        if heart_end != -1:
            content = content[:heart_end] + heart_additional + content[heart_end:]
    
    # 第十章 RENUNCIATION
    if 'RENUNCIATION' in content:
        ren_end = content.find('FATE AND FREEWILL')
        if ren_end != -1:
            content = content[:ren_end] + renunciation_additional + content[ren_end:]
    
    # 第十一章 FATE AND FREEWILL
    if 'FATE AND FREEWILL' in content:
        fate_end = content.find('JNANI')
        if fate_end != -1:
            content = content[:fate_end] + fate_freewill_additional + content[fate_end:]
    
    # 第十二章 JNANI
    if 'JNANI' in content:
        jnani_end = content.find('MISCELLANEOUS')
        if jnani_end != -1:
            content = content[:jnani_end] + jnani_additional + content[jnani_end:]
    
    # 第十三章 MISCELLANEOUS
    if 'MISCELLANEOUS' in content:
        content = content + miscellaneous_additional
    
    # 保存修改后的文件
    with open('/workspace/pdf_content/gems_from_bhagavan.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Successfully enriched Gems from Bhagavan!")
    print(f"Final file length: {len(content)} characters")

if __name__ == "__main__":
    enrich_gems_book()
