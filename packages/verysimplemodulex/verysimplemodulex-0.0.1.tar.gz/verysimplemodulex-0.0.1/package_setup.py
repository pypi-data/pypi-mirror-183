from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "My first package"
LONG_DESCRIPTION = "My very first package"

setup(
    # The name must match the folder name "verysimplemodulex"
    name="verysimplemodulex",
    version=VERSION,
    author="Seunfunmi Adegoke",
    author_email="adegokeseunfunmi1999@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # Add any package that needs to be installed alongside your package
    keywords=["python", "my first package"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
