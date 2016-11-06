# pure-python package, this can be removed when we'll support any python package
from toolchain import PythonRecipe, shprint
from os.path import join
import sh, os

class SixRecipe(PythonRecipe):
    version = "master"
    url = "https://github.com/RekindleInc/python-six/archive/{version}.zip"
    depends = ["python"]
    name = "six"

recipe = SixRecipe()
