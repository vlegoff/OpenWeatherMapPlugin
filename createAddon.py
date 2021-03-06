"""This script creates the addon file (.nvda-addon).

It should be called to create the nvda-addon file from the source
tree.  Are included:
  manifest.ini -- the file describing the add-on
  globalPlugins -- the path containing the global plugin itself

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import os
from zipfile import ZipFile

def recursiveWrite(archive, path):
	"""Write into the archive the path and its content."""
	archive.write(path)
	if os.path.isfile(path):
		return

	for subpath in os.listdir(path):
		subpath = "/".join((path, subpath))
		if subpath.endswith(".pyc"):
			continue
		elif subpath.endswith("/tests"):
			continue
		else:
			recursiveWrite(archive, subpath)

with ZipFile('OpenWeatherMapPlugin.nvda-addon', 'w') as archive:
	archive.write("manifest.ini")
	recursiveWrite(archive, "globalPlugins")
