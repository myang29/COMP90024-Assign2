# *** VARIABLES ***
HOST_FILE=inventory/demo.ini
RC_FILE=../unimelb-ee40617-openrc.sh

. $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-apt.yaml


# # *** common tasks for all instances ***
# # configure (http|https|no) proxyRC_FILE
# . $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-proxy.yaml
# # mount /dev/vdb to /data
# . $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-mount.yaml
# # update cache and install [pip, git, ...]
# . $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-apt.yaml

# # *** task for couchdb node ***
# # configure docker: install docker.io, run couchdb container
# . $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-docker_envr.yaml
# . $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-docker_run.yaml
# . $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-docker_start.yaml

# # *** task for harvester instances ***
# # configure git repository
# # . $RC_FILE; ansible-playbook -i $HOST_FILE host_deploy/simple-git.yaml


