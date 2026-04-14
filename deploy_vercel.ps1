$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

# Step 1: Trigger deployment via v13 API
Write-Host "=== Triggering deployment ==="
$deployBody = @{
    gitSource = @{
        type = "github"
        repo = "gstar-byte/ramana-kb"
        ref  = "main"
    }
    project      = "ramana-kb"
    target       = "production"
    name         = "ramana-kb"
    rootDirectory = "pages"
} | ConvertTo-Json -Compress

try {
    $r = Invoke-RestMethod -Uri "https://api.vercel.com/v13/deployments" -Headers $headers -Method POST -Body $deployBody -TimeoutSec 20
    Write-Host "Deployment created! URL: $($r.url)"
    Write-Host "ID: $($r.id)"
} catch {
    Write-Host "Deploy error: $($_.Exception.Message)"
    $body = try { $_.Exception.Response.GetResponseStream().ReaderToEnd(); } catch { "" }
    Write-Host "Response body: $body"
}

# Step 2: Add domain
Write-Host "`n=== Adding domain ==="
$domainBody = @{
    name = "RamanaMaharshi.space"
} | ConvertTo-Json -Compress

try {
    $d = Invoke-RestMethod -Uri "https://api.vercel.com/v4/domains" -Headers $headers -Method POST -Body $domainBody -TimeoutSec 20
    Write-Host "Domain added: $($d.name)"
    Write-Host "Verification: $($d | ConvertTo-Json -Depth 3)"
} catch {
    Write-Host "Domain error: $($_.Exception.Message)"
    $body = try { $_.Exception.Response.GetResponseStream().ReaderToEnd(); } catch { "" }
    Write-Host "Response body: $body"
}
