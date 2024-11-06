from flask import Flask, render_template, send_file
# render_template를 이용해서 HTML연결
# render_template를 사용할 파일은 모두 templates라는 폴더안에 들어가야 된다.
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# 데이터 시각화 함수
def create_scatter_plot():
    # 예제 데이터
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 25]

    # 산점도 생성
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, color='blue')
    plt.title('Sample Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # 이미지를 메모리로 저장
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()  # 메모리 절약을 위해 닫기
    return img

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
    img = create_scatter_plot()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)