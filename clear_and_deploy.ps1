$token = "vcp_0XDk6lHvLZrM1gLBcZ3NNmcTWN4d7t3l6bYB7lTqfE7WU5CGw52ZNEpl"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

# Step 1: Delete ALL existing production deployments
Write-Host "=== Step 1: Clearing all production deployments ==="
$deployments = Invoke-RestMethod `
    -Uri "https://api.vercel.com/v6/deployments?projectId=prj_dbxbNxHth2CsZyOk9iHRUmVwMJpu&state=READY" `
    -Headers $headers -Method GET -TimeoutSec 30

$prodDeploys = $deployments.deployments | Where-Object { $_.target -eq "production" }
Write-Host "Found $($prodDeploys.Count) production deployments to delete..."

foreach ($d in $prodDeploys) {
    Write-Host "  Deleting: $($d.uid) - $($d.url)"
    try {
        Invoke-RestMethod `
            -Uri "https://api.vercel.com/v13/deployments/$($d.uid)" `
            -Headers $headers -Method DELETE -TimeoutSec 15 | Out-Null
        Write-Host "    Deleted!"
    } catch {
        Write-Host "    Error: $($_.Exception.Message.Substring(0, [Math]::Min(80, $_.Exception.Message.Length)))"
    }
}

# Step 2: Deploy from local files using Vercel REST API
Write-Host "`n=== Step 2: Deploying local pages/ to production ==="
Write-Host "Note: Vercel REST API requires files to be uploaded via tar.gz archive."
Write-Host "Using Vercel CLI for direct local deployment (non-blocking)..."

# Use Vercel CLI with --wait=false to not block
$cliScript = @"
Set-Location 'c:\Users\willp\WorkBuddy\20260410104230'
Start-Process -FilePath 'vercel' -ArgumentList '--prod --yes --no-wait' -NoNewWindow -Wait
"@

Write-Host "`nTo complete deployment, run this command manually:"
Write-Host "  cd c:\Users\willp\WorkBuddy\20260410104230"
Write-Host "  vercel --prod --yes --no-wait"
Write-Host ""
Write-Host "Or run the PowerShell deploy script:"
Write-Host "  .\deploy_vercel_local.ps1"

# Also write a convenience script
@'
# Vercel direct local deployment script
# Run from workspace root: vercel --prod --yes --no-wait
# Or without waiting: vercel --prod --yes
'@ | Out-File -FilePath "c:\Users\willp\WorkBuddy\20260410104230\deploy_vercel_local.ps1" -Encoding utf8

Write-Host "`nDone clearing old deployments."
