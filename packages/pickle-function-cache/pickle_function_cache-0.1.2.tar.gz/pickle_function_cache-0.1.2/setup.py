from distutils.core import setup
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='pickle_function_cache',
    version='0.1.2',
    author='Oleksandr Zelentsov',
    author_email='oleksandrzelentsov@gmail.com',
    packages=['.'],
    url='https://gitlab.com/oleksandr.zelentsov/pickle-function-cache',
    license='LICENSE.txt',
    description='Caching of the function results in a file.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
)
