# open関数でファイルを開く
# open引数１：ファイルのパス
# open引数２：どんなモードで開くかの文字列
# r：ファイルを読み込み専用で開く。
# w：ファイルを書き出し専用で開く。 すでにあるファイルパスを指定すると上書きされる。ファイルがまだない場合新規作成される。
# w+：は良い書き両方で切るようにファイルを開く。 すでにあるファイルパスを指定すると上書きされる。ファイルがまだない場合新規作成される。

# パスを組み立てる関数os.path.join関数
# フォルダの名前を入れていくとパスを作ってくれる。
# import os
# print(os.path.join("Users", "fujitamasaaki", "Downloads", "data.csv"))

# ファイルを開いて文章を書いて閉じる。書き出し専用で開く。
# st = open("/Users/fujitamasaaki/Desktop/独学プログラマー/st.txt", "w")
# st.write("Hi from Python!!")
# st.close()

# 日本語でファイル文字列を書き込む場合
# st = open("/Users/fujitamasaaki/Desktop/独学プログラマー/st.txt", "w", encoding="utf-8")
# st.write("pythonからこんにちは")
# st.close()

# ファイルを自動的に閉じる
# with open (ファイルパス, モード) as 変数名:
    # コード
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/st.txt", "w", encoding="utf-8") as f:
#     f.write("python意外と簡単だな！")

# ファイルから読み込む
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/st.txt", "r", encoding="utf-8") as f:
#   print(f.read())
# encoding ="utf-8"はアスキー文字のみで書かれている場合でも記載しておいて問題ない。
# windowsでよく使われているシフトjisの場合はencoding="cp932"と記載する

# read()メソッドはファイル内のイテラブルのオブジェクトを返す。ファイル開いてから一度だけ使える。
# 何度も使いてたい場合は変数に代入しておくと便利
# my_list = []
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/st.txt", "r", encoding="utf-8") as f:
#   my_list.append(f.read())
# print(my_list)

# csvファイル
# csvファイルを書き出す
# csv:comma separated values
# デリミタ：区切り文字
# writer()メソッド:ファイルオブジェクトとデリミタを受け取ってcsvオブジェクトを返す。白紙のcsvを返すイメージ。
# writerrow()メソッド:csvオブジェクトのメソッド。リストで受け取ってcsvファイルに書き出す。2行書くにはwriterowが必要。
# import csv
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/st.csv", "w", newline="") as f:
#   w = csv.writer(f, delimiter=",")
#   w.writerow(["one", "two", "three"])
#   w.writerow(["four", "five", "six"])

# csvファイルを読込む。ファイルと同じコンテンツと同じように表示する。
# import csv
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/st.csv","r") as f:
#   r = csv.reader(f,delimiter=",")
#   for row in r:
#     print(",".join(row))
# forを入れずにprint(r)だけだと
# <_csv.reader object at 0x7f966240cf90>が返ってきた。
# for入れてjoinなしだとテキストとして読む。
# ['one', 'two', 'three']
# ['four', 'five', 'six']が返ってきた。テキストとして読んでいる。

# チャレンジ
# pcの中にある何かのファイルをpythonで開いて、コンテンツを出力しよう。
# encoding=""のパターン shift-jisだいたいこれ。utf-8これもよく使う。jisメールなど。euc extendedunixcode日本語unixで使用。
# import csv
# with open("/Users/fujitamasaaki/Downloads/data.csv","r",encoding="shift-jis") as f:
#   r = csv.reader(f,delimiter=",")
#   for row in r:
#     print(",".join(row))

# 何か質問するプログラムを書き、入力された回答をファイルに書き出そう。
# answer = input("What do you want?:")
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/challenge.txt","w",encoding="shift-jis") as f:
#   f.write(str(answer))


# リストのリストに含まれている要素をcsvファイルに書き出す。
# データの各要素はcsvの1行でその1行に含まれる各要素がカンマで区切られるように書き出す。
# import csv
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/challenge2.csv","w",encoding="shift-jis") as f:
#   w = csv.writer(f,delimiter=",")
#   w.writerow(["a", "b", "c", "d", "e", "f", "g", "h", "i"])
# 答え
# import csv
# movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/movies.csv", "w") as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=",")
#     for movie_list in movies:
#         spamwriter.writerow(movie_list)

# 再チャレンジ
# import csv
# list = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]#リストを作成
# with open("/Users/fujitamasaaki/Desktop/独学プログラマー/challange2_2.csv","w",encoding="shift-jis") as f:#csvの白紙を作成
#   w = csv.writer(f,delimiter=",")
#   for a in list:#白紙のcsvに書き出す
#     w.writerow(a)