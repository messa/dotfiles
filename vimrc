" Vim configuration - link/copy this file to ~/.vimrc

syntax enable
colors slate
:hi Type ctermfg=cyan
:hi LineNr ctermfg=darkgray cterm=bold
:hi Function ctermfg=white
:hi Comment ctermfg=gray

set shiftwidth=4     " sirka odsazeni
set tabstop=4        " sirka tabulatoru
set expandtab        " mezery misto tabulatoru
set smarttab         " backspace snizi odsazeni
set autoindent       " chytre odsazovani
set hlsearch         " zvyraznovani pri hledani
set number           " cisla radku
set backspace=indent,eol,start
