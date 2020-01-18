from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# declare constants
HOST = '0.0.0.0'
PORT = 5000
SQLALCHEMY_DATABASE_NAME= 'test_db'
SQLALCHEMY_DATABASE_URI = f"postgresql://localhost/{SQLALCHEMY_DATABASE_NAME}"

# initialize flask application
app = Flask(__name__)
# add SQL connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# sample hello world page
@app.route('/')
def hello():
    return "<h1>Response from Hello World Handler!</h1>"

# sample api endpoint
@app.route('/api/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # get parameters from post request
        parameters = request.get_json()
        if 'test' in parameters:
            return jsonify({'value': parameters['test']})
        return jsonify({'error'})
    else:
        return jsonify({'test': 'success'})


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
