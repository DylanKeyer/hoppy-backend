from flask_restful import Resource
from flask import jsonify

def api_response(HTTP_code, result, error_message, original_request):
    return jsonify(
        HTTP_CODE = HTTP_code,
        Result = result,
        Error_Message = error_message,
        Original_Request = original_request.get_json()
    )

class HomePage(Resource):
    def get(self):
        return 'Please refer to the API documentation.'