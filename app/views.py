import os
from app import app
from wordnet import *
from flask import jsonify, request
import json
from .auth import requires_auth


word_net = retrieve_net(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/data/network_sample.wrnt'
    )


resource = {
    1:{
        'name':'Anurag',
        'age':22
    },
    2:{
        'name': 'tushar',
        'age': 17
    }
}

@app.route('/')
def home():
    return 'Hello There.'

'''
Example views: only experimental
'''
@app.route('/index/<id>')
def homeindex(id):
    return 'index'+str(id)

@app.route('/api/<int:i>')
@requires_auth
def api(i):
    if i not in resource : return not_found()
    resp = jsonify(resource[i])
    resp.status_code = 200
    return resp

'''
main views start here onwards.
'''
@app.route('/api/net/<root>')
def get_words(root):
    output = {
        'words': return_net(root, word_net, depth=1)
    }

    resp = jsonify(output)
    resp.status_code = 200
    return resp

'''
Error Handlers
'''
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

