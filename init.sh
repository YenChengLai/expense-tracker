#!/bin/bash
# Loop through sh files in .cmds folder
for script in .cmds/*.sh; do
    # Grant executable permissions to the scripts
    sudo chmod +x "$script"
    # Check if the file is executable and is a regular file
    if [ -x "$script" ] && [ -f "$script" ]; then
        echo "Running $script"
        # Source the script to run it in the current shell
        source "$script"
    fi
done