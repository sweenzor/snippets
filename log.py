import os
import time

os.system('title Work Log')
target = '../log.txt'

while True:
	os.system('cls')
	
	with open(target, 'r+') as f:
		initial = f.readlines()

	for line in initial[-6:]:
		print line[:-1][:76]
	print '\n'

	entry = raw_input("New Log Entry: ")
	entrytime = time.strftime("%a %d %b %Y %H:%M", time.localtime())

	with open(target, 'a') as f:
		f.write('\n')
		f.write(entrytime)
		f.write('\t')
		f.write(entry)
		f.write(' ')