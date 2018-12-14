
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

    # begin private methods

    def __filterbyLocation__(self, searchResults, requestParams):
        results = []
        searchcity = requestParams["city"].lower()
        searchstate = requestParams["state"].lower()

        for res in searchResults:
            if searchcity != self.unknown and searchstate != self.unknown and res['city'].lower() == searchcity and res['state'].lower() == searchstate:
                results.append(res)

        return results

    def __reduceResult__(self, parentList, smallList):
        reduced = []
        for keyitem in parentList:
            found = False
            for item in smallList:
                if keyitem['business_id'] == item['business_id']:
                    found = True
                    break
            if found == False:
                reduced.append(keyitem)
        return reduced

            

    def __extractRequestParams__(self, query_parameters):
        if 'text' in query_parameters:
            searchtext = query_parameters['text']
        else:
            return self.__errorNoSearchText__()

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

    def __bySentiment__(self, item):
        return float(item['sentiment'])


    def __errorNoSearchText__(self):
        error = {
                "errorCode": 400, 
                "message": "Search Text not provided in request."
                }
        return error

    # end private methods

    # begin public methods
    def Search(self, query_parameters):
        
        requestParams = self.__extractRequestParams__(query_parameters)
        if 'errorCode' in requestParams:
            return requestParams

        # call queryResults
        # qresults = self.indexer.queryResults(requestParams['text'])
        # perform lookup
        # resultdocs = self.lookup.documentLookup(qresults)
        resultdocs = self.lookup.documentLookup({}, 50)
        # filter on location
        resultsbylocation = self.__filterbyLocation__(resultdocs, requestParams)
        resultsNotbylocation = self.__reduceResult__(resultdocs, resultsbylocation)

        requestResults = {
            "searchResults": sorted(resultsbylocation, key=self.__bySentiment__, reverse=True),
            "recommendations": sorted(resultsNotbylocation, key=self.__bySentiment__, reverse=True) 
        }

        return requestResults


    def load(self):
        self.lookup.load()
        self.indexer.load()

    # end public methods

