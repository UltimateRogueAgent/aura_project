# Python-dotenv Documentation

Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in developing applications following the 12-factor principles.

## Installation

### Basic Installation

```bash
pip install python-dotenv
```

### With CLI Support

```bash
pip install "python-dotenv[cli]"
```

## Quick Start

### Basic Usage

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')
debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
```

### Example .env File

```bash
# .env
DATABASE_URL=postgresql://user:password@localhost/dbname
API_KEY=your-secret-api-key
DEBUG=True
SECRET_KEY=your-secret-key
PORT=8000
```

## Core Functions

### load_dotenv()

Loads environment variables from a .env file into the current process.

```python
from dotenv import load_dotenv

# Load from default .env file
load_dotenv()

# Load from specific file
load_dotenv('.env.production')

# Load and override existing environment variables
load_dotenv(override=True)

# Load from a specific path
load_dotenv('/path/to/.env')

# Don't search parent directories
load_dotenv(find_dotenv=False)
```

### dotenv_values()

Parses a .env file and returns its contents as a dictionary without modifying the environment.

```python
from dotenv import dotenv_values

# Parse .env file to dictionary
config = dotenv_values(".env")
print(config)  # {"DATABASE_URL": "postgresql://...", "API_KEY": "..."}

# Combine multiple .env files
import os

config = {
    **dotenv_values(".env.shared"),    # shared development variables
    **dotenv_values(".env.secret"),    # sensitive variables
    **os.environ,                      # override with environment variables
}
```

### find_dotenv()

Finds the path to a .env file by searching upward from the current directory.

```python
from dotenv import find_dotenv

# Find .env file
dotenv_path = find_dotenv()
print(dotenv_path)  # /path/to/project/.env

# Find specific file
dotenv_path = find_dotenv('.env.local')

# Don't raise exception if not found
dotenv_path = find_dotenv(raise_error_if_not_found=False)
```

## Advanced Usage

### Loading from Stream

```python
from io import StringIO
from dotenv import load_dotenv

# Load from string/stream
config_string = "DATABASE_URL=sqlite:///app.db\nDEBUG=True"
config_stream = StringIO(config_string)
load_dotenv(stream=config_stream)
```

### Multiple Environment Files

```python
from dotenv import load_dotenv
import os

# Load base configuration
load_dotenv('.env')

# Load environment-specific configuration
environment = os.getenv('ENVIRONMENT', 'development')
load_dotenv(f'.env.{environment}', override=True)

# Load local overrides
load_dotenv('.env.local', override=True)
```

### Conditional Loading

```python
from dotenv import load_dotenv
import os

# Only load if not in production
if os.getenv('ENVIRONMENT') != 'production':
    load_dotenv()

# Load different files based on environment
env = os.getenv('ENVIRONMENT', 'development')
if env == 'development':
    load_dotenv('.env.dev')
elif env == 'testing':
    load_dotenv('.env.test')
```

## Environment Variable Formats

### Basic Key-Value Pairs

```bash
# Simple values
DATABASE_URL=postgresql://localhost/mydb
API_KEY=abc123
PORT=8000
```

### Quoted Values

```bash
# Values with spaces
APP_NAME="My Application"
DESCRIPTION='This is a description with spaces'

# Values with special characters
PASSWORD="p@ssw0rd!#$"
```

### Multiline Values

```bash
# Multiline values
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7...
-----END PRIVATE KEY-----"

# Alternative multiline format
SQL_QUERY="SELECT *
FROM users
WHERE active = true"
```

### Variables Without Values

```bash
# Variable without value (results in None with dotenv_values)
OPTIONAL_FEATURE

# Empty string value
EMPTY_VALUE=""
```

### Comments

```bash
# This is a comment
DATABASE_URL=postgresql://localhost/mydb  # Inline comment

# Multi-line comment
# This configuration is for development
# Do not use in production
DEBUG=True
```

### Variable Expansion

```bash
# Reference other variables
BASE_URL=https://api.example.com
API_ENDPOINT=${BASE_URL}/v1/users

# With default values
PORT=${PORT:-8000}
```

## Command Line Interface

### python-dotenv Installation

```bash
pip install "python-dotenv[cli]"
```

### Basic Commands

```bash
# Set environment variables
dotenv set DATABASE_URL postgresql://localhost/mydb
dotenv set API_KEY your-secret-key

# List all variables
dotenv list

# List in JSON format
dotenv list --format=json

# Get specific variable
dotenv get DATABASE_URL

# Unset variable
dotenv unset API_KEY

# Run command with loaded environment
dotenv run -- python manage.py runserver
dotenv run -- npm start
```

### Working with Different Files

```bash
# Use specific .env file
dotenv -f .env.production set DATABASE_URL postgresql://prod/mydb

