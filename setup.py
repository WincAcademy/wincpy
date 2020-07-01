from setuptools import find_packages, setup

setup(
    name="wincpy",
    version="0.1",
    packages=['wincpy'],
    entry_points={'console_scripts': ['wincpy=wincpy.__main__:console_entry']}
)
