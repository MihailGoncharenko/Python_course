import os
import subprocess
import shlex
import glob
import shutil
os.getcwd()
convert = os.path.abspath("convert.exe")
os.chdir("Source")
if os.path.exists("Result") == 0:
    os.mkdir("Result")
for infile in glob.glob("*.jpg"):
    name = str(infile)
    shutil.copy(name, 'Result')
os.chdir("Result")
for infile in glob.glob("*.jpg"):
    name = str(infile)
    altname = "converted_" + name
    subprocess.run([convert, name, '-resize', '200', altname])
    os.remove(name)
