import re
if __name__ == '__main__':
	count = 0
	content = []
	updated_content = []
	with open('raw.html') as f:
	    content = f.readlines()
	for line in content:
		if '{' in line:
			line = re.sub('\{.*?\}', '{' + str(count) + '}', line)
			count = count + 1
		updated_content.append(line)
	print ''.join(updated_content)