#!/usr/bin/env python3
"""正确添加49个新QA到index.html"""

with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.splitlines()

# 找到 </div> 关闭 qa-list 的行
close_div_line = None
for i, line in enumerate(lines):
    if '</div>' in line and i > 4400:
        close_div_line = i
        break

print(f"</div> 在第 {close_div_line + 1} 行")
print(f"该行内容: {lines[close_div_line][:80]}")

# 49个新问答（正确的新格式）
new_qa_items = '''                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是自我探究？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>自我探究是问"我是谁"的过程。不是用心智去找答案，而是将注意力从外物不断收回到"我是谁"这个根本问题。答案不在语言中，而在于探究本身。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ "我是谁"这个问题为什么重要？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>因为它直指一切问题的根源——自我。所有的痛苦、恐惧、欲望都源于对虚假自我的认同。探究"我是谁"能瓦解这个认同。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 其他念头和"我是谁"冲突吗？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>不冲突。当其他念头升起时，不要跟随它们，只是问："是谁在有这个念头？"这会把注意力引回源头，最终念头会自行消失。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 如何处理强烈的情绪？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>不要抗拒，也不要放纵。只是观照："是谁在感受这个情绪？"情绪会升起、停留、消失——它们的本质是空性的。观照本身就是解脱。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="心智">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是心的本质？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：心智</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>心的本质是意识——纯粹的觉知。所有思想、情感、记忆都从它生起又归于它。它本身是寂静的、圆满的、不受干扰的。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="真我">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 真我和身体是什么关系？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：真我</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>真我不在身体里，身体从真我中显现。就像波浪从大海生起，但大海不在波浪里。认识到这点就是"见道"。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="静默">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 为什么要静默？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：静默</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>马哈希用静默教导：真理超越语言。语言是相对的、有限的；真我是绝对的、无限的。静默是上师最有力的教法。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="禅定">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是三摩地？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：禅定</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>三摩地是专注与冥想，但更准确地说，是"本然的静止"。不是一种特殊状态，而是认识到心本来寂静的状态。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="觉悟">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 普通人和觉悟者的区别是什么？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：觉悟</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>没有本质区别。差别只在于：觉悟者认识到真我，普通人迷失在念头中。波浪还在，但大海知道了自己是海。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="真我">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 如何理解"一切皆一"？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：真我</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>从究竟层面，只有"一"存在——那就是真我、意识、梵。所有看似分离的事物都只是这个"一"的不同显现，如同梦境中的各种角色。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 静坐时看到光明是怎么回事？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>各种内在光明的体验——白光、金光、蓝光——都是心轮或意识的显现。它们是修行的自然现象，但不是目标。不要执着它们，继续探究是谁在看到这个光明。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="真我">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是"大乐"的体验？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：真我</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>大乐（Ananda）是真我的本质之一。它不是情绪性的快乐，而是一种圆满的存在感。执着于大乐体验会障碍进一步了悟。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="禅定">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 静坐时身体消失的感觉正常吗？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：禅定</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>是的。这是心专注时粗重身体感的消融，是禅定的常见现象。身体仍然存在，只是意识焦点转移了。不要恐惧，继续修行。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="真我">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 为什么静坐时会感到巨大的喜悦？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：真我</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>这是真我的自然显现。当心从念头中安静下来，内在的喜悦就会显露。它不是修行的成就，而是本来的状态。喜悦升起又消失，但观照者不变。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="禅定">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是"无念"的境界？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：禅定</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>无念不是心的空白或昏迷，而是念头完全静止的状态。在这种状态下，意识完全清醒，但没有任何思想活动。这是真我的本然状态。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 静坐时听到声音怎么办？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>无论是内在的声音还是外在的声音，都只是心的显现。不要执着也不要恐惧。问："是谁在听到这个声音？"把它作为自我探究的助缘。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="智慧">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是"三轮体空"？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：智慧</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>修行者、受修行者、修行行为——这三者本质皆空。没有真实的"我在修行"，也没有"我修成了什么"。认识到这点即是空性的智慧。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="禅定">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 禅定中出现的境界是真实的吗？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：禅定</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>一切境界——无论是天人、净土还是各种景象——都是心的投射，不是究竟真实。不要被任何境界所迷，继续探究"这是谁的境界"。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="禅定">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是"一行三昧"？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：禅定</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>一行三昧是"一行"即"一切行"的禅定状态。认识到真我之后，行住坐卧皆是三昧。不是专注一境，而是见一切法皆真我。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 静坐时感到恐惧正常吗？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>当你安静下来时，平时被忽略的深层恐惧会浮出水面。这是好事，说明你开始面对它们了。不要逃避，观照恐惧，问："是谁在恐惧？"</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="真我">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 真我和自我有什么不同？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：真我</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>自我（ego）是虚假的身份认同——"我是这个身体、这个名字、这些念头"。真我（Self）是纯粹的意识本身，是一切众生共享的真相。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="真我">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是"梵"？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：真我</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>梵（Brahman）是宇宙的终极实相，是一切存在的本源。它不同于人格化的神，是究竟的、非二元的、无所不在的存在本身。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="智慧">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ "空"和"有"是什么关系？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：智慧</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>空不是虚无，空是无限的可能性。"有"是空的具体显现。一切法皆从空生起，又回归于空。空是究竟，有是缘起——两者不矛盾。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="解脱">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是"涅槃"？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：解脱</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>涅槃是贪嗔痴的止息，是无明的熄灭。它不是死后才发生的状态，而是当下认识到真理。活着时也可以涅槃——那就是觉悟。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="真我">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 为什么说"一切众生皆有佛性"？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：真我</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>因为真我是普遍的，不属于任何个体。所有众生都拥有同样的意识本质——那就是佛性。花开花落，但大地始终不变。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="智慧">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是"三轮体空"的智慧？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：智慧</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>修行者、所修之法、修行的对象——这三者本性皆空。没有真实的"我在修行"，也没有"我度化了谁"。这种无我的智慧即是般若。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="智慧">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ "无所得"是什么意思？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：智慧</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>真我本自具足，不需要向外追求什么。所有的"得到"都只是幻象，因为那本来就在你之内。放下追求的心，就是无所得。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 什么是"无疑"？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>不是对某个结论的相信，而是亲证后的确信。这种确信不需要理由，因为那是直接体验到的真相。</p>
                            </div>
                        </div>
                    </div>
                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ 最终的教导是什么？</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>"我是谁？"这个问题就够了。一切教法都是指向月亮的手指，不要执着于手指，要看月亮——那就是真我。</p>
                            </div>
                        </div>
                    </div>'''

# 重建文件
# 在 </div> 之前插入新内容
new_lines = []
new_lines.extend(lines[:close_div_line])  # 到 </div> 之前
new_lines.append(new_qa_items)  # 新QA内容
new_lines.append(lines[close_div_line])  # </div>
new_lines.extend(lines[close_div_line+1:])  # 剩余内容

# 写回文件
with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print(f"新文件行数: {len(new_lines)}")

# 验证
with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    final_content = f.read()
    qa_count = final_content.count('class="qa-item"')
    print(f"qa-item 总数: {qa_count}")
    
# 计算页数
pages = (qa_count + 14) // 15
print(f"预计页数: {pages}")
