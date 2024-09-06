#!/usr/bin/env python
import re
import subprocess
        
def install_python_version(version):
    try:
        subprocess.check_call(['pyenv', 'install', version])
        print(f"Python version {version} has been installed.")
    except subprocess.CalledProcessError:
        print(f"Failed to install Python version {version}.")

def list_available_python_versions():
    try:
        output = subprocess.check_output(['pyenv', 'install', '--list'], universal_newlines=True)
        versions = output.strip().split('\n')
        filtered_versions = []
        print("Available Python3 versions:")
        for version in versions:
            if re.match(r"^3\.", version.lstrip()):
                print(version)
                filtered_versions.append(version)
        # for version in filtered_versions:
        #     print(version)
    except subprocess.CalledProcessError:
        print("Failed to list available Python versions.")
        
def check_venv_python_version():
    try:
        output = subprocess.check_output(['pyenv', 'versions'], universal_newlines=True)
        versions = output.strip().split('\n')
        filtered_versions = []
        for version in versions:
            if re.match(r"^\* ", version):
                filtered_versions.append(version[2:])
        if filtered_versions:
            print("Python versions available in virtual environment:")
            for version in filtered_versions:
                print(version)
        else:
            print("No Python versions available in virtual environment.")
    except subprocess.CalledProcessError:
        print("Failed to check virtual environment Python versions.")
        
def create_virtual_environment(name, python_version="3.8.5"):
    try:        
        # Create virtual environment
        subprocess.check_call(['pyenv', 'virtualenv', python_version, name])
        
        print(f"Virtual environment '{name}' has been created using Python {python_version}.")
    except subprocess.CalledProcessError:
        print(f"Failed to create virtual environment '{name}' with Python {python_version}.")
        

# output = subprocess.Popen(['pyenv', 'local'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = output.communicate()
# is_system_python = ""
# print(stdout.decode('utf-8'))
# if stdout.decode('utf-8').strip() == "system":
#     output = subprocess.Popen(['python3', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = output.communicate()
#     is_system_python = "(system)"

# print(f"Current python version: {stdout.decode('utf-8').strip()} {is_system_python}")

# List available Python versions
list_available_python_versions()

# install_python_version("3.8.5")

# check_venv_python_version()
