$ErrorActionPreference = "Stop"
$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{"Authorization" = "Bearer $token"}
try {
    $r = Invoke-WebRequest -Uri "https://api.vercel.com/v1/user" -Headers $headers -TimeoutSec 15
    Write-Host $r.Content
} catch {
    Write-Host "ERROR: $($_.Exception.Message)"
}
