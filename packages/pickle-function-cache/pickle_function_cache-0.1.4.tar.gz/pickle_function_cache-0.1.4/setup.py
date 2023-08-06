from distutils.cmd import Command
from distutils.core import setup
import os
from pathlib import Path
from shutil import rmtree
import sys


NAME = 'pickle_function_cache'
VERSION = "0.1.4"


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(this_directory, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION



class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(this_directory, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/* --verbose")

        self.status("Pushing git tags…")
        os.system(f"git tag v{about['__version__']}")
        os.system("git push --tags")

        sys.exit()



setup(
    name=NAME,
    version=about["__version__"],
    author='Oleksandr Zelentsov',
    author_email='oleksandrzelentsov@gmail.com',
    packages=['.'],
    url='https://gitlab.com/oleksandr.zelentsov/pickle-function-cache',
    license='LICENSE.txt',
    description='Caching of the function results in a file.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    cmdclass={"upload": UploadCommand},
)
