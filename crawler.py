#crawl imdb to get a csv file full of top movies 
import requests
from bs4 import BeautifulSoup
import os, csv

class movieObj:
    movieName = None
    directorName = None
    rating = None

    def printObject():
        print(movieName)
        print(directorName)
        print(rating)

noOfMovies = 0
listOfMovies = {}


def crawlThisPage(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text , "lxml")
    temp = movieObj()
    name = soup.find_all("div" , class_="title_wrapper")
    name = name[0].h1.get_text()
    print(name)
    if(name in listOfMovies):
        return False
    listOfMovies[name] = {}
    listOfMovies[name]["url"] = url
    rating = soup.find_all("div" , class_="ratingValue")
    listOfMovies[name]["rating"] = rating[0].span.get_text();
    director = soup.find_all("div" , class_="credit_summary_item")
    listOfMovies[name]["director"] = director[0].span.get_text()
    print(name)
    print(listOfMovies[name])
    return True


def writeList():
    # print("in print list")
    # for item in listOfMovies.keys():
    #     # print("name : "+item + "\nlink : " + item[url] + "\ndirector : " + item[director] + "\nrating : "+item[rating])
    #     print(item)
    #     print(listOfMovies[item])
    os.chdir("/media/neelansh/New Volume/elixir jan/python/moviesCrawler/")
    with open("listofmovies.csv" , "w") as toWrite:
        writer = csv.writer(toWrite, delimiter=",")
        writer.writerow(["name" , "url" , 'rating' , "director"])
        for i in listOfMovies.keys():
            writer.writerow([i , listOfMovies[i]["url"] , listOfMovies[i]["rating"] , listOfMovies[i]["director"]])


def getLinks(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text , "lxml")
    links = soup.find_all("div" , class_="rec-title")
    href = []
    for link in links:
        href.append("http://www.imdb.com/"+link.a.attrs["href"])
    return href;


def init(url):
    global noOfMovies
    global listOfMovies
    href = getLinks(url)
    count = 0
    while (True):
        if(noOfMovies == 50):
            writeList()
            break
        if(crawlThisPage(url)):
            href = getLinks(url)
            url = href[0]
            noOfMovies += 1
            count = 0
        else:
            url = href[count]
            count += 1
    return

init("http://www.imdb.com/title/tt0111161/")
