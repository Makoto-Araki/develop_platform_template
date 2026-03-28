![PR Status](https://github.com/Makoto-Araki/develop_platform_template/actions/workflows/pull_request.yaml/badge.svg)
![Main Status](https://github.com/Makoto-Araki/develop_platform_template/actions/workflows/main_ci.yaml/badge.svg)
![Release Status](https://github.com/Makoto-Araki/develop_platform_template/actions/workflows/release.yaml/badge.svg)

# develop_platform_template 開発用テンプレート

## 目的
- 社内開発に最適なテンプレート作成および開発手順の備忘録、エンジニア向けの説明のため注意

## 開発履歴
| 日付       | バージョン | 説明                                           |
| ---------- | --------- | ---------------------------------------------- |
| 2026/03/29 | 0.12.0    | kube-linter導入(KubernetesのYAML品質向上)       |
| 2026/03/28 | 0.11.0    | mypy導入(静的型チェックによる品質向上)            |
| 2026/03/22 | 0.10.0    | テーブル結合の処理追加                           | 
| 2026/03/21 | 0.9.0     | SQL文をORMモデルに変更                          |
| 2026/03/20 | 0.8.0     | コード品質向上のためRuff導入                     |
| 2026/03/18 | 0.7.2     | ChromeとChromeDriverの存在確認をUnitテストに追加 |
| 2026/03/17 | 0.7.1     | MySQL結合テスト用の初期化スクリプトの役割分担     |
| 2026/03/16 | 0.7.0     | MySQLのテスト項目追加                           |
| 2026/03/15 | 0.6.0     | MySQLのIntegrationテスト実装                    |
| 2026/03/14 | 0.5.0     | MySQLからデータ取得機能を実装                    |
| 2026/03/14 | 0.4.0     | JSONファイルのロード関数追加                     |
| 2026/03/14 | 0.3.0     | CI/CD導入                                      |
| 2026/03/11 | 0.2.0     | 日本語文字列操作の関数追加                       |
| 2026/03/08 | 0.1.0     | 新規作成                                        |

## 社内開発環境
- Windows11
- Docker Desktop (Kubernetes有効化 + Dockerhubログイン済)
- VSCode
- WSL
- Github (リモートリポジトリ)
- Dockerhub (Dockerイメージ保存先)

## 前提条件
- Docker Desktopがインストール済でKubernetesクラスタ有効化
- Docker DesktopでDockerhubにログイン済
- Githubにアクセス可
- Dockerhubにアクセス可
- WSL Terminal上で作業 (DevContainer内の作業も存在)
- WSL Terminal上でkubectlが使用可能でKubernetesクラスタ接続可

## コード品質管理 (Ruff)
- Ruffの設定はpyproject.tomlで一元管理
- DevContainer内でコード保存時に自動フォーマットおよび修正
- WSL Terminal上でgit commit時に自動チェック
- PR作成時にCIで最終チェック

## 静的型チェック (mypy)
- DevContainer内で型チェックを実行
- PR時にCIで型整合性を検証
- 実行前に型不整合を検出し、バグを未然に防止
- 型チェック対象はsrcディレクトリ配下(アプリケーションコードのみ対象)

## Kubernetesマニフェスト検証 (kube-linter)
- kube-linter によりKubernetesマニフェストの静的解析を実施
- セキュリティ設定やリソース定義などのベストプラクティス違反を検出
- DevContainer内でローカルチェック可能
- PR作成時にCIで自動検証

## CI/CD導入前の開発手順
### 環境構築＋開発作業＋テスト実行
- リモートリポジトリ名とローカルリポジトリ名を同名にしている
- テスト実行時にコマンド失敗したら python -m pytest を実行してみる

```bash
## ディレクトリ作成
$ mkdir develop_platform_template

## ディレクトリ移動
$ cd develop_platform_template

## ローカルリポジトリ初期化
$ git init

## メインブランチ設定
$ git branch -M main

## リモートリポジトリ設定
$ git remote add origin git@github.com:Makoto-Araki/develop_platform_template.git

## Githubのリモートリポジトリからクローン
$ git clone git@github.com:Makoto-Araki/develop_platform_template.git

## VSCode起動 => DevContainer起動時に環境構築、DevContainer起動後に開発作業
$ code .

## DevContainer内でRuffチェック
$ ruff check .

## DevContainer内でRuff修正
$ ruff format . --check

## DevContainer内でmypy型チェック
$ mypy src

## DevContainer内で全テスト実行
$ python -m pytest

## DevContainer内でunitテスト実行
$ python -m pytest test/unit

## DevContainer内でintegrationテスト実行
$ python -m pytest test/integration

## DevContainer内でkubernetesのYAMLチェック
$ kube-linter lint ./k8s
```

### 手動デプロイ
- Docker Desktop上のKubernetesクラスタをデプロイ先に想定
- Namespace名はuser-appsに想定
- KubernetesリソースはCronjobリソースを使用

```bash
## 本番用のDockerイメージをビルド
$ docker build \
    --no-cache \
    -t makotoaraki346/develop_platform_template_image:X.Y.Z \
    -f .devcontainer/Dockerfile .

## 本番用のDockerイメージをDockerhubにプッシュ
$ docker push makotoaraki346/develop_platform_template_image:X.Y.Z

## Kubernetesクラスタの稼働確認
$ kubectl get nodes

## Kubernetesクラスタのコンテキスト一覧
$ kubectl config get-contexts

## Kubernetesクラスタのコンテキスト確認
$ kubectl config current-context

## Kubernetesクラスタのコンテキスト切替
$ kubectl config use-context コンテキスト名

## Kubernetesクラスタのnamespace確認
$ kubectl get namespaces

## Kubernetesクラスタにnamespace作成
$ kubectl create namespace user-apps

## KubernetesクラスタのCronjobリソース差分チェック
$ kubectl diff -n user-apps -f k8s/cronjob.yaml

## KubernetesクラスタにCronjobリソース作成
$ kubectl apply -n user-apps -f k8s/cronjob.yaml

## KubernetesクラスタのCronjobリソース確認
$ kubectl get cronjob -n user-apps
```

## CI/CD導入後の開発手順
### 開発用ブランチ作成＋開発作業＋リモートリポジトリへプッシュ
- ブランチ名は feature/******* という名称で統一
- リモートリポジトリ上で issue を作成しておくこと

```bash
## 開発用ブランチ作成
$ git checkout -b feature/*******

## 開発用ブランチ確認
$ git branch

## VSCode起動 => DevContainer起動時に環境構築、DevContainer起動後に開発作業
$ code .

## DevContainer内でRuffチェック
$ ruff check .

## DevContainer内でRuff修正
$ ruff format . --check

## DevContainer内でmypy型チェック
$ mypy src

## DevContainer内で全テスト実行
$ python -m pytest

## DevContainer内でunitテスト実行
$ python -m pytest test/unit

## DevContainer内でintegrationテスト実行
$ python -m pytest test/integration

## DevContainer内でkubernetesのYAMLチェック
$ kube-linter lint ./k8s

## ステージング移行
$ git add .

## コミット ※11はissue番号
$ git commit -m "feature/*******(#11)"

## プッシュ
$ git push origin feature/*******
```

### リモートリポジトリ
- プルリクエスト作成
- マージ実行 (mainブランチに統合)

### ブランチ統合
```bash
## ブランチ切替
$ git checkout main

## ブランチ確認
$ git branch

## プル
$ git pull origin main

## 開発ブランチ削除
$ git branch -d feature/*******
```

### デプロイ作業
- DockerイメージのビルドとDockerhubへのアップロード (CI) は自動化済み
- KubernetesクラスタへのCronjobリソース更新 (CD) は手動で行う

```bash
## Kubernetesクラスタの稼働確認
$ kubectl get nodes

## Kubernetesクラスタのコンテキスト一覧
$ kubectl config get-contexts

## Kubernetesクラスタのコンテキスト確認
$ kubectl config current-context

## Kubernetesクラスタのコンテキスト切替
$ kubectl config use-context コンテキスト名

## Kubernetesクラスタのnamespace確認
$ kubectl get namespaces

## Kubernetesクラスタにnamespace作成
$ kubectl create namespace user-apps

## KubernetesクラスタのCronjobリソース差分チェック
$ kubectl diff -n user-apps -f k8s/cronjob.yaml

## KubernetesクラスタにCronjobリソース作成
$ kubectl apply -n user-apps -f k8s/cronjob.yaml

## KubernetesクラスタのCronjobリソース確認
$ kubectl get cronjob -n user-apps
```
