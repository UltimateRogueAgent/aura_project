# Ruff Documentation

Ruff is an extremely fast Python linter and code formatter, written in Rust, offering broad compatibility with existing tools and extensive rule support.

## Installation

### Using uv (Recommended)

```bash
# Install globally
uv tool install ruff@latest

# Add to project
uv add --dev ruff
```

### Using pip

```bash
pip install ruff
```

### Using pipx

```bash
pipx install ruff
```

### Standalone Installers

```bash
# macOS and Linux
curl -LsSf https://astral.sh/ruff/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/ruff/install.ps1 | iex"

# Specific version
curl -LsSf https://astral.sh/ruff/0.5.0/install.sh | sh
```

### Package Managers

```bash
# Alpine Linux
apk add ruff

# openSUSE Tumbleweed
sudo zypper install python3-ruff

# pkgx
pkgx install ruff
```

### Using uvx (No Installation Required)

```bash
uvx ruff check   # Lint all files in the current directory
uvx ruff format  # Format all files in the current directory
```

## Quick Start

### Basic Usage

```bash
# Lint all files in current directory
ruff check

# Format all files in current directory
ruff format

# Lint specific files
ruff check src/

# Fix auto-fixable issues
ruff check --fix

# Show all available rules
ruff linter
```

### Common Commands

```bash
# Check and fix in one command
ruff check --fix && ruff format

# Check with specific output format
ruff check --output-format=github

# Show statistics
ruff check --statistics

# Show fixes that would be applied
ruff check --diff

# Watch for changes
ruff check --watch
```

## Configuration

### pyproject.toml

```toml
[tool.ruff]
# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
]

# Same as Black.
line-length = 88
indent-width = 4

# Assume Python 3.8+
target-version = "py38"

[tool.ruff.lint]
# Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)  codes by default.
# Unlike Flake8, Ruff doesn't enable pycodestyle warnings (`W`) or
# McCabe complexity (`C901`) by default.
select = ["E4", "E7", "E9", "F"]
ignore = []

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[tool.ruff.format]
# Like Black, use double quotes for strings.
quote-style = "double"

# Like Black, indent with spaces, rather than tabs.
indent-style = "space"

# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false

# Like Black, automatically detect the appropriate line ending.
line-ending = "auto"

# Enable auto-formatting of code examples in docstrings. Markdown,
# reStructuredText code/literal blocks and doctests are all supported.
docstring-code-format = false

# Set the line length limit used when formatting code snippets in
# docstrings.
docstring-code-line-length = "dynamic"
```

### ruff.toml

```toml
# Alternative configuration file
line-length = 88
target-version = "py38"

[lint]
select = [
    # pycodestyle
    "E",
    # Pyflakes
    "F",
    # pyupgrade
    "UP",
    # flake8-bugbear
    "B",
    # flake8-simplify
    "SIM",
    # isort
    "I",
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
]

[format]
quote-style = "double"
indent-style = "space"
```

## Linting

### Rule Selection

```bash
# Enable specific rules
ruff check --select E,F,UP,B

# Ignore specific rules
ruff check --ignore E501,W503

# Show all available rules
ruff linter

# Show rules for specific categories
ruff linter --show-source
```

### Common Rule Categories

```toml
[tool.ruff.lint]
select = [
    "E",     # pycodestyle errors
    "W",     # pycodestyle warnings
    "F",     # Pyflakes
    "UP",    # pyupgrade
    "B",     # flake8-bugbear
    "SIM",   # flake8-simplify
    "I",     # isort
    "N",     # pep8-naming
    "D",     # pydocstyle
    "S",     # flake8-bandit
    "BLE",   # flake8-blind-except
    "FBT",   # flake8-boolean-trap
    "A",     # flake8-builtins
    "COM",   # flake8-commas
    "C4",    # flake8-comprehensions
    "DTZ",   # flake8-datetimez
    "T10",   # flake8-debugger
    "DJ",    # flake8-django
    "EM",    # flake8-errmsg
    "EXE",   # flake8-executable
    "FA",    # flake8-future-annotations
    "ISC",   # flake8-implicit-str-concat
    "ICN",   # flake8-import-conventions
    "G",     # flake8-logging-format
    "INP",   # flake8-no-pep420
    "PIE",   # flake8-pie
    "T20",   # flake8-print
    "PYI",   # flake8-pyi
    "PT",    # flake8-pytest-style
    "Q",     # flake8-quotes
    "RSE",   # flake8-raise
    "RET",   # flake8-return
    "SLF",   # flake8-self
    "SLOT",  # flake8-slots
    "TID",   # flake8-tidy-imports
    "TCH",   # flake8-type-checking
    "INT",   # flake8-gettext
    "ARG",   # flake8-unused-arguments
    "PTH",   # flake8-use-pathlib
    "TD",    # flake8-todos
    "FIX",   # flake8-fixme
    "ERA",   # eradicate
    "PD",    # pandas-vet
    "PGH",   # pygrep-hooks
    "PL",    # Pylint
    "TRY",   # tryceratops
    "FLY",   # flynt
    "NPY",   # NumPy-specific rules
    "AIR",   # Airflow
    "PERF",  # Perflint
    "FURB",  # refurb
    "LOG",   # flake8-logging
    "RUF",   # Ruff-specific rules
]
```

