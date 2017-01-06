from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Index(Resource):
    def get(self, ):

        return {'message': 'Hello world'}, 200