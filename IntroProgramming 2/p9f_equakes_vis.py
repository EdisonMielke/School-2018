''' 
World-Wide Earthquake Watch
CIS 210 W19 Project 9

Author: Edison Mielke

Credits:

Use file processing and data mining to discover patterns of earthquakle activity
around the world over the past year; plot results on a world map.
'''
import random
import math
import turtle
def readFile(filename):
    '''
    #(txt) -> dict

    #creates dictionary from a text document
    '''
    dataf = open(filename , "r")
    datadict = {}
    key = 0
    for aline in dataf:
        items = aline.split(",")
        if key !=0:
            lat = float(items[1])
            lon = float(items[2])
            mag = float(items[4])
            datadict[key] = [lon,lat,mag]
        key = key + 1
    dataf.close()
    return datadict

def euclidD(point1 , point2):
    '''
    (int,int) -> float

    calculates the distance between two points
    
    '''
    total = 0
    for index in range(len(point1)):
        diff = (point1[index]-point2[index]) ** 2
        total = total + diff
        
    euclidDistance = math.sqrt(total)
    return  euclidDistance

def createCentroids(k, datadict):
    '''
    (int, data) -> centroids
    
    creates k amount of centroids from the dictionary datadict
    '''
    
    centroids=[]
    centroidCount = 0
    centroidKeys = []
    while  centroidCount < k:
        rkey = random.randint(1,len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return  centroids

def createClusters(k, centroids , datadict , repeats):
    '''
    (int, centroid, dict, int) -> list

    Takes previous clusters, centroids, datadict, and how many repeats
    and creates a list of clusters
    '''
    for apass in range(repeats):
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey],centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/clusterLen

            centroids[clusterIndex] = sums

    return clusters

def eqDraw(k, eqDict, eqClusters):
    '''
    (int,dict,cluster) -> turtle

    draws the final image using turtle graphics
    '''
    t = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap1800_900.gif")
    quakeWin.screensize(1800,900)
    t.speed('fastest')
    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    t.hideturtle()
    t.up()
    

    for clusterIndex in range(k):
        for akey in eqClusters[clusterIndex]:
            lon = eqDict[akey][0]
            lat = eqDict[akey][1]
            mag = eqDict[akey][2]
            t.goto(lon*wFactor ,lat*hFactor)
            t.dot((2*int(mag))^2,'red')
    quakeWin.exitonclick()
    return None

def visualizeQuakes(k, r, dataFile):
    '''
    (int,int,dict -> Turtle)

    Makes the data into a more readable world map format, as opposed to dictionaries
    '''
    datadict = readFile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids , datadict , r)

    eqDraw(k, datadict, clusters)
    
    return None

def main():
    '''
    sets k and r and calls visualizeQuakes
    '''
    k = 6
    r = 7
    visualizeQuakes(k,r,"earthquakes.csv")

    return None

main()
