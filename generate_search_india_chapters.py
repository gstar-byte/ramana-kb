#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成《印度探秘》所有章节页面（除第9章已手动创建）
注意：所有内容字符串一律使用单引号'...'界定，避免与双引号嵌套冲突。
"""

import os

# 每章数据格式：
# (章节号, 中文标题, 英文标题,
#  概要段落1, 概要段落2, 概要段落3,
#  关键词1, 关键词2, 关键词3, 关键词4,
#  洞见列表 [(标题, 正文, 引用HTML)],
#  概念链接列表 ['href|名称'],
#  上一章href, 上一章标题, 下一章href, 下一章标题)

chapters = [
    (1, '向读者鞠躬', 'Wherein I Bow to the Reader',
     '布朗顿阐述他写作本书的初衷与方法。作为一名英国记者与灵性探索者，他带着科学的批判精神和对真理的热切渴望踏上印度之旅，在怀疑与开放之间保持平衡。',
     '布朗顿在本章开篇便坦白：他并非一个轻信者，而是一个受过科学训练的记者，习惯于用怀疑的眼光审视一切。然而，正是这种双重特质——批判的理性与灵性的敏感——使他能够在印度众多自称大师的人中辨别真伪。',
     '他明白，印度有两类人称为「圣人」：一类是表演者，以神奇把戏和催眠吸引信众；另一类是真正的探索者，以内在的安宁和对真理的坚守感化他人。他的目标是找到后者。',
     '探索动机', '辨别真伪', '科学态度', '灵性敏感',
     [
         ('探索的动机', '布朗顿从小便对东方神秘主义怀有强烈兴趣。他不满足于西方物质文明的解释，渴望亲自探寻那传说中隐藏于印度的古老智慧。',
          '"我想要亲眼看到。不是听说，不是阅读，而是亲身体验那些只在传说中出现的真理。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('批判与开放的平衡', '他明确表示，自己既不是盲目的信仰者，也不是顽固的怀疑论者。真正的探索需要保持开放，同时不放弃理性的判断。',
          '"印度的灵性传统中，玉石混杂。要找到真正的宝石，需要既有耐心，又有辨别力。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['self-enquiry.html|自我参究', 'self.html|真我', 'silence.html|静默'],
     'search-secret-india.html', '书籍主页', 'search-secret-india-ch2.html', '第二章：探索的序曲'),

    (2, '探索的序曲', 'A Prelude to the Quest',
     '布朗顿抵达印度，开始接触这片神秘土地的第一印象。从孟买到加尔各答，他在大城市中感受到印度的多样性，并开始建立他第一批灵性联系。',
     '布朗顿踏上印度土地的那一刻，立刻感受到了文化冲击。拥挤的街道、繁复的宗教仪式、随处可见的苦行僧……这片土地与他所熟悉的西方世界截然不同。',
     '在孟买和加尔各答，他开始寻访当地有名的灵性导师。然而他很快发现，大多数所谓的「圣人」不过是骗子或表演者，真正有智慧的人往往深居简出，不易寻访。',
     '印度初印象', '文化冲击', '第一次接触', '寻访圣者',
     [
         ('印度的神秘面貌', '布朗顿描述了他初抵印度时的震撼：这片土地同时存在着极度的贫穷与极致的灵性追求，物质的匮乏与精神的丰富并存。',
          '"印度是一本需要一生来读的书。它的表面令人困惑，但深处蕴藏着人类最古老的智慧。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('辨别真假圣人', '他迅速学会了如何区分真正的灵性探索者和那些利用宗教谋利的人。这种辨别能力成为他整个旅程的关键技能。',
          '"在一百个自称圣者的人中，也许只有一个是真实的。但那一个的价值，超过了其余九十九个的总和。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['guru.html|上师', 'grace.html|恩典', 'sadhana.html|修行'],
     'search-secret-india-ch1.html', '第一章：向读者鞠躬', 'search-secret-india-ch3.html', '第三章：来自埃及的魔术师'),

    (3, '来自埃及的魔术师', 'A Magician Out of Egypt',
     '布朗顿遇见了一位来自埃及的神秘魔术师，亲眼目睹了令人难以置信的超能力表演。这次相遇让他深入思考神秘现象的本质。',
     '这位魔术师是一位以操控物理现象著称的神秘主义者。布朗顿亲眼看到他从空气中凭空取出花朵、改变气味、甚至展示了其他让科学难以解释的现象。',
     '然而，布朗顿很快意识到：这些神奇的能力虽然令人叹为观止，却并不是真正的灵性觉醒的标志。能够创造奇迹的人，不一定是能够指引灵魂的人。',
     '神迹展示', '超能力疑问', '真伪之辨', '科学解释',
     [
         ('奇迹的诱惑与局限', '布朗顿见识了真实的奇迹，但他警觉地意识到，神迹本身并不等于智慧。一个人可以拥有强大的精神力量，却没有道德或灵性的深度。',
          '"我见到了真正的奇迹。然而奇迹只是证明了心灵的力量，却并未告诉我如何获得内心的平静。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('力量与智慧的区别', '这次相遇帮助布朗顿建立了一个重要的判断标准：真正的圣者拥有智慧和慈悲，而不仅仅是神奇的能力。',
          '"力量可以被训练，但智慧需要被觉醒。一个能移山的人，不一定能平息内心的波澜。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['sadhana.html|修行', 'mind.html|心智', 'maya.html|摩耶'],
     'search-secret-india-ch2.html', '第二章：探索的序曲', 'search-secret-india-ch4.html', '第四章：我遇见一位弥赛亚'),

    (4, '我遇见一位弥赛亚', 'I Meet a Messiah',
     '布朗顿拜访了梅赫巴巴，一位被称为新弥赛亚的精神导师，以自我强迫性沉默著称。这次相遇让布朗顿思考沉默的真正含义。',
     '梅赫巴巴是20世纪初印度最有影响力的灵性人物之一。他从1925年起保持完全沉默，通过手势和字母板与人交流，吸引了大量东西方追随者。',
     '布朗顿注意到，梅赫巴巴的沉默与马哈希的沉默有着本质的不同。前者是一种有意为之的宗教行为，而马哈希的沉默则是内在实现后的自然状态。',
     '梅赫巴巴', '弥赛亚崇拜', '沉默的形式', '真正的教化',
     [
         ('不同形式的沉默', '布朗顿观察到，沉默有多种形式。有些人因为没有值得分享的东西而沉默，有些人的沉默是一种修行方式，而少数人的沉默是因为语言已经无法表达他们所知的真理。',
          '"并非所有的沉默都是平等的。马哈希的沉默是满溢，梅赫巴巴的沉默是寻找。"\n                        <div class="source">—— 保罗·布朗顿（反思）</div>'),
         ('东西方灵性的融合', '梅赫巴巴的追随者来自世界各地，展示了灵性追求的普遍性，也让布朗顿思考东方智慧如何能够真正被西方世界接受。',
          '"真正的灵性真理超越文化、超越语言。它是人类共同的遗产，无论你来自东方还是西方。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['silence.html|静默', 'guru.html|上师', 'grace.html|恩典'],
     'search-secret-india-ch3.html', '第三章：来自埃及的魔术师', 'search-secret-india-ch5.html', '第五章：阿迪亚河的隐士'),

    (5, '阿迪亚河的隐士', 'The Anchorite of the Adyar River',
     '在阿迪亚河畔，布朗顿遇见了一位深居简出的隐士。这位隐士的生活方式和教导让作者对印度灵性传统有了更深的理解，也让他思考孤独与出世的意义。',
     '这位住在阿迪亚河畔的隐士过着极其简朴的生活，每天只有少量的食物和时间用于世俗事务，其余时间全部用于冥想和内省。他的宁静和专注给布朗顿留下了深刻印象。',
     '与这位隐士的相遇让布朗顿思考：真正的灵性修行是否需要彻底的出世？还是在世俗生活中同样可以达到内在的解脱？这个问题在他后来与马哈希的对话中得到了回答。',
     '隐士生活', '河畔教导', '简朴之道', '出世与入世',
     [
         ('简朴生活的智慧', '这位隐士的生活让布朗顿看到：外在的简朴不是贫困，而是一种有意识的选择，为了让心灵能够专注于内在的探索。',
          '"他所拥有的，比任何百万富翁都要少；他所体验的，比任何百万富翁都要丰富。这就是简朴生活的悖论。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('内在宁静的价值', '与这位隐士共处的时光，让布朗顿体验到了一种他在繁忙的西方世界从未有过的宁静。这种宁静不是空洞的，而是充满了生机与觉知。',
          '"在他的陪伴中，我感到一种深沉的宁静，仿佛世界的喧嚣在这里找到了它的源头，然后归于平静。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['peace.html|安宁', 'sadhana.html|修行', 'surrender.html|臣服'],
     'search-secret-india-ch4.html', '第四章：我遇见一位弥赛亚', 'search-secret-india-ch6.html', '第六章：征服死亡的瑜伽'),

    (6, '征服死亡的瑜伽', 'The Yoga Which Conquers Death',
     '布朗顿深入了解哈他瑜伽和某些高级瑜伽士如何通过特殊的修行方法达到对身体的极限控制，包括看似征服死亡的能力，以及这些能力背后的灵性意义。',
     '布朗顿遇到了一位能够控制自身生理功能的瑜伽士——减缓心跳、控制呼吸、甚至在表面上进入死亡状态然后苏醒。这些能力震撼了布朗顿，但也让他陷入困惑。',
     '这些令人惊叹的身体控制能力代表了瑜伽修行的一个层面，但布朗顿逐渐明白，这些能力本身不是目的，而只是特定修行道路上的副产品。真正的瑜伽是关于意识的转化，而非身体的控制。',
     '哈他瑜伽', '身体控制', '呼吸修炼', '生死超越',
     [
         ('身体的限制与可能', '这次经历让布朗顿意识到，人类的身体远比西方科学所认为的更有潜力。但同时，他也明白，这些身体层面的成就不是灵性觉醒的真正标志。',
          '"身体是心灵的工具，而非目的。控制身体的极限是值得尊重的成就，但真正的修行是控制心灵，最终超越心灵。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('生死的真正含义', '通过对征服死亡的瑜伽的研究，布朗顿开始思考死亡的真正含义。印度灵性传统认为，真正的不死不是身体的长寿，而是对真我的认识——真我是永恒的，不生不灭。',
          '"真正的不死，是认识到那个从未诞生也不会死亡的真我。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['samadhi.html|三摩地', 'self.html|真我', 'moksha.html|解脱'],
     'search-secret-india-ch5.html', '第五章：阿迪亚河的隐士', 'search-secret-india-ch7.html', '第七章：从不言语的圣人'),

    (7, '从不言语的圣人', 'The Sage Who Never Speaks',
     '布朗顿遇见了一位完全保持沉默的圣人，在真正意义上沉默——不仅不说话，而且安住于无言的真我中。这次相遇让布朗顿开始理解静默教法的深意。',
     '这位从不开口的圣人与梅赫巴巴的沉默不同——他的沉默不是一种有意的宗教行为，而是一种自然的状态。他已经如此深刻地安住于内在的真我，以至于言语对他来说已经是多余的。',
     '在这位圣人面前，布朗顿第一次体验到了真正的沉默传导。不是信息的传达，不是哲学的讲授，而是一种直接的存在与存在之间的相遇——在那里，语言永远无法到达的地方。',
     '真正的沉默', '无言教导', '静默传导', '前体验',
     [
         ('沉默的层次', '布朗顿开始区分不同层次的沉默：有些人沉默是因为没有话说，有些人沉默是一种戒律，而这位圣人的沉默则是因为他已经超越了言语所能表达的境界。',
          '"有些沉默是空洞的，有些沉默是充实的。他的沉默如同宇宙诞生前的那种寂静——不是无，而是一切可能性的源泉。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('无言的传导', '布朗顿描述了一种神奇的体验：在这位圣人面前，他感到自己的思绪自然平静，某种深刻的平和感渗入了他的内心。这不是通过言语传递的，而是通过存在本身。',
          '"他什么都没有教我，但我从他那里学到了一切。这就是最高的教导——存在对存在，真我对真我。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['silence.html|静默', 'awareness.html|觉知', 'self.html|真我'],
     'search-secret-india-ch6.html', '第六章：征服死亡的瑜伽', 'search-secret-india-ch8.html', '第八章：南印度的精神领袖'),

    (8, '南印度的精神领袖', 'With the Spiritual Head of South India',
     '布朗顿拜访了商羯罗阿阇黎，南印度最受尊敬的宗教权威和哲学大师。这次相遇让布朗顿了解了印度传统宗教权威与纯粹灵性体验之间的关系。',
     '商羯罗阿阇黎代表了印度传统宗教权威的最高层级，他是吠檀多哲学的传承者，博学多才，受到整个南印度的尊敬和崇拜。布朗顿与他进行了一次深刻的哲学对话。',
     '然而，布朗顿也注意到：即使是这样博学的宗教权威，也不同于马哈希那种直接来自自我实现的教导。知识和智慧是两种不同的东西——前者可以通过学习获得，后者只能通过直接的体验。',
     '吠檀多哲学', '传统权威', '知识与智慧', '学与悟',
     [
         ('吠檀多哲学的精华', '商羯罗阿阇黎向布朗顿介绍了印度非二元论哲学的核心：梵（宇宙意识）与阿特曼（个体真我）是同一的，世界的多样性是摩耶（幻相）的产物。',
          '"你就是梵。不是变成，不是靠近，而是本来就是。无明让你忘记了这一点，智慧让你重新认识这一点。"\n                        <div class="source">—— 商羯罗阿阇黎</div>'),
         ('学问与体验的差距', '布朗顿通过这次相遇意识到，真正的灵性觉醒不是通过知识积累达到的，而是通过直接的体验。博学可以帮助理解，但不能代替体验。',
          '"我读过所有的圣典，我教导了所有的学生，但真正的觉醒不是通过阅读实现的，而是通过回归内在的静默。"\n                        <div class="source">—— 商羯罗阿阇黎</div>'),
     ],
     ['brahman.html|梵', 'self.html|真我', 'maya.html|摩耶', 'jnana.html|智慧'],
     'search-secret-india-ch7.html', '第七章：从不言语的圣人', 'search-secret-india-ch9.html', '第九章：圣光之山'),

    (10, '魔术师与圣者之间', 'Among the Magicians and Holy Men',
     '离开阿鲁那佳拉后，布朗顿继续他的旅程，遇见了更多声称有神奇能力的瑜伽士和魔术师。经过与马哈希的相遇，他对这些人有了全新的判断标准。',
     '有了与马哈希相遇的经历作为对比，布朗顿现在能够更清楚地看到这些声称有超能力者的局限性。他们的能力或许是真实的，但那种深沉的安宁与慈悲，是他们所缺乏的。',
     '这段旅程成为了一种验证——马哈希的静默和存在所给予他的，是那些最神奇的表演者都无法给予的。真正的灵性不在于能力，而在于内在的实现。',
     '能力与觉醒', '外在神迹', '内在实现', '新的判断标准',
     [
         ('以马哈希为标准', '布朗顿承认，遇见马哈希之后，他对其他灵性导师的评判标准发生了根本性的转变。现在他寻找的不是神奇的能力，而是那种深沉的内在宁静。',
          '"遇见马哈希之后，我发现自己无法再对那些华而不实的表演感到惊讶。那是因为我已经见到了真正的光。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('神迹的局限', '布朗顿最终得出结论：神迹可以吸引注意力，但不能带来真正的灵性觉醒。真正的教导是通过存在影响存在，而不是通过奇异的表演。',
          '"凡是需要证明自己的，往往才是真正需要被质疑的。真正的智者不需要奇迹，他的存在本身就已足够。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['grace.html|恩典', 'self-enquiry.html|自我参究', 'jnani.html|觉者'],
     'search-secret-india-ch9.html', '第九章：圣光之山', 'search-secret-india-ch11.html', '第十一章：贝拿勒斯的奇迹工作者'),

    (11, '贝拿勒斯的奇迹工作者', 'The Wonder-Worker of Benares',
     '在圣城贝拿勒斯，布朗顿遇见了一位以神奇力量闻名的圣者，他展示了用太阳光线加热物体等令人震惊的能力，引发了布朗顿对神秘力量本质的深层思考。',
     '贝拿勒斯是印度最神圣的城市，恒河在此缓缓流淌，数千年来是灵性追求者的聚集地。在这里，布朗顿再次遇到了神奇力量的展示，但这次他已经有了更成熟的判断力。',
     '与这位奇迹工作者的相遇让布朗顿进一步思考：这些超自然能力究竟来自哪里？它们是修行的副产品，还是某种特殊才能？更重要的是，这些能力对于真正的灵性觉醒有什么帮助？',
     '贝拿勒斯圣城', '超自然力量', '神奇才能源头', '真正的意义',
     [
         ('力量的来源', '布朗顿探讨了这些神奇能力的可能来源，包括某些高级的冥想修行、对自然法则的深刻理解，以及可能存在的意识与物质之间的联系。',
          '"这些能力证明了心灵的力量超越我们的通常想象。但证明了这一点之后，更重要的问题是：这股力量最终应该服务于什么目的？"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('神迹与内在转化', '布朗顿最终理解，真正的灵性修行的目的不是获得特殊能力，而是内在的转化——从痛苦走向宁静，从无明走向觉悟。',
          '"所有的能力，如果不以内在的解脱为目标，都只不过是更复杂的束缚。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['samadhi.html|三摩地', 'mind.html|心智', 'maya.html|摩耶'],
     'search-secret-india-ch10.html', '第十章：魔术师与圣者之间', 'search-secret-india-ch12.html', '第十二章：写在星辰中'),

    (12, '写在星辰中', 'Written in the Stars',
     '布朗顿探讨占星术在印度灵性传统中的角色，以及命运与自由意志的关系。他遇到了精通占星的圣人，了解了印度人对时间、命运和宇宙秩序的独特理解。',
     '印度占星术被视为吠陀知识体系的重要组成部分，不仅仅是预测命运的工具，更是理解宇宙秩序和个人灵魂旅程的一种方式。布朗顿遇见了一位精通此道的智者。',
     '然而，布朗顿也记录了马哈希对命运的独特看法：从真我的角度来看，命运与自由意志的争论是在身份认同层面上的，当你认识到真我，这个问题就自然消融了。',
     '占星智慧', '命运之谜', '自由意志', '宇宙秩序',
     [
         ('命运的两个层面', '布朗顿了解到，印度传统区分了两种命运：宿业（已经开始显现的业力）和现世业（通过当下的行为积累的业力）。两者都真实，却不等于最终的束缚。',
          '"你的过去塑造了你，但不能限制你。在每一个当下，你都有选择——向内还是向外，迈向解脱还是加深束缚。"\n                        <div class="source">—— 布朗顿遇见的占星圣者</div>'),
         ('超越命运', '马哈希的观点更为直接：只要你把自己认同为有限的个体，命运与自由意志的问题就存在。一旦你认识到真我，你会发现自己从未真正受命运束缚。',
          '"谁在受命运束缚？找到这个「谁」，你就会发现，那个真正的你是不受命运束缚的。"\n                        <div class="source">—— 室利·拉玛那·马哈希</div>'),
     ],
     ['fate.html|命运', 'freewill.html|自由意志', 'karma.html|业力', 'prarabdha.html|宿业'],
     'search-secret-india-ch11.html', '第十一章：贝拿勒斯的奇迹工作者', 'search-secret-india-ch13.html', '第十三章：主的花园'),

    (13, '主的花园', 'The Garden of the Lord',
     '布朗顿访问了一处充满灵性气息的花园式静修社区，被称为主的花园。这里的修行者通过集体生活、服务和奉爱的方式追求灵性觉醒。',
     '这处美丽的灵性社区将自然之美与灵性修行完美融合。修行者们在花园中劳作、祈祷、唱颂，以一种整体化的方式追求与神的合一。',
     '这次访问让布朗顿思考不同的灵性道路：有些人通过孤独冥想觉醒，有些人通过知识和哲学探索，有些人通过奉爱和服务。马哈希的教导表明，这些都可以通向同一个目标。',
     '集体修行', '奉爱与服务', '自然与灵性', '多种道路',
     [
         ('奉爱之道', '在这处花园社区，布朗顿体验了印度的奉爱传统——通过对神的深沉爱慕和服务，达到自我消融和与神合一的境界。',
          '"在奉爱中，个体与宇宙的界限消融。当你全心全意地爱神，你就会发现，你爱的正是你自己的真正本性。"\n                        <div class="source">—— 花园社区的圣者</div>'),
         ('美与灵性的结合', '布朗顿注意到，这处花园的美丽本身也是一种教导——大自然的秩序与和谐，反映了宇宙意识的属性。在美中，我们能够瞥见那超越言语的真理。',
          '"美是真理的一个面貌。当你真正欣赏一朵花，你触碰到的不仅是那朵花，而是创造了那朵花的宇宙意识。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['bhakti.html|奉爱', 'grace.html|恩典', 'satchidananda.html|存在-意识-喜悦'],
     'search-secret-india-ch12.html', '第十二章：写在星辰中', 'search-secret-india-ch14.html', '第十四章：在帕西弥赛亚的总部'),

    (14, '在帕西弥赛亚的总部', 'At the Parsee Messiah\'s Headquarters',
     '布朗顿拜访了帕西社区（拜火教）的一位精神领袖，了解了这个古老宗教传统的灵性追求，以及不同宗教如何指向同一个普世真理。',
     '帕西人（拜火教徒）是印度少数族群中极具智慧和贡献的群体。他们的宗教传统源自古代波斯，强调光明对抗黑暗、真理对抗谎言的宇宙观。',
     '这次相遇让布朗顿看到，无论是印度教、拜火教还是其他宗教传统，最终都在指向同一个普世的灵性真理——内在的光明、真理与善。',
     '帕西传统', '拜火教智慧', '普世灵性', '宗教对话',
     [
         ('光明的象征', '拜火教以圣火作为神的象征，强调光明是神圣本质的体现。布朗顿发现，这与马哈希所说的真我如同太阳、始终在照耀有着深刻的共鸣。',
          '"真理之光永远不熄灭。无论你用什么名字称呼它，无论你通过什么路径接近它，它都是同一个光。"\n                        <div class="source">—— 帕西精神领袖</div>'),
         ('不同宗教的共同心脏', '通过这次跨宗教的对话，布朗顿更加确信：所有伟大的灵性传统都有一个共同的心脏——对真理的追求，对内在神性的认识，对无限爱的体验。',
          '"剥去所有的形式、仪式和教义，所有宗教的核心都是同一个灵性追求：认识自己，认识神，认识那内在的光明。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['self.html|真我', 'grace.html|恩典', 'brahman.html|梵'],
     'search-secret-india-ch13.html', '第十三章：主的花园', 'search-secret-india-ch15.html', '第十五章：一次奇异的相遇'),

    (15, '一次奇异的相遇', 'A Strange Encounter',
     '布朗顿记录了一次意外而神秘的相遇，这次经历进一步挑战了他对现实的理解，也让他更深刻地思考意识与物质世界的关系。',
     '在旅程即将结束之际，布朗顿遭遇了一次令他难以解释的神秘体验。这次体验挑战了他惯常的世界观，也进一步印证了印度灵性传统关于意识超越物质的主张。',
     '然而，最终让布朗顿印象最深的并不是这次神秘体验本身，而是这次体验过后他的内心感受——那种短暂的宁静和清明，让他更加渴望找到马哈希所体现的那种永久的内在安宁。',
     '神秘体验', '意识扩展', '现实的本质', '渴望安宁',
     [
         ('神秘体验的价值与局限', '布朗顿意识到，神秘体验可以打开一扇窗，让我们窥见意识的更广阔可能性，但它们本身不是终点，而是指向更深探索的路标。',
          '"每一次神秘体验都像是一道闪光，照亮了我们真实本性的一个侧面。但闪光是短暂的，我需要的是能够持续照亮的阳光。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('体验与存在的区别', '这次相遇让布朗顿思考一个深刻的问题：为什么神秘体验是短暂的，而马哈希的那种宁静和觉知似乎是永久性的？答案在于：前者是体验，后者是存在的状态。',
          '"体验有来有去，但那个体验的人——那个觉知本身——永远在那里。真正的觉醒不是获得一个更好的体验，而是认识到你本来就是那永恒的觉知。"\n                        <div class="source">—— 保罗·布朗顿（后期反思）</div>'),
     ],
     ['awareness.html|觉知', 'self.html|真我', 'samadhi.html|三摩地'],
     'search-secret-india-ch14.html', '第十四章：在帕西弥赛亚的总部', 'search-secret-india-ch16.html', '第十六章：丛林隐修院中'),

    (16, '丛林隐修院中', 'In a Jungle Hermitage',
     '布朗顿深入丛林，拜访了一处偏远的隐修院。在这里的修行者过着最简朴的生活，完全隔绝于世俗，专注于最纯粹的灵性探索。',
     '这处丛林隐修院远离尘嚣，修行者们只在最基本的生存需求上花费时间，其余一切精力都投入到内在探索中。与他们的相遇，让布朗顿思考完全出世的修行方式。',
     '在这里，布朗顿体验到了一种前所未有的深沉宁静。丛林的寂静、修行者的专注、以及远离世俗喧嚣所带来的清明，都让他更加接近那种他一直在寻找的内在真相。',
     '丛林修行', '彻底简朴', '深度冥想', '出世的智慧',
     [
         ('彻底出世的意义', '布朗顿思考，彻底出世的修行方式是否是必要的？他后来从马哈希那里了解到：解脱可以在任何生活处境中实现，出世与否不是关键，关键是内心对真我的认识。',
          '"山中的修行者和市场中的商人，如果都认识了真我，他们的解脱是同等真实的。地点不重要，认识才重要。"\n                        <div class="source">—— 室利·拉玛那·马哈希</div>'),
         ('深度静默的体验', '在丛林的夜晚，布朗顿体验到了一种罕见的深度静默——不仅是外在环境的寂静，而且是内心的静止。在那片刻，他感到了一种难以言说的完整。',
          '"那一夜的丛林告诉了我什么叫做真正的静默。不是声音的缺失，而是所有寻找的停止，以及对那一直存在的东西的认识。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['silence.html|静默', 'samadhi.html|三摩地', 'peace.html|安宁', 'sadhana.html|修行'],
     'search-secret-india-ch15.html', '第十五章：一次奇异的相遇', 'search-secret-india-ch17.html', '第十七章：被遗忘的真理碑'),

    (17, '被遗忘的真理碑', 'Tablets of Forgotten Truth',
     '全书结语。布朗顿总结他的印度之旅，提炼出他所发现的永恒真理。他反思整个旅程，最终认识到，那些被遗忘的真理其实从未真正消失，只是等待着被重新发现。',
     '经过数月的旅行和无数次相遇，布朗顿回顾他的印度之旅。他遇见了魔术师、圣者、哲学家、宗教领袖——形形色色的人，代表着灵性探索的不同面向。',
     '然而，最终留在他心中最深处的，是在阿鲁那佳拉与马哈希相遇的那段时光。那无言的教化，那静默中的智慧，那超越一切的宁静——这才是他来印度真正寻找的东西。',
     '旅程总结', '永恒真理', '重新发现', '东西方融合',
     [
         ('被遗忘的古老智慧', '布朗顿认为，印度的古老灵性智慧代表了人类最宝贵的遗产之一。这些智慧并未消失，只是在现代世界的喧嚣中被暂时遗忘了。随着越来越多的人开始关注内在，这些真理正在重新被发现。',
          '"这些古老的真理比所有的现代发现更加深刻。它们揭示的不是外在世界的规律，而是意识本身的本质——这才是所有知识中最基本、最重要的知识。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
         ('写给西方世界的信', '这本书是布朗顿写给西方世界的一封信，告诉他们：在东方，在印度，存在着一种对生命意义的理解，这种理解可以补充和丰富西方文明的物质成就。',
          '"我们从东方获得了香料、丝绸和棉花。是时候向东方学习更宝贵的东西了——一种关于意识、关于真我、关于内在宁静的智慧。"\n                        <div class="source">—— 保罗·布朗顿</div>'),
     ],
     ['self-enquiry.html|自我参究', 'self.html|真我', 'silence.html|静默', 'moksha.html|解脱'],
     'search-secret-india-ch16.html', '第十六章：丛林隐修院中', 'search-secret-india.html', '书籍主页'),
]


def make_sidebar_items(chap_num):
    items = ''
    labels = {
        1: '第一章：向读者鞠躬',
        2: '第二章：探索的序曲',
        3: '第三章：来自埃及的魔术师',
        4: '第四章：我遇见一位弥赛亚',
        5: '第五章：阿迪亚河的隐士',
        6: '第六章：征服死亡的瑜伽',
        7: '第七章：从不言语的圣人',
        8: '第八章：南印度的精神领袖',
        9: '第九章：圣光之山',
        10: '第十章：魔术师与圣者之间',
        11: '第十一章：贝拿勒斯的奇迹工作者',
        12: '第十二章：写在星辰中',
        13: '第十三章：主的花园',
        14: '第十四章：在帕西弥赛亚的总部',
        15: '第十五章：一次奇异的相遇',
        16: '第十六章：丛林隐修院中',
        17: '第十七章：被遗忘的真理碑',
    }
    for i in range(1, 18):
        label = labels.get(i, f'第{i}章')
        active = ' class="sidebar-item active"' if i == chap_num else ' class="sidebar-item"'
        items += f'                    <a href="search-secret-india-ch{i}.html"{active}>{label}</a>\n'
    return items


def make_concept_tags(concepts):
    tags = ''
    for c in concepts:
        href, name = c.split('|')
        tags += f'                        <a href="../concepts/{href}" class="concept-tag">{name}</a>\n'
    return tags


def make_insight_sections(insights):
    html = ''
    for title, body, quote in insights:
        html += f"""
                    <h3 style="color:var(--accent);margin:1.5rem 0 1rem;">{title}</h3>
                    <p style="margin-bottom:1rem;">{body}</p>
                    <div class="quote-box">
                        {quote}
                    </div>
