import sys 
import subprocess

def packetManager(lib):
    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

libs = ["beautifulsoup4", "requests", "openpyxl", "lxml"]

for lib in libs:
    packetManager(lib)