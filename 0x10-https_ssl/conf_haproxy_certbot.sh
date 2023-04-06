#usr/bin/env bash
# Script for config haproxy and cerbot for generate	Let's Encrypt Authority X3
if [ ! -e "$(which certbot)" ]
then
	sudo apt-get update
	sudo apt-get -y install certbot
fi
if [ ! -e '$(which haproxy)' ]
then
	sudo apt-get update
	sudo apt-get -y install haproxy
fi
sudo service haproxy stop
sudo certbot certonly --standalone -d '$1'
sudo mkdir -p /etc/haproxy/certs
DOMAIN='$1' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs

