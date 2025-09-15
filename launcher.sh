#!/bin/bash

# AURA - Autonomous Unit & Resource Arbitrator
# Launcher Script

# Activate the virtual environment
if [ -d "aura_env" ]; then
    echo "Activating virtual environment..."
    source aura_env/bin/activate
else
    echo "Virtual environment 'aura_env' not found. Please run the setup script first."
    exit 1
fi

# Run the main application
echo "Starting AURA..."
python main.py

# Deactivate the virtual environment on exit
deactivate
echo "AURA has been shut down."
