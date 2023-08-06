from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'a python module that will allow you to make a colorful text with dynamics colors and display your text slowly'

# Setting up
setup(
    name="pyshade",
    version=VERSION,
    author="Platipus (PLATIPUS#5696)",
    author_email="<plati@platipuss.xyz>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['pyshade','python', 'colors', 'beautiful_colors', 'shade', 'animation', 'display', 'dynamics_colors', 'command', 'terminal', 'prompt'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)