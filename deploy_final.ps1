$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

# Step 1: Create a deploy hook for main branch
Write-Host "=== Create deploy hook ==="
$hookBody = @{
    name = "Deploy from main branch"
    ref  = "main"
} | ConvertTo-Json -Compress

try {
    $h = Invoke-RestMethod -Uri "https://api.vercel.com/v1/projects/prj_sDZNG0DN2KmbTlQmvcW99THpFlf6/hooks" -Headers $headers -Method POST -Body $hookBody -TimeoutSec 15
    Write-Host "Hook URL: $($h.url)"
    $hookUrl = $h.url
} catch {
    Write-Host "Hook error: $($_.Exception.Message)"
    try {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        Write-Host "Body: $($reader.ReadToEnd())"
    } catch {}
    $hookUrl = $null
}

# Step 2: Trigger via deploy hook
if ($hookUrl) {
    Write-Host "`n=== Trigger via hook ==="
    try {
        $r = Invoke-WebRequest -Uri $hookUrl -Method POST -TimeoutSec 15
        Write-Host "Status: $($r.StatusCode)"
        Write-Host "Response: $($r.Content)"
    } catch {
        Write-Host "Hook trigger error: $($_.Exception.Message)"
    }
}

# Step 3: Check domain
Write-Host "`n=== Domain RamanaMaharshi.space ==="
try {
    $dom = Invoke-RestMethod -Uri "https://api.vercel.com/v4/domains/ramanamaharshi.space" -Headers $headers -TimeoutSec 10
    Write-Host "Name:        $($dom.name)"
    Write-Host "Verified:    $($dom.verified)"
    Write-Host "NS Verified: $($dom.nsVerifiedAt)"
    Write-Host "TXT Verified:$($dom.txtVerifiedAt)"
    Write-Host "NS records:  $($dom.nameservers -join ', ')"
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}
