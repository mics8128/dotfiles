#!/usr/bin/env sh
#
# Easy stow by Mics
# v0.2
#

# pre-install for this package ONLY
# ============
if [ ! -d "$HOME/.zim" ]; then
    curl -fsSL https://raw.githubusercontent.com/zimfw/install/master/install.zsh | zsh
fi

# config
# ============

# where you want to put files
export PREFIX='' 
# put $HOME or /
export ROOT="$HOME"                


# starting
# ============

export KEY="$1"
export TARGET=$HOME/$PREFIX
export SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
exec $SCRIPTPATH/../tools/stow.sh
