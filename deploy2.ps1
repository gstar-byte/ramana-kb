$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

# Get project details
Write-Host "=== Project: site ==="
try {
    $p = Invoke-RestMethod -Uri "https://api.vercel.com/v1/projects/site?teamId=team_Y89oibIIusVBBzwRLqZRsR6b" -Headers $headers -TimeoutSec 10
    Write-Host "Project name: $($p.name)"
    Write-Host "RootDir: $($p.rootDirectory)"
    Write-Host "Framework: $($p.framework)"
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}

# Trigger deployment via v13
Write-Host "`n=== Triggering deployment ==="
$deployBody = @{
    project = "site"
    target  = "production"
} | ConvertTo-Json -Compress

try {
    $r = Invoke-RestMethod -Uri "https://api.vercel.com/v13/deployments" -Headers $headers -Method POST -Body $deployBody -TimeoutSec 20
    Write-Host "Deployment: $($r.url)"
    Write-Host "ID: $($r.id)"
} catch {
    Write-Host "Error: $($_.Exception.Message)"
    try {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        $body = $reader.ReadToEnd()
        Write-Host "Body: $body"
    } catch {}
}
