# pure-python package, this can be removed when we'll support any python package
from toolchain import PythonRecipe, shprint
from os.path import join
import sh, os

class AutobahnRecipe(PythonRecipe):
    version = "v0.15.0"
    url = "https://github.com/crossbario/autobahn-python/archive/{version}.zip"
    depends = ["python", "txaio", "twisted"]
    name = "autobahn-python"

    def prebuild_arch(self, arch):
        if self.has_marker("patched"):
            return
        self.apply_patch("autobahn.patch")
        self.set_marker("patched")

recipe = AutobahnRecipe()

