from flask import Flask, render_template, send_file
# render_template를 이용해서 HTML연결
# render_template를 사용할 파일은 모두 templates라는 폴더안에 들어가야 된다.
import matplotlib.pyplot as plt
import io

app = Flask(__name__) # 파스칼 케이스 생성자

# 데이터 시각화 함수
def create_scatter_plot():
    # 예제 데이터
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 25]

    # 산점도 생성
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, color='blue')
    plt.title('Sample Scatter Plot') # 타이틀
    plt.xlabel('X-axis') # x축
    plt.ylabel('Y-axis') # y축

    # 이미지를 메모리로 저장
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()  # 메모리 절약을 위해 닫기
    return img

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    return 'hello'

@app.route('/plot.png')
def plot_png():
    img = create_scatter_plot()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)