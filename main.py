from pyghimporter import github

github(
    "mavnt",  # gh user
    "pyguess",  # gh repository
    "9cac4d51bddf91553c17c81a4c2781b285efbf97",  # specific commit or branch, default "master"
    "from pyguess import pyguess",  # import statement, default f"import {module}"
    force=True,  # force reinstallation even if .zip module file is found or import attempt does not fail
)
github("mavnt", "d", "master", "from d import d")
github("mavnt", "with_colors", "master", "from with_colors import *")

if __name__ == "__main__":
    with color(red):
        a = 1
        b = 2
        print(d(a, b, c=3))
        print(pyguess(str(a)))
