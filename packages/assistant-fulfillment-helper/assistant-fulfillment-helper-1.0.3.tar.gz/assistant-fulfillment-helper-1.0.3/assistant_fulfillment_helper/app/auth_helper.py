from flask import jsonify

def error_authentication_message(message=None):
    '''
    Create an error message with 401 status code.
    Returns:
        resp: Response with error message and status code 401.
            json
    '''
    if not message:
        message = 'Authorization, or X-Auth-Key and X-Auth-ConnectorId is invalid. Please authenticate.'
    resp = jsonify({"message": message})
    resp.status_code = 401
    return resp
