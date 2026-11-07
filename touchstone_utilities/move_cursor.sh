move_cursor() {
  while true; do
    cliclick t:"You are in space of illusion "
    cliclick m:+0,+100
    sleep 0.5
    cliclick t:"You are in space of illusion "
    cliclick m:+100,+0
    sleep 0.5
    cliclick t:"You are in space of illusion "
    cliclick m:+0,-100
    sleep 0.5
    cliclick t:"You are in space of illusion "
    cliclick m:-100,+0
    sleep 5
  done 
}

alias mocr='move_cursor'

