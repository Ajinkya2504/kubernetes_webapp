#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

f = cgi.FieldStorage()

cmd = f.getvalue("e")
port = f.getvalue("b")
replica = f.getvalue("c")
name = f.getvalue("k")

if (("all" in cmd) and ("pods" in cmd)):
   output = subprocess.getoutput("sudo /usr/local/bin/kubectl get pods")
   print("[root@localhost ~]# ",output)
elif ("all" in cmd) and ("deployment" in cmd):
    output = subprocess.getoutput("sudo /usr/local/bin/kubectl get deployment")
    print("[root@localhost ~]# ",output)
elif (("create" in cmd) or ("launch" in cmd)) and ("pod" in cmd):
   output = subprocess.getoutput("sudo /usr/local/bin/kubectl run --image=httpd")
   print(" [root@localhost ~]# ", output)
elif ("deployment" in cmd) and ("create" in cmd):
   output = subprocess.getoutput("sudo /usr/local/bin/kubectl create deployment db --image=httpd")
   print("[root@localhost ~]# ", output)
elif ("deployment" in cmd) and ("expose") and ("port number"):
   output = subprocess.getoutput("sudo /usr/local/bin/kubectl expose deployment --port=" ,  port , "--type=NodePort")
   print("[root@localhost ~]# ",output)
elif (("create" in cmd) or ("scale" in cmd)) and (("replica" in cmd) or ("deployment" in cmd )):
   output = subprocess.getoutput("sudo /usr/local/bin/kubectl scale deployment", name ,"--replicas=" , replica)
   print(" [root@localhost ~]# ", output)
elif ("delete" in cmd) and ("deployment" in cmd):
   output = subprocess.getoutput("sudo /usr/local/bin/kubectl delete deployment  ", name)
   print("Deployment Deleted")
   print("[root@localhost ~]# ",output)
else:
   print("[root@localhost ~]# Invalid Input")


