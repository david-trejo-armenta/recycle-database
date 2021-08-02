from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
import db_config as database
from flask_cors import CORS

#Resources
from res.user import User
from res.profile import Profile
from res.goal import Goal
from res.reward import Reward
from res.career import Career
from res.transactions import Transaction



app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/all/school/')
def get_all_school_utch():
    response = list(database.db.Recycling.find({'school': {"$eq":"1"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)
    
@app.route('/all/school/')
def get_all_school_uach():
    response = list(database.db.Recycling.find({'school': {"$eq":"2"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/school/')
def get_all_school_itch():
    response = list(database.db.Recycling.find({'school': {"$eq":"3"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/grade/')
def get_all_grade():
    response = list(database.db.Recycling.find({'grade': {"$eq":"5"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/career/')
def get_all_career():
    response = list(database.db.Recycling.find({'carrer': {"$eq":"2"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)


@app.route('/all/transactions/')
def get_all_user_transactions():
    response = list(database.db.Badges.find({}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/')
def get_all_user_information():
    response = list(database.db.Badges.find({}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)


api.add_resource(User, '/user/new/', '/user/<string:by>:<string:data>/')
api.add_resource(Transaction, '/transaction/new/', '/transaction/<string:by>:<string:data>/')
api.add_resource(Career, '/career/<carrer>/')
api.add_resource(Profile, '/profile/new/', '/profile/<string:_id>/', '/profile/<string:by>/<string:data>/')
api.add_resource(Goal, '/goal/new/', '/goal/<string:by>:<string:data>/')
api.add_resource(Reward, '/reward/new/', '/reward/<string:by>:<string:data>/')


if __name__ == '__main__':
    app.run(load_dotenv = True)