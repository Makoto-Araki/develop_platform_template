# develop_platform_template 開発用テンプレート

## 目的
- 社内開発に最適なテンプレート作成および開発手順の備忘録、エンジニア向けの説明のため注意

## 開発履歴
2026/03/11 - 0.2.0 - 関数追加
2026/03/08 - 0.1.0 - 新規作成

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

## 環境構築＋開発作業＋テスト実行
説明の都合上、リモートリポジトリ名とローカルリポジトリ名を同名にしている
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

## DevContainer内でテスト実行
$ pytest
```

## 手動デプロイ(CI/CD導入前)
- Docker Desktop上のKubernetesクラスタをデプロイ先に想定
- Namespace名はuser-appsに想定
- KubernetesリソースはCronjobリソースを使用

```bash
## 本番用のDockerイメージをビルド
$ docker build --no-cache -t makotoaraki346/develop_platform_template_image:X.Y.Z -f .devcontainer/Dockerfile .

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

## KubernetesクラスタにCronjobリソース作成
$ kubectl apply -n user-apps -f k8s/cronjob.yaml

## KubernetesクラスタのCronjobリソース確認
$ kubectl get cronjob -n user-apps
```


