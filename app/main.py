from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from utils.list_helpers import union_list, count_dictionary
from services.preference_service import extract_top_5_list
from routers.router_test import test_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(test_bp)

@app.route('/')
def home():
    insa = '안녕하세요.'
    return jsonify(insa)

@app.route("/test", methods=['POST'])
def post_test():
    params = request.get_json()
    print(request.headers["Authorization"])
    # print("받은 Json 데이터 ", params)
    response = {
        "result": "받기 성공"
    }

    return jsonify(response)



@app.route('/movie-list', methods=['GET'])
def send_movie_list():
    with open("./test_data/movie_list.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        movieNames = []
        for data in datas["movies"]:
            movieNames.append(data["name"])

        return jsonify(movieNames)



@app.route('/preference', methods=['GET'])
def send_preference():
    age = request.args.get('age') #query의 age를 가져온다
    v = request.args.get('v') #query의 age를 가져온다
    print(v)
    print(age)
    return jsonify('전송')

@app.route('/user-info', methods=["GET"])
def get_user_info():
    option = request.args.get('option') # all과 top_5로 받을것

    with open("./test_data/movie-information.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        users = datas["users"]

        ages = []

        twenties_like_list = [] # 20대의 like 리스트들의 배열의 값을 넣는다.
        twenties_like_dictionary = {}

        for user in users :            
            if "age" in user : # dictionary의 key값을 가지고 있는지 확인
                ages.append(user["age"])
                if 20 <= user["age"] < 30 : # 20대의 인원
                    # print(f"{user['name']}는 20대 입니다")
                    
                    if "preferences" in user : # 선호도값을 가지고 있다면
                        user_pref_list = user["preferences"]
                        if "like" in user_pref_list : #like를 가지고 있다면
                            twenties_like_list = union_list(twenties_like_list, user_pref_list["like"])

                            for item in user_pref_list["like"]:
                                count_dictionary(twenties_like_dictionary, item)
        
        top_5 = extract_top_5_list(twenties_like_dictionary)
        print(twenties_like_list)

        if option == 'all' :
            return jsonify(twenties_like_list)
        else :
            return jsonify(top_5)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)