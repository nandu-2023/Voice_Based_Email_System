import subprocess
import time

p1=subprocess.Popen('python gui1.py', shell=True)
time.sleep(2)
p2=subprocess.Popen('python main_f.py', shell=True)
p1.wait()
p2.wait()