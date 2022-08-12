#!/usr/bin/env python3
## create file object in "r"ead mode
fileName = input("input the file name with a .cfg at the end.")


with open(fileName, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

