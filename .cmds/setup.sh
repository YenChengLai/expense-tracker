#!/bin/bash

# Name of your virtual environment
venv_name="expense-tracker"

# Get the directory of this script
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if virtual environment already exists
if [ -d "$venv_name" ]; then
    echo "Deleting existing virtual environment $venv_name"
    sudo rm -rf "$venv_name"  # Delete the existing virtual environment directory
fi

# Create virtual environment
python3 -m venv "$venv_name"

# Ensure the activation script has the correct permissions
sudo chmod +x "$venv_name/bin/activate"

# Activate virtual environment
source "$venv_name/bin/activate"

# Install dependencies from requirements.txt
pip install -r "$script_dir/requirements.txt"

# Upgrade pip version
pip install --upgrade pip

# Check if .env file exists
if [ -f ".env" ]; then
    # Check if GOOGLE_APPLICATION_CREDENTIALS already exists in the file
    if grep -q "^GOOGLE_APPLICATION_CREDENTIALS=" ".env"; then
        echo "GOOGLE_APPLICATION_CREDENTIALS already exists in .env"
    else
        # Append the content to the file if it doesn't exist
        echo "GOOGLE_APPLICATION_CREDENTIALS=" >> .env
    fi
else
    # If it doesn't exist, create it and write the content
    echo "GOOGLE_APPLICATION_CREDENTIALS=" > .env
fi

echo "Virtual environment $venv_name created."