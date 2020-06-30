# =========================
# ====== custom line ======
# =========================

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

# set PATH for composer vendor global tools bin
if [ -d "$HOME/.config/composer/vendor/bin/" ] ; then
    PATH="$HOME/.config/composer/vendor/bin/:$PATH"
fi

# powerline for bash
POWERLINE_SCRIPT=/usr/share/powerline/bindings/bash/powerline.sh
if [ -f $POWERLINE_SCRIPT ]; then
  source $POWERLINE_SCRIPT
fi 

export EDITOR=vim

# ls
alias ls='ls --color=auto'
alias ll='ls -l'
alias la='ls -a'
#alias lla='ls -la'
#alias lh='ll -h'
alias l=ls

# systemctl
alias start='sudo systemctl start'
alias stop='sudo systemctl stop'
alias restart='sudo systemctl restart'
alias status='sudo systemctl status'
alias enable='sudo systemctl enable'
alias disable='sudo systemctl disable'

# df
alias df='df -h'
