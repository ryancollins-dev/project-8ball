# Random Project
# Author: R
# Original creation date: 2021-03-03
# Update 2021-03-05
# Version: 3
# 8Ball for my projects
#!/usr/bin/env python3

import random

a = []
with open("8ball.txt", "r") as f:
  a = f.readlines()
print("Your project is:",random.choice(a)),
