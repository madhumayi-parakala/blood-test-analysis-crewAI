from functools import wraps
from flask import request, jsonify, current_app
import jwt
import os

# Secret key for encoding and decoding JWT tokens
SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

def generate_token(username):
    """
    Generates a JWT token for the given username.
    
    Parameters:
    - username: The username for which to generate the token.
    
    Returns:
    - token: The generated JWT token.
    """
    token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
    return token

def token_required(f):
    """
    Decorator to check if a token is present in the request headers.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Check for token in the request headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Bearer token format
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Decode the token
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = data['username']
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)

    return decorated
