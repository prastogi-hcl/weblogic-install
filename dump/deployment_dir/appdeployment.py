import os
import re
import time

userName="weblogic"
passWord="welcome1"
adminURL="t3://127.0.0.1:7001"
#fp = open(r'/home/centos/weblogic-part2/deployment_dir/deployment_config.csv','r')

def wlDeploy(appName, appPath, target):
    try:
        #connect to admin server
        #connect(userName, passWord, adminURL)

        #start edit operation
        edit()
        startEdit()

        appList = re.findall(appName, ls('/AppDeployments'))
        print "App name is ", appList
        print len(appList)
	if len(appList) >= 1:
                print "lets undeploy"
    		#oldestArchiveVersion = min(map(int, appList))
    		undeploy(appName)
                java.lang.Thread.sleep(1 * 1000 * 60)
        #start deploying application to admin server
        progress = deploy(appName,appPath,targets=target,upload='true')
        progress.printStatus()
        save()
        activate(20000,block="true")
        startApplication(appName)
        #disconnect from Admin server
        #disconnect()
        #exit()
    except Exception, ex:
        print ex.toString()
        cancelEdit('y')

def run():
    #connect to admin server
    connect(userName, passWord, adminURL)
    print "Run"
    file_path='/home/centos/weblogic-part2/deployment_dir/deployment_config.txt'
    f = open(file_path)
    L = f.readlines()
    print "line", L
    for line in L:
          line_s = line.split(",")
          print "Lines ", line_s
          appName = line_s[0].strip()
          appPath = line_s[1].strip()
          target = line_s[2].strip()
          print "Appname, AppPath & taget is \n", appName,appPath, target
          wlDeploy(appName, appPath, target)

    #disconnect from Admin server
    disconnect()
    exit()

if __name__ == "main" or "__main__":    
     run()

#wlDeploy("weblogic","welcome1","t3://127.0.0.1:7001","myApp", "/home/centos/ansible-weblogic/sample.war")
#wlDeploy("<Admin User Name>","<Password>","<AdminUrl","<App Name>", "<Path of war file>")
