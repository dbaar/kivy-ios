# pure-python package, this can be removed when we'll support any python package
from toolchain import CythonRecipe, shprint
from os.path import join
import sh, os

class TwistedRecipe(CythonRecipe):
    version = "16.4.1"
    url = "https://github.com/twisted/twisted/archive/twisted-{version}.zip"
    depends = ["python", "zope_interface"]
    cythonize = False

    def prebuild_arch(self, arch):
        if self.has_marker("patched"):
            return
        self.apply_patch("dist.patch")
        self.set_marker("patched")

recipe = TwistedRecipe()

