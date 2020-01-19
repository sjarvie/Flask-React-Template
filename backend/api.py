
from flask import Blueprint
api = Blueprint('api', __name__)

#from app import app, db
from flask import jsonify, request, current_app
import models 
from app import db

# sample hello world page
@api.route('/')
def hello():
    return "<h1>Response from Hello World Handler!</h1>"

# sample api endpoint
@api.route('/api/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # get parameters from post request
        parameters = request.get_json()
        if 'test' in parameters:
            return jsonify({'value': parameters['test']})
        return jsonify({'error'})
    else:
        rows = TestRow.query.all()
        return jsonify({'test': 'success'})

    

# create a test row
@api.route('/api/test_rows', methods=['GET', 'POST'])
def test_rows():
    if request.method == 'POST':
        params = request.get_json()
        try:
            row = models.TestRow(params.get("data"))
            db.session.add(row)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify({'result': 'failure'})
        return jsonify({'result': 'success'})