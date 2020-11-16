import os
import sys
import subprocess

pid = os.fork()
if pid:
    sys.exit(0)

os.umask(0)
os.setsid()

_pid = os.fork()
if _pid:
    sys.exit(0)

sys.stdout.flush()
sys.stdin.flush()

if not os.path.exists('./IO'):
    os.makedirs('./IO')

with open('/dev/null') as in_file, open('./IO/out.txt', 'w') as out_file, open('./IO/err.txt', 'w') as err_file:
    os.dup2(in_file.fileno(), sys.stdin.fileno())
    os.dup2(out_file.fileno(), sys.stdout.fileno())
    os.dup2(err_file.fileno(), sys.stderr.fileno())

while True:
    proc = subprocess.run("python3 manage.py runserver 0.0.0.0:80", shell=True)