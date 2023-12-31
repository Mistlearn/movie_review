# Movie Review Sentiment Analysis

## 概要
Movie Review Sentiment Analysis は、映画のレビューから感情を分析するFlaskベースのWebアプリケーションです。このプロジェクトでは、映画レビューのテキストデータを処理し、ポジティブまたはネガティブな感情を予測します。

## データソース
このプロジェクトで使用した映画レビューデータは、Kaggleの「IMDb Dataset of 50K Movie Reviews」から取得しました。このデータセットには、50,000件の映画レビューが含まれており、各レビューはポジティブまたはネガティブの感情ラベルが付与されています。

データセットの詳細やダウンロード方法については、以下のリンクを参照してください：
[IMDb Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

このデータセットの使用は、Kaggleの利用規約に従っています。


## 主な特徴
- 映画レビューのテキストデータの感情分析
- Flask Webアプリケーション
- ロジスティック回帰モデルによる感情の分類

## プロジェクトのセットアップ

このプロジェクトのディレクトリ構造を作成するには、以下のコマンドを実行してください：

```bash
python setup_project_structure.py

## インストール方法
このプロジェクトをローカルで実行するには、以下の手順に従ってください。

1. リポジトリをクローンする
git clone https://github.com/Mistlearn/movie_review.git
cd movie-review-sentiment-analysis


2. 仮想環境を作成し、アクティベートする
python -m venv venv
source venv/bin/activate # Windowsの場合は venv\Scripts\activate


3. 必要な依存関係をインストールする
pip install -r requirements.txt


4. アプリケーションを実行する
python app.py


## 使い方
アプリケーションを実行した後、ブラウザを開いて `http://127.0.0.1:5000` にアクセスしてください。テキストボックスに映画レビューを入力し、「Analyze」ボタンをクリックすると、感情分析の結果が表示されます。


## 作者
Hideki Goto
