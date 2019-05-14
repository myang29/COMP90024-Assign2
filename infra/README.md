# Infrastructure for COMP90024 Project 2

## Architecture  

- one to many tweet-harvesters
- `CouchDB` single node solution running on Docker
- Web hosting using `nginx` running on Docker

## Folder structure

All paths below are relative to `infra/os-playbook/`.

- `host_deploy/`: self-contained playbooks for deployment of a single feature

  - | File Name under host_deploy | Purpose                                          |
    | --------------------------- | ------------------------------------------------ |
    | simple-apt.yaml             | install apt packages                             |
    | simple-aurin.yaml           | configure CouchDB views and populate AURIN data  |
    | simple-docker_*.yaml        | pull, create, start CouchDB and nginx containers |
    | simple-harvester.yaml       | run harvester script pulled from github          |
    | simple-mount.yaml           | create mount point and mount volumes             |
    | simple-proxy.yaml           | configure proxy in /etc/environment              |
    | vars_docker.yaml            | var file for playbooks in this folder            |

- `host_vars/`: variables used in `main.yaml`

  - `host_vars/uom.yaml`: specification for the instances created by `main.yaml`.

- `inventory/`: inventory file

  - `inventory/hosts.ini`: IPs of all 4 instances created.

- `roles/`: roles used in `mail.yaml`

- `main.yaml`: playbook for creating 4 instances according to specifications in `host_vars/uom.yaml`

- `openrc-withpw.sh`: openrc file for the UniMelb cloud project with user password embedded.



## What has/has not been implemented  

Achieved *with Ansible automation*:

- [x] Create security groups for
  - [x] CouchDB access
- [x] Create instances on UoM cloud with
  - [x] network: qh2-uom-internal
  - [x] volumes: each instance will have a volume attached
- [ ] Get instance facts from UoM cloud as inventory list
- [x] Configure proxy settings on instances 
- [x] Install packages on instances
- [x] Set up CouchDB instance 
  - [x] As a single node
  - [x] With volumes for persistent storage
- [x] Run harvester script from Github repository on multiple instances

## Issues

- The currently solution requires manually fill in host IPs in `infra/os-playbook/inventory/hosts.ini` after creating instances.
- The current deployment script cannot completely adapt to change of IP of the instance called `pilot` hosting CouchDB.
  - **Need to change** the {{ remote_ip }} variable in `infra/os-playbook/host_deploy/simple-harvester.yaml`
  - **Cannot use script** `infra/os-playbook/host_deploy/simple-aurin.yaml` to define views in CouchDB in case of IP change of the instance.