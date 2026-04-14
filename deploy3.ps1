$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

# Update project to static/other framework
Write-Host "=== Updating project config ==="
$updateBody = @{
    framework  = $null
    buildCommand = $null
    outputDirectory = "pages"
    rootDirectory = "pages"
} | ConvertTo-Json -Compress

try {
    $r = Invoke-RestMethod -Uri "https://api.vercel.com/v1/projects/site?teamId=team_Y89oibIIusVBBzwRLqZRsR6b" -Headers $headers -Method PATCH -Body $updateBody -TimeoutSec 15
    Write-Host "Updated! RootDir: $($r.rootDirectory)"
} catch {
    Write-Host "Update error: $($_.Exception.Message)"
}

# Trigger deployment
Write-Host "`n=== Triggering deployment ==="
$deployBody = @{
    project = "site"
    target  = "production"
    gitSource = @{
        type = "github"
        repo = "gstar-byte/ramana-kb"
        ref  = "main"
    }
} | ConvertTo-Json -Compress

try {
    $d = Invoke-RestMethod -Uri "https://api.vercel.com/v13/deployments" -Headers $headers -Method POST -Body $deployBody -TimeoutSec 20
    Write-Host "Deployment created! URL: $($d.url)"
    Write-Host "Status: $($d.readyState)"
} catch {
    Write-Host "Deploy error: $($_.Exception.Message)"
    try {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        $body = $reader.ReadToEnd()
        Write-Host "Body: $body"
    } catch {}
}

# Check domain
Write-Host "`n=== Domain status ==="
try {
    $dom = Invoke-RestMethod -Uri "https://api.vercel.com/v4/domains/ramanamaharshi.space" -Headers $headers -TimeoutSec 10
    Write-Host "Domain: $($dom.name)"
    Write-Host "Verified: $($dom.verified)"
    Write-Host "Zone: $($dom.zone)"
} catch {
    Write-Host "Domain error: $($_.Exception.Message)"
}
