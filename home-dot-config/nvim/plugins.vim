" Leaderf
" =======================
" config
let g:Lf_GtagsAutoGenerate = 1

" shortcut
let g:Lf_ShortcutF = "<leader>f"
nnoremap <leader>t :<C-U><C-R>=printf("Leaderf bufTag %s", "")<CR><CR>
nnoremap <leader>p :<C-U><C-R>=printf("Leaderf gtags %s", "")<CR><CR>
nnoremap <leader>F :<C-U><C-R>=printf("Leaderf! function %s", "")<CR><CR>

" vim-easymotion
" =======================
" config
let g:EasyMotion_smartcase = 1
let g:EasyMotion_use_smartsign_us = 1
let g:EasyMotion_do_mapping = 0

" shortcut
nmap <Leader>s <Plug>(easymotion-s)
nmap <Leader>j <Plug>(easymotion-j)
nmap <Leader>k <Plug>(easymotion-k)
nmap <Leader>w <Plug>(easymotion-W)
nmap <Leader>b <Plug>(easymotion-B)
