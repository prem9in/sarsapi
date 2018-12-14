import flask
from flask import request, jsonify
from flask_cors import CORS
import controller
import lookup
import indexer

debug = False
app = flask.Flask(__name__)
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

indx = indexer.Indexer()
lp = lookup.Lookup()
ctrl = controller.Controller(lp, indx)

@app.errorhandler(404)  
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/v1/search', methods=['GET'])
def search():
    query_parameters = request.args
    sresults = ctrl.Search(query_parameters)
    return jsonify(sresults)


if __name__ == '__main__':
   
    ctrl.load()
    app.run(debug=debug)