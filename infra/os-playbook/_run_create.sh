# Authors: Team 45 COMP90024
# 705577 Meng Yang myang2@student.unimelb.edu.au
# 825847 Tong Su tsu2@student.unimelb.edu.au 
# 830665 Wan-Yun Sun wanyuns@student.unimelb.edu.au 
# 929739 Zeyu Huang z.huang56@student.unimelb.edu.au
# 938134 Zhizhou Chen zhizhouc@student.unimelb.edu.au



. ./openrc-withpw.sh; ansible-playbook --ask-become-pass main.yaml
echo "Instance(s) launched. Please configure inventory files, OK?"
read _