"""
    return html


template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="印度探秘第{num}章：{title}。{desc_short}">
    <meta name="keywords" content="印度探秘, 保罗·布朗顿, 马哈希, 阿鲁那佳拉, 灵性探索, {kw1}, {kw2}">
    <title>印度探秘 第{num}章：{title} | 拉玛那马哈希知识库</title>
    <link rel="stylesheet" href="../styles.css">
    <meta name="theme-color" content="#1a1a2e">
    <link rel="manifest" href="../manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🙏%3C/text%3E%3C/svg%3E">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://ramanamaharshi.space/books/search-secret-india-ch{num}">
    <meta property="og:title" content="印度探秘 第{num}章：{title} | 拉玛那马哈希知识库">
    <meta property="og:description" content="{desc_short}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://ramanamaharshi.space/books/search-secret-india-ch{num}">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="拉玛那马哈希知识库">
    <meta property="og:image" content="https://ramanamaharshi.space/images/og-default.jpg">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-MYFWHFPSYB');
    </script>
    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "拉玛那马哈希知识库", "item": "https://ramanamaharshi.space/"}},
    {{"@type": "ListItem", "position": 2, "name": "书籍", "item": "https://ramanamaharshi.space/books"}},
    {{"@type": "ListItem", "position": 3, "name": "印度探秘", "item": "https://ramanamaharshi.space/books/search-secret-india"}}
  ]
}}
    </script>
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <aside class="sidebar" id="sidebar" data-chapter-mode="true">
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 拉玛那知识库</a>
            </div>
            <div class="search-box">
                <input type="text" id="search-input" placeholder="搜索..." autocomplete="off">
                <div id="search-results"></div>
            </div>
            <div class="sidebar-section" id="chapter-section">
                <div class="sidebar-section-title">🔍 印度探秘</div>
                <div class="sidebar-items">
{sidebar_items}                </div>
            </div>
            <div class="sidebar-section collapsed" id="other-books-section">
                <div class="sidebar-section-title">📚 其他书籍</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item">📚 书籍总览</a>
                    <a href="../books/be-as-you-are.html" class="sidebar-item">📖 走向静默，如你本来</a>
                    <a href="../books/gems.html" class="sidebar-item">💎 宝钻集</a>
                    <a href="../books/talks.html" class="sidebar-item">💬 对谈录</a>
                    <a href="../books/face-to-face.html" class="sidebar-item">👁️ 面对面</a>
                </div>
            </div>
        </aside>

        <main class="main-content">
            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">印度探秘</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="../index.html" class="active">书籍</a>
                    <a href="../concepts/index.html">概念</a>
                    <a href="../methods/index.html">方法</a>
                    <a href="../qa/index.html">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>

            <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="../books/index.html">书籍</a> /
                    <a href="search-secret-india.html">印度探秘</a> /
                    <span>第{num}章：{title}</span>
                </nav>

                <header class="page-header">
                    <h1>第{num}章：{title}</h1>
                    <p class="subtitle">{en_title} | 保罗·布朗顿 著</p>
                </header>

                <!-- 章节概要 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1.5rem;">📝 章节概要</h2>
                    <p style="margin-bottom:1rem;">{summary1}</p>
                    <p style="margin-bottom:1rem;">{summary2}</p>
                    <p>{summary3}</p>
                </div>

                <!-- 核心板块 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1.5rem;">🌟 核心板块</h2>
                    <div class="concept-tags" style="margin-bottom:1.5rem;">
                        <span class="tag">{kw1}</span>
                        <span class="tag">{kw2}</span>
                        <span class="tag">{kw3}</span>
                        <span class="tag">{kw4}</span>
                    </div>
                    {insight_sections}
                </div>

                <!-- 相关概念 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1.5rem;">🔗 相关概念</h2>
                    <div class="concept-tags">
{concept_tags}                    </div>
                </div>

                <!-- 章节导航 -->
                <div class="page-nav">
                    <a href="{prev_href}">
                        <span class="nav-label">← 上一章</span>
                        <span class="nav-title">{prev_title}</span>
                    </a>
                    <a href="{next_href}" class="next">
                        <span class="nav-label">下一章 →</span>
                        <span class="nav-title">{next_title}</span>
                    </a>
                </div>
            </div>

            <footer class="site-footer">
                <p>拉玛那马哈希Space | <a href="search-secret-india.html">← 返回书籍主页</a></p>
            </footer>
        </main>
    </div>
    
    <script>
        function toggleSidebar() {{
            const s = document.getElementById('sidebar');
            const o = document.getElementById('sidebarOverlay');
            s.classList.toggle('open');
            if (o) o.classList.toggle('open');
        }}
        document.querySelectorAll('.sidebar-section-title').forEach(title => {{
            title.addEventListener('click', () => title.parentElement.classList.toggle('collapsed'));
        }});
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') document.getElementById('sidebar').classList.remove('open');
        }});
    </script>
<script src="../script.js"></script>
</body>
</html>'''

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages', 'books')

# 第9章已手动创建，跳过
skip_chapters = {9}

created = 0
for chapter_data in chapters:
    (num, title, en_title,
     summary1, summary2, summary3,
     kw1, kw2, kw3, kw4,
     insights, concepts,
     prev_href, prev_title, next_href, next_title) = chapter_data

    if num in skip_chapters:
        continue

    filename = f'search-secret-india-ch{num}.html'
    filepath = os.path.join(output_dir, filename)

    # 如果已存在则跳过
    if os.path.exists(filepath):
        print(f'已存在，跳过: {filename}')
        continue

    sidebar_items = make_sidebar_items(num)
    concept_tags = make_concept_tags(concepts)
    insight_sections = make_insight_sections(insights)
    desc_short = summary1[:100] if len(summary1) > 100 else summary1

    content = template.format(
        num=num,
        title=title,
        en_title=en_title,
        desc_short=desc_short,
        summary1=summary1,
        summary2=summary2,
        summary3=summary3,
        kw1=kw1, kw2=kw2, kw3=kw3, kw4=kw4,
        sidebar_items=sidebar_items,
        insight_sections=insight_sections,
        concept_tags=concept_tags,
        prev_href=prev_href,
        prev_title=prev_title,
        next_href=next_href,
        next_title=next_title,
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'创建: {filename}')
    created += 1

print(f'\n共创建 {created} 个章节页面（第9章已手动创建，跳过）')
