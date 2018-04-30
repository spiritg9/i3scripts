#!/bin/bash
string() {
    VOLUME=$(~/.myScripts/volume.py "v")
    echo $VOLUME%
    COLOR=$(~/.myScripts/volume.py "c")
    echo \#$COLOR
    echo \#$COLOR
    keyboard.py mute $COLOR
    keyboard.py volume $VOLUME $COLOR
}

case $BLOCK_BUTTON in
    1) amixer -D pulse sset Master toggle | string ;;  # left click, stop
    4) amixer -D pulse sset Master playback 2%+ | string ;;  # scroll up
    5) amixer -D pulse sset Master playback 2%- | string ;;  # scroll down
    *) string
esac
