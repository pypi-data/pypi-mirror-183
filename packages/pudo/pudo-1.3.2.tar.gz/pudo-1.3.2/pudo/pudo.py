#!/usr/bin/python3
import os
import sys
import subprocess


def run(cmd):
	'''
	Usage:
		user$ python3 # or python2
		>>> from pudo import pudo
		>>> (ret, out) = pudo.run(('ls', '/root')) # or pudo.run('ls /root')
		>>> print(ret)
		>>> 0
		>>> print(out)
		>>> b'Desktop\\nDownloads\\nPictures\\nMusic\\n'
	'''
	from . import PUDO_BINARY
	if (not os.access(PUDO_BINARY, os.X_OK)):
		raise FileNotFoundError
	if not os.stat(PUDO_BINARY).st_mode & stat.S_ISUID:
		print('Please Accept the Disclaimer using the following command:')
		print('\t$ sudo pudo --accept-disclamer')
		raise Exception('Disclaimer Not Accepted')
	if (isinstance(cmd, str)):
		cmd = cmd.split()
	elif (isinstance(cmd, tuple)) or (isinstance(cmd, list)):
		cmd = (PUDO_BINARY, ) + cmd
	else:
		print('Unsupported cmd object: %s' %(repr(cmd)))
		raise TypeError
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	(out, _) = process.communicate()
	ret = process.wait()
	return(ret, out)


if (__name__ == '__main__'):
	(ret, out) = run(' '.join(sys.argv[1:]))
	print(out)
	sys.exit(ret)
