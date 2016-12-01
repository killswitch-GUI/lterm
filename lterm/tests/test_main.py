import os
import sys
from lterm import lterm


def test_all():
	l = lterm.lterm(test_cmd='-h')
	l.execute()
	l = lterm.lterm(test_cmd='-i')
	l.execute()
	l = lterm.lterm(test_cmd='-i -v')
	l.execute()
	l = lterm.lterm(test_cmd='-i -v -l ~/ -b')
	l.execute()
	l = lterm.lterm(test_cmd='-i -v -l ~/')
	l.execute()
	l = lterm.lterm(test_cmd='-r -v')
	l.execute()