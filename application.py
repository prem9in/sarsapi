import flask
from flask import request, jsonify
from flask_cors import CORS
import math
import sys
import time
import metapy
import pytoml


app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

unknown = "UNKNOWN"

def errorNoSearchText():
    error = {
            "code": 400, 
            "message": "Search Text not provided in request."
            }
    return jsonify(error)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

def queryResults(searchtext):
    ranker = metapy.index.OkapiBM25() 
    query = metapy.index.Document()
    query.content(searchtext)  
    # we need to load index (idx) at application start
    top_results = ranker.score(idx, query, num_results=5)
    return top_results

def documentLookup(qresults):
    # we will have to perform a reverse look up and provide the results
    # for now returning some dummy results
    searchResults = [
        {
            'rank': 1,
            'businessName': 'Chat House',
            'city': 'Bellevue',
            'state': 'WA',
            'address': 'Near FredMyer.',
            'recommended': True,
            'setimentScore': 0.89
        }, {
            'rank': 2,
            'businessName': 'Baitong',
            'city': 'Redmond',
            'state': 'WA',
            'address': 'Near Bank of America.',
            'recommended': True,
            'setimentScore': 0.89
        },{
            'rank': 3,
            'businessName': 'Kanishka',
            'city': 'Redmond',
            'state': 'WA',
            'address': 'Near Redmond towncenter',
            'recommended': True,
            'setimentScore': 0.89
        },
    ]

    return searchResults


def filterbyLocation(searchResults, searchcity, searchstate, searchzip):
    results = []
    searchcity = searchcity.lower()
    searchstate = searchstate.lower()

    for res in searchResults:
        if searchcity != unknown and searchstate != unknown and res['city'].lower() == searchcity and res['state'].lower() == searchstate:
            results.append(res)

    return results
    
def mergeResults(fullresults, filtered):
    


@app.route('/v1/search', methods=['GET'])
def search():
    query_parameters = request.args
    if 'text' in query_parameters:
        searchtext = query_parameters['text']
    else:
        return errorNoSearchText(), 400

    if 'city' in query_parameters:
        searchcity = query_parameters['city']
    else:
        searchcity = unknown

    if 'state' in query_parameters:
        searchstate = query_parameters['state']
    else:
        searchstate = unknown
    
    if 'zip' in query_parameters:
        searchzip = query_parameters['zip']
    else:
        searchzip = unknown

    # call queryResults
    # qresults = queryResults(searchtext)
    # perform lookup
    # resultdocs = documentLookup(qresults)
    resultdocs = documentLookup({})
    # filter on location
    resultsbylocation = filterbyLocation(resultdocs, searchcity, searchstate, searchzip)



    return jsonify(resultsbylocation)


if __name__ == '__main__':
    app.run(debug=True)