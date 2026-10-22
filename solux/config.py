# Default Solux configuration in Python.
# Edit ~/.config/solux/config.py to override these values.

import random

terminal = "foot"
corner_radius = 0

class Appearance:
    sloppyfocus = True
    bypass_surface_visibility = False
    borderpx = 0
    rootcolor = "0x101B20ff"
    fullscreen_bg = [0.0, 0.0, 0.0, 1.0]
    scenefx_opacity_inactive = 1.0
    scenefx_opacity_active = 1.0
    scenefx_shadow = False
    scenefx_shadow_only_floating = False
    scenefx_shadow_color = "0x00000080"
    scenefx_shadow_color_focus = "0x000000b0"
    scenefx_shadow_blur_sigma = 20
    scenefx_shadow_blur_sigma_focus = 30
    scenefx_corner_radius = corner_radius
    scenefx_corner_radius_inner = corner_radius
    scenefx_corner_radius_only_floating = False

class Blur:
    blur = True
    blur_xray = False
    blur_ignore_transparent = True
    blur_radius = 10
    blur_num_passes = 3
    blur_noise = 0.02
    blur_brightness = 0.90
    blur_contrast = 0.90
    blur_saturation = 1.10

n = 120

type_animation = "zoom"

class Animations:
    animations = True
    animation_type_open = type_animation
    animation_type_close = type_animation
    animation_fade_in = True
    animation_fade_out = True
    tag_animation_direction = "horizontal"
    zoom_initial_ratio = 0.20
    zoom_end_ratio = 0.80
    fadein_begin_opacity = 0.50
    fadeout_begin_opacity = 0.50
    animation_duration_move = 380 + n
    animation_duration_open = 380+n
    animation_duration_tag = 380+n
    animation_duration_close = 380+n
    animation_duration_focus = 0
    animation_curve_move = [0.0,0.0,0.2,1.0]
    animation_curve_open = [0.0, 0.0, 0.2, 1.0]
    animation_curve_tag = [0.0, 0.0, 0.2, 1.0]
    animation_curve_close = [0.4, 0.0, 1.0, 1.0]
    animation_curve_focus = [0.46,1.0,0.29,1]
    animation_curve_opafadein = [0.5,0.5,0.5,0.5]
    animation_curve_opafadeout = [0.0,0.0,0.2,1.0]

class Gaps:
    gappx = 10
    smartgaps = False
    gaps = True

class Border_Details:
    urgentcolor = "0xB0A883ff"
    bordercolor = "0x596070ff"
    focuscolor = "0x8A9FADff"
    borderspx = 3
    borderepx = 2
    borderspx_offset = 2
    borderepx_negative_offset = 0
    borderscolor = "0x2A2F38ff"
    borderecolor = "0x1C2027ff"
    borders_focuscolor = "0x8A9FADff"
    borders_urgentcolor = "0xB0A883ff"
    bordere_focuscolor = "0x1C2027ff"
    bordere_urgentcolor = "0x1C2027ff"
    border_color_type = "BrdStartEnd"
    borders_only_floating = False

class Input:
    modkey = "super"
    keyboard_layout = "us,ru"
    keyboard_options = "grp:win_space_toggle"
    repeat_rate = 25
    repeat_delay = 600
    tap_to_click = True
    tap_and_drag = True
    drag_lock = True
    natural_scrolling = False
    disable_while_typing = True
    left_handed = False
    middle_button_emulation = False
    scroll_method = "LIBINPUT_CONFIG_SCROLL_2FG"
    click_method = "LIBINPUT_CONFIG_CLICK_METHOD_BUTTON_AREAS"
    send_events_mode = "LIBINPUT_CONFIG_SEND_EVENTS_ENABLED"
    accel_profile = "LIBINPUT_CONFIG_ACCEL_PROFILE_ADAPTIVE"
    accel_speed = 0.0
    button_map = "LIBINPUT_CONFIG_TAP_MAP_LRM"
    swipe_min_threshold = 20

class Dwindle_Settings:
    dwindle_type = "dwindle"
    dwindle_attach = False
    dwindle_mirror = False
    dwindle_mouse_client = True

tags = 9

