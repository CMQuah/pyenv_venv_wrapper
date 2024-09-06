#!/bin/bash

# Check if both arguments are provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 <venv_name> <python_script or pip install (by putting Install)\
    )> [script_arguments...]"
    exit 1
fi

# Set the name of your virtual environment
venv_name="$1"

# Set the path to your Python script
python_script="$2"

# Activate the virtual environment
source "$(pyenv root)/versions/$venv_name/bin/activate"

# Shift the arguments to exclude the venv name and script name
shift 2

# Check if the second argument is "install"
if [ "$python_script" = "install" ]; then
    # Run pip install with the provided arguments
    pip install "$@"
else
    # Run the Python script with the provided arguments
    python "$python_script" "$@"
fi

# Deactivate the virtual environment
deactivate