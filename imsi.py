from flask import Flask, request, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    insa = '안녕하세요 파이썬에서 보냈어요'
    return jsonify(insa)

@app.route("/test", methods=['POST'])
def test():
    params = request.get_json()
    print("받은 Json 데이터 ", params)
    response = {
        "result": "받기 성공"
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)