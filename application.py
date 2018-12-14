import flask
from flask import request, jsonify
from flask_cors import CORS
import controller
import lookup
import indexer
import apptrace

debug = True
app = flask.Flask(__name__)
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

trx = apptrace.AppTrace(debug)
indx = indexer.Indexer(trx)
lp = lookup.Lookup(trx)
ctrl = controller.Controller(lp, indx, trx)

@app.errorhandler(404)  
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/v1/search', methods=['GET'])
def search():
    query_parameters = request.args
    sresults = ctrl.Search(query_parameters)
    if debug == True:
        resultWithTrace = {
            "response": sresults,
            "traces": trx.get()
        }
        return jsonify(resultWithTrace)

    return jsonify(sresults)


if __name__ == '__main__':
    trx.log("__main__", "calling ctrl.load()")
    ctrl.load()
    app.run(debug=debug)