# forループ
# for 変数名 in イテラブル:
#     コードブロック
# 変数名はここで自由にかける。事前に定義したものではない。
# name = "Ted"
# for character in name:
#   print(character)
# nameの要素をcharacterに入れていくイメージ

# リストを使ったループ処理
# shows = ["GOT", "Narcos", "Vice"]
# for show in shows:
#   print(show)

# タプルを使ったループ処理
# coms = ("a.development", "friends", "always sunny")
# for show in coms:
#   print(show)

# 辞書を使ったループ処理 キーが繰り返される。
# people = {"G.Bluth Ⅱ":"A. Development",
#           "Barney":"HIMYM",
#           "Dennis":"Always Sunny",
#           }
# for character in people:
#   print(character)

# リストなどのミュータブルなイテラブルを更新可能。
# tv = ["Got", "Narcos", "Vice"]
# i = 0
# for show in tv:
#     new = tv[i]
#     new = new.upper()
#     tv[i] = new
#     i += 1
# print(tv)

# i,enumerates関数
# 上記i=0とi+=1を自動的に要してくれる関数。インデックスindex値を自動で増加してくれる
# tv = ["Got", "Narcos", "Vice"]
# for i, new in enumerate(tv):
#     new = tv[i]
#     new = new.upper()
#     tv[i] =new
# print(tv)

# forループのなかでデータを加工して別のリストに入れる。
# tv = ["Got", "Narcos", "Vice"]
# coms =["Arrested Development", "friends", "Always Sunny"]
# all_shows = []
# for show in tv:
#     show =show.upper()
#     all_shows.append(show)
# for show in coms:
#     show =show.upper()
#     all_shows.append(show)
# print(all_shows)

# range関数：指定された領域の整数を順番に生成する
# for i in range(5,11):
#   print(i)

# whileループ:式がTrueの間コードの実行を繰り返す
# while 式
#    コードブロック
# x = 10
# while x > 0:
#   print("{}".format(x))
#   x -= 1
# print("Happy New Year!")

# 常にTrueになる式をwhileループの条件に指定した場合無限ループになる。
# 止めるときはControl+c で止める。長すぎる処理もこれで止められる。

# break：ループを終了させるための文 pythonはbreak文に到達するとすぐにループを終了する
# for i in range(0,101):
#     print(i)
#     break

# breakを利用したプログラム
# qs = ["What is your name?", "What is you fav.color?", "What is your quest?"]
# n = 0
# while True:
#   print("Type q to quit")
#   a = input(qs[n])
#   if a =="q":
#     break
#   n = (n + 1) % 3

# continue 実行中の反復処理を途中で終了して次の反復処理へを開始する。
# breakと違ってループ終了はしない。
# 以下の処理は３を除く1−5を出力する
# for i in range(1,6):
#   if i == 3:
#     continue
#   print(i)
# whileでも同じ処理を書ける
# i = 1
# while i <= 5:
#     if i ==3:
#       i += 1
#       continue
#     print(i)
#     i += 1

# 入れ子のループ、ネストしたループ：ループの中にループがあること
# for i in range(1,3):
#     print(i)
#     for letter in ["a", "b", "c"]:
#       print(letter)
# 次のプログラムは数字の全ての組み合わせの足し算を新しいリストに代入する処理です。
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# added = []
# for i in list1:
#   for j in list2:
#     added.append(i+j)
# print(added)

# forループをwhileループに入れることもできるしその逆もできる。
# while input("y or n") != "n":
#   for i in range(1,6):
#     print(i)

# イテレーション（反復処理）
# インデックス変数：繰り返しが何回目なのかを示す整数。

# チャレンジ

# リストを出力しよう。
# tv = ["ウォーキングデッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
# for name in tv:
#   print(name)

# ２５から５０までの数値を出力しよう
# for i in range(25,51):
#   print(i)

# インデックス値と一緒に出力しよう。
# tv = ["ウォーキングデッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
# for i, name in enumerate(tv):
#   print(i)
#   print(name)

# 無限ループ処理を作成
# ユーザーに入力を数字してもらう
# qが入力されたら終了
# 数字が入力されたらリストの中の数字と一致しているかを判定して出力する
# 数字、q以外の入力で「数字を入力するか、qで終了します」と表示しよう。
# nlist = [1,2,3,4,5]
# while True:
#     n = input("number?:")
#     if n == "q":
#       break
#     try:
#       n = int(n)
#     except ValueError:
#       print("数字を入力するか、qで終了します")
#     if n in nlist:
#       print("right!!!")
#     else:
#       print("fuck!")

# 正解はこれ。ValueErrorでもelse処理がされる。
# numbers = [11, 32, 33, 15, 1]

# while True:
#     answer = input("Guess a number or type q to quit.")
#     if answer == "q":
#         break
#     try:
#         answer = int(answer)
#     except ValueError:
#         print("please type a number or q to quit.")
#     if answer in numbers:
#         print("You guessed correctly!")
#     else:
#         print("You guessed incorrectly!")

# ２つのリストに含まれる全ての数字の掛け算を実施。
# a = [8, 19, 148, 4]
# b = [9, 1, 33, 83]
# c = []
# for i in a:
#   for j in b:
#     c.append(i * j)
# print(c)

