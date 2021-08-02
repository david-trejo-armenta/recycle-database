from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Transaction(Resource):
    ''' Handeling the data from one user at a time '''

    def get(self,by,data):
        response = self.abort_if_not_exist(by, data)
        response['_id'] = str(response['_id'])
        
        return jsonify(response)

    def post(self):
        _id = str(database.db.transaction.insert_one({
                "glass": request.json["glass"],
                "aluminum": request.json["aluminum"],
                "username": request.json["username"],
        }).inserted_id)

        return jsonify({"_id": _id})

    def put(self, by, data):
        response = self.abort_if_not_exist(by, data)

        for key, value in request.json.items():
            response[key] = value

        database.db.transaction.update_one({'_id':ObjectId(response['_id'])},
        {'$set':{
            'username': request.json['username'],
        }})

        response['_id'] = str(response['_id'])
        return jsonify(response)

    def abort_if_not_exist(self,by,data):
        if by == "_id":
            response = database.db.transaction.find_one({"_id":ObjectId(data)})
        else:
            response = database.db.transaction.find_one({f"{by}": data})

        if response:
            return response
        else:
            abort(jsonify({"status":404, f"{by}": f"{data} not found"}))