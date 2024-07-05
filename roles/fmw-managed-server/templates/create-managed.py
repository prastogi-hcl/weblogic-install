ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

edit();
startEdit();
# applyJRF(target='{{ managed_server_name }}', domainDir='{{ domain_home }}');
cd('/')
cmo.createMachine('{{ server_hostname }}')

cd('/Machines/' + '{{ server_hostname }}' + '/NodeManager/' + '{{ server_hostname }}')
cmo.setListenAddress('{{ node_manager_listen_address }}')
#cmo.setListenAddress('{{ node_manager_listen_address }}')

#cd('/')
#cmo.createServer('{{ managed_server_name }}')

#cd('/Servers/' + '{{ managed_server_name }}')
#cmo.setListenAddress('127.0.0.1')
#cmo.setListenPort({{ managed_server_port }})
#cmo.setMachine(getMBean('/Machines/' + '{{ server_hostname }}'))

# Create Cluster
# ==================
cd ('/')
cobj = create('{{ClusterName}}','Cluster')


# Create Managed Servers
# =======================
cd ('/')
cmo.createServer('{{ managed_server_name }}')

cd('/Servers/' + '{{ managed_server_name }}')
cmo.setListenAddress('127.0.0.1')
cmo.setListenPort({{ managed_server_port }})
cmo.setMachine(getMBean('/Machines/' + '{{ server_hostname }}'))
#cmo.setMachine(getMBean('/Machines/' + '{{ admin_server_hostname }}'))
cbean_name='/Clusters/'+'{{ClusterName}}'
cmo.setCluster(getMBean(cbean_name))


cd ('/')
cmo.createServer('{{ ManagedServer2_Name }}')

cd('/Servers/' + '{{ ManagedServer2_Name }}')
cmo.setListenAddress('127.0.0.1')
cmo.setListenPort({{ ManagedServer2_Port }})
cmo.setMachine(getMBean('/Machines/' + '{{ server_hostname }}'))
cbean_name='/Clusters/'+'{{ClusterName}}'
cmo.setCluster(getMBean(cbean_name))
# Create Cluster
# applyJRF(target='{{ managed_server_name }}', domainDir='{{ domain_home }}');

# applyJRF wil call save and activate
save();
activate(block='true');
disconnect();
