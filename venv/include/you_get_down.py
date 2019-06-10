import sys
import you_get


def download(url, path):
	sys.argv = ['you-get', '-o', path, url]
	you_get.main()


if __name__ == '__main__':
	# 视频网站的地址
	url = 'https://www.bilibili.com/bangumi/play/ep118488?from=search&seid=5050973611974373611'
	# 视频输出的位置
	path = 'G:/test'
	download(url, path)
