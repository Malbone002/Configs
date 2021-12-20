syntax on

set mouse=a
set noerrorbells
set sw=2
set expandtab
set smartindent
set number
set rnu
set numberwidth=1
set noswapfile
set nobackup
set incsearch
set ignorecase
set clipboard=unnamedplus
set encoding=utf-8
set showmatch
set cursorline
set termguicolors
set nocompatible


set colorcolumn=120
highlight ColoColumn ctermbg=0 guibg=lightgrey

call plug#begin(expand('~/.config/nvim/plugged'))

"Themes
Plug 'ghifarit53/tokyonight-vim'
Plug 'vim-airline/vim-airline'
"Functionality
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'jiangmiao/auto-pairs'
"Code modification
Plug 'neoclide/coc.nvim', {'branch': 'release'}

call plug#end()

"Tema
let g:airline_theme = "tokyonight"
let g:tokyonight_style = 'night' " available: night, storm
let g:tokyonight_enable_italic = 1
colorscheme tokyonight
"Config plugs
let NERDTreeQuitOnOpen=1

let mapleader = " "

"Atajos
nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
nmap <Leader>Q :q!<CR>
