#!/bin/bash

# This script installs the required packages for pyenv on Ubuntu (For first time setup only)

# Update package lists
sudo apt update

# Install required packages
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev git

echo "Required Ubuntu modules installed successfully."

# Download and install pyenv
curl https://pyenv.run | bash

# Add pyenv to the PATH
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Reload the shell
source ~/.bashrc

# Verify the installation
pyenv --version

echo "pyenv installed successfully."