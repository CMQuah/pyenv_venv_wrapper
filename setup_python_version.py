#!/usr/bin/env python
import re
import subprocess
import argparse
        
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
        
def check_python_version_installed(version):

    output = subprocess.check_output(['pyenv', 'versions'], universal_newlines=True)
    versions = output.strip().split('\n')
    for v in versions:
        if version in v:
            print(f"Python version {version} is installed.")
            return
    print(f"Python version {version} is not installed.")
        
def create_virtual_environment(name, python_version="3.8.5"):
    try:        
        check_python_version_installed(python_version)
        # Create virtual environment
        subprocess.check_call(['pyenv', 'virtualenv', python_version, name])
        
        print(f"Virtual environment '{name}' has been created using Python {python_version}.")
    except subprocess.CalledProcessError:
        print(f"Failed to create virtual environment '{name}' with Python {python_version}.")
        
def main():
    parser = argparse.ArgumentParser(description='Python Version Setup')
    parser.add_argument('--install', metavar='VERSION', help='Install a specific Python version')
    parser.add_argument('--check-venv', action='store_true', help='Check available Python versions in virtual environment')
    parser.add_argument('--create-venv', metavar='NAME',
                        help='Create a virtual environment with a specific name. Use --venv-python-version'
                        ' to specify the Python version')
    parser.add_argument('--venv-python-version', metavar='VERSION', help='Specify the Python version for the virtual environment')
    parser.add_argument('--list-versions', action='store_true', help='List available Python versions')
    args = parser.parse_args()

    if args.install:
        install_python_version(args.install)
    elif args.check_venv:
        check_venv_python_version()
    elif args.create_venv:
        if args.venv_python_version:
            create_virtual_environment(args.create_venv, args.venv_python_version)
        else:
            print("Please specify the Python version for the virtual environment using the --venv-python-version flag.")
    elif args.list_versions:
        list_available_python_versions()
    else:
        print("Please specify an action to perform.")

if __name__ == '__main__':
    main()
