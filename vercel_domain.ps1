$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{"Authorization" = "Bearer $token"; "Content-Type" = "application/json"}

# Try without team ID
Write-Output "=== Without teamId ==="
try {
    $r = Invoke-WebRequest -Uri "https://api.vercel.com/v6/domains" -Headers $headers -TimeoutSec 20
    Write-Output "Status: $($r.StatusCode) - $($r.Content)"
} catch {
    $stream = $_.Exception.Response.GetResponseStream()
    $body = [System.IO.StreamReader]::new($stream).ReadToEnd()
    Write-Output "Error Status: $($_.Exception.Response.StatusCode)"
    Write-Output "Body: $body"
}

# Try project-level domain add
Write-Output "`n=== Project level domain add ==="
$body = '{"domain":"RamanaMaharshi.space","gitBranch":"main"}'
try {
    $r2 = Invoke-WebRequest -Uri "https://api.vercel.com/v6/projects/prj_dbxbNxHth2CsZyOk9iHRUmVwMJpu/domains?teamId=team_Y89oibIIusVBBzwRLqZRsR6b" -Headers $headers -Method POST -Body $body -TimeoutSec 20
    Write-Output "Status: $($r2.StatusCode) - $($r2.Content)"
} catch {
    $stream = $_.Exception.Response.GetResponseStream()
    $body = [System.IO.StreamReader]::new($stream).ReadToEnd()
    Write-Output "Error Status: $($_.Exception.Response.StatusCode)"
    Write-Output "Body: $body"
}
