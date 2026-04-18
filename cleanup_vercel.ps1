$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

$CUTOFF_HOURS = 48
$PROJECT_ID = "prj_sDZNG0DN2KmbTlQmvcW99THpFlf6"
$TEAM_ID = "team_Y89oibIIusVBBzwRLqZRsR6b"

# Step 1: Get all deployments
Write-Host "=== 获取所有部署... ==="
try {
    $deployments = Invoke-RestMethod `
        -Uri "https://api.vercel.com/v6/deployments?projectId=$PROJECT_ID&teamId=$TEAM_ID" `
        -Headers $headers -Method GET -TimeoutSec 30
} catch {
    Write-Host "获取部署失败: $($_.Exception.Message)"
    try {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        Write-Host "响应内容: $($reader.ReadToEnd())"
    } catch {}
    exit 1
}

$allDeploys = $deployments.deployments
Write-Host "找到 $($allDeploys.Count) 个部署"

# Step 2: Filter old deployments (older than 48h)
$cutoff = [DateTime]::UtcNow.AddHours(-$CUTOFF_HOURS)
$oldDeploys = @()
$keptDeploys = @()

foreach ($d in $allDeploys) {
    $createdAt = [DateTimeOffset]::FromUnixTimeMilliseconds($d.created).UtcDateTime
    if ($createdAt -lt $cutoff) {
        $oldDeploys += $d
    } else {
        $keptDeploys += $d
    }
}

Write-Host "`n=== 分析结果 ==="
Write-Host "- 总部署数: $($allDeploys.Count)"
Write-Host "- $CUTOFF_HOURS 小时内的部署: $($keptDeploys.Count)"
Write-Host "- 超过 $CUTOFF_HOURS 小时的部署: $($oldDeploys.Count)"

if ($oldDeploys.Count -eq 0) {
    Write-Host "`n没有需要清理的旧部署！"
    exit 0
}

Write-Host "`n=== 即将删除以下 $($oldDeploys.Count) 个部署 ==="
foreach ($d in $oldDeploys) {
    $createdAt = [DateTimeOffset]::FromUnixTimeMilliseconds($d.created).LocalDateTime
    Write-Host "  - $($d.url) (创建于: $($createdAt.ToString('yyyy-MM-dd HH:mm')), 目标: $($d.target))"
}

# Step 3: Delete old deployments
Write-Host "`n=== 开始删除 $($oldDeploys.Count) 个部署 ==="
$deleted = 0
$failed = 0

foreach ($d in $oldDeploys) {
    try {
        Invoke-RestMethod `
            -Uri "https://api.vercel.com/v13/deployments/$($d.uid)?teamId=$TEAM_ID" `
            -Headers $headers -Method DELETE -TimeoutSec 15 | Out-Null
        Write-Host "  ✓ 删除成功: $($d.url)"
        $deleted++
    } catch {
        Write-Host "  ✗ 删除失败: $($d.url) - $($_.Exception.Message.Substring(0, [Math]::Min(80, $_.Exception.Message.Length)))"
        $failed++
    }
    Start-Sleep -Milliseconds 500
}

Write-Host "`n=== 完成！共删除 $deleted 个部署, 失败 $failed 个 ==="
