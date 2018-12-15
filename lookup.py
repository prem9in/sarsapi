import json
import sys, os

class Lookup:

    def __init__(self, trace, settings):
        self.trace = trace
        self.filepath = settings.lookupFilePath
       

    def load(self):
        lookupdata = {}
        self.trace.log("Lookup.load", "Number of items before loading file: {}".format(len(lookupdata)))
        lookupPath = os.path.abspath(self.filepath)
        self.trace.log("Lookup.load", "Path to load file: {}".format(lookupPath))
        
        with open(lookupPath, encoding="utf8") as json_file:  
            lookupdata = json.load(json_file)
            self.trace.log("Lookup.load", "File loaded, number of items loaded: {}".format(len(lookupdata)))
        return lookupdata

        
    def get(self):
        return self.lookup
    
    
    def documentLookup(self, qresults, lookupdata, max_results):

        lookupresult = []     
        count = 0
        for item in qresults:
        # for item in lookupdata:
            if item in lookupdata:
                lookupresult.append(lookupdata[item])
                count = count + 1
                if count >= max_results:
                    break
        return lookupresult

