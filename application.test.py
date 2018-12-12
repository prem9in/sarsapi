import math
import sys
import time
import metapy
import pytoml
import application as app


def stdout(listtoprint, title):
    print(title)
    for item in enumerate(listtoprint):
        print(item)
    print()


def starttest():
    searchcity = app.unknown
    searchstate = app.unknown
    searchzip = app.unknown
    # get results
    resultdocs = app.documentLookup({})
    stdout(resultdocs, "Printing document results")
    # filter on location
    resultsbylocation = app.filterbyLocation(resultdocs, searchcity, searchstate, searchzip)
    stdout(resultsbylocation, "Printing document by location")


# execute
if __name__ == '__main__':
    starttest()