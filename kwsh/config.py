# ~/.config/kwsh/config.py

autostart = [
    ""
]

class PS1_settings:
    ps1_mini_shell = {
        "_pwd": {
            "spawn": "pwd",
            "!homedir": "~",
            "color": "0x596070ff"
        },
        "_dollar": {
            "spawn": "echo $",
            "color": "0x8A9FADff"
        },
    }

    PS1 = "[_pwd] [_dollar] "
    PS2 = "> "

class Syntax_lightning_settings:
    syn_correct: str = "0x84916Aff"
    syn_mistake: str = "0xAB8E89ff"
    syn_element_string: str = "0xB0A883ff"
    syn_element_int: str = "0x9C9E9Eff"
    syn_operators: str = "0x8A9FADff"
    syn_tablet: str = "0x596070ff"

aliases: dict[str, str] = {
    "ll": "ls -l",
    "mci": "doas make clean install",
    "brct": "doas brightnessctl set 100%",
    "xi": "doas xbps-install"
}

keys: list[list] = [
    ["CTRL|", "l", "spawn", "clear"],
    ["ALT", "x", "spawn", "fastfetch"],
    ["NONE", "Up", "history", 1],
    ["NONE", "Down", "history", -1],
    ["CTRL", "r", "reload_config", "NONE"],
]
