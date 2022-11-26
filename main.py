import multiprocessing
import os
import json

class command():
    def __init__(self, name, args, description, script):
        self.name = name
        self.args = args
        self.description = description
        self.script = script

def loadPackages():
    rootdir = 'packages'
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            if os.path.isfile(f"{d}\\manifest.json"):
                with open(f"{d}\\manifest.json") as manifest:
                    load = json.load(manifest)
                    pckname = load["manifest"]["name"]
                    print(f"Loading package {pckname}.")
            else:
                print(f"Package \"{d}\" is invalid.")

print("=====MagmaShell=====")
print("SYSTEM INFORMATION:")
print(f"CPU Cores: {multiprocessing.cpu_count()}")
print("====================")

loadPackages()
