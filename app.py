from flask import Flask, jsonify



app = Flask(__name__)

@app.route('/',methods = ['GET'])
def hello_heroku():
    return jsonify(
        title = 'hello_heroku!',
    )

@app.route('/',methods = ['POST'])
def fetch_data_sample():
    # personality = request.form['personality']
    # weight = request.form['weight']
    # face_value = request.form['face_value']
    # height = request.form['height']

    #値をどうやって受け取るか・値をどのようにするか
    personality = 82
    weight = 59
    face_value = 4
    height = 180

    return jsonify(
        personality = personality,
        weight = weight,
        face_value = face_value,
        height = height
    )
    

if __name__ == '__main__':
    app.run(debug=True)