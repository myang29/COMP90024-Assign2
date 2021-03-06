# Authors: Team 45 COMP90024
# 705577 Meng Yang myang2@student.unimelb.edu.au
# 825847 Tong Su tsu2@student.unimelb.edu.au 
# 830665 Wan-Yun Sun wanyuns@student.unimelb.edu.au 
# 929739 Zeyu Huang z.huang56@student.unimelb.edu.au
# 938134 Zhizhou Chen zhizhouc@student.unimelb.edu.au




# *** VARIABLES ***
HOST_FILE=inventory/hosts.ini
# HOST_FILE=inventory/demo.ini
# HOST_FILE=inventory/hosts_limited.ini
RC_FILE=./openrc-withpw.sh
# RC_FILE=../unimelb-ee40617-openrc.sh

# *** prerequisite ***
# copy private key
cp ./comp90024-group45-privatekey ~/.ssh
sudo chmod 600 ~/.ssh/comp90024-group45-privatekey

# *** common tasks for all instances ***
# --------------------------------------
# configure (http|https|no) proxy
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-proxy.yaml
# mount /dev/vdb to /data
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-mount.yaml
# update cache and install [pip, git, ...]
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-apt.yaml

# *** tasks for couchdb node ***
# -----------------------------
# http://172.26.38.75:9024/_utils/#/_all_dbs
# configure docker: install docker.io, run couchdb container
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-docker_envr.yaml
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-docker_run.yaml
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-docker_start.yaml
# after starting the couchdb container, define views with python scripts
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-aurin.yaml
# set up nginx for web hosting
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-docker_nginx.yaml




# *** tasks for harvester instances ***
# -------------------------------------
# configure git repository
. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-harvester.yaml


