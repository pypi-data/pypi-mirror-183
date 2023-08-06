import os
import re
from setuptools import setup

_long_description = """
### How to import the Rubik's library

``` bash
from rubixgram import Client
```

### How to install the library

``` bash
pip install rubixgram==1.0.3
```

### My ID in Rubika

``` bash
@MeDarkCoder
```
"""

setup(
    name = "rubixgram",
    version = "1.1.0",
    author = "Mohamad",
    author_email = "rubixgram@gmail.com",
    description = ("Robot Rubika"),
    license = "MIT",
    keywords = ["rubixgram","Rubika","rubika","Robot","robot","Rubixgram"],
    url = None,
    packages=['rubixgram'],
    long_description=_long_description,
    long_description_content_type = 'text/markdown',
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: Implementation :: PyPy",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11'
    ],
)
