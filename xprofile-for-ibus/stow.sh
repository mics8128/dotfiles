#!/usr/bin/env sh
#
# Easy stow by Mics
# v0.1
#


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
case $KEY in
"-D")
    stow --dotfile --ignore="^stow\.sh$" --verbose \
        --target="$TARGET" --delete .
    ;;
*)
    mkdir -p $TARGET
    stow --dotfile --ignore="^stow\.sh$" --verbose \
        --target="$TARGET" .
    ;;
esac
