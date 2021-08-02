from flask import Flask, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Career(Resource):
    """ handeling profile behavior """

    def get(self, carrer):
        response = self.abort_if_not_exist(carrer)
        response['carrer'] = str(response['carrer'])
        return jsonify(response)

    def abort_if_not_exist(self, carrer):
        response = database.db.Badges.find_one({'carrer': carrer}, {"name": 1, "profile": 1})

        if response:
            return response
        else:
            abort(jsonify({"status": 404, "carrer": f"{carrer} not found"}))

















''' @app.route('/transaction/', methods=['GET'])
def get():
    id = request.args.get("id")
    c_quantity = request.args.get("cardboard_quantity")
    g_quantity = request.args.get("glass_quantity")
    a_quantity = request.args.get("aluminium_quantity")
    time =  request.args.get("created_at")
    return jasonify(
        "transaction" = {
            "cardboard_quantity": c_quantity
            "glass_quantity": g_quantity
            "aluminium_quantity": a_quantity
            "created_at": time
        }
    ) '''