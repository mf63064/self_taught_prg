# バージョン管理
# コードベース
#   ソフトウェアのためのフォルダやファイルの集まりで他の人の変更を全員で共有するもの。
# バージョン管理システム（vcs:version control system）
#   チーム内のコードの変更と共有問題を解決するためのもの
#   GitとSVNが人気のバージョン管理システム。
# ここからはGitでコードバージョンを管理し、GitHubというWebサービスにコードを保存する方法を実施する。
# Git
#   分散管理バージョン。DVCS(Distoributed Version Control System)
#   ネットに繋がっていなくてもコミット出来きる。pushやpullで中央リポジトリ等のリモートリポジトリと同期するまで共有されない。
# SVN
#   ネットに繋がっていないとコミット自体できない。コミットと中央リポジトリとの同期が同じ意味を持つ

# リポジトリ
#   GitのようなVCSによって作られるデータの構造。リストや辞書もデータ構造。
#   コードの変更を記録しているデータ構造にアクセル出来る。
#   ディレクトリやファイルが置いてある。

# ローカルリポジトリ
#   チームメンバー個人がコードの変更差分を記録しておく。
# 中央リポジトリ(リモートリポジトリ多分)
#   GitHubのようなウェブサイトで提供され、全てのローカルリポジトリは中央リポジトリと同期している。
#   自分のリポジトリ、他人のリポジトリが常に中央リポジトリを通して同期される。
# プッシュ
#   ローカルリポジトリの内容を中央リポジトリに同期させること。
# プル
#   中央リポジトリの新しい差分をローカルリポジトリに同期させること。

# githubでリポジトリを新規作成
#   ログイン後右上の+ボタンをクリック
#   new repository を選ぶ
#   リポジトリ名をつける
#   publicを選択
#   initialeze the repository with a read meにチェック
#   create repositoryをクリック

# リポジトリをダウンロード 
#   ダウンロードしたいディレクトリに移動して$ git clone リポジトリurl
#     $ git clone https://github.com/mf63064/hangman.git

# 中央リポジトリのurl表示方法
#   ローカルリポジトリ（ここではhangmanディレクトリ）へ移動。
#   git remote -v  #-vはverboseの意味。多くの情報を出力すると言う意味
#     https://github.com/mf63064/hangman.git (fetch)
#     https://github.com/mf63064/hangman.git (push)
#   と表示される。1行目がプル、2行目がプッシュ、の中央リポジトリのurl。通常同じurl。プッシュとプルの相手は同じ中央リポジトリのなので。

# プル、プッシュをしてみる。
# ローカルリポジトリにhangmanのコードのファイルを作成。

# プッシュの手順
#   各ファイルがステージ状態かどうかを確認する：ローカルリポジトリのディレクトリで$ git status
#     赤表示が非ステージ状態、緑がステージ状態
#   ステージ状態にする：中央リポジトリにプッシュしたい変更がどれかをgitに伝えること
#     ローカルリポジトリで$ git add ステージにしたいファイル名 
#       git add hangman.py
#   ステージ状態を取り消す
#     ローカルリポジトリで$ git reset ステージにしたいファイル名
#       git reset hangman.py
#   コミットする：ステージ状態の変更差分をローカルリポジトリへ保存すること。
#     ローカルリポジトリで$ git commit -m "メッセージ" 
#       git commit -m "my first commit"
#   fatal: unable to auto-detect email address と出た時の対処法
#     gitに自分をわかるようにすれば良い。
#       $ git config --global user.email ここに自分のアドレス
#       $ git config --global user.name ここに自分の名前
#   中央リポジトリへプッシュする
#     $ git push origin master
#       変更、追加したコードをoriginというリモートリポジトリのmasterブランチにpush（アップロード）するという意味。
#       これではエラーがでた。fatal: 'master' does not appear to be a git repository
#       masterが存在しないとのこと
#     $ git push origin
#       これでいった。webにもupされてた。
#     masterとoriginの違い
#       master：ブランチのマスターのこと。今回はブランチが存在しないためマスターもない。多分。
#       origin：リモートリポジトリのurlのこと。多分。

# プルしてみる
#   githubのサイトでhangmanの中にnew.pyファイルを作成。「add file」ボタンをクリック。
#   $ git pull origin master
#   これではエラーがでた。多分ブランチがないから。
#   $ git pull
#   これでいけた。ファイルもできてた。

# ローカルリポジトリを前のverに戻す
#   全てのフォルダとファイルをその時点の状態に戻すこと、最新のコミットまで進めることもできる。
#   コミットには番号（id文字列）があり、gitはこのコミット番号で各コミットを判別する。
#      コミット番号（id）を確認する
#       $git log
#      コミットをしてして元に戻す。
#       $git checkout コミット番号

# 差分
# ファイルの状態とローカルリポジトリとの差分を表示する
#     ローカルリポジトリのディレクトリで $ git diff ファイル名


