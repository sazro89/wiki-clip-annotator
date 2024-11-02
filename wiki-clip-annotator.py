#!/usr/bin/python3

import os         # access files and such
import subprocess # use linux utils
# import re         # regex

proc = subprocess.Popen(["ls", "/home/phauzie/Videos/Strive/clips"], stdout=subprocess.PIPE)
out = subprocess.check_output(("fzf"), stdin=proc.stdout)
proc.wait()

# print(re.findall(br"'(.*?)'", out))
out = out[:len(out)-1] # strip \n character
print(out)

# proc = subprocess.Popen(["fzf", clips], stdout=subprocess.PIPE)
# for clip in clips:
#     print(clip)

# how to pipe outputs without using shell=True (good security practice)
# ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
# output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
# ps.wait()