#!/usr/bin/env python3

ipchk = input("Insert ip:")

if ipchk == "192.168.70.1":
    print("ip address is "+ipchk)
elif ipchk:
    print("Ip is now: "+ ipchk)
else: 
    print("you didn't provide anything")

