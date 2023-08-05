import os
import sys
import spinne

from .main import *
from .index import *
import css # TODO: add css support

def new(name):
    print("Creating app...")
    if not os.path.exists(name):
        os.mkdir(name)
    with open(f"{name}/main.py", "w") as f:
        f.write(main)
        print("created main file...")
    with open(f"{name}/index.py", "w") as f:
        f.write(index)
        print("created index...")

try:
    if sys.argv[1] == "--new" or "-n":
        new(sys.argv[2])
except IndexError:
    print("Usage: spinne --new <name>")