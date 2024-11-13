#!/usr/bin/python3

import os         # access files and such
import subprocess 
# import re         # regex

from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()

clips_path = "/home/phauzie/Videos/Strive/clips/"

main_prompt = [
    '3) Exit',
    '2) Settings',
    '1) Process Clip',
    'WCA'
]

def main_menu():
    selection = fzf.prompt(main_prompt, '--no-sort --cycle')
    if main_prompt[3] in selection[0]:
        main_menu()
    elif main_prompt[2] in selection[0]:
        clip = select_clip(clips_path)
        process_clip(clip)
        main_menu()
    elif main_prompt[1] in selection[0]:
        settings()
    elif main_prompt[0] in selection[0]:
        exit()

def select_clip(path):
    files = os.listdir(path)
    files = [f for f in files if os.path.isfile(path+'/'+f)]
    result = fzf.prompt(files, '--cycle')
    return result

def process_clip(clip):
    # avidemux3_qt5 --load Replay_2024-11-09_02-52-10.mp4 --run ~/.avidemux6/custom/wiki_clip.py
    # need to look up string concatenation in python
    # also need to run this program
    # also need to make a note in zk open so that would be a new kitty window
    # subprocess.run(["avidemux3_qt5", "--load", clip, "--run", "~/.avidemux6/custom/wiki_clip.py"])
    subprocess.Popen(["avidemux3_qt5", "--load", clips_path + clip[0], "--run", "/home/phauzie/.avidemux6/custom/wiki_clip.py"])

main_menu()

# files = os.listdir(path)


# files = [f for f in files if os.path.isfile(path+'/'+f)]

# any array that can be displayed as text can work for the first field
# second field is fzf options
# prompt returns all values in an array
# result = fzf.prompt(files, '--cycle')

# print(result)


# menu
# 1) Process Clip
#   1) Open up the clip in a floating avidemux with a wiki fast decode preset
#       - should also point to an export directory
#       - should also trash the file (avidemux loads this all into memory)
#       - the timestamp of the zk prompt should be copied to the clipboard
#       - paste the timestamp as a default title
#   2) Open up a new zk prompt for the clip alongside it
#       - use a md embed for video linking to the clip just rendered
#       - point out useful info, questions, and tag the clip
#   3) If possible, that directory they go into should be in the cloud somehow
#       - ask mara about tailscale
#       - that's out of the scope of this but files should go into a special folder
# 2) Settings
#   - set scan directory
#   - set encode presets
#   - set output directory (this might not be needed we could just manually shift)
#       - less automation is less prone to breaking and it's not that bad of a step
#   - exit
# 3) Exit
