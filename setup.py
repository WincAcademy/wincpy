import os

from setuptools import find_packages, setup


def gather_package_data_paths():
    package_data_paths = []

    # Reuse .gitignore to keep it in sync
    ignorelist = open(".gitignore").read().split("\n")

    for root, dirs, files in os.walk("wincpy"):
        for item in ignorelist:
            if item in dirs:
                dirs.remove(item)

        # Trim off 'wincpy/'
        root = root[7:]
        for f in files:
            # We don't exclude non-Python files because then Python files that
            # are in a folder without __init__.py in it are omitted.
            package_data_paths.append(os.path.join(root, f))
    return package_data_paths


setup(
    name="wincpy",
    author="Stefan Wijnja (stfwn)",
    author_email="stefan@stfwn.com",
    description="Assists students in doing Winc Academy exercises.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    version="1.0.0",
    packages=find_packages(),
    url="https://github.com/WincAcademy/wincpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.9",
    package_data={"wincpy": gather_package_data_paths()},
    entry_points={"console_scripts": ["wincpy=wincpy.__main__:console_entry"]},
    install_requires=["rich>=10.9.0"],
)
