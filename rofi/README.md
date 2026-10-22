# rofi

Configuration for [rofi](https://github.com/davatorium/rofi), an application launcher and window switcher.

- `theme.rasi` - Tre Cime color variables.
- `we.rasi.d` - the launcher layout and options (modes `run`, `drun`, `window`, icons, two-column list). It imports `theme.rasi` and is used by waybar via `rofi -show drun -theme ~/.config/rofi/we.rasi.d`.

## Origin

The layout is a fork of the rofi config from **Zproger/bspwm-dotfiles**:
https://github.com/Zproger/bspwm-dotfiles/tree/main/config/rofi

The upstream folder contains `catppuccin.rasi` (colors) and `config.rasi` (layout). Here the colors were replaced with the Tre Cime palette in `theme.rasi`, and the layout was adapted in `we.rasi.d`.

## Font

These configs use **Libertinus Mono**, part of the [Libertinus](https://github.com/alerque/libertinus) font family by Khaled Hosny and contributors (maintained by Caleb Maclennan), licensed under the SIL Open Font License 1.1. Releases: https://github.com/alerque/libertinus/releases

Rofi uses it as `Libertinus Mono 14`.
