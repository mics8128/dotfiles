set nocompatible
set rtp+=~/.config/nvim/

" load vundle
source ~/.config/nvim/vim-plug.vim
source ~/.config/nvim/general.vim

" auto reload vimrc when editing it
autocmd! bufwritepost ~/.config/nvim/init.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/.config/nvim/vim-plug.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/.config/nvim/general.vim source ~/.config/nvim/init.vim

" auto reload vimrc when editing it
autocmd! bufwritepost ~/dotfiles/home-dot-config/nvim/init.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/dotfiles/home-dot-config/nvim/vim-plug.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/dotfiles/home-dot-config/nvim/general.vim source ~/.config/nvim/init.vim

