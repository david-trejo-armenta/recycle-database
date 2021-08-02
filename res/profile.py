from flask import Flask, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Profile(Resource):
    """ handeling profile behavior """

    def get(self,by,data):
        response = self.abort_if_not_exist(by, data)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    def post(self):
        _id = str(database.db.profile.insert_one({
            "name": request.json["name"],
            "last name": request.json["last_name"],
            "state": request.json["state"],
            "city": request.json["city"],
            "enrollment": request.json["enrollment"],
            "zip code": request.json["zip_code"],
            "carrer": request.json["carrer"],
            "grade": request.json["grade"],
            "school": request.json["school"],
            "username": request.json["username"]
            
        }).inserted_id)

        return jsonify({"Profile _id": _id})

    def put(self, by, data):
        response = self.abort_if_not_exist(by, data)

        for key, value in request.json.items():
            response[key] = value

        database.db.profile.update_one({'_id':ObjectId(response['_id'])},
        {'$set':{
            "name": request.json["name"],
            "last name": request.json["last_name"],
            "state": request.json["state"],
            "city": request.json["city"],
            "enrollment": request.json["enrollment"],
            "zip code": request.json["zip_code"],
            "carrer": request.json["carrer"],
            "grade": request.json["grade"],
            "school": request.json["school"],
        }})

        response['_id'] = str(response['_id'])
        return jsonify(response)

    def abort_if_not_exist(self,by,data):
        if by == "_id":
            response = database.db.profile.find_one({"_id":ObjectId(data)})
        else:
            response = database.db.profile.find_one({f"{by}": data})

        if response:
            return response
        else:
            abort(jsonify({"status":404, f"{by}": f"{data} not found"}))

