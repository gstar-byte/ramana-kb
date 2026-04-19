# 从 pages/ 目录部署到 Vercel（使用原有项目 20260410104230）
# 交互式：首次需要选择/链接项目
Set-Location "c:\Users\willp\WorkBuddy\20260410104230\pages"
Write-Host "当前目录: $(Get-Location)"
Write-Host "开始部署..."
vercel --prod --yes
