set nocompatible
set rtp+=~/.config/nvim/

" load vundle
source ~/.config/nvim/vundle.vim

" auto reload vimrc when editing it
autocmd! bufwritepost ~/.config/nvim/init.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/.config/nvim/vundle.vim source ~/.config/nvim/init.vim

" Backup & swap
silent !mkdir -p ~/.cache/nvim/backup > /dev/null 2>&1
silent !mkdir -p ~/.cache/nvim/swap > /dev/null 2>&1
set backupdir=~/.cache/nvim/backup
set directory=~/.cache/nvim/swap
