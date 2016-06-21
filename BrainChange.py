#Scrape skill share classes
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

def profileView(url):
    global listOfSongs
    global count
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    followerClass = soup.find('div', {'class': 'follow-stat left'})
    followers = followerClass.find('div', {'class':'number'})
    print("FOLLOWERS")
    print(followers.contents[0])
    topicsList = soup.findAll('li',{'class':'class-row col-12'})
    for topic in topicsList:
        topicTitleClass = topic.find('p', {'class':'title-link'})
        topicTitleFollowSpan = topic.find('span', {'class':'ss-icon-user num-students left'})
        print("\nTOPIC NAME\n")
        print(topicTitleClass.find('a').contents[0])
        print("\n \nNUMBER OF STUDENTS IN THE ABOVE COURSE")
        print(topicTitleFollowSpan.contents[0])
        print("---------------------")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter a website url to fetch images")
    else:
        profileView(sys.argv[1])
