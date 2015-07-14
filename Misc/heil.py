#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from time import sleep


swastika = '''

        _
       / /\\
      / / /
     / / /   _
    /_/ /   / /\\
    \ \ \  / /  \\
     \ \ \/ / /\ \\
  _   \ \ \/ /\ \ \\
/_/\   \_\  /  \ \ \\
\ \ \  / /  \   \_\/
 \ \ \/ / /\ \\
  \ \ \/ /\ \ \\
   \ \  /  \ \ \\
    \_\/   / / /
          / / /
         /_/ /
         \_\/
'''

swaslines = swastika.split('\n')

while True:
	for line in swaslines:
		print line
		sleep(0.01)