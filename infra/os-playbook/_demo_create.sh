RC_FILE=../unimelb-ee40617-openrc.sh
. $RC_FILE; ansible-playbook --ask-become-pass demo.yaml
echo "Instance(s) launched. Please configure inventory files, OK?"
