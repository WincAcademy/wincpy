from setuptools import find_packages, setup

long_description = open('README.md', 'r').read()

setup(
    name='wincpy',
    author='Stefan Wijnja (stfwn)',
    author_email='stefan@stfwn.com',
    description='Assists students in doing Winc Academy exercises.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/WincAcademy/wincpy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>= 3.6',
    entry_points={'console_scripts': ['wincpy=wincpy.__main__:console_entry']}
)