### Per-File Ignores

```toml
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py
"tests/*" = ["S101"]      # Allow assert statements in tests
"migrations/*" = ["E501"] # Allow long lines in migrations
```

## Formatting

### Basic Formatting

```bash
# Format all files
ruff format

# Format specific files
ruff format src/

# Check formatting without applying changes
ruff format --check

# Show diff of what would be formatted
ruff format --diff
```

### Format Configuration

```toml
[tool.ruff.format]
# Use single quotes instead of double quotes
quote-style = "single"

# Use tabs instead of spaces
indent-style = "tab"

# Don't respect magic trailing commas
skip-magic-trailing-comma = true

# Use specific line ending
line-ending = "lf"  # or "crlf"

# Format code in docstrings
docstring-code-format = true

# Line length for docstring code
docstring-code-line-length = 72
```

## Integration

### Pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.1.6
    hooks:
      # Run the linter.
      - id: ruff
        args: [--fix]
      # Run the formatter.
      - id: ruff-format
```

### GitHub Actions

```yaml
name: CI
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ruff
      - name: Run Ruff
        run: ruff check --output-format=github .
      - name: Run Ruff formatter
        run: ruff format --check .
```

### VS Code

```json
// settings.json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": true
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

### Neovim

```lua
-- Using nvim-lspconfig
require('lspconfig').ruff_lsp.setup {
  init_options = {
    settings = {
      -- Any extra CLI arguments for `ruff` go here.
      args = {},
    }
  }
}
```

### PyCharm/IntelliJ

1. Install the Ruff plugin from the marketplace
2. Configure in Settings → Tools → Ruff
3. Enable "Run ruff on save"

## Advanced Usage

### Custom Rules

```toml
[tool.ruff.lint.flake8-naming]
# Allow Pydantic's `@validator` decorator to trigger class method treatment.
classmethod-decorators = ["classmethod", "pydantic.validator"]

[tool.ruff.lint.flake8-quotes]
docstring-quotes = "double"

[tool.ruff.lint.flake8-import-conventions.aliases]
# Declare the default aliases.
altair = "alt"
matplotlib = "mpl"
matplotlib.pyplot = "plt"
numpy = "np"
pandas = "pd"
seaborn = "sns"

[tool.ruff.lint.isort]
known-first-party = ["mypackage"]
```

### Ignoring Violations

```python
# Ignore specific rule for one line
import os  # noqa: F401

# Ignore multiple rules
import sys  # noqa: F401, E402

# Ignore all rules for one line
import whatever  # noqa

# Ignore for entire file
# ruff: noqa

# Ignore specific rule for entire file
# ruff: noqa: F401
```

### Configuration Inheritance

```toml
# pyproject.toml
[tool.ruff]
extend = "ruff-defaults.toml"  # Inherit from another config file

# Override specific settings
line-length = 100
```

## Performance and Caching

### Cache Management

```bash
# Clear cache
ruff clean

# Show cache location
ruff --cache-dir

# Disable cache
ruff check --no-cache
```

### Performance Tips

1. Use `.ruffignore` file for large exclusions
2. Configure `exclude` patterns in configuration
3. Use `--target-version` to enable version-specific optimizations
4. Run on specific directories rather than entire project when possible

## Migration from Other Tools

### From Black

```toml
[tool.ruff.format]
# Ruff's formatter is designed to be a drop-in replacement for Black
# Most Black configurations translate directly
line-length = 88
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
```

### From isort

```toml
[tool.ruff.lint]
select = ["I"]  # Enable isort rules

[tool.ruff.lint.isort]
known-first-party = ["mypackage"]
force-single-line = true
```

### From Flake8

```toml
[tool.ruff.lint]
# Most Flake8 rules are supported
select = ["E", "F", "W", "B", "SIM"]
ignore = ["E501"]  # Same ignore patterns work

# Plugin equivalents
# flake8-bugbear -> "B"
# flake8-simplify -> "SIM"
# flake8-import-conventions -> "ICN"
```

## Troubleshooting

### Common Issues

```bash
# Rule not found
ruff check --select XYZ123  # Check if rule exists with `ruff linter`

# Configuration not loaded
ruff check --show-settings  # Show current configuration

# Performance issues
ruff check --statistics  # Show timing information

# Formatting conflicts
ruff format --diff  # See what would change
```

### Debug Mode

```bash
# Verbose output
ruff check --verbose

# Show all settings
ruff check --show-settings

# Show files being processed
ruff check --show-files
```

## Best Practices

### Project Setup

1. Add `ruff.toml` or configure in `pyproject.toml`
2. Set up pre-commit hooks
3. Configure CI/CD pipeline
4. Set up editor integration
5. Document team conventions

### Rule Selection Strategy

1. Start with default rules
2. Add rules incrementally
3. Use `--fix` to auto-fix issues
4. Review and adjust ignore patterns
5. Document rule choices in configuration

### Team Adoption

1. Introduce gradually
2. Fix existing violations first
3. Set up automated formatting
4. Train team on configuration
5. Monitor and adjust rules based on feedback

This documentation covers the essential features of Ruff for Python code linting and formatting with high performance and extensive rule support.
