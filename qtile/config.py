import os
import subprocess
from libqtile import hook

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
colorBarra ="#282a36"
tamano_barra = 24
fuente_preterminada = "Ubuntu Mono Nerd Font"
tamano_fuente = 16
tamano_iconos = 22
color_inactivo = "#6272a4"
color_oscuro = "#44475a"
color_claro = "#bd93f9"
color_urgent = "#ff5555"
color_texto1 = "#bd93f9"
color_bg = "#282a36"
color_fg = "#ffffff"
color_grupo1 = "#bd93f9"
color_grupo2 = "#6495ed" #ab47bc
color_actualizaciones = "#ffffff"
dispositivo_red = "enp4s0"
color_grupo3 = "bd93f9"
color_grupo4 = "#6495ed"#8E24AA
color_grupo5 = "#bd93f9"

# Funciones
def fc_separador(uColor):
    return widget.Sep(
        linewidth = 0,
        padding = 5,
        foreground = color_fg,
        background = uColor
    )

def fc_powerline(vColor, bColor):
    return widget.TextBox(
        text = "",
        fontsize = 37,
        foreground = vColor,
        background = bColor,
        padding = -3
    )

def fc_icono(icono,color_grupo):
    return widget.TextBox(
        text = icono,
        foreground = color_fg,
        background = color_grupo,
        fontsize = tamano_iconos
    )



keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("vivaldi-stable")),

    # File Explorer
    ([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot 'screenshot_%Y-%m-%d-%T_$wx$h.png' -e 'mv $f ~/screenshots/'")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s 'screenshot_%Y-%m-%d-%T_$wx$h.png' -e 'mv $f ~/screenshots/'")),
    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
]]

# Listado iconos
# 1- nf-dev-chrome
# 2- nf-dev-rust
# 3- nf-dev-terminal
# 4- nf-fa-code
# 5- nf-dev-git
# 6- nf-mdi-image
# 7- nf-fa-spotify

groups = [Group(i) for i in [ 
    "  ","  ","  "," ","  ","  "," "
]]

for i, group in enumerate(groups):
    numeroEscritorio =str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], numeroEscritorio, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], numeroEscritorio, lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Max(),
    layout.MonadTall(
        border_focus = "#bd93f9",
        border_width = 2,
        margin = 4
    ),
    layout.MonadWide(
        border_focus = "#bd93f9",
        border_width = 2,
        margin = 4
    ),
    layout.Bsp(
        border_focus = "#bd93f9",
        border_width = 2,
        margin = 4
    ),
    layout.Matrix(
        columns = 2,
        border_focus = "#bd93f9",
        border_width = 2,
        margin = 4
    ),
    layout.RatioTile(
        border_focus = "#bd93f9",
        border_width = 2,
        margin = 4
    ),
    # layout.Columns(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=fuente_preterminada,
    fontsize=tamano_fuente,
    padding= 3
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active="#ffffff",
                    border_width = 1,
                    disable_drag = True,
                    fontsize = 22,
                    foreground ="#ffffff",
                    highlight_method = "block",
                    margin_x = 0,
                    margin_y = 5,
                    other_current_screen_border = color_oscuro,
                    other_screen_border = color_oscuro,
                    padding_x = 0,
                    padding_y = 10,
                    this_current_screen_border = color_claro,
                    this_screen_border = color_claro,
                    urgent_alert_method = 'block',
                    urgent_border = color_urgent
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 12,
                    foreground = color_fg,
                    background = color_bg
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground = color_texto1,
                    background = color_bg
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 3,
                    foreground = color_fg,
                    background = color_bg
                ),
                # Inicio del Grupo 1
                #fc_rectangulo(color_grupo1, 0),
                #fc_icono("", color_grupo1),
                #widget.ThermalSensor(
                    #foreground = color_fg,
                    #background = color_grupo1,
                    #threshold = 50,
                    #tag_sensor = "Tdie",
                    #fmt = 'T1:{}'
                #),
                #widget.ThermalSensor(
                    #foreground = color_fg,
                    #background = color_grupo1,
                    #threshold = 50,
                    #tag_sensor = "edge",
                    #fmt = 'T2:{}'
                #),
                #fc_icono("  ", color_grupo1),
                #widget.Memory(
                    #foreground = color_fg,
                    #background = color_grupo1
                #),
                # Iconos
                widget.TextBox(
                    text = "",
                    background = colorBarra,
                    foreground = colorBarra,
                    padding = -3,
                    fontsize = 37
                ),
                widget.Systray(
                    icon_size = tamano_iconos,
                    background = colorBarra,
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = color_fg,
                    background = color_bg
                ),
                # Grupo 1
                widget.TextBox(
                    text = "",
                    background = colorBarra,
                    foreground = color_grupo1,
                    padding = -3,
                    fontsize = 37
                ),
                fc_icono(" 龍", color_grupo1),
                widget.Net(
                    foreground = color_fg,
                    background = color_grupo1,
                    format = '{down}   {up}',
                    interface = dispositivo_red,
                    use_bits = True
                ),
                # Grupo 2
                fc_separador(color_grupo1),
                fc_powerline(color_grupo2, color_grupo1),
                widget.CurrentLayoutIcon(
                    background = color_grupo2,
                    scale = 0.7
                ),
                widget.CurrentLayout(
                    background = color_grupo2
                ),
                # Grupo 3
                fc_powerline(color_grupo3, color_grupo2),
                fc_icono("  ", color_grupo3),
                widget.PulseVolume(
                    foreground = color_fg,
                    background = color_grupo3,
                    limit_max_volume = True,
                    fontsize = tamano_fuente
                ),
                fc_icono("  ", color_grupo3),
                widget.CheckUpdates(
                    background = color_grupo3,
                    colour_have_updates = color_actualizaciones,
                    colour_no_updates = color_fg,
                    no_update_string = '0',
                    display_format = 'Updates: {updates}',
                    update_interval = 1800,
                    distro = 'Arch_checkupdates'
                ),
                # Grupo 4
                fc_separador(color_grupo3),
                fc_powerline(color_grupo4, color_grupo3),
                widget.Clock(
                    background = color_grupo4,
                    foreground = color_fg,
                    format = "%A, %B %d - %H:%M"
                ),
                fc_separador(color_grupo4),
            ],
            tamano_barra,
            background=colorBarra
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
])
auto_fullscreen = True
auto_minimize = True
reconfigure_screens = True
focus_on_window_activation = "smart"
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
