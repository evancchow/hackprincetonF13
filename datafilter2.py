#python datafilter2.py data1.json data2.json datastats.json

# goes from data1.json into data2.json and datastats.json (for stats)

# Takes formatted JSON data and creates freqdict with keys/values. removes keys without values, 
# and also skips if value is not a number.

import sys, re, time

start_time = time.time() ###

itemCount = 0;
stFile = open(sys.argv[1], 'r+')
stFinal = open(sys.argv[2], 'r+')
stStats = open(sys.argv[3], 'r+')

## pop into word frequency dict
fromlist = list()
for line in stFile:
	strLine = str(line)
	strLine = re.sub('\n','',strLine)
	strLine = strLine.split(": ")
	# remove keys without values
	if len(strLine) == 1:
		continue
	# skip if value is not a number
	if strLine[1].isdigit() is False:
		continue
	fromlist = fromlist + strLine

	# write data ready to be parsed
	stFinal.write(strLine[0])
	stFinal.write(' ')
	stFinal.write(strLine[1])
	stFinal.write('\n')

	itemCount+=1

## record itemCount as last thing in file
print "Number of words: ",itemCount
stStats.write(str(itemCount))

print time.time() - start_time, "seconds" ###