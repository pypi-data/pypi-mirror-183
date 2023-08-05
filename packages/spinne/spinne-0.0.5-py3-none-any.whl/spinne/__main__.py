import os
import sys

def main(name):
    print("Creating app...")
    if not os.path.exists(name):
        os.mkdir(name)
    with open(f"{name}/main.py", "w") as f:
        f.write(open("templates/main.py", "r").read())
        print("created main file...")
    with open(f"{name}/index.py", "w") as f:
        f.write(open("templates/index.py", "r").read())
        print("created index...")
    with open(f"{name}/index.css", "w") as f:
        f.write(open("templates/index.css", "r").read())
        print("created index.css...")

try:
    if sys.argv[1] == "--new" or "-n":
        main(sys.argv[2])
except IndexError:
    print("Usage: spinne --new <name>")