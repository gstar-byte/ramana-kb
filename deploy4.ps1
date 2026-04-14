$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

# Get full project info
Write-Host "=== Current project config ==="
$p = Invoke-RestMethod -Uri "https://api.vercel.com/v1/projects/site?teamId=team_Y89oibIIusVBBzwRLqZ6b" -Headers $headers -TimeoutSec 10
Write-Host ($p | ConvertTo-Json -Depth 3)

# Try deployment with all fields
Write-Host "`n=== Deploy attempt 1 ==="
$body1 = @{
    name = "site"
    project = "site"
    target = "production"
    gitSource = @{
        type = "github"
        repo = "gstar-byte/ramana-kb"
        ref = "main"
    }
} | ConvertTo-Json -Compress
try {
    $r = Invoke-RestMethod -Uri "https://api.vercel.com/v13/deployments" -Headers $headers -Method POST -Body $body1 -TimeoutSec 20
    Write-Host "OK: $($r.url)"
} catch {
    Write-Host "E1: $($_.Exception.Message)"
}

# Try with teamId in body
Write-Host "`n=== Deploy attempt 2 ==="
$body2 = @{
    name = "site"
    project = "site"
    target = "production"
    teamId = "team_Y89oibIIusVBBzwRLqZRsR6b"
    gitSource = @{
        type = "github"
        repo = "gstar-byte/ramana-kb"
        ref = "main"
    }
} | ConvertTo-Json -Compress
try {
    $r = Invoke-RestMethod -Uri "https://api.vercel.com/v13/deployments" -Headers $headers -Method POST -Body $body2 -TimeoutSec 20
    Write-Host "OK: $($r.url)"
} catch {
    Write-Host "E2: $($_.Exception.Message)"
}
