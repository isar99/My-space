sudo su
export registry_user=isar
export registry_password=IITjee@2017
export version=5.4.0


export user=user1
export password=voereir@123456
export mysql_password='T0uchStone_123!kR8#nQ2wX5pLm9z'
export mysql_touchstone_user="touchstoneUser"
export mysql_touchstone_user_password='T0uchStone_123!kR8#nQ2wX5pLm9z'
export mongo_touchstone_user="touchstoneUser"
export mongo_touchstone_user_password='T0uchStone_123!kR8#nQ2wX5pLm9z'
export apache_enable_http='Y'
export security_implement_database='Y'
export security_implement_apache='Y'
export security_implement_ssh='Y'
export security_implement_linux='Y'
touch /tmp/installation_logging
wget http://repo.voereir.io/script/$version/default_install_scripts.tar.gz
tar xf default_install_scripts.tar.gz -C /tmp/
cd /tmp/$version
nohup bash -E install.sh > /tmp/installation_logging &

# To check log after exiting from nohup
tail -f /tmp/installation_logging




# for MP upgradation
export MP_VERSION=5.4.0
export user=user1
export password=voereir@123456
export mysql_password='T0uchStone_123!kR8#nQ2wX5pLm9z'
export mysql_touchstone_user="touchstoneUser"
export mysql_touchstone_user_password="T0uchStone_123"
export touchstone_management_mysql_password="T0uchStone_123"
export mongo_touchstone_user="touchstoneUser"
export mongo_touchstone_user_password="T0uchStone_123"
export web_console_ssh_user=ubuntu
export apache_enable_http='Y'
export security_implement_database='Y'
export security_implement_apache='Y'
export security_implement_ssh='Y'
export security_implement_linux='Y'
wget --user $user --password $password http://repo.voereir.io/script/management/${MP_VERSION}/touchstone-management-portal-${MP_VERSION}.tgz
tar -xvf touchstone-management-portal-${MP_VERSION}.tgz
cd ${MP_VERSION}
nohup bash -E install.sh > /tmp/mp_installation_logging &

# To check log after exiting from nohup
tail -f /tmp/mp_installation_logging
