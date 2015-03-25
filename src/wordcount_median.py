#!/usr/bin/env python

import os
import collections

def count(wc_input, wc_output):

	data_files = os.listdir(wc_input)
	os.chdir(wc_input)
	
	with open('temp.txt', 'w') as outfile:
		for files in data_files:
			if files.endswith('txt'):
				with open(files) as infile:
					for line in infile:
						outfile.write(line+'\n')

	data = open('temp.txt' , 'r')

	text = data.read()
	content = [word.strip('.,?/:"{)(-!').lower() for word in text.split()]

	y = {}

	os.chdir(wc_output)
	wc_result = open('wc_result.txt', 'w')
	wc_result.write('*** WORD COUNT ***' + '\n' + '\n')

	for word in content:
			
		x = content.count(word)
		y[word] = x

	sort = collections.OrderedDict(sorted(y.items()))
		
	for i, j in sort.items():
		wc_result.write(str(i) + ' ' + str(j) + '\n')

	median(wc_input, wc_output)


def median(wc_input, wc_output):

	os.chdir(wc_input)

	stripped = [line.strip() for line in open('temp.txt')]

	lis = []

	for lines in stripped:
		words = lines.split(' ')
		x = len(words)
		lis.append(x)

	lis = [0 if x==1 else x for x in lis]

	os.chdir(wc_output)
	median_calc(lis, wc_output)



def median_calc(lis, wc_output):

	os.chdir(wc_output)
	wc_result = open('med_result.txt', 'w')
	wc_result.write('*** MEDIAN ***' + '\n' + '\n')

	for i in range(1, len(lis)+1):

		temp = lis[0:i]
		temp.sort()
		
		if len(temp) % 2 == 0:
			try:
				mid = len(temp) / 2
				res1 = (temp[mid] + temp[mid-1]) / 2.0
				wc_result.write(str(res1) + '\n')
			
			except:
				mid = lis[i]
				wc_result.write(str(mid) + '\n')


		else:
			mid = (len(temp) - 1) / 2
			res2 = temp[mid] / 1.0
			wc_result.write(str(res2) + '\n')



def main():

	wc_input = 'C:/Users/Vikas/Desktop/wc_input'
	wc_output = 'C:/Users/Vikas/Desktop/wc_output'

	if not os.path.exists(wc_output):
		os.mkdir(wc_output)

	else:
		pass
	
	count(wc_input, wc_output)

		
main()
