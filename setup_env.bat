@echo off
echo Creating AURA virtual environment...

if exist .venv (
    echo Virtual environment already exists. Activating...
) else (
    echo Creating new virtual environment...
    python -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Installing Playwright browsers...
playwright install

echo Checking Ollama connection...
python -c "import ollama; print('Ollama client imported successfully')" 2>nul
if %errorlevel% neq 0 (
    echo Warning: Ollama client test failed. Make sure Ollama is installed and running.
)

echo.
echo Setup complete! To activate the environment, run:
echo .venv\Scripts\activate.bat
pause