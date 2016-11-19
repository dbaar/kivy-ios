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

        #shprint(hostpython, "bootstrap.py")
        #shprint(hostpython, "setup.py", "install", "--prefix=" + join(self.ctx.dist_dir, "hostpython"))

        sh.curl("-O",  "https://bootstrap.pypa.io/ez_setup.py")
        shprint(hostpython, "./ez_setup.py")
        # Extract setuptools egg and remove .pth files. Otherwise subsequent
        # python package installations using setuptools will raise exceptions.
        # Setuptools version 28.3.0
        site_packages_path = join(
            self.ctx.dist_dir, 'hostpython',
            'lib', 'python2.7', 'site-packages')
        os.chdir(site_packages_path)
        with open('setuptools.pth', 'r') as f:
            setuptools_egg_path = f.read().strip('./').strip('\n')
            unzip = sh.Command('unzip')
            shprint(unzip, setuptools_egg_path)
        os.remove(setuptools_egg_path)
        os.remove('setuptools.pth')
        os.remove('easy-install.pth')
        shutil.rmtree('EGG-INFO')

recipe = HostSetuptools()