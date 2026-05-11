#!/usr/bin/env python3
"""
清理 Vercel 项目 24 小时前的旧部署（只保留24小时内的所有部署）
"""
import requests
import json
from datetime import datetime, timedelta
import sys

# 配置
TOKEN = "vcp_1fvNg5Tj42DrucdOieUIZSr7vFCLVrvseHpqRF05ZeYnZ2gLOj4DUj8g"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_projects():
    """获取所有项目"""
    url = "https://api.vercel.com/v9/projects"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("projects", [])
    else:
        print(f"获取项目列表失败: {response.status_code}")
        print(response.text)
        return []

def get_deployments(project_id):
    """获取项目的所有部署"""
    url = f"https://api.vercel.com/v6/deployments?projectId={project_id}&limit=100"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("deployments", [])
    else:
        print(f"获取部署列表失败: {response.status_code}")
        print(response.text)
        return []

def delete_deployment(deployment_id):
    """删除指定部署"""
    url = f"https://api.vercel.com/v13/deployments/{deployment_id}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code in [200, 204]:
        print(f"  ✓ 已删除: {deployment_id}")
        return True
    else:
        print(f"  ✗ 删除失败 {deployment_id}: {response.status_code}")
        return False

def main():
    print("正在获取项目列表...")
    projects = get_projects()

    if not projects:
        print("没有找到项目")
        return

    print(f"\n找到 {len(projects)} 个项目:")
    for p in projects:
        print(f"  - {p.get('name')} (ID: {p.get('id')})")

    # 查找 ramana-kb 项目
    target_project = None
    for p in projects:
        if p.get('name') == 'ramana-kb' or 'ramana' in p.get('name', '').lower():
            target_project = p
            break

    if not target_project:
        print("\n未找到 ramana-kb 项目，使用第一个项目")
        target_project = projects[0]

    project_id = target_project.get('id')
    project_name = target_project.get('name')
    print(f"\n使用项目: {project_name} (ID: {project_id})")

    print("\n正在获取部署列表...")
    deployments = get_deployments(project_id)

    if not deployments:
        print("没有部署或获取失败")
        return

    print(f"共找到 {len(deployments)} 个部署")

    # 计算 24 小时前的时间
    cutoff_time = datetime.utcnow() - timedelta(hours=24)
    print(f"清理 24 小时前的部署 (截止: {cutoff_time.isoformat()})")

    deleted_count = 0
    skipped_count = 0

    for dep in deployments:
        dep_id = dep.get("uid")
        dep_url = dep.get("url", "")
        created_at = dep.get("created")
        state = dep.get("state")
        is_prod = dep.get("target") == "production"

        # 解析创建时间 (Vercel返回的是Unix时间戳毫秒)
        try:
            if isinstance(created_at, (int, float)) or (isinstance(created_at, str) and created_at.isdigit()):
                # Unix时间戳（毫秒）
                timestamp_ms = int(created_at)
                created_time = datetime.fromtimestamp(timestamp_ms / 1000)
            else:
                # ISO格式字符串
                created_time_str = created_at.replace("Z", "+00:00")
                created_time = datetime.fromisoformat(created_time_str.replace("+00:00", ""))
        except Exception as e:
            print(f"  时间解析错误: {e}, 使用当前时间")
            created_time = datetime.utcnow()

        # 判断是否超过 24 小时
        is_old = created_time < cutoff_time

        print(f"\n部署: {dep_url}")
        print(f"  ID: {dep_id}")
        print(f"  创建时间: {created_at}")
        print(f"  状态: {state}")
        print(f"  生产环境: {is_prod}")

        # 只保留24小时内的部署
        if not is_old:
            print(f"  → 跳过 (24小时内)")
            skipped_count += 1
            continue

        # 删除24小时前的部署（包括生产部署）
        if delete_deployment(dep_id):
            deleted_count += 1

    print(f"\n{'='*50}")
    print(f"清理完成!")
    print(f"删除: {deleted_count} 个部署")
    print(f"跳过: {skipped_count} 个部署")

if __name__ == "__main__":
    main()
