#!/usr/bin/env sh
#
# Easy stow by Mics
# v0.2 - exec part
#

case $KEY in
"-D")
    stow --dotfile --ignore="^stow\.sh$" --verbose --delete \
        --target="$TARGET" --dir="`dirname $SCRIPTPATH`" `basename $SCRIPTPATH`
    ;;
*)
    mkdir -p $TARGET
    stow --dotfile --ignore="^stow\.sh$" --verbose \
        --target="$TARGET" --dir="`dirname $SCRIPTPATH`" `basename $SCRIPTPATH`
    ;;
esac
