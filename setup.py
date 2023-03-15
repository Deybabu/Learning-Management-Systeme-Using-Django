import os

from setuptools import find_packages, setup
from sphinx.setup_command import BuildDoc

DEV_REQUIRES: tuple = (
    "ipython",
    "ipdb",
    "isort",
    "pylint",
    "autopep8",
    "django-linter",
    "django-debug-toolbar",
    "django-extensions"
)

cmdclass = {'build_sphinx': BuildDoc}

name = "Learning Management System"
version = "1.0"


def read(fname: str = None) -> str:
    if fname:
        fname_path = os.path.join(os.path.dirname(__file__), fname)
        if os.path.exists(fname_path):
            return open(fname_path).read()


setup(
    name=name,
    version=version,
    author="coderj001",
    description="This project is learning management system for student.",
    long_description=read('README.md'),
    python_requires=">=3.9",
    install_requires=(
        "django",
        "sphinx",
    ),
    extras_require={'dev': DEV_REQUIRES},
    include_package_data=True,
    packages=find_packages("."),
    package_dir={"": "."},
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
        }
    },
    classifiers=[
        'Development Status:: 4',
        'Operation System:: Linux and Windows'
    ]
)
