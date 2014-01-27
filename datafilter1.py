# python datafilter1.py data1.json data2.json
# goes from data1.json into data2.json

import sys
import re
import json
from collections import defaultdict
from nodebox.graphics import *
from nodebox.graphics.physics import *

# Keys w/o values prob -- fixed in keyvalue.py
# Convert file to just words
stFile = open(sys.argv[1], 'r')
stFileOut = open(sys.argv[2], 'w')
for line in stFile:
	strLine = str(line)

	strLine = re.sub('[0-9a-zA-Z_"]:{','\n', strLine)
	strLine = re.sub('{"','',strLine)
	strLine = re.sub(',"','\n',strLine)
	strLine = re.sub('":',': ',strLine)
	strLine = re.sub('"','',strLine)
	strLine = re.sub('[{}]','',strLine)
	# remove blank lines
	strLine = "\n".join([s for s in strLine.splitlines() if s])

	stFileOut.write(strLine)
	stFileOut.write('\n')