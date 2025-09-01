# Generate SHA-256 checksums for all files in originals/ (recursive)
# Excludes: originals\not public\**
# Output is saved to originals\CHECKSUMS.txt (relative Unix-style paths)

# Find repo root by walking up until a marker is found
$dir = Get-Item -LiteralPath $PSScriptRoot
$markers = @('.git','originals')

while ($dir -and $dir.PSIsContainer) {
    if ($markers | ForEach-Object { Test-Path (Join-Path $dir.FullName $_) } | Where-Object { $_ }) {
        break
    }
    $dir = $dir.Parent
}

if (-not $dir) { throw "Repo root not found." }

Push-Location $dir.FullName

$Output = "originals\CHECKSUMS.txt"
$Root   = Join-Path (Get-Location) "originals"
$Header = "# SHA-256 checksums for originals/ (generated on $(Get-Date -Format 'yyyy-MM-dd'))"

$lines = @()
$lines += $Header
$lines += ""

# Collect files recursively, exclude 'originals\not public\**' and control files at root
$files = Get-ChildItem -Path $Root -File -Recurse |
    Where-Object {
        # Exclude anything under originals\not public\
        $_.FullName -notmatch [Regex]::Escape("\originals\not public\")
    } |
    Where-Object {
        # Exclude control files at originals root
        $rel = $_.FullName.Substring($Root.Length + 1)
        $rel -ne "CHECKSUMS.txt" -and $rel -ne "SOURCES.md" -and $rel -ne "sources_meta.json"
    } |
    Sort-Object FullName

foreach ($f in $files) {
    $hash = Get-FileHash $f.FullName -Algorithm SHA256
    # relative path with forward slashes
    $rel = $f.FullName.Substring($Root.Length + 1) -replace "\\","/"
    $lines += ("{0}  {1}" -f $hash.Hash.ToUpper(), $rel)
}

$lines | Out-File $Output -Encoding utf8
Write-Host "Checksums written to $Output"

Pop-Location
