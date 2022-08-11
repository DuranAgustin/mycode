#!/usr/bin/env python3
def main():
    list1 =["cisco_nxos","arista_eoa","cisco_ios"]
    print(list1)
    print(list1[1])
    list2=["juniper"]
    list1.extend(list2) #extends iterates through and appends each index to list
    print(list1)
    
    list3 = ["10.1.0.1","10.2.0.1","10.3.0.1"]
    list1.append(list3) # appends appends the list entirely list(list)
    print(list1)
    print(list1[4])
    print(list1[4][0])

main()
