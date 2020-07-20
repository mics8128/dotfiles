" Leaderf config
let g:Lf_GtagsAutoGenerate = 1

" Leaderf shortcut
let g:Lf_ShortcutF = "<leader>ff"
nnoremap <leader>ft :<C-U><C-R>=printf("Leaderf bufTag %s", "")<CR><CR>
nnoremap <leader>fp :<C-U><C-R>=printf("Leaderf gtags %s", "")<CR><CR>

nnoremap <leader>b :<C-u>call gitblame#echo()<CR>
