# 修复竖条问题：在 lang-toggle 前添加分隔线（border-left）
# 查找所有包含 lang-toggle 的 HTML 文件，统一添加 border-left 样式

$base = "F:\26年4月\kb01\pages"

# 简体版 pattern
$simpleOld = '<a href="#" class="lang-toggle" title="切换为繁体中文" onclick="location.href=''/zh-TW/''+location.pathname.substring(1);return false;">繁</a>'
$simpleNew = '<a href="#" class="lang-toggle" style="border-left:1px solid rgba(255,255,255,.3);" title="切换为繁体中文" onclick="location.href=''/zh-TW/''+location.pathname.substring(1);return false;">繁</a>'

# 繁体版 pattern
$tradOld = '<a href="#" class="lang-toggle" title="切换为繁体中文" onclick="location.href=location.pathname.replace(''/zh-TW/'',''/'');return false;">繁</a>'
$tradNew = '<a href="#" class="lang-toggle" style="border-left:1px solid rgba(255,255,255,.3);" title="切换为繁体中文" onclick="location.href=location.pathname.replace(''/zh-TW/'',''/'');return false;">繁</a>'

# 繁体版 pattern (zh-TW/ 目录下)
$tradOld2 = '<a href="#" class="lang-toggle" title="切換爲簡體中文" onclick="location.href=location.pathname.replace(''/zh-TW/'',''/'');return false;">簡</a>'
$tradNew2 = '<a href="#" class="lang-toggle" style="border-left:1px solid rgba(255,255,255,.3);" title="切換爲簡體中文" onclick="location.href=location.pathname.replace(''/zh-TW/'',''/'');return false;">簡</a>'

$count = 0

# 处理简体版文件
Get-ChildItem -Path "$base" -Recurse -Filter "*.html" | Where-Object { $_.FullName -notlike "*\zh-TW\*" } | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    if ($content -match [regex]::Escape($simpleOld)) {
        $newContent = $content -replace [regex]::Escape($simpleOld), $simpleNew
        Set-Content -Path $_.FullName -Value $newContent -NoNewline
        Write-Host "[简体] $($_.Name)" -ForegroundColor Cyan
        $count++
    }
}

# 处理繁体版文件
Get-ChildItem -Path "$base\zh-TW" -Recurse -Filter "*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $changed = $false
    if ($content -match [regex]::Escape($tradOld)) {
        $content = $content -replace [regex]::Escape($tradOld), $tradNew
        $changed = $true
    }
    if ($content -match [regex]::Escape($tradOld2)) {
        $content = $content -replace [regex]::Escape($tradOld2), $tradNew2
        $changed = $true
    }
    if ($changed) {
        Set-Content -Path $_.FullName -Value $content -NoNewline
        Write-Host "[繁体] $($_.Name)" -ForegroundColor Magenta
        $count++
    }
}

Write-Host "`n总计修复 $count 个文件" -ForegroundColor Green
