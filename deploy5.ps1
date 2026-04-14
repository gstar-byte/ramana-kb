$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

# Deploy using projectId
Write-Host "=== Deploy with projectId ==="
$body = @{
    name       = "site"
    projectId  = "prj_sDZNG0DN2KmbTlQmvcW99THpFlf6"
    target     = "production"
    gitSource  = @{
        type = "github"
        repo = "gstar-byte/ramana-kb"
        ref  = "main"
    }
} | ConvertTo-Json -Compress

try {
    $r = Invoke-RestMethod -Uri "https://api.vercel.com/v13/deployments" -Headers $headers -Method POST -Body $body -TimeoutSec 20
    Write-Host "Deployment: $($r.url)"
    Write-Host "State: $($r.readyState)"
} catch {
    Write-Host "Error: $($_.Exception.Message)"
    try {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        Write-Host "Body: $($reader.ReadToEnd())"
    } catch {}
}

# Check domain status
Write-Host "`n=== Domain RamanaMaharshi.space ==="
try {
    $dom = Invoke-RestMethod -Uri "https://api.vercel.com/v4/domains/ramanamaharshi.space" -Headers $headers -TimeoutSec 10
    Write-Host "Name:       $($dom.name)"
    Write-Host "Verified:   $($dom.verified)"
    Write-Host "Zone:       $($dom.zone)"
    Write-Host "NS:         $($dom.nameservers -join ', ')"
    Write-Host "ConfigVer:  $($dom.configVerifiedAt)"
    Write-Host "NS Verified: $($dom.nsVerifiedAt)"
    Write-Host "TXT Verified: $($dom.txtVerifiedAt)"
    Write-Host "Verification record: $($dom.verificationRecord)"
} catch {
    Write-Host "Domain error: $($_.Exception.Message)"
}
