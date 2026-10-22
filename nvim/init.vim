set number
set autoindent
set tabstop=2
set smarttab
set shiftwidth=2
set softtabstop=2
set mouse=a
set termguicolors
set clipboard^=unnamed,unnamedplus
set selection=exclusive

set backspace=indent,eol,start
set whichwrap+=<,>,h,l,[,]

set fillchars+=eob:\ 

set langmap=ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯ;ABCDEFGHIJKLMNOPQRSTUVWXYZ,фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz

nnoremap <C-f> <C-a>
inoremap ( ()<Left>
inoremap [ []<Left>
inoremap { {}<Left>
inoremap " ""<Left>
inoremap ' ''<Left>
inoremap ` ``<Left>

call plug#begin("~/.config/nvim/plugged")

Plug 'nvim-lualine/lualine.nvim'
Plug 'nvim-tree/nvim-web-devicons'

Plug 'preservim/nerdtree'
Plug 'fxn/vim-monochrome'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ryanoasis/vim-devicons'
Plug 'akinsho/toggleterm.nvim', {'tag': '*'}

call plug#end()

nnoremap e :NERDTree<CR>
nnoremap n :NERDTreeToggle<CR>
nnoremap q :q!<CR>
nnoremap <C-q> :wq!<CR>
nnoremap <C-s> :w<CR>
nnoremap t :ToggleTerm<CR>

nnoremap <C-a> ggVG
inoremap <C-a> <Esc>ggVG
vnoremap <C-a> <Esc>ggVG

vmap <C-c> "+y
vmap <C-y> "+y
vmap <C-x> "+x
nmap <C-v> "+p
imap <C-v> <C-r>+
nmap <C-z> u
imap <C-z> <C-o>u

nnoremap <C-u> u<CR>

vmap <BS> d
vmap <Del> d

lua << EOF
local colors = {
  bg       = "#14171D",
  mantle   = "#1C2027",
  crust    = "#14171D",
  surface  = "#2A2F38",
  border   = "#596070",
  text     = "#D2D3CE",
  subtext  = "#9C9E9E",
  accent   = "#8A9FAD",
  accent2  = "#B0A883",
  red      = "#AB8E89",
  green    = "#84916A",
  warning  = "#B0A883",
}

pcall(vim.cmd.colorscheme, "monochrome")

local highlights = {
  Normal       = { fg = colors.text, bg = colors.bg },
  NormalNC     = { fg = colors.text, bg = colors.bg },
  NormalFloat  = { fg = colors.text, bg = colors.mantle },
  FloatBorder  = { fg = colors.accent, bg = colors.mantle },

  CursorLine   = { bg = colors.mantle },
  CursorColumn = { bg = colors.mantle },

  LineNr       = { fg = colors.subtext, bg = colors.bg },
  CursorLineNr = { fg = colors.accent, bg = colors.bg, bold = true },
  SignColumn   = { fg = colors.subtext, bg = colors.bg },

  Visual       = { fg = colors.bg, bg = colors.accent },
  Search       = { fg = colors.bg, bg = colors.accent },
  IncSearch    = { fg = colors.bg, bg = colors.accent2 },

  StatusLine   = { fg = colors.text, bg = colors.crust },
  StatusLineNC = { fg = colors.subtext, bg = colors.crust },

  VertSplit    = { fg = colors.border, bg = colors.bg },
  WinSeparator = { fg = colors.border, bg = colors.bg },

  Pmenu        = { fg = colors.text, bg = colors.mantle },
  PmenuSel     = { fg = colors.bg, bg = colors.accent },
  PmenuSbar    = { bg = colors.surface },
  PmenuThumb   = { bg = colors.border },

  Directory    = { fg = colors.accent },
  Title        = { fg = colors.accent, bold = true },
  ErrorMsg     = { fg = colors.red, bold = true },
  WarningMsg   = { fg = colors.warning },
  MoreMsg      = { fg = colors.green },
  Question     = { fg = colors.accent },

  NvimTreeNormal       = { fg = colors.text, bg = colors.bg },
  NvimTreeNormalNC     = { fg = colors.text, bg = colors.bg },
  NvimTreeFolderName   = { fg = colors.accent },
  NvimTreeOpenedFolderName = { fg = colors.accent, bold = true },
  NvimTreeRootFolder   = { fg = colors.accent, bold = true },
  NvimTreeWinSeparator = { fg = colors.border, bg = colors.bg },

  CocMenu       = { fg = colors.text, bg = colors.mantle },
  CocMenuSel    = { fg = colors.bg, bg = colors.accent },
  CocFloating   = { fg = colors.text, bg = colors.mantle },
  CocErrorFloat = { fg = colors.red, bg = colors.mantle },
  CocWarningFloat = { fg = colors.warning, bg = colors.mantle },
}

for group, opts in pairs(highlights) do
  vim.api.nvim_set_hl(0, group, opts)
end

local status_ok, lualine = pcall(require, "lualine")
if status_ok then
  local theme = {
    normal = {
      a = { fg = colors.bg, bg = colors.accent, gui = "bold" },
      b = { fg = colors.text, bg = colors.mantle },
      c = { fg = colors.subtext, bg = colors.crust },
    },
    insert = {
      a = { fg = colors.bg, bg = colors.green, gui = "bold" },
      b = { fg = colors.text, bg = colors.mantle },
      c = { fg = colors.subtext, bg = colors.crust },
    },
    visual = {
      a = { fg = colors.bg, bg = colors.accent2, gui = "bold" },
      b = { fg = colors.text, bg = colors.mantle },
      c = { fg = colors.subtext, bg = colors.crust },
    },
    replace = {
      a = { fg = colors.bg, bg = colors.red, gui = "bold" },
      b = { fg = colors.text, bg = colors.mantle },
      c = { fg = colors.subtext, bg = colors.crust },
    },
    command = {
      a = { fg = colors.bg, bg = colors.warning, gui = "bold" },
      b = { fg = colors.text, bg = colors.mantle },
      c = { fg = colors.subtext, bg = colors.crust },
    },
    inactive = {
      a = { fg = colors.subtext, bg = colors.crust },
      b = { fg = colors.subtext, bg = colors.crust },
      c = { fg = colors.subtext, bg = colors.crust },
    },
  }

  lualine.setup({
    options = {
      theme = theme,
      icons_enabled = true,
      component_separators = { left = "│", right = "│" },
      section_separators = { left = "", right = "" },
    }
  })
end

local toggleterm_ok, toggleterm = pcall(require, "toggleterm")
if toggleterm_ok then
  toggleterm.setup({
    dir = vim.fn.getcwd(),
    highlights = {
      Normal = { guibg = colors.bg },
      NormalFloat = { guibg = colors.mantle },
      FloatBorder = { guifg = colors.accent, guibg = colors.mantle },
    },
  })
end

local function toggle_value()
  local word = vim.fn.expand("<cword>")
  local toggles = {
    ["true"] = "false", ["false"] = "true",
    ["True"] = "False", ["False"] = "True",
    ["0"] = "1", ["1"] = "0"
  }
  if toggles[word] then
    vim.cmd("normal! ciw" .. toggles[word])
  end
end

vim.keymap.set("n", "m", toggle_value, { noremap = true, silent = true })
EOF

function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1] =~# '\s'
endfunction

inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"
set updatetime=300
