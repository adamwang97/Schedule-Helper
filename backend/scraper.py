import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
import re


def getRatings(str):
	url_base = "http://www.ourumd.com/reviews/"	
	first,last = str.split()
	
	if last == "TBA":
		return none
		
	url_request = url_base + last + ",%20" + first[0] + "/"
	contents = urllib.request.urlopen(url_request).read()
	soup = BeautifulSoup(contents, "html.parser")
	
	img_tag = soup.find_all("img")	
	ratings = list()
	
	#grabs and matches the ratings
	for tag in img_tag:
		src_re = tag['src']
		match = re.search('stars/\?avg=(\d\.?\d*)', src_re)
		if match is not None:
			ratings.append(match.group(1))
		

	#remove the overall rating
	if(len(ratings)==0):
                return None
	ratings.pop(0)
	return(ratings)
	
def getReviews(str):
	url_base = "http://www.ourumd.com/reviews/"	
	first,last = str.split()
	
	if last == "TBA":
		return none
		
	url_request = url_base + last + ",%20" + first[0] + "/"
	contents = urllib.request.urlopen(url_request).read()
	soup = BeautifulSoup(contents, "html.parser")
	
	reviews = list()
	td_tag = soup.select("tr td")	
	
	for x in range(3, len(td_tag), 2):
		tag = td_tag[x]
		
		review = tag.string
		if review is None:
			text = tag.get_text().split("<br>")
			temp = ""
			for i in text:
				temp += i
			review = temp		
		
		reviews.append(review)
		
	return reviews
		
	
