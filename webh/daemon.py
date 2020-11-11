import os
import sys
import subprocess

pid = os.fork()
if pid:
    sys.exit(0)

os.setsid()
log = open("/home/log.txt", "a+", encoding='utf8')
log.write("pid:" + str(pid))

cnt = 100

while cnt:
    proc = subprocess.run("python3 manage.py runserver 0.0.0.0:80", shell=True)
    cnt -= 1
