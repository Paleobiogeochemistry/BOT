#!/usr/bin/env python

#correr desde consola

import math
import sys

#------------------------------------------------------------------

def calculateDistance(x1,y1,x2,y2):
    d = []
    for i in range(len(x1)):
        dist = math.sqrt(((x2-x1[i])**2)+((y2-y1[i])**2))
        d.append(dist)
    return d


def extractMesurement(fileName, latitude, depth):
    latitudeSource =[]
    depthSource = []
    dataSource = []
    archivo = open(fileName,"r")
    lineas = archivo.readlines()
    lineas.pop(0)
    archivo.close()
    for iLinea in lineas: #lineas es el elemnto a recorrer
        k = iLinea.split()
        latitudeSource.append(float(k[0]))
        depthSource.append(float(k[1]))
        dataSource.append(float(k[2]))
        
    distance = calculateDistance(latitudeSource, depthSource,latitudeGap,depthGap)
   
    i_min = 0
    min_value = distance[0]
    for i in range(len(distance)):
        if distance[i] < min_value:
            min_value = distance[i]
            i_min = i
    return (latitudeSource[i_min] ,depthSource[i_min] , dataSource[i_min])


#input------------------------------------------------------------------
latitudeGap  = float(sys.argv[1])
depthGap = float(sys.argv[2])
fileSource = sys.argv[3]


#output-----------------------------------------------------------------
result = extractMesurement(fileSource, latitudeGap, depthGap)
print(fileSource, latitudeGap, depthGap, result[0], result[1], result[2])

