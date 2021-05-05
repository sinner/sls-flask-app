from flask import Flask
import json
import ast

appVersion = 'v1.0.0'

class LocalFlask(Flask):
    def process_response(self, response):
        #Every response will be processed here first
        response.headers['App-Version'] = appVersion
        success = True if response.status_code in [ 200, 201, 204 ] else False
        message = 'Ok' if success else 'Error'
        dict_str = response.data.decode("UTF-8")
        dataDict = ast.literal_eval(dict_str)
        
        standard_response_data = {
            'success': success,
            'message': message,
            'result': dataDict
        }
        response.data = json.dumps(standard_response_data)

        super(LocalFlask, self).process_response(response)
        return response
