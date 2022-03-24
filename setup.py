from setuptools import setup
from setuptools import find_packages
 
VERSION = '1.0.0'
DESCRIPTION = 'REST API functions Blue-Fez Ansible boilerplate module'
LONG_DESCRIPTION = 'A package that provides REST API functions Blue-Fez Ansible boilerplate module'
 
# Setting up
setup(
    name="bf_restapi",
    version=VERSION,
    author="""
        Diederick de Buck
        """,
    author_email="""
        diederick.de.buck@blue-fez.com
        """,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=['requests'],
    keywords=['python', 'REST API', 'HTTP', 'HTTPS', 'Ansible', 'collection', 'module'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
    license_files = ('LICENSE.txt',)
)