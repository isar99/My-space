RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'


sync_repos() {
  local repos=(
    "touchstone-agent-webservice"
    "touchstone-CLI"
    "touchstone-doc"
    "touchstone-externals"
    "touchstone-package"
    "touchstone-web"
    "touchstone-api"
    "touchstone-common"
    "touchstone-engine"
    "touchstone-management-portal"
    "touchstone-ui"
  )

  for repo in "${repos[@]}"; do
    cd "$repo" || {
      echo -e "${RED}ERROR: Could not enter repo — $repo${NC}"
      continue
    }

    echo -e "${CYAN}###### Inside repo — $repo ######${NC}"

    if ! git checkout main; then
      echo -e "${RED}ERROR: Failed to checkout main — $repo${NC}"
      cd ..
      continue
    fi

    if ! git pull; then
      echo -e "${RED}ERROR: Failed to pull — $repo${NC}"
      cd ..
      continue
    fi

    echo -e "${GREEN}Successfully pulled main branch — $repo${NC}"

    cd ..
  done
}

