import os
import re
import time

userName="weblogic"
passWord="welcome1"
adminURL="t3://127.0.0.1:7001"
#fp = open(r'/home/centos/weblogic-part2/deployment_dir/deployment_config.csv','r')

def wlDeploy(appName, appPath, target):
    try:
        print "++++++++++ Starting App deployment ++++++++++\n", appName
        edit()
        startEdit()

        appList = re.findall(appName, ls('/AppDeployments'))
        print "App name is ", appList
        print len(appList)
	if len(appList) >= 1:
                print "lets undeploy"
    		#oldestArchiveVersion = min(map(int, appList))
    		undeploy(appName)
                java.lang.Thread.sleep(4000)
        #start deploying application to admin server
        progress = deploy(appName,appPath,targets=target,upload='true')
        progress.printStatus()
        save()
        activate(20000,block="true")
        startApplication(appName)
        print "\n +++++++++++ Completed App Deployment: \n", appName
    except Exception, ex:
        print ex.toString()
        cancelEdit('y')

def run():
     try:
    	#connect to admin server
    	connect(userName, passWord, adminURL)
    	print "Run"
    	file_path='/oracle/fmw12.2.1/deployment/deployment_config.txt'
    	f = open(file_path)
    	L = f.readlines()
    	print "line", L
    	for line in L:
            line_s = line.split(",")
            print "Lines ", line_s
            #print "len", len(line_s)
            if len(line_s) == 4:
          	appName = line_s[0].strip()
          	appPath = line_s[1].strip()
          	target = line_s[2].strip()
          	deploy = str(line_s[3].strip())
          	print "\n +++++++++++ Appname, AppPath & taget, Deploy_Flag is  +++++++++++++", appName,appPath, target, deploy
            	if deploy == 'true':
           	    wlDeploy(appName, appPath, target)
            else:
                print "Please check deployment_config.txt', probably not provided the proper confi", line

            deploy=''

    	#disconnect from Admin server
    	disconnect()
    	exit()
     except Exception, ex:
         print ex.toString()
         disconnect()
         exit()

if __name__ == "main" or "__main__":    
     run()
