import multiprocessing
import os

def loadPackages():
    rootdir = 'packages'
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            d = d.replace("packages\\", "")
            print(d)

print("=====MagmaShell=====")
print("SYSTEM INFORMATION:")
print(f"CPU Cores: {multiprocessing.cpu_count()}")
print("====================")

loadPackages()
