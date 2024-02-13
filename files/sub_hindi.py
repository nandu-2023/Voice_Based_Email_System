import subprocess
import time

p1=subprocess.Popen('python gui4.py', shell=True)
time.sleep(2)
p2=subprocess.Popen('python Hindi.py', shell=True)
p1.wait()
