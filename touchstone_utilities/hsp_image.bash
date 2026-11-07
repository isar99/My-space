### Setup of HSP in VM ###

* Create VM with an image ubuntu24.04

* Create directories
sudo mkdir /opt/host_ssh_proxy_server
sudo mkdir /etc/host_ssh_proxy_server
sudo mkdir /opt/touchstone_agent
sudo chown 10100:10100 /opt/touchstone_agent

* Add certificates
scp /Users/isarahmad/Documents/ofc_imp_doc/hsp_ca.crt ubuntu@172.16.227.33:/home/ubuntu
scp /Users/isarahmad/Documents/ofc_imp_doc/hsp_ca.key ubuntu@172.16.227.33:/home/ubuntu

sudo cp /home/ubuntu/hsp_ca.* /etc/host_ssh_proxy_server/

* Copy ssh key to vm
scp ~/.ssh/id_ed25519 ubuntu@172.16.227.33:/home/ubuntu

* # Install podman (if not done)
sudo apt update
sudo apt install -y podman
# Check whether installed successfully or not
sudo podman --version



* Download docker (if not present)

sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install -y \
docker-ce \
docker-ce-cli \
containerd.io \
docker-buildx-plugin \
docker-compose-plugin

sudo systemctl enable docker
sudo systemctl start docker

sudo docker version





### For builder ###

sudo docker login registry.voereir.io -uisar -pIITjee@2017

export TOUCHSTONE_BUILDER_NAME="ve-touchstone-builder"
export TOUCHSTONE_BUILDER_VERSION="v5.4.0"
export DOCKER_SOCK_FILE="/run/docker.sock"
export HARBOR_REGISTRY="registry.voereir.io"
export container_name="builder"
export BUILDER_HARBOR_REPO="voereir-qa"

# container path -> "registry.voereir.io/voereir-qa/ve-touchstone-builder:v5.3.0"
CONTAINER_ID=$(sudo docker run -v $DOCKER_SOCK_FILE:$DOCKER_SOCK_FILE -d -i --network host \
               --name ${container_name} \
               -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
               ${HARBOR_REGISTRY}/${BUILDER_HARBOR_REPO:-voereir-qa}/${TOUCHSTONE_BUILDER_NAME}:${TOUCHSTONE_BUILDER_VERSION})

# sudo podman exec -it $CONTAINER_ID bash
sudo docker exec -i "${CONTAINER_ID}"  mkdir -p /root/.ssh/
# Copy ssh private key from host to container to get the git pull access.
sudo docker cp id_ed25519 "${CONTAINER_ID}":/root/.ssh/id_rsa_repo

sudo docker exec -it $CONTAINER_ID bash





### Inside Container ###

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa_repo 

ssh -T git@github.com  

TOUCHSTONE_BUILDER_NAME="ve-touchstone-builder"
TOUCHSTONE_BUILDER_VERSION="v5.3.0"
DOCKER_SOCK_FILE="/run/docker.sock"
HARBOR_REGISTRY="registry.voereir.io"
container_name="ve-host_ssh_proxy_server"
BUILDER_HARBOR_REPO="voereir-dev"

git clone --branch containerise_host_ssh_proxy_VOER3155 git@github.com:VoerEirAB/touchstone-package.git

cd touchstone-package/cloud_native/docker-images/host_ssh_proxy_server

# Install podman
sudo apt update
sudo apt-get install –y podman

# Check whether installed successfully or not
sudo podman --version

podman login registry.voereir.io -uisar -pIITjee@2017

bash docker_image_creation.sh 5.4.0 --build-mode dev --cython no

# Use either ve-host-ssh-proxy-server-yardstick or ve-host-ssh-proxy-server





                         
### How to run an image? ###

Inside Host VM
```bash
# 10100 is UID for voereir
sudo mkdir -p /opt/touchstone_agent /etc/host_ssh_proxy_server /var/log/touchstone
sudo touch /var/log/touchstone/agent.log
sudo chown -R 10100:10100 /opt/touchstone_agent /etc/host_ssh_proxy_server /var/log/touchstone
```

Copy files in VM from you local machine
```bash
scp /path/to/ca.crt <Host VM>:/etc/host_ssh_proxy_server/
scp /path/to/ca.key <Host VM>:/etc/host_ssh_proxy_server/
```

