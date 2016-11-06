# pure-python package, this can be removed when we'll support any python package
from toolchain import CythonRecipe, shprint
from os.path import join
import sh, os

class ZopeInterfaceRecipe(CythonRecipe):
    version = "4.3.2"
    url = "https://github.com/zopefoundation/zope.interface/archive/{version}.zip"
    depends = ["python"]
    name = "zope.interface"

    # def install(self):
    #     arch = list(self.filtered_archs)[0]
    #     build_dir = self.get_build_dir(arch.arch)
    #     os.chdir(build_dir)
    #     hostpython = sh.Command(join(self.ctx.dist_dir, "hostpython", "bin", "python"))
    #     build_env = arch.get_env()
    #     dest_dir = join(self.ctx.dist_dir, "root", "python")
    #     build_env['PYTHONPATH'] = join(dest_dir, 'lib', 'python2.7', 'site-packages')
    #     shprint(hostpython, "setup.py", "install", "--prefix", dest_dir, _env=build_env)

recipe = ZopeInterfaceRecipe()

