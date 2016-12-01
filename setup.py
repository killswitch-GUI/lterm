from setuptools import setup

setup(name='lterm',
      version='0.1',
      description='lterm is a small script built to install a bash hook for full terminal logging.',
      url='http://github.com/killswitch-GUI/lterm',
      author='Alexander Rymdeko-Harvey',
      author_email='lolyearight@cybersyndicates.com',
      license='GNU 3.0',
      packages=['lterm'],
      install_requires=[
          'argparse',
      ],
      scripts = [
        'lterm/lterm.py'
      ],
      zip_safe=False)