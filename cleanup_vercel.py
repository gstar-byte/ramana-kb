#!/usr/bin/env python3
import urllib.request
import urllib.error
import json
from datetime import datetime, timedelta
import time

VERCEL_TOKEN = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
TEAM_ID = "team_Y89oibIIusVBBzwRLqZRsR6b"
PROJECT_NAME = "site"
CUTOFF_HOURS = 48


def make_request(url, method="GET", data=None):
    headers = {
        "Authorization": f"Bearer {VERCEL_TOKEN}",
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(url, headers=headers, method=method)
    if data:
        req.data = json.dumps(data).encode("utf-8")
    
    try:
        with urllib.request.urlopen(req) as response:
            return response.read().decode("utf-8"), response.status
    except urllib.error.HTTPError as e:
        return e.read().decode("utf-8"), e.code


def main():
    # Step 0: Get project info with team ID
    print(f"=== 正在获取项目 {PROJECT_NAME} 的信息 (团队: {TEAM_ID})... ===")
    projects_url = f"https://api.vercel.com/v9/projects/{PROJECT_NAME}?teamId={TEAM_ID}"
    response_body, status_code = make_request(projects_url)

    if status_code != 200:
        print(f"获取项目失败: {status_code}")
        print(response_body)
        return

    project_data = json.loads(response_body)
    project_id = project_data["id"]
    print(f"找到项目: {PROJECT_NAME}, ID: {project_id}\n")

    # Step 1: Get all deployments with team ID
    print(f"=== 正在获取 {PROJECT_NAME} 的所有部署... ===")
    url = f"https://api.vercel.com/v6/deployments?projectId={project_id}&teamId={TEAM_ID}"
    response_body, status_code = make_request(url)

    if status_code != 200:
        print(f"获取部署失败: {status_code}")
        print(response_body)
        return

    data = json.loads(response_body)
    deployments = data.get("deployments", [])

    if not deployments:
        print("没有找到部署！")
        return

    print(f"找到 {len(deployments)} 个部署\n")

    # Step 2: Filter old deployments (older than 48h)
    cutoff = datetime.now() - timedelta(hours=CUTOFF_HOURS)
    old_deployments = []
    kept_deployments = []

    for d in deployments:
        created_at = datetime.fromtimestamp(d["created"] / 1000)
        is_old = created_at < cutoff

        if is_old:
            old_deployments.append(d)
        else:
            kept_deployments.append(d)

    print(f"=== 分析结果 ===")
    print(f"- 总部署数: {len(deployments)}")
    print(f"- 48小时内的部署数: {len(kept_deployments)}")
    print(f"- 超过48小时的部署数: {len(old_deployments)}")

    if not old_deployments:
        print("\n没有需要清理的旧部署！")
        return

    print(f"\n=== 即将删除以下 {len(old_deployments)} 个部署 ===\n")
    for d in old_deployments:
        created_at = datetime.fromtimestamp(d["created"] / 1000)
        print(f"  - {d['url']} (创建于: {created_at.strftime('%Y-%m-%d %H:%M')}, 目标: {d.get('target', 'preview')})")

    # Step 3: Auto delete without confirmation
    print(f"\n自动删除 {len(old_deployments)} 个部署...")

    print(f"\n=== 开始删除 {len(old_deployments)} 个部署 ===")
    deleted = 0
    for d in old_deployments:
        del_url = f"https://api.vercel.com/v13/deployments/{d['uid']}?teamId={TEAM_ID}"
        try:
            response_body, status_code = make_request(del_url, method="DELETE")
            if status_code in [200, 204]:
                print(f"  ✓ 删除成功: {d['url']}")
                deleted += 1
            else:
                print(f"  ✗ 删除失败: {d['url']} - {status_code}")
                print(response_body)
            # 避免 API 限流
            time.sleep(0.5)
        except Exception as e:
            print(f"  ✗ 删除出错: {d['url']} - {str(e)}")

    print(f"\n=== 完成！共删除了 {deleted} 个部署 ===")


if __name__ == "__main__":
    main()