autostart = [
    "pipewire",
    "pipewire-pulse",
    "wireplumber",
    "wl-copy",
    "swaybg -i /home/nszmak/wey.jpg",
    "mako",
    "dbus-update-activation-environment --all",
    "pkill -q xdg-desktop-portal",
    "pkill -q xdg-desktop-portal-wlr",
    "/usr/libexec/xdg-desktop-portal-wlr",
    "/usr/libexec/xdg-desktop-portal",
    "waybar -c /home/nszmak/solux/waybar/config.jsonc -s /home/nszmak/solux/waybar/style-5.css",
]

rules = [
    {"appid": "Gimp_EXAMPLE", "workspace": 0, "floating": True, "fullscreen": False, "monitor": -1}
]

r = 1/random.randint(1, 5)

monrules = [
    [None, 0.5, 1, 1.0, "float", "WL_OUTPUT_TRANSFORM_NORMAL", -1, -1],
]

layouts = {
    "dwindle": "dwindle",
    "float": "float",
    "monocle": "monocle"
}

gestures = [
    ["SWIPE", "left", 3, "cycletag", -1, "int"],
    ["SWIPE", "right", 3, "cycletag", 1, "int"],
    ["SWIPE", "left", 4, "focusstack", -1, "ui"],
    ["SWIPE", "right", 4, "focusstack", 1, "int"],
    ["SWIPE", "up", 4, "swapdir", 2, "ui"],
    ["SWIPE", "down", 4, "swapdir", 3, "ui"],
    ["TZOOM", "out", 3, "zoomcanvas", -1],
    ["TZOOM", "in", 3, "zoomcanvas", 1],
    ["SWIPE", "up", 3, "spawn", "rofi -show window -window-thumbnail -show-icons -theme ~/.config/rofi/we.rasi.d"]
]

if Gaps.gappx > 10:
    Border_Details.borderspx = 2
    Border_Details.borderepx = 2
    Border_Details.borderspx_offset = 2

keys = [
    ["MODKEY", "r", "spawn", "rofi -show window -window-thumbnail -show-icons -theme ~/.config/rofi/we.rasi.d"],
    ["MODKEY|SHIFT", "e", "spawn", "dolphin"],
    ["MODKEY|SHIFT", "t", "spawn", "foot -L bash"],
    ["MODKEY", "e", "spawn", "nemo"],
    ["MODKEY", "t", "spawn", terminal],
    ["MODKEY", "p", "spawn", "xeyes"],
    ["MODKEY", "b", "spawn", "qutebrowser"],
    ["MODKEY|SHIFT", "b", "spawn", "chromium"],
    ["MODKEY|SHIFT", "Left", "movecanvas", 0, "ui"],
    ["MODKEY|SHIFT", "Right", "movecanvas", 1, "ui"],
    ["MODKEY|SHIFT", "Up", "movecanvas", 2, "ui"],
    ["MODKEY|SHIFT", "Down", "movecanvas", 3, "ui"],
    ["MODKEY|SHIFT", "equal", "zoomcanvas", 1, "int"],
    ["MODKEY|SHIFT", "minus", "zoomcanvas", -1, "Int"],
    ["MODKEY|SHIFT", "e", "spawn", "dolphin"],
    ["MODKEY", "y", "spawn", "pkill -SIGUSR2 waybar"],
    ["MODKEY", "w", "reload_config"],
    ["MODKEY", "f", "togglefloating", "NONE"],
    ["MODKEY", "End", "spawn", "loginctl suspend"],
    ["MODKEY", "Print", "spawn", "flameshot gui"],
    ["MODNONE", "Print", "spawn", "python /home/nszmak/solux/screen.py"],
    ["MODKEY|CTRL", "Left", "swapdir", 0, "ui"],
    ["MODKEY|CTRL", "Right", "swapdir", 1, "ui"],
    ["MODKEY|CTRL", "Up", "swapdir", 2, "ui"],
    ["MODKEY|CTRL", "Down", "swapdir", 3, "ui"],
    ["MODKEY", "Left", "focusdir", 0, "ui"],
    ["MODKEY", "Right", "focusdir", 1, "ui"],
    ["MODKEY", "Up", "focusdir", 2, "ui"],
    ["MODKEY", "Down", "focusdir", 3, "ui"],
    ["MODKEY|CTRL", "h", "swapdir", 0, "ui"],
    ["MODKEY|CTRL", "l", "swapdir", 1, "ui"],
    ["MODKEY|CTRL", "k", "swapdir", 2, "ui"],
    ["MODKEY|SHIFT", "equal", "zoomcanvas", 1, "int"],
    ["MODKEY|CTRL", "j", "swapdir", 3, "ui"],
    ["MODKEY", "j", "focusstack", 1, "int"],
    ["MODKEY", "k", "focusstack", -1, "int"],
    ["MODKEY", "i", "incnmaster", 1, "int"],
    ["MODKEY", "d", "incnmaster", -1, "int"],
    ["MODKEY", "g", "togglegaps", "NONE"],
    ["MODKEY|SHIFT", "h", "setmfact", -0.05, "float"],
    ["MODKEY|SHIFT", "l", "setmfact", 0.05, "float"],
    ["MODKEY", "Return", "zoom", "NONE"],
    ["MODKEY", "Tab", "view", 0, "ui"],
    ["MODKEY", "q", "killclient", "NONE"],
    ["MODKEY", "z", "cyclelayout", 1, "int"],
    ["MODKEY", "x", "spawn", "soluxctl set-layout '[ monocle ]'"],
    ["MODKEY|SHIFT", "z", "cyclelayout", -1, "int"],
    ["MODKEY|CTRL", "k", "setopacityunfocus", 0.1, "float"],
    ["MODKEY|CTRL", "j", "setopacityunfocus", -0.1, "float"],
    ["MODKEY|CTRL|SHIFT", "K", "setopacityfocus", 0.1, "float"],
    ["MODKEY|CTRL|SHIFT", "J", "setopacityfocus", -0.1, "float"],
    ["MODKEY|CTRL", "f", "togglefullscreen", "NONE"],
    ["MODKEY", "0", "view", "ALL", "ui"],
    ["MODKEY|SHIFT", "parenright", "tag", "ALL", "ui"],
    ["MODKEY", "comma", "focusmon", -1, "int"],
    ["MODKEY", "period", "focusmon", 1, "int"],
    ["MODKEY|SHIFT", "less", "tagmon", -1, "int"],
    ["MODKEY|SHIFT", "greater", "tagmon", 1, "int"],
    ["MODKEY|CTRL", "q", "quit", "NONE"],
    ["CTRL|ALT", "Terminate_Server", "quit", "NONE"],
]

