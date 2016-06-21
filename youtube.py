#crawl youtube to get a list of top songs 
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

def searchSong(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	musicLink = soup.findAll("a")
	for music in musicLink:
		print("IN FOR")
		if("#Music" in music.contents[0]):
			musicTag = music
			print("IN IF")
			print(musicTag)
			print("LEFT IF")


def findSongs(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	count = 0
	# for i in soup.findAll('li', attrs = {'class':'channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item'}):
	# 	print("IN FOR")
	# 	print(count)
	# 	print(i)
	# 	count = count+1
	musicLink = soup.findAll("a")
	for music in musicLink:
		# print("IN FOR")
		# if("#Music" in music.contents[0]):
		# 	musicTag = music
		# 	print("IN IF")
		# 	print(musicTag)
		# 	print("LEFT IF")
		if music.get('href') is not None:
			# anchorTitle = soup.findAll('a',{'class':'title'})
			href = "http://www.youtube.com"+music.get('href')
			print(count)
			print(href)
			if music.contents[0] is not None:
				print("IN IF")
				printName = music.contents[0]
				views = music.find('li')
				print(views)
				# print(views.contents[0])
				# if views.get_text() is not None:
				# 	print("IN NESTED IF")
				# 	print(printName)
				# 	print(views.contents[0])
				# # print(printName)
			else:
				print("NO CONTENT")
			count = count+1

def findSongs2(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	count = 1

	musicDiv = soup.findAll('div',{'class':'yt-lockup-content'})
	for div in musicDiv:
		musicLink = "http://www.youtube.com"+div.find('a')['href']
		if div.find('a').contents[0] is not None:
			views = div.find('li')
			viewString = views.get_text()[:-6]
			conditionViews = int(viewString.replace(',',''))
			if(conditionViews > 109368518):
				print(count)
				print(musicLink)
				printname = div.find('a').contents[0]
				print(printname)
				# views = div.find('li')
				# print(views.get_text()[:-6])
				print(conditionViews)
				# postURL(musicLink)
				print("POSTURL SUCCESS")
				print("\n")
				count = count+1

def postURL(url):
	siteURL = "http://www.youtube-mp3.org/"
	post = requests.post(siteURL,data = url)
	print(post.text)

def check(url):
	# post = requests.post("http://www.google.com",data = url)
	# print(post.text)
# import requests

	# url = 'https://duckduckgo.com/html/'
	payload = {'q':'facebook'}
	r = requests.post(url, data=payload)
	with open("requests_results.html", "w") as f:
		print(f.write(r.text))
# check("https://www.google.co.in/?gfe_rd=cr&ei=GYLLVrHUM5PLugSq1Z6QDQ&gws_rd=ssl")
# findSongs2("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
# findSongs("https://www.youtube.com")


# def check2(url):
# 	payload = {'q':'python'}
# 	r = requests.get(url,params = payload)
# 	with open("requests_results.html", "w") as f:
# 		print(f.write(r.text))

# check2("https://duckduckgo.com/html/")

listOfSongs = {}

count = 1
def findSongs3(url):
	global listOfSongs
	global count
	r = requests.get(url)
	soup = BeautifulSoup(r.text)


	musicDiv = soup.findAll('div',{'class':'yt-lockup-content'})
	for div in musicDiv:
		musicLink = "http://www.youtube.com"+div.find('a')['href']
		if div.find('a').contents[0] is not None:
			listOfSongs[url] = musicLink
			views = div.find('li')
			viewString = views.get_text()[:-6]
			conditionViews = int(viewString.replace(',',''))
			if(conditionViews >= 10000000):
				print(count)
				print(musicLink)
				printname = div.find('a').contents[0]
				print(printname)
				# views = div.find('li')
				# print(views.get_text())
				# print(conditionViews)
				# postURL(musicLink)
				# print("POSTURL SUCCESS")
				print("\n")
				count = count+1
				nestedLinks(musicLink)

def nestedLinks(url):
	global count
	global listOfSongs
	r2 = requests.get(url)
	soup2 = BeautifulSoup(r2.text)
		# print(soup2)
	print(count)
	inheritedDivs = soup2.findAll('div',{'class':'content-wrapper'})
	# print("MOVING TO NESTED FOR")

	for newDivs in inheritedDivs:
		# print("IN NESTED FOR")
		newDivsLink = "http://www.youtube.com"+newDivs.find('a')['href']
		if newDivsLink in listOfSongs:
			break
		else:

			listOfSongs[url] = newDivsLink
			views = newDivs.find('a').find('span',{'class':'stat view-count'})
			viewString = views.get_text()[:-6]
			conditionViews = int(viewString.replace(',',''))
			if(conditionViews >= 10000000):
				print(count)
				print(newDivsLink)
				print(newDivs.find('a').find('span').contents[0])
			# print("PRINTING VIEWS")
				# print(conditionViews)
				print(views.get_text())
				print("\n")
				count = count+1
				nestedLinks(newDivsLink)
	# if div.find('a').contents[0] is not None:
	# 	views = div.find('li')
	# 	viewString = views.get_text()[:-6]
	# 	conditionViews = int(viewString.replace(',',''))
	# 	# if(conditionViews > 109368518):
	# 	print(count)
	# 	print(musicLink)
	# 	printname = div.find('a').contents[0]
	# 	print(printname)
	# 		# views = div.find('li')
	# 	print(views.get_text())
	# 		# print(conditionViews)
	# 		# postURL(musicLink)
	# 		# print("POSTURL SUCCESS")
	# 	print("\n")
	# 	count = count+1
		# if inheritedDivs.findAll('a').contents[0] is not None:
	# 	print("WORKINGGGG")

findSongs3("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
