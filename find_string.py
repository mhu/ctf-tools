#!/usr/bin/env python3

import subprocess
import sys

if len(sys.argv) < 3:
    sys.exit('Expected 3 parameters')

file_to_search = sys.argv[1]
substring = sys.argv[2]

strings = subprocess.run(['strings', file_to_search], capture_output=True, text=True).stdout.split('\n')

for string in strings:
    if string.find(substring) > -1:
        print(string)
