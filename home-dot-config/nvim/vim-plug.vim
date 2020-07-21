call plug#begin(stdpath('data') . '/plugged')

" Make sure you use single quotes

" Theme
Plug 'lifepillar/vim-solarized8'

" 自動補完/搜尋 (通用)
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'Yggdroot/LeaderF', { 'do': './install.sh' }

" 增加效率
Plug 'easymotion/vim-easymotion'

" Language support
Plug 'sheerun/vim-polyglot' " AIO
Plug 'jwalton512/vim-blade' " Laravel blade

" Initialize plugin system
call plug#end()
