# Rogue Agent - Global Chat Mode Setup

## Overview

This document describes how to set up Rogue Agent as a global chat mode available in all VS Code workspaces.

## Installation Locations

The Rogue Agent chat mode has been installed in multiple locations to ensure maximum compatibility:

### Primary Location
```
%APPDATA%\Code\User\chatmodes\
└── Rogue Agent.chatmode.md
```

### Alternative Location
```
%APPDATA%\Code\User\.github\chatmodes\
└── Rogue Agent.chatmode.md
```

### Backup Location (with knowledge base)
```
%APPDATA%\Code\User\rogue-agent\
├── Rogue Agent.chatmode.md
└── rogueai\                      # Complete knowledge base
```

## Knowledge Base Location

The Rogue Agent knowledge base is located at:
```
%APPDATA%\Code\User\rogue-agent\rogueai\
```

This contains all the documentation, methodologies, templates, and system instructions that define Rogue Agent's behavior.

## How It Works

1. **Global Availability**: The chat mode is available in any VS Code workspace
2. **Automatic Loading**: When you select "Rogue Agent" mode, it automatically loads the global knowledge base
3. **Project Context**: Additionally loads any project-specific `.rogue\steering\*.md` files from the current workspace
4. **Layered Configuration**: Global settings + project-specific overrides

## Testing Installation

To verify the installation:

1. Open any VS Code workspace
2. Open the chat panel
3. Look for "Rogue Agent" in the chat mode selector
4. Select it and try a simple command like "analyze this project"

## Updating

To update Rogue Agent:

### Update Knowledge Base
Edit files in: `%APPDATA%\Code\User\rogue-agent\rogueai\`

### Update Chat Mode Definition
Edit: `%APPDATA%\Code\User\chatmodes\Rogue Agent.chatmode.md`

Changes take effect immediately in new chat sessions.

## Troubleshooting

If Rogue Agent doesn't appear in chat modes:

1. **Check file locations**: Ensure files exist in the paths above
2. **Restart VS Code**: Sometimes required for new chat modes
3. **Check VS Code version**: Ensure you have a recent version with chat mode support
4. **Verify file format**: Ensure the `.chatmode.md` file has correct YAML frontmatter

## Fallback Option

If global installation doesn't work, you can always copy the files to individual projects:

```
your-project\
└── .github\
    └── chatmodes\
        └── Rogue Agent.chatmode.md
```

## File Paths Reference

All paths use Windows environment variables:
- `%APPDATA%` = `C:\Users\[username]\AppData\Roaming`
- Full path example: `C:\Users\rogue\AppData\Roaming\Code\User\chatmodes\`