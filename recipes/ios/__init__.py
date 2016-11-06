from toolchain import CythonRecipe, shprint
from os.path import join, exists
from os import chdir
import shutil
import sh

class IosRecipe(CythonRecipe):
    version = "master"
    url = "src"
    library = "libios.a"
    depends = ["python"]
    pbx_frameworks = ["MessageUI", "CoreMotion", "UIKit"]

    def install(self):
        self.install_python_package(name="ios.so", is_dir=False)

    def install_python_package(self, name=None, env=None, is_dir=True):
        """Automate the installation of a Python package into the target
        site-packages.

        It will works with the first filtered_archs, and the name of the recipe.
        """
        arch = self.filtered_archs[0]
        if name is None:
            name = self.name
        if env is None:
            env = self.get_recipe_env(arch)
        print("Install {} into the site-packages".format(name))
        build_dir = self.get_build_dir(arch.arch)
        chdir(build_dir)
        hostpython = sh.Command(join(self.ctx.dist_dir, "hostpython", "bin", "python"))
        iosbuild = join(build_dir, "iosbuild")
        shprint(hostpython, "setup.py", "install", "-O2", "--prefix", iosbuild, _env=env)
        dest_dir = join(self.ctx.site_packages_dir, name)
        self.remove_junk(iosbuild)
        if is_dir:
            if exists(dest_dir):
                shutil.rmtree(dest_dir)
            func = shutil.copytree
        else:
            func = shutil.copy
        func(join(iosbuild, "lib", self.ctx.python_ver_dir, "site-packages", name), dest_dir)


recipe = IosRecipe()


