# Bash：コマンドラインインターフェース。
#       macで言うとターミナル。ここから先はコマンドラインと呼ぶ。
#       shellを同義。
# コマンドラインのドルマーク：ドルマーク、スペースの次の文字からコマンドラインで実行すると言う意味。
# echo:print関数と同じ。
# コマンドラインでは色々なプログラムが使える。
# pythonを使ってみる。
# $ python3
# enter
# print("hello world")
# enter

# pythonを終了
# exit()
# コマンド履歴一覧
# history

# 相対パスvs絶対パス
# ディレクトリ：フォルダのこと
# パス：ディレクトリやファイルがos内のどこにあるのかを表したもの。
# Bash使用中はどこかのディレクトリにいてパスで正確に表現できる。
# pwd：作業ディレクトリパスを表示
# print working directoryの意味。


# ツリー構造
# 自分のいるディレクトリはツリー構造で表現される。
# トップをルートとよぶ。
# ツリー構造の例
#                       root
#                       / \
#                   home   etc
#                   /          \
#             bernie            bin
#             /    \
#          test    projects
# 絶対パス：ルートディレクトリからたどったもの。パスを / から書くと絶対パスのこと
# 例：/home/bernie/test
# 相対パス：現在の作業ディレクトリからたどったもの。最初の文字が / ではない。
# 例（作業ディレクトリがhomeの場合）：bernie/test

# 作業ディレクトリの変更。change directory
# cd 絶対パス    
# cd 相対パス    
# cd /  でルート    
# cd ~ で自分のホームディレクトリに移動
# cd .. 一つ親のディレクトリに移動
#  
# 作業ディレクトリに何があるかを表示。listの意味
# ls

# 新ディレクトリの作成
# mkdir ディレクトリ名

# ディレクトリ削除
# rmdir ディレクトリ名

# コマンドの動作を変更する
#  ls と ls -author の違い
# lsではauthorフラグがFalseで ls -author ではauthorフラグがTrueになっている。

# ショートオプション：ls -a
# ロングオプション：ls --all
# 同じ意味。
# 以下の３つも同じ意味
# ls --all --time=use --sort=time
# ls -a -u -t
# ls -aut

# 構造やフラグの意味の確認には
# https://explainshell.com
# が便利。

# 隠しファイル
#   隠しファイル名は.で始まる
#   隠しファイルの表示はlsコマンドに引数-aフラグを渡す

# ファイルを作成
#   touch : ファイルを作成

# 隠しファイルを作成してみる
#   touch .sef_taught

#   ls
#   lsでは.self_taughtファイルは表示されない
#   ls -a
#   ls -aでは表示される

# パイプ  
#   あるコマンドの実行結果を別のコマンドへの入力として渡せる。
# 例
#   ls | less
#   qで終了

# 環境変数  
#   osに値を記録しておくための変数。
#   プログラムは実行されている環境のコンピュータ名やos名などを環境変数から取得して使用可能。
#   環境変数はBashウィンドウの中だけで使用可能。終了して起動するとなくなる。

# 環境変数を表示する書き方
#   $printenv
#     USER=FUJITAMASAAKIのように現在設定されている環境変数が表示される。

# 環境変を設定する書き方
#   export 変数名 = 変数の値
#   例：新しい環境変数を設定してみる。Bash（ターミナル）で設定してみる。
#   export x = 100
#   echo $x
#   $マークは環境変数の意味。$がないと文字xが表示される。

# どんな操作を許可するのかの権限：パーミッションと言う。
# whoami:ユーザー名を表示
# 権限のもっとも高いユーザー：rootユーザー
# sudo:super user do の略
# 例
# sudo echo x  #「echo x」をrootユーザーとして実行と言う意味。
# Bashの参考
# http://theselftaughtprogrammer.io/bash

# ファインダーで隠しファイルを表示：shift + command + .

# チャレンジ
# Bashで「self-taught」出力しよう
# echo self-taught
# ホームディレクトリ以外のパスからホームディレクトリに現在の作業ディレクトリを移動しよう。絶対パス、相対パス
# cd ~
# 環境変数を作ってどこかのパスを設定しその環境変数を使って作業ディレクトリを移動しよう。
# export p=/Users/fujitamasaaki/Desktop/独学プログラマー
# cd $p


# メモ
# 新規ファイル作成
#   touch ファイル名
# ファイル削除
#   rm ファイル名
# ファイル中身確認
#   cat ファイル名
# ディレクトリ削除
#   rm -r
# 補完機能
#   途中まで打ってtab
# コマンド履歴の利用
#   ↑キー
# フォルダ作成
#   mkdir ディレクトリ名
# カレントディレクトリ表示
#   pwd   (print working directory)
# カレントディレクトリのフォルダ、ファイル一覧を表示
#   ls    (list)
# 親のディレクトリへ移動
#   cd ..
# ファイルを移動させる
#   mv 移動させるファイル名 移動先のディレクトリ名
#   mv 移動させるディレクトリ名 移動先のディレクトリ名
# ファイル名変更
#   mv 現在のファイル名 新しいファイル名
#   mv 現在のディレクトリ名 新しいディレクトリ名
# ファイルコピー
#   cp コピーするファイル名 新しいファイル名
#   cp コピーするディレクトリ名 新しいディレクトリ名
# ディレクトリ全部コピー
#   cp -r


