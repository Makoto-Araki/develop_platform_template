FROM makotoaraki346/python_base_image:v1.3.0

# PIP更新
RUN pip install --upgrade pip

# コンテナ内の作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルを先にコピー(ビルドキャッシュの最適化のため)
COPY requirements/requirements.txt requirements/requirements.txt

# requirements.txtに基づきPythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements/requirements.txt

# 残りのソースコードをコンテナ内にコピー
COPY . .

# バッチ処理実行
CMD ["python", "src/main.py"]
