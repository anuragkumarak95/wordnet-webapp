from functools import wraps
from flask import jsonify, request

def check_auth(username,password):
    return username=="admin" and password=="root" 

def authenticate():
    message = {'message': "Authentication required."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        
        auth = request.authorization
        if not auth: 
            return authenticate()

        elif not check_auth(auth.username,auth.password): 
            return authenticate()
        
        return f(*args,**kwargs)
    return decorated