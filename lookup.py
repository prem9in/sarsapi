import json
import sys, os

class Lookup:

    def __init__(self, trace, settings):
        self.lookup = {}
        self.trace = trace
        self.filepath = settings.lookupFilePath
       
    def load(self):
        self.trace.log("Lookup.load", "Number of items before loading file: {}".format(len(self.lookup)))
        self.trace.log("Lookup.load", "Path to load file: {}".format(self.filepath))
        with open(os.path.abspath(self.filepath), encoding="utf8") as json_file:  
            self.lookup = json.load(json_file)
            self.trace.log("Lookup.load", "File loaded, number of items loaded: {}".format(len(self.lookup)))
      
        
    def get(self):
        return self.lookup
    
    
    def documentLookup(self, qresults, max_results):
        lookupresult = []
        lookupItems = self.lookup        
        count = 0
        # for item in qresults:
        for item in lookupItems:
            if item in lookupItems:
                lookupresult.append(lookupItems[item])
                count = count + 1
                if count >= max_results:
                    break
        return lookupresult

