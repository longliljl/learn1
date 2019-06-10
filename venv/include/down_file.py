# coding=utf-8

# !/usr/bin/python

import os

import requests

from bs4 import BeautifulSoup

# 给请求指定一个请求头来模拟chrome浏览器
global headers
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

# 定义存储位置

global save_path
save_path = 'G:\\xigua'


def do_load_media(url, path):
	try:
		pre_content_length = 0
		# 循环接收视频数据
		while True:
			# 若文件已经存在，则断点续传，设置接收来需接收数据的位置
			if os.path.exists(path):
				headers['Range'] = 'bytes=%d-' % os.path.getsize(path)
			res = requests.get(url, stream=True, headers=headers)

			content_length = int(res.headers['content-length'])
			# 若当前报文长度小于前次报文长度，或者已接收文件等于当前报文长度，则可以认为视频接收完成
			if content_length < pre_content_length or (
					os.path.exists(path) and os.path.getsize(path) == content_length):
				break
			pre_content_length = content_length

			# 写入收到的视频数据
			with open(path, 'ab') as file:
				file.write(res.content)
				file.flush()
				print('receive data，file size : %d  total size:%d' % (os.path.getsize(path), content_length))
	except Exception as e:
		print(e)


def load_media(src):
	do_load_media(src, save_path)


def get_video_src(url):
	res = requests.get(url, headers=headers)
	# 使用自带的html.parser解析
	soup = BeautifulSoup(res.text, 'html.parser')
	video = soup.find('div', class_='player')
	src = video.attrs['src']
	return src


def main():
	url = 'https://www.ixigua.com/i6588499309950403080/'
	src = get_video_src(url)
	load_media(src)


if __name__ == '__main__':
	main()
