#!/usr/bin/env python3
"""
修复 graph.html 的三个问题：
1. 移动端3D图触摸点击无反应（被D3 drag拦截）
2. PC端鼠标在节点上快速抖动（simulation稳定参数不够激进）
3. 手机浏览器打不开侧边栏（touch-action被浏览器拦截）
"""

import re

def fix_graph_html():
    with open('pages/graph.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # ========== 修复1: 移动端触摸事件 ==========
    # 问题：D3 drag 会拦截 touchstart，导致自定义 touch 事件无法工作
    # 解决：在 touchstart 事件中立即停止传播，防止 D3 拦截

    # 找到并修复 touchstart 事件处理
    old_touchstart = '''.on("touchstart", function(event, d) {
            event.preventDefault();
            const self = this;'''

    new_touchstart = '''.on("touchstart", function(event, d) {
            // 关键修复：立即停止传播，防止 D3 drag 拦截触摸事件
            event.stopPropagation();
            event.preventDefault();
            const self = this;'''

    content = content.replace(old_touchstart, new_touchstart)

    # 修复 touchmove 事件：也停止传播
    old_touchmove = '''.on("touchmove", function(event, d) {
            // 手指移动则取消所有待定操作'''

    new_touchmove = '''.on("touchmove", function(event, d) {
            // 手指移动也停止传播，确保触摸交互正确
            event.stopPropagation();
            // 手指移动则取消所有待定操作'''

    content = content.replace(old_touchmove, new_touchmove)

    # 修复 touchend 事件：也停止传播
    old_touchend = '''.on("touchend", function(event, d) {
            const self = this;'''

    new_touchend = '''.on("touchend", function(event, d) {
            // 停止传播，确保触摸结束事件正确处理
            event.stopPropagation();
            const self = this;'''

    content = content.replace(old_touchend, new_touchend)

    # ========== 修复2: PC端鼠标抖动 ==========
    # 问题：simulation 的 alphaDecay(0.1) 不够激进，节点仍有微小抖动
    # 解决：使用更激进的参数让节点快速稳定

    old_stabilize = '''// 第3秒后强制停止大幅跳动：把 alpha 压低，让节点基本稳定
        setTimeout(() => {
            // 把当前位置全部固定，等一帧后再松开 → 节点从此只有极小的热运动
            nodes.forEach(d => { d.fx = d.x; d.fy = d.y; });
            simulation.alpha(0.05).alphaTarget(0).alphaDecay(0.1).restart();
            // 短暂延迟后解除固定，允许拖拽仍然有效
            setTimeout(() => {
                nodes.forEach(d => { d.fx = null; d.fy = null; });
            }, 300);
        }, 3000);'''

    new_stabilize = '''// 第3秒后强制停止节点抖动
        setTimeout(() => {
            // 方案1：完全停止 simulation，让节点固定在当前位置
            simulation.stop();

            // 方案2：同时固定所有节点位置，防止任何后续运动
            nodes.forEach(d => {
                d.fx = d.x;
                d.fy = d.y;
                d.vx = 0;  // 清除速度
                d.vy = 0;
            });

            // 500ms 后允许拖拽（松开固定），但 simulation 已停止，节点不会抖动
            setTimeout(() => {
                nodes.forEach(d => {
                    d.fx = null;
                    d.fy = null;
                    // vx/vy 保持为 0，确保节点不动
                });
            }, 500);
        }, 3000);'''

    content = content.replace(old_stabilize, new_stabilize)

    # ========== 修复3: 移动端汉堡菜单 ==========
    # 在 graph.html 的 <style> 中添加移动端触摸优化

    # 找到移动端样式部分并添加 touch-action
    old_mobile_style = '''/* 移动端适配 */
        @media (max-width: 767px) {
            .graph-wrapper {
                min-height: 350px;
                height: 350px;
                margin: 0 -4px;
            }
            #graph-svg {
                height: 350px;
            }
            .concept-categories {
                grid-template-columns: 1fr !important;
            }
            .graph-controls {
                top: 0.3rem;
                right: 0.3rem;
            }
            .graph-controls button {
                padding: 0.25rem 0.5rem;
                font-size: 0.7rem;
            }
        }'''

    new_mobile_style = '''/* 移动端适配 */
        @media (max-width: 767px) {
            .graph-wrapper {
                min-height: 350px;
                height: 350px;
                margin: 0 -4px;
            }
            #graph-svg {
                height: 350px;
            }
            .concept-categories {
                grid-template-columns: 1fr !important;
            }
            .graph-controls {
                top: 0.3rem;
                right: 0.3rem;
            }
            .graph-controls button {
                padding: 0.25rem 0.5rem;
                font-size: 0.7rem;
            }
            /* 修复移动端汉堡菜单触摸 */
            .hamburger {
                touch-action: manipulation;
                -webkit-tap-highlight-color: transparent;
                /* 确保 z-index 足够高 */
                z-index: 1001 !important;
            }
            /* 修复侧边栏触摸 */
            .sidebar {
                touch-action: pan-y; /* 允许垂直滚动，禁用水平手势 */
                overscroll-behavior: contain;
            }
        }'''

    content = content.replace(old_mobile_style, new_mobile_style)

    # 在全局样式中添加 SVG 触摸支持
    old_svg_style = '''#graph-svg {
            width: 100%;
            height: 650px;
        }'''

    new_svg_style = '''#graph-svg {
            width: 100%;
            height: 650px;
            /* 修复移动端触摸问题：允许触摸事件穿透到节点 */
            touch-action: none;
        }'''

    content = content.replace(old_svg_style, new_svg_style)

    # 同时修改 drag 配置，在移动端禁用双击缩放等默认行为
    old_drag = '''.call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended));'''

    new_drag = '''.call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended)
                // 禁用移动端的拖拽（触摸交互由自定义 touch 事件处理）
                .filter(function(event) {
                    // 在触摸设备上禁用拖拽，让节点可点击
                    return !event.sourceEvent ||
                           event.sourceEvent.type !== 'touchstart';
                })
            );'''

    content = content.replace(old_drag, new_drag)

    # ========== 保存修复后的文件 ==========
    with open('pages/graph.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ graph.html 修复完成！")

    # 验证修复
    with open('pages/graph.html', 'r', encoding='utf-8') as f:
        verified = f.read()

    checks = [
        ('event.stopPropagation()' in verified, 'touchstart 事件停止传播'),
        ('simulation.stop()' in verified, 'simulation 停止调用'),
        ('touch-action: none' in verified, 'SVG 触摸配置'),
        ('touch-action: manipulation' in verified, '汉堡菜单触摸配置'),
    ]

    print("\n📋 修复验证：")
    for passed, desc in checks:
        status = '✅' if passed else '❌'
        print(f"  {status} {desc}")

if __name__ == '__main__':
    fix_graph_html()
