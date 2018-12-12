import json

class Lookup:

    def __init__(self):
        self.lookup = {}
       
    def load(self):
        with open('data\lookup.json') as json_file:  
            self.lookup = json.load(json_file)
        
    def get(self):
        return self.lookup
    
    def documentLookup(self, qresults):
        lookupresult = []
        lookupItems = self.lookup
        for item in lookupItems:
            lookupresult.append(lookupItems[item])
        return lookupresult

