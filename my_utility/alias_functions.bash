#Kubernetes functions

kubectl_get_cmd() {
	resource=$1
	cmd="kubectl --kubeconfig ${KUBECONFIG} get ${resource}"
	eval "$cmd"
}

kubectl_describe_cmd() {
	resource=$1
	resource_value=$2
	cmd="kubectl --kubeconfig ${KUBECONFIG} describe ${resource} ${resource_value}"
	eval "$cmd"
}

kubectl_get_output_cmd() {
	resource=$1
	resource_value=$2
	output=$3
	cmd="kubectl --kubeconfig ${KUBECONFIG} get ${resource} ${resource_value} -o ${output}"
	eval "$cmd"
}



# Assertion functions

choose_yes_or_no() {
	cmd="$1"
	if [[ "$answer" == "yes" ]]; then
	    echo "You chose to continue."
	    eval "$cmd"
	elif [[ "$answer" == "no" ]]; then
	    echo "You chose not to continue."
	    return 1
	else
	    echo "Invalid input. Please enter yes or no."
	    read -r answer
	    choose_yes_or_no "$cmd"
	fi
}


# Find functions

find_and_move() {
	regex="$1"
	directory="$2"
	if [[ "$1" == "--help" || "$1" == "-h" ]]; then
        	echo "Usage: find_cmd_shortcuts [options] [arguments]"
        	echo ""
        	echo "Options: regex, directory"
        	echo "  --help, -h    This command is to find files based on regex and move all files to specific directory"
      		return
    	fi

	if [ ! -d "$directory" ]; then
      	  echo "Target directory does not exist. Please create it first."
          return 1
    	fi

#	echo "You are inside this directory: $(pwd)"
#	find "$regex"

#	echo "Do you want to move files to directory? (yes/no)"
#	read -r answer
        cmd="find ${regex} -exec mv {} ${directory} \;"   # Find files or directories and move to specific directory
#	choose_yes_or_no ${cmd}
        eval "$cmd"

}


