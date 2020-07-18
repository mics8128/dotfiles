set nocompatible " be improved, required
filetype off " require before vundle#begin

" Auto Install Vundle
let vundle_readme=$HOME . '/.config/nvim/bundle/Vundle.vim/README.md'
if !filereadable(vundle_readme)
    echo "Installing Vundle.."
    echo ""
    silent !mkdir -p ~/.config/nvim/bundle
    silent !git clone https://github.com/gmarik/vundle ~/.config/nvim/bundle/Vundle.vim
endif

" Vundle begin
set rtp+=~/.config/nvim/bundle/Vundle.vim
call vundle#begin('~/.config/nvim/bundle/')
Plugin 'VundleVim/Vundle.vim'

" Vundle end
call vundle#end()            " required
filetype plugin indent on    " required
