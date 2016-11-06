# pure-python package, this can be removed when we'll support any python package
from toolchain import PythonRecipe, shprint
from os.path import join
import sh, os

class TxaioRecipe(PythonRecipe):
    version = "v2.5.1"
    url = "https://github.com/crossbario/txaio/archive/{version}.zip"
    depends = ["python", "six"]
    name = "txaio"

recipe = TxaioRecipe()
