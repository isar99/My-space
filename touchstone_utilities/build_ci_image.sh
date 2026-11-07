FARM_NAME=ts-test-agent-farm
touchstone_key=/Users/isarahmad/Documents/ofc_imp_doc/touchstone_key
os_vm=<os-vm>
arm_vm=<arm-vm>
podman farm create ${FARM_NAME}
podman system connection add os_vm ssh://$os_vm --socket-path /run/user/1000/podman/podman.sock --identity $touchstone_key
podman system connection add arm_vm ssh://$arm_vm --socket-path /run/user/1000/podman/podman.sock --identity $touchstone_key
podman farm update ${FARM_NAME} --add os_vm
podman farm update ${FARM_NAME} --add arm_vm

podman system connection list

export MYSQL_PASSWORD="T0uchStone_123"
export GITHUB_TOKEN="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"
export CONTAINER_REGISTRY="registry.voereir.io"
export CONTAINER_USER_NAME="voereir-qa"
export CONTAINER_IMAGE_TAG="5.4.0"
export CONTAINER_FILE="Dockerfile"
export PODMAN_FARM_NAME=ts-test-agent-farm


repos=(
    "touchstone-management-portal-ui"
    "touchstone-CLI"
    "notification-dispatcher"
    "touchstone-externals"
    "touchstone-common"
    "touchstone-api"
    "touchstone-ui"
    "touchstone-management-portal-ui"
    "touchstone-engine"
    "touchstone-ui"
    "touchstone-management-portal"
    "touchstone-ai"
    "touchstone-doc"
)

GREEN='\033[0;32m'
NC='\033[0m'

for repo in "${repos[@]}"; do
    echo -e "${GREEN}Inside ${repo}${NC}"

    target_project="$repo"
    CONTAINER_REPO_NAME="${repo}-ci"

    ./container_image_build.sh "$repo"
    ssh -i $touchstone_key $os_vm "podman system prune --all --force" 
done
