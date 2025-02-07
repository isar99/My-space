source ~/Documents/my_github/alias_functions

# Kubectl aliases

alias kgn='kubectl_get_cmd "nodes"'
alias kgp='kubectl_get_cmd "pods"'
alias kgnad='kubectl_get_cmd "net-attach-def"'
alias kgs='kubectl_get_cmd "services"'
alias kgsc='kubectl_get_cmd "sc"'
alias kgpv='kubectl_get_cmd "pv"'

alias kdn='kubectl_describe_cmd "node"'
alias kdp='kubectl_describe_cmd "pod"'
alias kdnad='kubectl_describe_cmd "net-attach-def"'
alias kds='kubectl_describe_cmd "service"'
alias kdsc='kubectl_describe_cmd "sc"'
alias kdpv='kubectl_describe_cmd "pv"'

alias kgno='kubectl_get_output_cmd "node"'
alias kgpo='kubectl_get_output_cmd "pod"'
alias kgnado='kubectl_get_output_cmd "net-attach-def"'
alias kgso='kubectl_get_output_cmd "service"'
alias kgsco='kubectl_get_output_cmd "sc"'
alias kgpvo='kubectl_get_output_cmd "pv"'


# Utility aliases

alias fm="find_and_move"
alias lst="ls -t" #Sorting ls with modified time

