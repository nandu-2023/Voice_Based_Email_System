import subprocess
import time

p1=subprocess.Popen('python gui3.py', shell=True)
time.sleep(2)
p2=subprocess.Popen('python Marathi.py', shell=True)
p1.wait()
