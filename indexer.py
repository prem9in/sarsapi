import metapy
import pytoml
import json

class Indexer:

        def __init__(self):
                self.index = {}
                self.num_results = 10
       
        def load(self):
                with open('./data/business_topicModels.json', encoding="utf8") as json_file:  
                        self.index = json.load(json_file)
                
        def get(self):
                return self.index


        def queryResults(self, searchtext):
                ranker = metapy.index.OkapiBM25() 
                query = metapy.index.Document()
                metapy.index.make_inverted_index()
                query.content(searchtext)  
                # we need to load index (idx) at application start
                top_results = ranker.score(self.index, query, num_results = self.num_results)
                return top_results
