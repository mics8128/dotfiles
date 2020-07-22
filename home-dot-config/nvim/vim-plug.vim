" ==================
" coc
" ==================
let g:coc_global_extensions = []

" Tools
call add(g:coc_global_extensions, 'coc-git')
call add(g:coc_global_extensions, 'coc-lists')
" call add(g:coc_global_extensions, 'coc-ultisnips')
call add(g:coc_global_extensions, 'coc-highlight')

" Languages
call add(g:coc_global_extensions, 'coc-python')
call add(g:coc_global_extensions, 'coc-phpls')
call add(g:coc_global_extensions, 'coc-css')
call add(g:coc_global_extensions, 'coc-html')
call add(g:coc_global_extensions, 'coc-tsserver') " TypeScript & JavaScript
call add(g:coc_global_extensions, 'coc-json')
call add(g:coc_global_extensions, 'coc-yaml')

" ==================
" vim-plug
" ==================
call plug#begin(stdpath('data') . '/plugged')

" Make sure you use single quotes

" Theme
Plug 'lifepillar/vim-solarized8'

" 自動補完/搜尋 (通用)
Plug 'neoclide/coc.nvim', {'branch': 'release', 'do': { -> coc#util#install() }}
Plug 'Yggdroot/LeaderF', { 'do': './install.sh' }

" 增加效率
Plug 'easymotion/vim-easymotion'

" Language support
Plug 'sheerun/vim-polyglot' " AIO
Plug 'jwalton512/vim-blade' " Laravel blade

" Initialize plugin system
call plug#end()
