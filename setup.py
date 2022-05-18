from setuptools import setup, find_packages

setup(
    name='colorcurses',
    version='1.0',
    license='GPL',
    author='Evan J Parker',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/leftbones/colorcurses',
    keywords='python curses color highlight',
    install_requires=[
        'curses',
    ],
)
