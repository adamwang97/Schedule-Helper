from .scraper import *


def ranker(l):
    total = 0
    for i in l:
        name = i.get_instructors()
        if(getRatings(name)!=None):            
            for k in getRatings(name):
                total+= float(k)
    return total

def rank(l):
    toReturn = []
    for i in l:
        toReturn.append((i,ranker(i)))
    return toReturn
