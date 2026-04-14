$ErrorActionPreference = "Continue"
$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$uri = "https://api.vercel.com/v1/user"
try {
    $r = Invoke-WebRequest -Uri $uri -Headers @{"Authorization"="Bearer $token"} -TimeoutSec 20
    Write-Host "SUCCESS: $($r.Content)"
} catch {
    Write-Host "FAILED: $($_.Exception.Message)"
}
