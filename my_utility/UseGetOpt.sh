# file: UseGetOpt-2
# UseGetOpt-2.sh parameter-completion

_UseGetOpt-2 ()
{
  local cur

  COMPREPLY=()
  cur=${COMP_WORDS[COMP_CWORD]}

  case "$cur" in *)

    COMPREPLY=( $( compgen -W '-a -d -f -l -t -h --aoption --debug \
                           --file --isar --ahmad --log --test --help --' -- $cur ));;
  esac
  return 0
}

complete -F _UseGetOpt-2 -o filenames ./UseGetOpt-2.sh
