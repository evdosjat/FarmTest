s = open('x').read()
curIndex = 1
while True:
	start = s.index(str(curIndex) + '.')
	end = s.find(str(curIndex + 1) + '.')
	if end < 0:
		end = len(s)

	curS = s[start+len(str(curIndex))+1:end].strip()
	curS = curS[curS.find(']')+1:].strip()
	curS = curS.replace('а)', '\n-').replace('б)', '\n-').replace('в)', '\n-').replace('г)', '\n-')
	curS = curS.replace('А)', '\n-').replace('Б)', '\n-').replace('В)', '\n-').replace('Г)', '\n-')
	print(curIndex)
	with open('temp/' + str(curIndex), 'w') as f:
		f.write(curS)

	if end == len(s):
		break
	else:
		curIndex += 1
		s = s[end:]