Pull Host SSH Proxy Server image from registory and run with mounting files
```bash
# There will be two images. One image is with Yardstick and another without Yardstick.

# Create SSH keys secret. SSH directory should have private key and public key.
tar czf ssh_bundle.tar.gz -C ssh .
podman secret create ssh_bundle ssh_bundle.tar.gz

# Image without Yardstick
podman pull registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-09-21-18-24-19


podman volume create ve-host-ssh-proxy-server-data
podman volume create ve-host-ssh-proxy-server-log

# Create SSH keys secret. SSH directory should have private key and public key.
tar czf ssh_bundle.tar.gz -C ssh .
podman secret create ssh_bundle ssh_bundle.tar.gz

podman secret create host-ssh-proxy-ca-crt /home/ubuntu/hsp_ca.crt
podman secret create host-ssh-proxy-ca-key /home/ubuntu/hsp_ca.key

podman secret create host-ssh-proxy-ca-crt /home/ubuntu/fullchain.pem
podman secret create host-ssh-proxy-ca-key /home/ubuntu/privkey.pem


podman run -d \
  --name ve-host-ssh-proxy-server -p 5001:5001 -p 5002:5002 \
  -v ve-host-ssh-proxy-server-data:/opt/touchstone_agent \
  -v ve-host-ssh-proxy-server-log:/var/log/touchstone \
  --secret source=ssh_bundle,type=mount,target=/run/secrets/ssh_bundle,uid=10100,gid=10100,mode=440 \
  --secret host-ssh-proxy-ca-crt,target=/etc/host_ssh_proxy_server/ca.crt \
  --secret host-ssh-proxy-ca-key,target=/etc/host_ssh_proxy_server/ca.key \
  registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-10-26-09-25-38

# Image with Yardstick
podman run -d \
  --name hsp-yardstick2 -p 8001:5001 -p 8002:5002 \
  -v hsp-yardstick-data:/opt/touchstone_agent \
  -v hsp-yardstick-log:/var/log/touchstone \
  --secret source=ssh_bundle,type=mount,target=/run/secrets/ssh_bundle,uid=10100,gid=10100,mode=440 \
  --secret host-ssh-proxy-ca-crt,target=/etc/host_ssh_proxy_server/ca.crt \
  --secret host-ssh-proxy-ca-key,target=/etc/host_ssh_proxy_server/ca.key \
  registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server-yardstick:v5.4.0-beta-2026-10-14-08-35-02




# for sleep infinity run of container
podman run -d \
  --name hsp9 -p 3001:5001 -p 3002:5002 \
  -v touchstone-agent:/opt/touchstone_agent \
  -v touchstone-agent-log:/var/log/touchstone \
  --entrypoint sleep \
  --secret source=ssh_bundle,type=mount,target=/run/secrets/ssh_bundle,uid=10100,gid=10100,mode=440 \
  --secret host-ssh-proxy-ca-crt,target=/etc/host_ssh_proxy_server/ca.crt \
  --secret host-ssh-proxy-ca-key,target=/etc/host_ssh_proxy_server/ca.key \
  registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-09-15-06-50-06 \
  infinty

# for running with entrypoint /bin/bash and sleep infinity
podman run -d --replace --entrypoint /bin/bash --name hsp1 -p 3001:5001 -p 3002:5002 \
  -v touchstone-agent:/opt/touchstone_agent -v touchstone-agent-log:/var/log/touchstone \
  --secret source=ssh_bundle,type=mount,target=/run/secrets/ssh_bundle,uid=10100,gid=10100,mode=440 \
  --secret host-ssh-proxy-ca-crt,target=/etc/host_ssh_proxy_server/ca.crt \
  --secret host-ssh-proxy-ca-key,target=/etc/host_ssh_proxy_server/ca.key \
  registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-09-23-11-50-44 \
  -c "trap : TERM INT; sleep infinity & wait"



`8ab3fc5ad0f5` -> 5.1.0
`03a3f0fb7a68` -> 5.3.0
`8019d37fd935` -> 5.4.0


sqlite3 /opt/touchstone_agent/taws.db
select * from command where command=="isar";
SELECT * FROM alembic_version; 


bash update_hsp_server.sh registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-10-25-15-41-05
db file in host vm -> sqlite3 /home/ubuntu/.local/share/containers/storage/volumes/touchstone-agent/_data/taws.db

podman run --rm --entrypoint alembic registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-10-22-10-49-57 heads | awk 'NR==1 {print $1}'

podman run --rm --entrypoint bash registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-10-22-10-49-57 -c '
cd /opt/app-root/lib64/python3.12/site-packages/touchstone_agent_server/database/migration/ &&
alembic heads
'

podman run --rm --entrypoint bash registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-10-22-10-49-57 -c '
      cd "${MIGRATION_DIR}" &&
      alembic heads
    '
  awk 'NR == 1 { print $1 }'

podman run -dit --entrypoint bash registry.voereir.io/voereir-dev/ve-host-ssh-proxy-server:v5.4.0-beta-2026-10-25-15-41-05




