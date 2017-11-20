# This file cleans the data from the transfer csv file

import csv
r = csv.reader(open('transfers.csv'))
lines = [l for l in r]
for i in range(1, len(lines)):
	for j in range(len(lines[0])):
		lines[i][j] = str.strip(lines[i][j])
	fee = lines[i][-1]
	if fee == "Free transfer" or fee == "gratuito" or fee == "Swap deal" or \
	fee == "Bonservissiz" or fee == "Libre para traspaso":
		lines[i][-1] = 0
	elif "Mill" in fee:
		ix = lines[i][-1].index('.') # Index of first occurrence of '.'
		lines[i][-1] = 1000000*float(lines[i][-1][:ix+3])
	elif "Th" in fee:
		ix = lines[i][-1].index(' ') # Index of first occurrence of ' '
		lines[i][-1] = 1000*float(lines[i][-1][:ix])
	elif fee == '?' or fee == '-':
		lines[i][-1] = -1
	else:
		ix = lines[i][-1].index(' ') # Index of first occurrence of ' '
		lines[i][-1] = float(lines[i][-1][:ix])



# Write ammended data back to file
writer = csv.writer(open('transfers2.csv', 'w'))
writer.writerows(lines)