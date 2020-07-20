call plug#begin(stdpath('data') . '/plugged')

" Make sure you use single quotes
Plug 'lifepillar/vim-solarized8'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'Yggdroot/LeaderF', { 'do': './install.sh' }
Plug 'easymotion/vim-easymotion'

" Language support -- php blade (Laravel)
Plug 'jwalton512/vim-blade'

" Initialize plugin system
call plug#end()
