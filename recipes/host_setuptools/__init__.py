from toolchain import Recipe, shprint
from os.path import join
import sh
import os

class HostSetuptools(Recipe):
    version = "v28.6.0"
    url = "https://github.com/pypa/setuptools/archive/{version}.zip"
    depends = ["hostpython"]
    archs = ["x86_64"]

    def install(self):
        arch = list(self.filtered_archs)[0]
        build_dir = self.get_build_dir(arch.arch)
        os.chdir(build_dir)
        hostpython = sh.Command(self.ctx.hostpython)
        shprint(hostpython, "bootstrap.py")
        shprint(hostpython, "setup.py", "install", "--prefix=" + join(self.ctx.dist_dir, "hostpython"))

recipe = HostSetuptools()