# List from specific file
dotenv -f .env.local list
```

## IPython/Jupyter Integration

### Loading Extension

```python
# In IPython or Jupyter
%load_ext dotenv

# Load default .env file
%dotenv

# Load specific file
%dotenv /path/to/.env

# Load with options
%dotenv -o  # Override existing variables
%dotenv -v  # Verbose output
%dotenv -o -v /path/to/.env.local
```

## Django Integration

### settings.py

```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Django settings
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Email configuration
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True').lower() == 'true'
```

### manage.py

```python
#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv

if __name__ == '__main__':
    # Load environment variables before Django setup
    load_dotenv()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
```

## Flask Integration

```python
from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration from environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'

@app.route('/')
def hello():
    return f"Running in {'debug' if app.config['DEBUG'] else 'production'} mode"

if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST', '127.0.0.1'),
        port=int(os.getenv('PORT', 5000)),
        debug=app.config['DEBUG']
    )
```

## FastAPI Integration

```python
from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(
    title=os.getenv('APP_NAME', 'My API'),
    debug=os.getenv('DEBUG', 'False').lower() == 'true'
)

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "environment": os.getenv('ENVIRONMENT', 'development')
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv('HOST', '127.0.0.1'),
        port=int(os.getenv('PORT', 8000))
    )
```

## Best Practices

### Environment File Organization

```bash
# .env (base configuration)
APP_NAME=MyApp
LOG_LEVEL=INFO

# .env.development
DEBUG=True
DATABASE_URL=sqlite:///dev.db

# .env.production
DEBUG=False
DATABASE_URL=postgresql://prod-server/mydb

# .env.local (local overrides, not in version control)
API_KEY=local-development-key
```

### Loading Strategy

```python
from dotenv import load_dotenv
import os

def load_environment():
    """Load environment variables with proper precedence."""
    # Load base configuration
    load_dotenv('.env')

    # Load environment-specific configuration
    env = os.getenv('ENVIRONMENT', 'development')
    load_dotenv(f'.env.{env}', override=True)

    # Load local overrides (highest precedence)
    load_dotenv('.env.local', override=True)

# Call at application startup
load_environment()
```

### Type Conversion Helpers

```python
import os
from typing import Optional

def get_bool_env(key: str, default: bool = False) -> bool:
    """Get boolean environment variable."""
    value = os.getenv(key, str(default)).lower()
    return value in ('true', '1', 'yes', 'on')

def get_int_env(key: str, default: int = 0) -> int:
    """Get integer environment variable."""
    try:
        return int(os.getenv(key, str(default)))
    except ValueError:
        return default

def get_list_env(key: str, separator: str = ',', default: Optional[list] = None) -> list:
    """Get list environment variable."""
    value = os.getenv(key)
    if value is None:
        return default or []
    return [item.strip() for item in value.split(separator)]

# Usage
DEBUG = get_bool_env('DEBUG')
PORT = get_int_env('PORT', 8000)
ALLOWED_HOSTS = get_list_env('ALLOWED_HOSTS')
```

### Configuration Class

```python
from dotenv import load_dotenv
import os

class Config:
    """Application configuration."""

    def __init__(self):
        load_dotenv()

        # Database
        self.DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')

        # Security
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY environment variable is required")

        # Application
        self.DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
        self.HOST = os.getenv('HOST', '127.0.0.1')
        self.PORT = int(os.getenv('PORT', 8000))

        # External services
        self.REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
        self.EMAIL_HOST = os.getenv('EMAIL_HOST')

    def validate(self):
        """Validate required configuration."""
        required = ['SECRET_KEY']
        missing = [key for key in required if not getattr(self, key)]
        if missing:
            raise ValueError(f"Missing required environment variables: {missing}")

# Usage
config = Config()
config.validate()
```

## Security Considerations

### .gitignore Setup

```bash
# Environment files
.env
.env.local
.env.*.local

# Keep template files
!.env.example
!.env.template
```

### Environment Template

```bash
# .env.example
# Copy this file to .env and fill in your values

# Database
DATABASE_URL=postgresql://user:password@localhost/dbname

# Security
SECRET_KEY=your-secret-key-here

# External Services
API_KEY=your-api-key
EMAIL_HOST=smtp.example.com
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-email-password

# Application
DEBUG=False
PORT=8000
```

### Validation and Defaults

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Validate critical environment variables
required_vars = ['SECRET_KEY', 'DATABASE_URL']
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    raise EnvironmentError(f"Missing required environment variables: {missing_vars}")

# Use secure defaults
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
```

This documentation covers the essential features of python-dotenv for managing environment variables in Python applications following the 12-factor app methodology.
