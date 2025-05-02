#! /usr/bin/bash

# if [condition]
# then 
#  statement
# fi

#count=10 

#if (($count >= 9 ))
#then
#  echo "condition is true"
#fi

#word=abc
#if [ $word == abc ]
#then
#  echo "condition is true"
#fi

word=a
if [[ $word == ab ]]
then
  echo "condition b is true"
elif [[ $word == "a" ]]
then 
  echo "condition a is true"
else
  echo "condition is false"
fi

