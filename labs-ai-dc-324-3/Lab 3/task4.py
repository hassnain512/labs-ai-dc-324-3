# Write a Python program to construct the following pattern, using a nested for loop.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

for i in range(1 ,5+1):
    for j in range(i):
     print("*", end=" ")
    print()
for i in range(5-1 ,0,-1):
    for j in range(i):
     print("*", end=" ")
    print()


    