# パッケージ管理ツール
#   プログラムの管理やインストールを行うプログラム。
#   パッケージ管理ツールpipを学ぶ。

# パッケージ
#   梱包されたソフトウェア。プログラムファイルやメタデータが含まれる。
# メタデータ
#   ソフトウェアの名前やバージョンプログラムが動作するのに必要な他のパッケージへの依存関係といった情報。
# パッケージ管理ツールがやること
#   パッケージをダウンロードしてそのコンピュータ上で動作するようにインストールしていく。
#   そのパッケージの動作に必要なその他のパッケージも依存関係に基づいてダウンロード、インストールしていく。
# $pip
# pipの使い方
#   pip install パッケージ名
# pipのインストール先
#   pythonのsite-packagesディレクトリを使う。
# インストールできるパッケージはここを見ればわかる
#   http://pypi.python.org/pypi

# ウェブフレームワークの一つflaskをインストールしてみる。
# インストール方法
#   最新バージョンをインストールする場合。
#     $ sudo pip install Flask
#   バージョンを指定してインストールする場合。
    # $ sudo pip install Flask==0.11.1

#pythonでflaskを使ってみる。
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def index():
#   return "hello world!"
# app.run(port=8000)
# flaskモジュールはウェブサーバーのプログラムを書く手伝いをする。ウェブサイトを素早く作成できる。
# 詳しく学ぶならここhttp://flask.pocoo.org/docs/0.11/tutorial

# pip freeze
#   インストールしたパッケージの一覧をみる。
# pip uninstall パッケージ名
#   パッケージをアンインストールする。

# Flaskをアンインストールしてみる。
# sudo pip uninstall Flask