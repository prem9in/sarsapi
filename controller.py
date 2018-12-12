
import math
import sys
import time
import metapy
import pytoml


class Controller:

    def __init__(self, lookup, indexer):
        self.lookup = lookup
        self.indexer = indexer
        self.unknown = "UNKNOWN"


    def load(self):
        self.lookup.load()


    def filterbyLocation(self, searchResults, requestParams):
        results = []
        searchcity = requestParams["city"].lower()
        searchstate = requestParams["state"].lower()

        for res in searchResults:
            if searchcity != self.unknown and searchstate != self.unknown and res['city'].lower() == searchcity and res['state'].lower() == searchstate:
                results.append(res)

        return results


    def extractRequestParams(self, query_parameters):
        if 'text' in query_parameters:
            searchtext = query_parameters['text']
        else:
            return self.errorNoSearchText()

        if 'city' in query_parameters:
            searchcity = query_parameters['city']
        else:
            searchcity = self.unknown

        if 'state' in query_parameters:
            searchstate = query_parameters['state']
        else:
            searchstate = self.unknown
        
        if 'zip' in query_parameters:
            searchzip = query_parameters['zip']
        else:
            searchzip = self.unknown
        
        return {
            "text": searchtext,
            "city": searchcity,
            "state": searchstate,
            "zip": searchzip
        }


    def Search(self, query_parameters):
        
        requestParams = self.extractRequestParams(query_parameters)

        # call queryResults
        # qresults = self.indexer.queryResults(searchtext)
        # perform lookup
        # resultdocs = self.lookup.documentLookup(qresults)
        resultdocs = self.lookup.documentLookup({})
        # filter on location
        resultsbylocation = self.filterbyLocation(resultdocs, requestParams)



        return resultsbylocation


    def errorNoSearchText(self):
        error = {
                "code": 400, 
                "message": "Search Text not provided in request."
                }
        return error