for vt in range(1, 13):
    keys.append(["CTRL|ALT", f"XF86Switch_VT_{vt}", "chvt", vt, "ui"])

# Tag bindings: the same semantics as the original TAGKEYS definitions.
for i in range(1, 10):
    mask = 1 << (i - 1)
    keys.extend([
        ["MODKEY", str(i), "view", mask, "ui"],
        ["MODKEY|CTRL", str(i), "toggleview", mask, "ui"],
        ["MODKEY|SHIFT", ["exclam", "at", "numbersign", "dollar", "percent", "asciicircum", "ampersand", "asterisk", "parenleft"][i-1], "tag", mask, "ui"],
        ["MODKEY|CTRL|SHIFT", ["exclam", "at", "numbersign", "dollar", "percent", "asciicircum", "ampersand", "asterisk", "parenleft"][i-1], "toggletag", mask, "ui"],
    ])

buttons = [
    ["ClkClient", "MODKEY", "BTN_LEFT", "moveresize", 2],
    ["ClkClient", "MODKEY", "BTN_RIGHT", "moveresize", 3],
    ["ClkClient", "MODKEY|SHIFT", "SCROLL_UP", "focusstack", 1, "int"],
    ["ClkClient", "MODKEY|SHIFT", "SCROLL_DOWN", "focusstack", -1, "int"],
    ["ClkClient", "MODKEY", "SCROLL_UP", "cycletag", -1, "int"],
    ["ClkClient", "MODKEY", "SCROLL_DOWN", "cycletag", 1, "int"],
    ["ClkClient", "MODKEY|CTRL", "SCROLL_DOWN", "zoomcanvas", -1],
    ["ClkClient", "MODKEY|CTRL", "SCROLL_UP", "zoomcanvas", 1],
    ["ClkClient", "MODKEY|SHIFT", "BTN_LEFT", "canvasdrag", 0],
    ["ClkRoot", "MODKEY|SHIFT", "BTN_LEFT", "canvasdrag", 0],
]
