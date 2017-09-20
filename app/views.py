from app import app
from flask import jsonify, request
import json
from .auth import requires_auth

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
