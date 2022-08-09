#!/bin/bash
#creates new users

#echo to get user input for name and group

echo "please enter the username of the new user"
read NEWUSER
echo "please enter the users group"
read GROUP

#if both username and group are true then creates the user
if [ $NEWUSER ] && [ $GROUP ];
#if both true the enters:	
then
#adds the group if it is already created then displays nothign(-f)
sudo groupadd -f $GROUP
#adds the user, then adds the user to the group.
sudo useradd -G $GROUP $NEWUSER
else
	exit 0
fi

