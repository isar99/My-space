#! /usr/bin/bash

#Pass Arguments to bash scripting
echo $0 $1 $2 $3 ' > echo $1 $2 $3'

#Passing an argument as array 
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}

echo $@
echo $#
