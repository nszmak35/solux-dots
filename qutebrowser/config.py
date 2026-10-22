config.load_autoconfig(False)

background = "#14171D"
surface    = "#1C2027"
surface2   = "#2A2F38"

text       = "#D2D3CE"
subtext    = "#9C9E9E"

accent     = "#8A9FAD"
accent2    = "#B0A883"
border     = "#596070"

red        = "#AB8E89"
green      = "#84916A"
yellow     = "#B0A883"

c.statusbar.padding = {
    "top": 8,
    "bottom": 8,
    "left": 10,
    "right": 10,
}

c.fonts.statusbar = "11pt default_family"

c.tabs.padding = {
    "top": 8,
    "bottom": 8,
    "left": 10,
    "right": 10,
}

c.fonts.tabs.selected = "11pt default_family"
c.fonts.tabs.unselected = "11pt default_family"

c.tabs.indicator.padding = {
    "top": 4,
    "bottom": 4,
    "left": 2,
    "right": 2,
}

c.tabs.indicator.width = 4

c.tabs.favicons.scale = 1.15

c.url.searchengines = {
    "DEFAULT": "https://search.brave.com/search?q={}",
}

c.url.start_pages = [
    "https://search.brave.com/"
]

c.url.default_page = "https://search.brave.com/"

c.colors.completion.fg = text

c.colors.completion.odd.bg = surface
c.colors.completion.even.bg = background

c.colors.completion.category.fg = accent
c.colors.completion.category.bg = surface
c.colors.completion.category.border.top = border
c.colors.completion.category.border.bottom = border

c.colors.completion.item.selected.fg = background
c.colors.completion.item.selected.bg = accent
c.colors.completion.item.selected.border.top = accent
c.colors.completion.item.selected.border.bottom = accent

c.colors.completion.match.fg = accent2

c.colors.completion.scrollbar.bg = background
c.colors.completion.scrollbar.fg = surface2

c.colors.statusbar.normal.bg = background
c.colors.statusbar.normal.fg = text

c.colors.statusbar.insert.bg = accent
c.colors.statusbar.insert.fg = background

c.colors.statusbar.command.bg = surface
c.colors.statusbar.command.fg = text

c.colors.statusbar.caret.bg = accent2
c.colors.statusbar.caret.fg = background

c.colors.statusbar.progress.bg = accent

c.colors.statusbar.url.fg = text
c.colors.statusbar.url.success.http.fg = green
c.colors.statusbar.url.success.https.fg = green
c.colors.statusbar.url.warn.fg = yellow
c.colors.statusbar.url.error.fg = red
c.colors.statusbar.url.hover.fg = accent

c.colors.tabs.bar.bg = background

c.colors.tabs.odd.bg = background
c.colors.tabs.odd.fg = text

c.colors.tabs.even.bg = background
c.colors.tabs.even.fg = text

c.colors.tabs.selected.odd.bg = surface
c.colors.tabs.selected.odd.fg = accent

c.colors.tabs.selected.even.bg = surface
c.colors.tabs.selected.even.fg = accent

c.colors.tabs.indicator.start = accent
c.colors.tabs.indicator.stop = accent2
c.colors.tabs.indicator.error = red
c.colors.tabs.indicator.system = "rgb"

c.colors.tabs.pinned.even.bg = surface
c.colors.tabs.pinned.even.fg = accent

c.colors.tabs.pinned.odd.bg = surface
c.colors.tabs.pinned.odd.fg = accent

c.colors.downloads.bar.bg = background

c.colors.downloads.start.bg = accent
c.colors.downloads.start.fg = background

c.colors.downloads.stop.bg = green
c.colors.downloads.stop.fg = background

c.colors.downloads.error.bg = red
c.colors.downloads.error.fg = text

c.colors.downloads.system.bg = "none"
c.colors.downloads.system.fg = "none"

config.bind("q", "tab-close")
config.bind("w", "undo")

c.colors.hints.bg = accent
c.colors.hints.fg = background
c.colors.hints.match.fg = red

c.colors.messages.info.bg = surface
c.colors.messages.info.fg = text
c.colors.messages.info.border = border

c.colors.messages.warning.bg = yellow
c.colors.messages.warning.fg = background
c.colors.messages.warning.border = border

c.colors.messages.error.bg = red
c.colors.messages.error.fg = text
c.colors.messages.error.border = border

c.colors.prompts.bg = surface
c.colors.prompts.fg = text
c.colors.prompts.border = border

c.colors.prompts.selected.bg = accent
c.colors.prompts.selected.fg = background

c.colors.contextmenu.menu.bg = surface
c.colors.contextmenu.menu.fg = text

c.colors.contextmenu.disabled.bg = background
c.colors.contextmenu.disabled.fg = subtext

c.colors.contextmenu.selected.bg = accent
c.colors.contextmenu.selected.fg = background

c.colors.keyhint.bg = surface
c.colors.keyhint.fg = text
c.colors.keyhint.suffix.fg = accent

c.colors.tooltip.bg = surface
c.colors.tooltip.fg = text

c.colors.webpage.bg = background

c.colors.webpage.preferred_color_scheme = "dark"
