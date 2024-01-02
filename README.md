# Introduction
This document contains instruction to setup the environment

## Setup  grafana
### Install grafana
Install grafana using below commands
```
https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/
sudo apt-get install -y apt-transport-https software-properties-common wget
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
# Updates the list of available packages
sudo apt-get update
# Installs the latest OSS release:
sudo apt-get install grafana
```

### Update Grafana configuration
1. edit vi /etc/grafana/grafana.ini
1. in grafana.ini file, add `root_url = %(protocol)://<IP>:3000/` (search for commented line containing root_url and add below it)
  e.g: `root_url = %(protocol)://34.221.9.184:3000/`
1. Save the file and restart the grafana server using command systemctl restart grafana-server

# Setup Grafana base
## Install Pre-requisites
1. Clone the Github repo to ubuntu machine and switch inside the directory
Install java, maven and docker using below commands. Ensure you are running as ubuntu user
```
sudo apt install default-jre
sudo apt install maven
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
sudo usermod -aG docker ${USER}
su - ${USER} / logout and login once again
```

## Build application containers
Build OTEL based application containers using below command
```
mvn clean package docker:build
```
## Run applications and tools
Run docker compose using below command
```
docker compose up -d
```
