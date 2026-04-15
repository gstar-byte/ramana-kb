# -*- coding: utf-8 -*-
"""提取《回到你心中》PDF内容"""
import pdfplumber
import sys

pdf_path = r"c:/Users/willp/WorkBuddy/20260410104230/回到你心中.pdf"
output_path = r"c:/Users/willp/WorkBuddy/20260410104230/pdf_content"

def extract_pdf_content(pdf_path, output_dir, max_pages=None):
    """提取PDF内容"""
    print(f"正在打开: {pdf_path}")
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"总页数: {total_pages}")
        
        if max_pages:
            total_pages = min(total_pages, max_pages)
        
        all_text = []
        
        for i in range(total_pages):
            print(f"正在处理第 {i+1}/{total_pages} 页...", end="\r")
            page = pdf.pages[i]
            text = page.extract_text()
            if text:
                all_text.append(f"=== 第 {i+1} 页 ===\n{text}\n")
        
        print(f"\n提取完成! 共 {len(all_text)} 页有内容")
        
        # 保存完整文本
        full_text = "\n\n".join(all_text)
        with open(f"{output_dir}/full_text.txt", "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"完整文本已保存到: {output_dir}/full_text.txt")
        
        # 保存摘要（前20页的主要内容）
        summary = "\n\n".join(all_text[:20])
        with open(f"{output_dir}/summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"摘要已保存到: {output_dir}/summary.txt")
        
        return all_text

if __name__ == "__main__":
    max_pages = int(sys.argv[1]) if len(sys.argv) > 1 else None
    extract_pdf_content(pdf_path, output_path, max_pages)
