$ErrorActionPreference = "Stop"

# Skriptverzeichnis → Projekt-Root → Zielverzeichnis
$ScriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $ScriptDir "..\..")
$TargetDir   = Join-Path $ProjectRoot "_internal"

# GitHub-URL
$RepoUrl     = "https://github.com/BYTE-RANGER-Software/_internal-indy-foy.git"
$Branch      = "main"

# Klonen
Write-Host "Cloning into: $TargetDir"
git clone --branch $Branch $RepoUrl $TargetDir

if ($LASTEXITCODE -ne 0) {
    throw "Git clone failed with exit code $LASTEXITCODE"
} else {
    Write-Host "Clone successful!"
}

