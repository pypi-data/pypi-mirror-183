from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Friends Show Related API'
LONG_DESCRIPTION = 'A package that allows to get details about friends show'

# Setting up
setup(
    name="friendspy",
    version=VERSION,
    author="Ashutosh Sharma",
    author_email="email2ashusharma@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'friends', 'entertainment', 'fun'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)