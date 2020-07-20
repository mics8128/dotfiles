set nocompatible
set rtp+=~/.config/nvim/

" load vundle
source ~/.config/nvim/vim-plug.vim
source ~/.config/nvim/general.vim
source ~/.config/nvim/plugins.vim

" auto reload vimrc when editing it
autocmd! bufwritepost ~/.config/nvim/init.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/.config/nvim/vim-plug.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/.config/nvim/general.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/.config/nvim/plugins.vim source ~/.config/nvim/init.vim

" auto reload vimrc when editing it
autocmd! bufwritepost ~/dotfiles/home-dot-config/nvim/init.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/dotfiles/home-dot-config/nvim/vim-plug.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/dotfiles/home-dot-config/nvim/general.vim source ~/.config/nvim/init.vim
autocmd! bufwritepost ~/dotfiles/home-dot-config/nvim/plugins.vim source ~/.config/nvim/init.vim

" When editing a file, always jump to the last known cursor position.
" Don't do it when the position is invalid or when inside an event handler
" (happens when dropping a file on gvim).
" Also don't do it when the mark is in the first line, that is the default
" position when opening a file.
autocmd BufReadPost *
            \ if line("'\"") > 1 && line("'\"") <= line("$") |
            \   exe "normal! g`\"" |
            \ endif
