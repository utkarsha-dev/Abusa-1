from flask import Flask, request, jsonify
from flask_cors import CORS
from Model.load_abuse import abuse
from Model.model import getData

app = Flask(__name__)
CORS(app)

@app.route('/')
def infer():
    return "Tested", 200
 
@app.route('/getAbusiveData')
def bad_words():
    return abuse, 200

@app.route('/modelData', methods = ['POST'])
def data_recieve():
    data = request.get_json(force=True)
    data = getData(data)
    
    return jsonify(data), 200
 
if __name__ == "__main__":
    app.run(debug=True)