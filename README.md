![PR Status](https://github.com/Makoto-Araki/develop_platform_template/actions/workflows/pull_request_ci.yml/badge.svg)
![Main Status](https://github.com/Makoto-Araki/develop_platform_template/actions/workflows/main_ci.yml/badge.svg)
![Release Status](https://github.com/Makoto-Araki/develop_platform_template/actions/workflows/release.yml/badge.svg)

# develop_platform_template 開発用テンプレート

## 目的
- 社内開発に最適なテンプレート作成および開発手順の備忘録、エンジニア向けの説明のため注意

## 開発履歴
| 日付       | バージョン | 説明                         |
| ---------- | --------- | --------------------------- |
| 2026/03/16 | 0.7.0     | MySQLのテスト項目追加        |
| 2026/03/15 | 0.6.0     | MySQLのIntegrationテスト実装 |
| 2026/03/14 | 0.5.0     | MySQLからデータ取得機能を実装 |
| 2026/03/14 | 0.4.0     | JSONファイルのロード関数追加  |
| 2026/03/14 | 0.3.0     | CI/CD導入                   |
| 2026/03/11 | 0.2.0     | 日本語文字列操作の関数追加    |
| 2026/03/08 | 0.1.0     | 新規作成                    |

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

## DBコンテナ起動 => MySQL関連のintegrationテスト実行時に使用
$ docker compose up -d db

## VSCode起動 => DevContainer起動時に環境構築、DevContainer起動後に開発作業
$ code .

## DevContainer内で全テスト実行
$ python -m pytest

## DevContainer内でunitテスト実行
$ python -m pytest test/unit

## DevContainer内でintegrationテスト実行
$ python -m pytest test/integration

## DBコンテナ停止 => MySQL関連のintegrationテスト実行時に使用
$ docker compose down -v
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

## DBコンテナ起動 => MySQL関連のintegrationテスト実行時に使用
$ docker compose up -d db

## VSCode起動 => DevContainer起動時に環境構築、DevContainer起動後に開発作業
$ code .

## DevContainer内で全テスト実行
$ python -m pytest

## DevContainer内でunitテスト実行
$ python -m pytest test/unit

## DevContainer内でintegrationテスト実行
$ python -m pytest test/integration

## DBコンテナ停止 => MySQL関連のintegrationテスト実行時に使用
$ docker compose down -v

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
