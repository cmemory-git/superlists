Provisioning a new site
=======================

##Required packages:

* nginx
* Python3
* Git
* pip
* virtualenv

eg, on Ubuntu (16 or higher):

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Systemd Unit (default service manager by Ubuntu 16 or higher)

* see gunicorn.systemd.template.service, gunicorn.systemd.template.socket
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|---sites
    |---SITENAME
        |---source
        |---static
        |---virtualenv

