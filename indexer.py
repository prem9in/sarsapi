import metapy
import pytoml

class Indexer:
      def queryResults(self, searchtext):
        ranker = metapy.index.OkapiBM25() 
        query = metapy.index.Document()
        query.content(searchtext)  
        # we need to load index (idx) at application start
        top_results = ranker.score(idx, query, num_results=5)
        return top_results
