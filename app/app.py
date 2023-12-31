# app.py

from flask import Flask, render_template, request
import joblib
import os

# スクリプトのあるディレクトリの絶対パスを取得
base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# モデルとベクトルライザーの読み込み（正しいファイル名を指定）
# ベースディレクトリに基づいて相対パスを設定
model_path = os.path.join(base_dir, "../notebooks/models/sentiment_analysis_model.pkl")
vectorizer_path = os.path.join(base_dir, "../notebooks/models/tfidf_vectorizer.pkl")
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = vectorizer.transform(data).toarray()
        prediction = model.predict(vect)
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)


