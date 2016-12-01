[![Build Status](https://travis-ci.org/killswitch-GUI/lterm.svg?branch=master)](https://travis-ci.org/killswitch-GUI/lterm)
[![Code Health](https://landscape.io/github/killswitch-GUI/lterm/master/landscape.svg?style=flat)](https://landscape.io/github/killswitch-GUI/lterm/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/85266d6254694b50b76b03a4cffd73d9)](https://www.codacy.com/app/iamfree2009/lterm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=killswitch-GUI/lterm&amp;utm_campaign=Badge_Grade)
[![PyPi version](https://img.shields.io/pypi/v/lterm.svg)](https://pypi.python.org/pypi/lterm)

# lterm
lterm is a small script built to install a bash hook for full terminal logging. I use this on Red Team engagments to track down and log issues. This is very helpful for backup of crictical data you may lose do to powerloss etc.

## Install lterm

### Install via git
You can do this to maintain newest version.
```
$ git clone https://github.com/killswitch-GUI/zlib_wrapper.git
$ python setup.py install
```

### Install via pip
Easy to setup and runs from any user global $PATH
```
$ pip install lterm
```

## Run lterm
open up a terminal:
```
$ lterm.py -h

usage: lterm.py [-i] [-l /root/test/] [-r] [-v] [-b]

lterm is utility to log all bash windows opened by any user on the system.
This offten is useful for data logging on critical systems.

optional arguments:
  -i              Install logging
  -l /root/test/  Logging location (full path)
  -r              Remove Logging and restore to intial state, this will
                  attempt to use the backup file created from -b
  -v              Set verbose output
  -b              Backup RC file during install

```

## Example Usage: YouTube
[![Example](http://img.youtube.com/vi/3rbCTW_IBrk/0.jpg)](https://www.youtube.com/watch?v=3rbCTW_IBrk&feature=youtu.be "Example")
