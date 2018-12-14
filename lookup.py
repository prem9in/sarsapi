import json

class Lookup:

    def __init__(self):
        self.lookup = {}
       
    def load(self):
        with open('./data/yelp_pennsylvania_business_recommendation_dataset.json', encoding="utf8") as json_file:  
            self.lookup = json.load(json_file)
        
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

