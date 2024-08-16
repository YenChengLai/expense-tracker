#!/bin/bash

# Name of your virtual environment
venv_name="expense-tracker"

# Activate virtual environment
source "$venv_name/bin/activate"

# Run the data fetching script
python scripts/fetch_data.py

# Check if fetching was successful (optional)
if [ $? -ne 0 ]; then
  echo "Error: Data fetching failed!"
  exit 1
fi

# Run the data cleaning script
python scripts/clean_data.py

# Check if cleaning was successful (optional)
if [ $? -ne 0 ]; then
  echo "Error: Data cleaning failed!"
  exit 1
fi

echo "Data preprocessed successfully!"

streamlit run scripts/visualize_data.py

if [ $? -ne 0 ]; then
  echo "Error: run Streamlit failed!"
  exit 1
fi
