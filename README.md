**Weblogic12c Admin Server, Node Manager and Managed Server in AWS with Ansible provisioner**
Centos 7:
sudo yun install-y  unzip, vim, git
sudo yum install epel-release
sudo yum install -y ansible

More Details Read : note.txt

Ansible playbook for deploy and create a WebLogic 12c Domain 

**Prerequisites:**

Ansible 2.8


Oracle Weblogic 12c

Oracle JDK 1.8.66

**Configuration**

Place Weblogic distributive to roles/fmw-software/files/fmw_12.1.3.0_wls

Place JDK distributive to roles/linux-jdk/files/jdk-8u202-linux-x64.tar.gz

Update the infra-vars.yml if required

**# JDK installer and target folder**

jdk_installation_archive: 'jdk-8u202-linux-x64.tar.gz'

jdk_folder: '{{ oracle_base }}/jdk1.8.0_202'

**# fmw installer**

mw_installer: 'fmw_12.2.1.0.0_wls.jar'

**Installation**

Run the playbook: ansible-playbook -vv -i hosts playbook.yml
Deploy application: ansible-playbook -vv -i hosts playbook.yml --tags deploy

Access Weblogic web interface at http://x.x.x.x:7001/console using weblogic/welcome1 credentials.

**Playbook includes the following roles:**

**linux-wls**

This role configures the Linux system with requirements to run the WebLogic domain.

**linux-jdk**

This role configures the Linux system with JDK 8

**fmw-software**

This role installs the the Weblogic 12c

**fmw-domain**

This role creates and configures a Domain with Fusion Middleware software

**node-manager**

This role configures and starts the Nodemanager. It also configures systemd to start automatically the nodemanager after restart

**start-admin-server**

This starts the Admin server using nodemanager for the first time. Creates some initial configuration like boot.properties file

**fmw-managed-server**

This role creates and starts a managed server
