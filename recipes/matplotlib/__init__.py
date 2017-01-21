# pure-python package, this can be removed when we'll support any python package
from toolchain import PythonRecipe, shprint
from os.path import join
import sh, os

setup_content = """
[packages]
tests = false
sample_data = false
toolkits = false

[gui_support]
cairo = false
gtk = false
gtk3agg = false
gtk3cairo = false
gtkagg = false
macosx = false
pyside = false
qt4agg = false
tkagg = false
windowing = false
wxagg = false
"""

class MatplotlibRecipe(PythonRecipe):
	version = "2.0.0"
	url = "https://github.com/matplotlib/matplotlib/archive/v{version}.tar.gz"
	depends = ["libpng", "freetype", "python", "numpy", "six"]
	cythonize = False

	def prebuild_arch(self, arch):
		if not self.has_marker("patched"):
			self.apply_patch("dist.patch")
			self.set_marker("patched")
		f = open(join(self.build_dir, 'setup.cfg'), 'w')
		f.write(setup_content)
		f.close()

recipe = MatplotlibRecipe()

