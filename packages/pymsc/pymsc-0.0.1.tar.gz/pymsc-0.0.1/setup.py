from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python Misc Tools Library'

# Setting up
setup(
    name="pymsc",
    version=VERSION,
    author="Xcoder_1 (Pomen Gtasa)",
    author_email="<mail@progamedev12.com>",
    url="http://bakerman.rf.gd",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyfiglet'],
    keywords=['python', 'misc', 'tools'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)