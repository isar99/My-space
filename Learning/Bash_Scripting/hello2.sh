#! /usr/bin/bash

#Taking input from user
echo "Enter name : "
read name 
echo "$name is playing right now" 

#Taking multiple input from user
echo "Enter three names : "
read name1 name2 name3 
echo "first Name : $name1, second name : $name2, third name = $name3"

#Taking input in same line 
read -p 'username : ' user_var
echo "username : $user_var"

#Taking input in same line but with hidden input
read -p "username : " user_var
read -sp "password : " pass_var
echo
echo "Your user name is $user_var"
echo "Your password is $pass_var"

#Entering names in array and calling using indexing
read -pa "Enter array of names: " names
echo "Names : ${names[0]}, ${names[4]}"

#If you are not passing any variables to read command, than by default it will take $REPLY variables
echo " Enter names : "
read
echo " Names : $REPLY"
