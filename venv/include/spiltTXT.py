# !/usr/bin/python
"""
 拆分文件
"""

filepath = "E:/test/jims.log"
path = "E:/test/"
global temp
temp = ''
global toPath
toPath = ''
global w


def spilt_file():
	global temp
	global toPath
	with open(filepath, 'r') as f:
		for line in f.readlines():
			if line == "\n":
				break
			else:
				date = line.split()[0]
				if date.startswith('2019') and date != temp:
					temp = date
					toPath = path + 'jims_' + date + '.log'
					print(toPath)
					w = open(toPath, 'a+')
					w.write(line)
				else:
					w = open(toPath, 'a+')
					w.write(line)


def main():
	spilt_file()


if __name__ == '__main__':
	main()
