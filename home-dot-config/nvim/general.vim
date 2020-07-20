" Theme
set termguicolors
set background=dark
colorscheme solarized8

" Show line numbers.
set number
set relativenumber

" 游標線
set cursorline

" 折行
set wrap	" 字數過長時換行。
set linebreak   " wrap but prevent linebreak
nnoremap <expr> k (v:count == 0 ? 'gk' : 'k')
nnoremap <expr> j (v:count == 0 ? 'gj' : 'j')
nnoremap <expr> <Up> (v:count == 0 ? 'gk' : 'k')
nnoremap <expr> <Down> (v:count == 0 ? 'gj' : 'j')

" 縮排
filetype indent on
set tabstop=8
set softtabstop=4
set shiftwidth=4
set noexpandtab

" Others
set mouse=nv                    " set mouse on n and v mode work

" Leader mapping
let mapleader=";"
