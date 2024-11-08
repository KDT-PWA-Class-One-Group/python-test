from flask import Blueprint, jsonify

# Blueprint를 사용하여 라우터 이름 정의.
# bp는 blueprint
test_bp = Blueprint('test', __name__, url_prefix='/api')

@test_bp.route('/test', methods=['GET'])
def get_info():
    return jsonify({"test": "OK", "message": "서버가 정상 동작 중입니다."})

@test_bp.route('/test2', methods=['GET'])
def get_test2():
    return jsonify({"code": 200, "msg": "테스트2번"})