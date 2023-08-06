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
    name='eazy_ui',
    version='0.0.2',
    description='Make beautifull ui easily',
    py_modules=["eazy_ui"],
    package_dir={'': 'src'},
    keywords=["easy", "ui", "simple", "checker", "generator"],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sysy's",
    author_email="sysys.owo@gmail.com",
    url="https://github.com/Sysys242/Eazy-UI",
    install_requires=install_requires
)