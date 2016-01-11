
Messa's dotfiles
================

There are some of my dotfiles.

How to install them:

    cd ~/code
    git clone https://github.com/messa/dotfiles.git
    cd ~
    mkdir -p .ssh/cm  # for control master sockets
    ln -s ~/code/dotfiles/ssh_config .ssh/config
    ln -s ~/code/dotfiles/vimrc      .vimrc

To install `bash_stuff`, add this to your `~/.bashrc` or `~/.bash_profile`:

    if [ -f ~/code/dotfiles/bash_stuff ]; then
        . ~/code/dotfiles/bash_stuff
    fi

See also https://github.com/messa/tips
