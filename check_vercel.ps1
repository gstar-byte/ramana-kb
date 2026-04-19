$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

Write-Host "=== Getting project by ID ==="
try {
    $r = Invoke-RestMethod -Uri "https://api.vercel.com/v2/projects/prj_dbxbNxHth2CsZyOk9iHRUmVwMJpu" -Headers $headers -Method GET -TimeoutSec 20
    Write-Host "Project Name: $($r.name)"
    Write-Host "Framework: $($r.framework)"
    Write-Host "Root Directory: $($r.rootDirectory)"
    Write-Host "Git Source: $($r.link | ConvertTo-Json -Depth 2)"
} catch {
    $_.Exception.Message
    $body = try { $_.Exception.Response.GetResponseStream().ReaderToEnd() } catch { "" }
    Write-Host "Response: $body"
}
