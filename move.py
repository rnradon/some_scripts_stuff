#move one file to another folder
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

# def download(url):
# 	domain = url.split('//')[-1].split('/')[0]
# 	os.makedirs(domain)
# 	response = requests.get(url)
# 	if response.status_code != 200:
# 		return
# 	soup = BeautifulSoup(response.text)
# 	img_tags  =soup.find_all('img')
# 	img_src_paths = set()

# 	for i in img_tags:
# 		src = i.get('src')
# 		if not src:
# 			ontinue
# 		if src[:7] == 'http://' or src[:8] == 'https://':
# 			img_src_paths.add(src)
# 		else:
# 			img_src_paths.add(urljoin(url,src))


# 	i = 0
# 	for img_ in img_src_paths:
# 		try:
# 			re = requests.het(img_url)
# 		except:
# 			continue
# 		i = i + 1
# 		filename = str(i) + "." + img_url.split('.')[-1]
# 		f = open(domain + '/' + filename, 'wb')
# 		f.write(re.content)
# 		f.close()

# if __name__ == '__main__':
# 	if len(sys.argv) < 2:
# 		print("Enter website url to fetch images")
# 	else:
# 		download(sys.argv[1])

# def getAbsPath(path):
# 	return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

# def internalFiles(extension, source, destination):
# 		directories = os.listdir(source)

# 		for files in directories:
# 			path = os.path.join(source, files)
# 			if(os.path.isdir(path)):
# 				internalFiles(extension, source, destination)
# 			else:
# 				fileExt = files.split('.'[-1])
# 				if(fileExt == extension):
# 					#fileName = files.split('/')[-1] can be removed because file in for is itself a relativr path
# 					os.rename(files, os.path.join(destination, fileName))


# def moveFile(extension, source, destination):
# 	print("WORKING")
# 	source = getAbsPath(source)
# 	print(source)
# 	destination = getAbsPath(destination)
# 	print(destination)

# 	if not os.path.isdir(destination):
# 		print("destination error")
# 		return
# 	if not os.path.isdir(source):
# 		print("source error")
# 		return

# 	internalFiles(extension, source, destination)



# # if __name__ == '__main__':
# #     if len(sys.argv) < 4:
# #         print("Enter extension, source, destination")
# #     else:
# #        moveFile(sys.argv[1], sys.argv[2], sys.argv[3])

# moveFile("pdf", "nf", "nf2")




def getAbsPath(path):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

def internalFiles(extension, source, destination):
		directories = os.listdir(source)

		for files in directories:
			print(files, end= ' ')
			print("FILES")
			print("AND SOURCE", end= ' ')
			print(source)
			path = os.path.join(source, files)
			print(path)
			if(os.path.isdir(path)):
				print("in if")
				internalFiles(extension, source, destination)
			else:
				fileExt = files.split('.')[-1]
				print(fileExt)
				print("in else")
				if(fileExt == extension):
					print("PDF FOUND")
					fileName = files.split('/')[-1]
					 # can be removed because file in for is itself a relativr path
					os.rename(source, os.path.join(destination, fileName))
					# os.rename(source + '', destination+'/'+fileName)

def moveFile(extension, source, destination):
	print("WORKING")
	source = getAbsPath(source)
	print(source)
	destination = getAbsPath(destination)
	print(destination)

	if not os.path.isdir(destination):
		print("destination error")
		return
	if not os.path.isdir(source):
		print("source error")
		return

	internalFiles(extension, source, destination)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Enter extension, source, destination")
    else:
       moveFile(sys.argv[1], sys.argv[2], sys.argv[3])

# moveFile("pdf", "nf", "nf2")
