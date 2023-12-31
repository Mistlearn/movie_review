import os
import json

# プロジェクトのディレクトリ構造を定義
project_structure = {
    "movie_reviews_sentiment_analysis": [
        "data/raw",
        "data/processed",
        "notebooks",
        "models",
        "app/static",
        "app/templates"
    ]
}

# プロジェクトのディレクトリ構造を作成
for key, value in project_structure.items():
    for folder in value:
        os.makedirs(os.path.join(key, folder), exist_ok=True)

# Jupyter Notebookの基本構造
basic_notebook_structure = {
    "cells": [],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

# ノートブックファイルのリスト
notebooks = [
    "01_data_preprocessing.ipynb",
    "02_feature_extraction.ipynb",
    "03_model_training.ipynb",
    "04_application_development.ipynb"
]

# ノートブックファイルを作成
for notebook in notebooks:
    notebook_path = os.path.join("movie_reviews_sentiment_analysis/notebooks", notebook)
    with open(notebook_path, 'w') as f:
        json.dump(basic_notebook_structure, f)

# その他の必要なファイルを作成
other_files = [
    "app/app.py",
    "requirements.txt",
    "README.md"
]

for file in other_files:
    file_path = os.path.join("movie_reviews_sentiment_analysis", file)
    with open(file_path, 'w') as f:
        pass  # ファイルを空で作成

print("プロジェクト構造が作成されました。")
