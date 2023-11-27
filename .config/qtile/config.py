# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


def powerline(bg :str, fg :str):
    return widget.TextBox(
        text="",
        background=bg,
        foreground=fg,
        padding=-0.5,
        fontsize=30
    ),

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Kitty
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    # Rofi
    Key(["mod1"], "Space", lazy.spawn("rofi -show run")),
    # Key(["control"], "Space", lazy.spawn("rofi -show")),
    # PcmanFM
    Key([mod], "e", lazy.spawn("pcmanfm")),
    # Firefox
    Key([mod], "b", lazy.spawn("brave")),
    # Notion
    Key([mod], "n", lazy.spawn("obsidian")),
    # VSCode
    Key([mod], "c", lazy.spawn("code")),
    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 5000")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),
    # Spotify
    Key([mod], "s", lazy.spawn("spotify-launcher")),
    # Bitwarden
    Key([mod], "p", lazy.spawn("bitwarden-desktop")),

    #Volumen
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),

    # Brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "z", lazy.window.toggle_fullscreen()),
]

groups = [Group(i) for i in "󱞁"]

for i, group in enumerate(groups):
    actual_key = str(i+1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
layouts = [
    
    # layout.Columns(border_focus="#9c4dcc", border_normal="#000"), 
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    layout.MonadTall(border_focus="#9c4dcc", border_width=2),
    layout.MonadWide(border_focus="#9c4dcc", border_width=2),
    #layout.Stack(num_stacks=2),
    #layout.Matrix(border_focus="#9c4dcc", border_width=2),
    layout.TreeTab(),
    layout.Max(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()

### WIDGETS ###

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.GroupBox(background="#06000f", active="9c4dcc", fontsize=19, borderwidth=0, padding_x=8, highlight_method="block"),
                widget.WindowName(background="#06000f", font="Hack Nerd Font", foreground="#9c4dcc", max_chars=150),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.CheckUpdates(
                    no_update_string="  0",
                    update_interval=2700,
                    font="Hack Nerd Font", fontsize=14,
                    colour_no_updates="#9c4dcc",
                    colour_have_updates="#9c4dcc",
                    display_format='  {updates}',
                    padding=10,
                    distro="Arch_checkupdates",
                ),
                widget.TextBox(
                        text="",
                        background="#000",
                        foreground="#A27EBB",
                        padding=-5,
                        fontsize=40,
                ),
                widget.Net(background="#A27EBB", format=" {down} ↓↑{up}'"),

                widget.TextBox(
                        text="",
                        background="#A27EBB",
                        foreground="#65499c",
                        padding=-5,
                        fontsize=40,
                ),

                widget.CurrentLayoutIcon(background="#65499c", scale=0.55, padding=0),
                widget.CurrentLayout(background="#65499c", padding=5),

                widget.TextBox(
                        text="",
                        background="#65499c",
                        foreground="#9c4dcc",
                        padding=-5,
                        fontsize=40,
                ),

                widget.Clock(background="#9c4dcc", format="%A, %B %d - %H:%M"),

                widget.TextBox(
                        text="",
                        background="#9c4dcc",
                        foreground="#A27EFE",
                        padding=-5,
                        fontsize=40,
                ),

                widget.Systray(background="#A27EFE", padding=5),

            ],
            25,
            background="#06000f",
            opacity=0,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        #Match(title="Microsoft Teams"),

    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
