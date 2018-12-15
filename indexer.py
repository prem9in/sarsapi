import metapy
import pytoml
import json
import sys, os

class Indexer:

        def __init__(self, trace, settings):                
                self.trace = trace
                self.num_results = settings.maxSearchResults
                self.cfg = settings.cfg
                self.index = None
                self.k1 = settings.bm25_K1
                self.b = settings.bm25_b
                self.k3 = settings.bm25_k3
       
       
        def load(self):
                cfgpath = os.path.abspath(self.cfg)
                self.trace.log("Indexer.load", "Indexing from : {}".format(cfgpath))
                self.index = metapy.index.make_inverted_index(cfgpath)
                self.trace.log("Indexer.load", "Number of docs : {}".format(self.index.num_docs()))
                self.trace.log("Indexer.load", "Number of unique terms : {}".format(self.index.unique_terms()))
                self.trace.log("Indexer.load", "Average document length : {}".format(self.index.avg_doc_length()))
                self.trace.log("Indexer.load", "Number of total corpus terms : {}".format(self.index.total_corpus_terms()))
                self.trace.log("Indexer.load", "Indexing complete")
                

        def queryResults(self, searchtext):
                self.trace.log("Indexer.queryResults", "Instantiating ranker with k1 {}, b {}, k3 {}".format(self.k1, self.b, self.k3))
                ranker = metapy.index.OkapiBM25(k1=self.k1, b=self.b, k3=self.k3) 
                self.trace.log("Indexer.queryResults", "Instantiating query for text {}".format(searchtext))
                query = metapy.index.Document()
                query.content(searchtext) 
                self.trace.log("Indexer.queryResults", "Getting top {} result".format(self.num_results))
                # we need to load index (idx) at application start
                top_results = ranker.score(self.index, query, num_results = self.num_results)
                self.trace.log("Indexer.queryResults", "Returning results")
                return top_results
