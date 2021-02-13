# 文字列はイテラブル（繰り返し可能）。
# indexにより取り出し可能。
# author = "kafka"
# print(author[0])
# print(author[1])
# print(author[2])
# print(author[3])
# print(author[4])

# マイナスインデックスの使い方
# author = "kafka"
# print(author[-1])
# print(author[-2])

# 文字列はイミュータブル（入れ替え不可能）
# 入れ替えたいときは代入し直す。
# ff = "masaaki"
# ff = "msaaaki"
# print(ff)

# 文字列の足し算掛け算
# print("cat" + "in" + "hat")
# print("cat" *999)

# 大文字変換：upper()メソッド
# 小文字変換：lower()メソッド
# print("fujitamasaaki".upper())
# print("FUJITMASAAKI".lower())

# 最初だけ大文字にする。キャピタライズと言う。capitalize()メソッドを使用
# print("masaaaki".capitalize() + "fujtia".capitalize())

# 書式化:.format()メソッドを使用。共通の部分だけ書いてあとから記載できる。波かっこ使用注意！
# print("こんにちは、{}".format("くそやろー"))

# name = "くそやろー"
# print("こんにちは、{}".format(name))

# author = "ウィリアム・フォークナー"
# year_born ="1897"
# print("{}は{}年に生まれました。".format(author, year_born))

# {} .format()メソッドは利用者が入力した文字を使って文章を組み立てる時に便利。
# what =input("何が：")
# when =input("いつ：")
# where =input("どこで：")
# how =input("どうした：")
# why =input("なぜ：")
# r = "{}は{}に{}で{}。{}だから。".format(what, when, where, how, why)
# print(r)

# 文字列の分割:.split()メソッド
# 分割した文をリストで返してくれる。分割する文字を引数として渡す。
# print("水溜りを超えたんだ。３メートルもあったんだぜ！".split("。"))

# 全ての文字と文字の間に新しい文字を入れる
# "".join()メソッドを使用。
# first_three = "abc"
# result = "+".join(first_three)
# print(result)
# words = ["the", "fox", "jumped", "over", "the", "fence", "."]
# print(words)
# one = "".join(words)
# print(one)
# one = " ".join(words)
# print(one)

# 空白除去
# .strip()メソッド:文字列の最初と最後の空白を除去する
# s = "   the end .   "
# print(s.strip())

# 置換:.replace()メソッドを使用。
# equ = "All animals are eqaul."
# print(equ.replace("a", "@"))

# 文字を検索する
# .index()メソッド:探したい文字を引数に渡すとその文字のインデックスを返す。
# print("animals".index("s"))

# 含まれているかどうかわからない文字のindexを調べるときは例外処理を書いておくと良い。
# try:
#   print("animals".index("n"))
# except :
#   print("Not Found")

# 文字列でも「in」「not in」演算子は使える。
# print("cat" in "cat eats birds")
# print("cat" not in "cat eats birds")

# エスケープ文字

# 文字列の中にクォートを含めるとエラーになる。
# print("彼女は"そうだね"と言った。")
# これを防ぐにはバックスラッシュを入れる。
# print("彼女は\"そうだね\"と言った。")
# クォートの前にバックスラッシュを書くと文字の始終の意味ではなく文字としてのクォートと認識される。

# ダブルクォートとシングルクォートを併用すれば大丈夫。
# print("彼女は'そうだね'と言った。")
# print('彼女は"そうだね"と言った。')

# 改行
# \nを使用。
# print("line1\nline2\nline3")

# スライス
# 開始インデックス位置の要素は含むが、終了インデックスの要素は含まないので注意！
# fict = ["a", "b", "c", "d", "e"]
# print(fict[0:3])
# ivan = "死の代わりに一つの光があった。"
# print(ivan[0:6])
# print(ivan[6:16])

# 開始インデックスが０のときは省略できる。
# ivan = "死の代わりに一つの光があった。"
# print(ivan[:6])
# print(ivan[:16])

# 終了インデックスが最期の要素の場合、省略できる。
# ivan = "死の代わりに一つの光があった。"
# print(ivan[6:])
# print(ivan[:])

# チャレンジ
# 文字列”カミュ”に含まれている文字を１文字ずつ出力しよう
# kamyu = "カミュ"
# print(kamyu[0])
# print(kamyu[1])
# print(kamyu[2])

# ２つの文字列を入力させるプログラムをかく。その文字列をそれぞれ、別の文字列の２つの箇所に穴埋めした新しい文章を作る。
# a = input("やりたいことは？：")
# b = input("いつまでに：")
# print("君は{}を{}までに成し遂げる。".format(a, b))

# 先頭の文字を大文字にしよう（capitalizeしよう）。”aldous Huxley was born in1894”
# print("aldous Huxley was born in1894".capitalize())

# 文字列を分割してリストで返そう。
# print("誰が、いつ、どこで".split("、"))

# リストの要素を繋げて文章を作成。ただしピリオドの前には空白は不必要。
# list = ["the", "fox", "jumped", "over", "the", "fence", "."]
# list1 = ["the", "fox", "jumped", "over", "the", "fence"]
# list2 = "."
# s = str(" ".join(list1)) + str(list2)
# print(s)
# 正解はこれ
# fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
# fox = " ".join(fox)
# fox = fox[0: -2] + "."
# print(fox)



# 文字列の置き換え
# print("A screaming comes across the sky".replace("s", "$"))

# インデックスの調査
# print("Hemingway".index("m"))

# クォート文字を含む文章を出力する
# print("\"いつかまた会えるよね、また会えるよね\"手を振る君が遠くに消えて")

# 文字列を＋＊で作成
# print("three"+"three"+"three")
# print("three"*3)

# 「四月の晴れた寒い日で、時計がどれも１３時を打っていた。」をスライスして「、」までの部分文字列を作成。
# s = "四月の晴れた寒い日で、時計がどれも１３時を打っていた。"
# print(s[:11])