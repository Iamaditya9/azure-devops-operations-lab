$required = @(
    "APP_ENV",
    "AZURE_SUBSCRIPTION_ID",
    "AZURE_RESOURCE_GROUP"
)

$missing = @()

foreach ($name in $required) {
    $value = (Get-Item "Env:$name" -ErrorAction SilentlyContinue).Value
    if ([string]::IsNullOrWhiteSpace($value)) {
        $missing += $name
    }
}

if ($missing.Count -gt 0) {
    Write-Host "Missing configuration:"
    $missing | ForEach-Object { Write-Host "- $_" }
    exit 1
}

Write-Host "Environment configuration is valid."
