#!/usr/bin/env python3

## create a list of l9ists of your favorite foods by adding three lists togther.
# print the list then print your favorite food item on the list.
favs1 = ["pizza", "pasta"]
favs2 = ["sushi", "burritos"]
favs3 = ["cereal", "steaks"]
favs4 = []
favs4.append(favs1)
favs4.append(favs2)
favs4.append(favs3)
#should print out cereal.. I can eat it for every meal....
print(favs4)
print()
print("my favorite food is :"+favs4[2][0])
print()
#make a disctionary defining three shares quals
#of your favorite fictional heroes!
#print all keys and values seperatly.
super1 = {"name":"thor", "power":"thunder", "funny":True}
 
print(super1.keys(),super1.values())

