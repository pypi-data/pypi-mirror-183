import os
import sys
from .templates import main, index, css
import spinne

def main(name):
    print("Creating app...")
    if not os.path.exists(name):
        os.mkdir(name)
    with open(f"{name}/main.py", "w") as f:
        f.write(main.main)
        print("created main file...")
    with open(f"{name}/index.py", "w") as f:
        f.write(index.index)
        print("created index...")

try:
    if sys.argv[1] == "--new" or "-n":
        main(sys.argv[2])
except IndexError:
    print("Usage: spinne --new <name>")