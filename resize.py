import os, sys
from PIL import Image
import glob

size = 416, 416

for dirname in sys.argv[1:]:
	files = glob.glob(str(dirname)+"*.jpg")
	for infile in files:
		outfile = os.path.splitext(infile)[0] + "_resized.jpg"
		if infile != outfile:
			try:
				im = Image.open(infile)
				im.thumbnail(size, Image.ANTIALIAS)
				im.save(outfile, "JPEG")
			except IOError:
				print ("cannot create thumbnail for '%s'" % infile)
