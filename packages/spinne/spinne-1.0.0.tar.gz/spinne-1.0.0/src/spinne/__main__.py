import os
import sys
import spinne

html = """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<style>
h1 {
  color: red;
}
</style>
<h1>This is a test</h1>
<p>This is a paragraph.</p>

</body>
</html>
"""

from .main import *
from .index import *
from .css import * # TODO: add css support

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
    with open(f"{name}/index.html", "w") as f:
        f.write(html)
        print("created index.html...")
    print("done!")

try:
    if sys.argv[1] == "--new" or "-n":
        new(sys.argv[2])
except IndexError:
    print("Usage: spinne --new <name>")