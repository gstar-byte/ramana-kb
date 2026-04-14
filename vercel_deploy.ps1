$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$teamId = "team_Y89oibIIusVBBzwRLqZRsR6b"
$projectId = "prj_dbxbNxHth2CsZyOk9iHRUmVwMJpu"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type" = "application/json"
}

# Create deployment with GitHub source
$body = @{
    name = "ramana-kb"
    gitSource = @{
        type = "github"
        org = "gstar-byte"
        repo = "ramana-kb"
        ref = "main"
    }
    project = $projectId
    target = "production"
} | ConvertTo-Json -Depth 5

$deployUrl = "https://api.vercel.com/v13/deployments?teamId=$teamId"
Write-Output "Creating deployment..."
$deploy = Invoke-RestMethod -Uri $deployUrl -Headers $headers -Method POST -Body $body -TimeoutSec 30
$deploy | ConvertTo-Json -Depth 5
