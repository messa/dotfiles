#!/bin/bash

set -e
set -x

sudo aptitude install \
    apt-file \
    build-essential \
    colordiff \
    colorgcc \
    git \
    htop \
    ifstat \
    mc \
    python3 \
    python3-setuptools \
    strace \
    subversion \
    tree \
    vim \

sudo apt-file update

cd ~
[ -d code ] || mkdir code
cd ~/code
[ -d dotfiles ] || git clone https://messa@github.com/messa/dotfiles.git
[ -d tools ]    || git clone https://messa@github.com/messa/tools.git

~/code/dotfiles/scripts/install_symlinks.py

echo "Done."

