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

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"

key_left = "h"
key_down = "j"
key_up = "k"
key_right = "l"

terminal = guess_terminal()

keys = [
    # Switch between windows in current stack pane
    Key([mod], key_left, lazy.layout.left(),
        desc="Move focus left in stack pane"),
    Key([mod], key_down, lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], key_up, lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], key_right, lazy.layout.right(),
        desc="Move focus right in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "shift"], key_left, lazy.layout.shuffle_left(),
        desc="Move window left in current stack "),
    Key([mod, "shift"], key_down, lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], key_up, lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod, "shift"], key_right, lazy.layout.shuffle_right(),
        desc="Move window right in current stack "),

    # Toggle screen
    Key([mod], "o",
        lazy.to_screen(0)),
    Key([mod], "p",
        lazy.to_screen(1)),

    # Switch window focus to other pane(s) of stack
    # Key([mod], "space", lazy.layout.next(),
    #     desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    # Key([mod, "shift"], "space", lazy.layout.rotate(),
    #     desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    #Key([mod], "r", lazy.spawncmd(),
    #    desc="Spawn a command using a prompt widget"),

    # Rofi
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
]

group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("MUS", {'layout': 'monadtall'}),
               ("VID", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen(toggle=False)))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [["#292d3e", "#292d3e"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

#prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
#             widget.Sep(
#                      linewidth = 0,
#                      padding = 6,
#                      foreground = colors[2],
#                      background = colors[0]
#                      ),
#             widget.Image(
#                      filename = "~/.config/qtile/icons/python.png",
#                      mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('dmenu_run')}
#                      ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
#             widget.Prompt(
#                      prompt = prompt,
#                      font = "Ubuntu Mono",
#                      padding = 10,
#                      foreground = colors[3],
#                      background = colors[1]
#                      ),
#             widget.Sep(
#                      linewidth = 0,
#                      padding = 40,
#                      foreground = colors[2],
#                      background = colors[0]
#                      ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.TextBox(
                       text = " 🌡",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 11
                       ),
#             widget.ThermalSensor(
#                      foreground = colors[2],
#                      background = colors[5],
#                      threshold = 90,
#                      padding = 5
#                      ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14
                       ),
#             widget.Pacman(
#                      update_interval = 1800,
#                      foreground = colors[2],
#                      mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
#                      background = colors[4]
#                      ),
#             widget.TextBox(
#                      text = "Updates",
#                      padding = 5,
#                      mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
#                      foreground = colors[2],
#                      background = colors[4]
#                      ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
#             widget.Memory(
#                      foreground = colors[2],
#                      background = colors[5],
#                      mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e htop')},
#                      padding = 5
#                      ),
#             widget.Net(
#                      interface = "enp6s0",
#                      format = '{down} ↓↑ {up}',
#                      foreground = colors[2],
#                      background = colors[4],
#                      padding = 5
#                      ),
              widget.TextBox(
                      text = " Vol:",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0
                       ),
#             widget.Volume(
#                      foreground = colors[2],
#                      background = colors[5],
#                      padding = 5
#                      ),
#             widget.CurrentLayoutIcon(
#                      custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
#                      foreground = colors[0],
#                      background = colors[4],
#                      padding = 0,
#                      scale = 0.7
#                      ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[5],
                       format = "%A, %B %d  [ %H:%M ]"
                       ),
#             widget.Sep(
#                      linewidth = 0,
#                      padding = 10,
#                      foreground = colors[0],
#                      background = colors[5]
#                      ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

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
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
