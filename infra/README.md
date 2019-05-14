# Infrastructure for COMP90024 Project 2

## Architecture  

- 1-3 tweet-harvesters
- CouchDB cluster of 1-3 servers running on Docker
- Web server implemented in CouchDB view

## What has been/to be implemented  

Achieved *with Ansible automation*:

- [x] Create security groups for
  - [x] CouchDB access
- [x] Create instances on UoM cloud with
  - [x] network: qh2-uom-internal
  - [x] volumes: each instance will have a volume attached
- [ ] Get instance facts from UoM cloud as inventory list
- [x] Configure proxy settings on instances 
- [x] Install packages on instances
- [ ] Set up CouchDB cluster 
  - [ ] Using docker
  - [ ] With volumes for persistent storage
- [ ] Run harvester script from Github repository

Package list:

- apt_packages:
  - git
  - python3-pip
  - docker.io
- pip_packages:
  - tweepy


## Instances  

Open for manual configuration, i.e. you can ssh onto these instances and run whatever command.
```
ssh -i <comp90024_file> ubuntu@172.26.37.215
# in case of error with message " key file ... too open", run
# chmod 600 <comp90024_file>
```

Can be deleted on demand for testing the automation process.
- `172.26.38.75`
- `172.26.38.85`
- `172.26.37.162`

## Issues/TODO  
- Update package list
