from setuptools import setup
import os

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = [] # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='kiauth',
    version='0.0.3',
    description='Dont put that shitty py file in your project, use this libs',
    py_modules=["kiauth"],
    package_dir={'': 'src'},
    keywords=["keyauth", "auth", "key"],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sysy's",
    author_email="sysys.owo@gmail.com",
    install_requires=install_requires
)