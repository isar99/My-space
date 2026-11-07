##### Initial Setup

eval "$(ssh-agent -s)" 
ssh-add ~/.ssh/id_ed25519

RED='\033[0;31m' 
GREEN='\033[0;32m' 
YELLOW='\033[1;33m' 
BLUE='\033[0;34m' 
CYAN='\033[0;36m' 
NC='\033[0m'
product_name="touchstone"



##### Run MySQL

mysql -uroot -pT0uchStone_123



##### Run Mongo

mongosh
> use admin
> db.createUser({user: "touchstoneUser", pwd: "T0uchStone_123", roles: [ { role:"root", db: "admin" } ]})

# To check
mongosh -u touchstoneUser -p T0uchStone_123



##### Checkout Codebase

for project in touchstone-CLI touchstone-agent-webservice touchstone-api \
        touchstone-common touchstone-engine touchstone-externals \
        touchstone-management-portal touchstone-package touchstone-ui; do
    git clone git@github.com:VoerEirAB/${project} && echo
    cd ${project}
    git checkout ${default_branch}
    cd -
done



##### Setup config and logging directory 

export conf_dir=/etc/${product_name}
sudo mkdir -p ${conf_dir}

# For ubuntu users use the below mentioned command 
sudo chown $(whoami):$(whoami) ${conf_dir}

# For MacOS users use the below mentioned command
sudo chown $(whoami):staff ${conf_dir}

cp ${product_dir}/touchstone-package/contents/db.conf ${conf_dir}



##### Create log files

log_dir=/var/log/${product_name}
sudo mkdir -p ${log_dir}
cd /var/log

# For ubuntu users use the below mentioned command
sudo chown -R $(whoami):$(whoami) ${product_name}

# For MacOS users use the below mentioned command
sudo chown -R $(whoami):staff ${product_name}

cd touchstone
touch api.log common.log engine.log stdout_log



##### Setup Python venv

cd ${product_dir}/
python3.12 -m pip install uv==0.9.2
uv venv venv312 --python python3.10
source venv312/bin/activate
for project in touchstone-common touchstone-api \
    touchstone-engine touchstone-externals touchstone-management-portal touchstone-agent-webservice/client;
do
  cd "${project}" && echo "${project}"
  uv pip install .
  cd -
done



##### Pull the latest code to main in each repo

repos=( "touchstone-agent-webservice" 
		"touchstone-CLI" 
		"touchstone-doc" 
		"touchstone-externals" 
		"touchstone-package" 
		"touchstone-web" 
		"touchstone-api" 
		"touchstone-common" 
		"touchstone-engine" 
		"touchstone-management-portal" 
		"touchstone-ui" )

for repo in "${repos[@]}"; do
	cd $repo
	echo "${CYAN}Inside repo — $repo${NC}"
	git checkout main
        git pull 
	echo "${GREEN}Successfully Pulled in main branch${NC}"
	cd -
done



##### Install repos as packages
for project in touchstone-common touchstone-api touchstone-package \
    touchstone-engine touchstone-externals touchstone-management-portal touchstone-agent-webservice/client;
do
  cd "${project}" && echo "${project}"
  if [ -f setup.py ]; then
  	echo "${CYAN}Inside project — $project${NC}"
    uv pip install -e .
    echo "${GREEN}Successfully installed repos${NC}"
  fi
  cd -
done

# !important, repo-packages cannot be imported now,
# but can be imported in future activation
deactivate
     


##### Create Databases

mysql -uroot -pT0uchStone_123

mysql> create database touchstone;
mysql> create database touchstone_mgmt;
mysql> exit



##### Setup Touchstone DB using alembic

cp ${product_dir}/touchstone-common/touchstone_common/db/migration/alembic.ini.sample ${product_dir}/touchstone-common/touchstone_common/db/migration/alembic.ini

cd ${product_dir}/touchstone-common/touchstone_common/db/migration/
mysql --protocol=tcp -uroot -pT0uchStone_123 -e "ALTER DATABASE touchstone CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;"
mysql --protocol=tcp -uroot -pT0uchStone_123 touchstone < "$(find . -name '*.sql' | tail -1)"
alembic upgrade head



##### Setup Touchstone MP DB using alembic

cp ${product_dir}/touchstone-management-portal/touchstone_management_portal/common/db/migration/alembic.ini.sample ${product_dir}/touchstone-management-portal/touchstone_management_portal/common/db/migration/alembic.ini

cd ${product_dir}/touchstone-management-portal/touchstone_management_portal/common/db/migration
alembic upgrade head



##### Setup Touchstone UI

nvm install v24.8.0
nvm use v24.8.0

cd "${product_dir}/touchstone-ui"
bash build_static.sh

ln -s static/static/js/index.js "${product_dir}/touchstone-api/touchstoneApi/extras/html/report_new.js"
ln -s static/static/css/index.css "${product_dir}/touchstone-api/touchstoneApi/extras/html/report_new.css"



##### Run Touchstone API and Touchstone UI

cd "${product_dir}"
source venv310/bin/activate
python "${product_dir}/touchstone-api/touchstoneApi/app.py"

# Another terminal
cd "${product_dir}"/touchstone-ui
nvm use v24.8.0
npm install
npm start



##### Run Touchstone Engine

cd "${product_dir}"
source venv310/bin/activate
python "${product_dir}/touchstone-engine/ve_engines/app.py"



##### Run Touchstone MP

cd "${product_dir}"
source venv310/bin/activate
python "${product_dir}/touchstone-management-portal/touchstone_management_portal/app.py"



##### Run Touchstone MP GUI

cd "${product_dir}"
cd "${product_dir}/touchstone-management-portal/frontend"
nvm use v8.17.0
npm install
npm start
