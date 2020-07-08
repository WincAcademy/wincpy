from setuptools import find_packages, setup

setup(
    name="wincpy",
    author="Stefan Wijnja (stfwn)",
    version="0.1",
    packages=find_packages(),
    entry_points={'console_scripts': ['wincpy=wincpy.__main__:console_entry']}
)
