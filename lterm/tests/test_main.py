import os
import sys
from lterm import lterm


def test_all():
	sys.argv.append('-h')
	l = lterm.lterm()
