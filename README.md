# develop_platform_template 開発用テンプレート

## 前提条件
- Docker Desktopがインストール済みでKubernetesクラスタを有効化
- Docker DesktopでDockerhubにログイン済み
- 基本的にWSLターミナル上で作業 (DevContainer内の作業も存在)

## 開発環境構築＋開発作業＋テスト実行
```bash
## Githubのリモートリポジトリからクローン
$ git clone ...

## Dockerイメージのビルド
$ docker build -t develop_platform_template_image -f .devcontainer/Dockerfile-dev .

## VSCode起動 => DevContainer起動後にDevContainer内で開発作業開始
$ code .

    ## DevContainer内でテスト実行
    $ pytest
```

