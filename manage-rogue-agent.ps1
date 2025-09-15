# Rogue Agent Management Script
# Run this script to manage your global Rogue Agent installation

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("install", "update", "status", "remove")]
    [string]$Action = "status"
)

$RogueAgentBase = "$env:APPDATA\Code\User\rogue-agent"
$ChatModeLocations = @(
    "$env:APPDATA\Code\User\chatmodes",
    "$env:APPDATA\Code\User\.github\chatmodes"
)
$ChatModeFile = "Rogue Agent.chatmode.md"

function Show-Status {
    Write-Host "=== ROGUE AGENT STATUS ===" -ForegroundColor Green
    Write-Host ""
    
    # Check knowledge base
    Write-Host "Knowledge Base:" -ForegroundColor Yellow
    if (Test-Path "$RogueAgentBase\rogueai") {
        $fileCount = (Get-ChildItem "$RogueAgentBase\rogueai" -Recurse -File).Count
        Write-Host "   ✓ $RogueAgentBase\rogueai ($fileCount files)" -ForegroundColor Green
    } else {
        Write-Host "   ✗ Knowledge base not found" -ForegroundColor Red
    }
    
    # Check chat mode files
    Write-Host ""
    Write-Host "Chat Mode Files:" -ForegroundColor Yellow
    foreach ($location in $ChatModeLocations) {
        $filePath = Join-Path $location $ChatModeFile
        if (Test-Path $filePath) {
            Write-Host "   ✓ $filePath" -ForegroundColor Green
        } else {
            Write-Host "   ✗ $filePath" -ForegroundColor Red
        }
    }
    
    # Check shortcuts
    Write-Host ""
    Write-Host "Desktop Shortcut:" -ForegroundColor Yellow
    $shortcutPath = "$env:USERPROFILE\Desktop\Rogue Agent Config.lnk"
    if (Test-Path $shortcutPath) {
        Write-Host "   ✓ $shortcutPath" -ForegroundColor Green
    } else {
        Write-Host "   ✗ $shortcutPath" -ForegroundColor Red
    }
}

function Install-RogueAgent {
    param([string]$SourcePath)
    
    Write-Host "Installing Rogue Agent globally..." -ForegroundColor Green
    
    # Create directories
    New-Item -ItemType Directory -Path $RogueAgentBase -Force | Out-Null
    foreach ($location in $ChatModeLocations) {
        New-Item -ItemType Directory -Path $location -Force | Out-Null
    }
    
    # Copy knowledge base if source provided
    if ($SourcePath -and (Test-Path "$SourcePath\rogueai")) {
        Write-Host "Copying knowledge base from $SourcePath\rogueai..." -ForegroundColor Yellow
        Copy-Item -Recurse -Path "$SourcePath\rogueai" -Destination "$RogueAgentBase\rogueai" -Force
    }
    
    # Copy chat mode file if exists
    if ($SourcePath -and (Test-Path "$SourcePath\.github\chatmodes\$ChatModeFile")) {
        Write-Host "Copying chat mode definition..." -ForegroundColor Yellow
        foreach ($location in $ChatModeLocations) {
            Copy-Item -Path "$SourcePath\.github\chatmodes\$ChatModeFile" -Destination $location -Force
        }
        Copy-Item -Path "$SourcePath\.github\chatmodes\$ChatModeFile" -Destination $RogueAgentBase -Force
    }
    
    # Create desktop shortcut
    $shortcutPath = "$env:USERPROFILE\Desktop\Rogue Agent Config.lnk"
    $WshShell = New-Object -comObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($shortcutPath)
    $Shortcut.TargetPath = $RogueAgentBase
    $Shortcut.Save()
    
    Write-Host "Installation completed!" -ForegroundColor Green
    Show-Status
}

function Update-RogueAgent {
    Write-Host "Updating Rogue Agent..." -ForegroundColor Green
    Write-Host "Please manually update files in: $RogueAgentBase" -ForegroundColor Yellow
    Write-Host "Or run with source path: .\manage-rogue-agent.ps1 update -SourcePath 'C:\path\to\project'" -ForegroundColor Yellow
}

function Remove-RogueAgent {
    Write-Host "Removing Rogue Agent..." -ForegroundColor Red
    
    # Remove chat mode files
    foreach ($location in $ChatModeLocations) {
        $filePath = Join-Path $location $ChatModeFile
        if (Test-Path $filePath) {
            Remove-Item $filePath -Force
            Write-Host "Removed: $filePath" -ForegroundColor Yellow
        }
    }
    
    # Remove base directory
    if (Test-Path $RogueAgentBase) {
        Remove-Item $RogueAgentBase -Recurse -Force
        Write-Host "Removed: $RogueAgentBase" -ForegroundColor Yellow
    }
    
    # Remove shortcut
    $shortcutPath = "$env:USERPROFILE\Desktop\Rogue Agent Config.lnk"
    if (Test-Path $shortcutPath) {
        Remove-Item $shortcutPath -Force
        Write-Host "Removed: $shortcutPath" -ForegroundColor Yellow
    }
    
    Write-Host "Rogue Agent removed!" -ForegroundColor Green
}

# Main execution
switch ($Action) {
    "install" { 
        $sourcePath = Read-Host "Enter source project path (or press Enter to skip)"
        if ($sourcePath) {
            Install-RogueAgent -SourcePath $sourcePath
        } else {
            Install-RogueAgent
        }
    }
    "update" { Update-RogueAgent }
    "remove" { Remove-RogueAgent }
    "status" { Show-Status }
}