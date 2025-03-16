#! /bin/bash

var1='A'
var2='B'

alpha() {
	local var1='D'
	var2='E'

	echo "Inside function VAR1:$var1, VAR2:$var2"
}

echo "Before function VAR1:$var1, VAR2:$var2"

alpha

echo "After function VAR1:$var1, VAR2:$var2"
