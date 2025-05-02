# Use return in function

#! /bin/bash

hello() {
	echo "Haa tu hai... haa tu hai..."
	return 101
}

my_func() {
	local func_result="some_result"
	echo "$func_result"
}

func_result="$(my_func)"
echo $func_result

hello
echo $?
