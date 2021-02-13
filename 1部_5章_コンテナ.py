# メソッド：関数との違いはオブジェクトにつけて呼び出す。
# df.indexのindexとか

# リスト：好きな順番でオブジェクトを保存できるコンテナ。
# fruit = ["Apple", "Orange", "Pear"]
# print(fruit)
# １単語を要素に分解して持つ事もできる
# a = "python"
# b = list(a)
# print(b)

# リストへのオブジェクト追加 append:リストの最後にオブジェクトを追加する
# fruit =["Apple", "Orange", "Pear"]
# fruit.append("Banana")
# fruit.append("Peach")
# print(fruit)

# リストはどんなオブジェクトでも格納できる
# random = []
# random.append(True)
# random.append(100)
# random.append(1.1)
# random.append("Hello")
# print(random)

# 文字列、リスト、タプルのように繰り返し処理で要素を１つづつ取り出せるオブジェクトは
# 「イテラブル(繰り返し可能)」という。

# インデックスで要素を取り出せる
# fruit =["Apple", "Orange", "Pear"]
# print(fruit[0])
# print(fruit[1])
# print(fruit[2])

# 存在しないインデックスで要素を取り出そうとするとエラーが出る。
# colors = ["blue", "green", "yellow"]
# print(colors[5])

# リストは変更可能。ミュータブルという。
# colors = ["blue", "green", "yellow"]
# print(colors)
# colors[2] = "red"
# print(colors)

# リストの末尾から要素を取り除。popメソッドを使用
# colors = ["blue", "green", "yellow"]
# print(colors)
# item = colors.pop()
# print(item)
# print(colors)

# リストは連結できる
# colors1 = ["blue", "green", "yellow"]
# colors2 = ["orange", "pink", "black"]
# print(colors1 + colors2)

# 特定の要素がリストに含まれているかを調べるには「in」演算子を使う。
# colors = ["blue", "green", "yellow"]
# print("green" in colors)

# 特定の要素がリストに入っていないことを調べるには「not in」演算子を使う。
# colors = ["blue", "green", "yellow"]
# print("black" not in colors)

# リストの要素の個数の取得「len」関数を使用。
# colors = ["blue", "green", "yellow"]
# print(len(colors))

# リストを使ったプログラム
# colors = ["purple", "orange", "green"]
# guess = input("naniirodeshou?")

# if guess in colors:
#     print("right!")
# else:
#     print("see you next time!")

# タプルは一度定義したら、要素の値、追加、削除、ができないリスト。丸かっこでかく。
# 変更不可能でイミュータブルという。
# rndm = ("M.Jackson", 1958,True)
# print(rndm)

# タプルの要素が１つのときは要素の直後にカンマをつけること。計算の丸かっこと認識してしまう。
# これはタプル
# print("self_taught",)
# これはタプルではなく計算の丸かっこ
# print((1+2)*4)

# タプルはあとから要素の変更はできない。
# dys = ("1984", "brand new world", "Fahrenheit 451")
# dys[1] = "Handmaid's Tale"

# タプルの要素の取り出し方法はリストと同じ
# dys = ("1984", "brand new world", "Fahrenheit 451")
# print(dys[0])

# タプルに要素が含まれている,含まれていないかどうかは「in」「not in」演算子を使う。リストと同じ。
# dys = ("1984", "brand new world", "Fahrenheit 451")
# print("1984" in dys)
# print("1984" not in dys)



# 辞書は２つのオブジェクトを関連づけて保持するコンテナ。ミュータブル。
# リスト、タプルと違って格納する順番は指定できない。
# キーバリューペア：片方のオブジェクトをキーとしてもう片方をマッピングして（関連づけて）保持すること

# 辞書の書き方は以下のとおり。
# a = dict()
# b = {}
# print(a)
# print(b)
# fruits = {"Apple":"Red", "Banana":"Yellow"}
# print(fruits)


# # 参照と追加
# facts = dict()

# # バリューを追加
# facts["code"] = "fun"
# # キーで参照
# print(facts["code"])

# # バリューを追加
# facts["Bill"] = "Gates"
# # キーで参照
# print(facts["Bill"])

# # バリューを追加
# facts["founded"] = 1776
# # キーで参照
# print(facts["founded"])

# 辞書のキーはイミュータブルでなければならない。
# キーとして使用可能：文字列、タプル    キーとして使用不可能：辞書、リスト

# 「in」演算子でキーに使われているかどうかを確認可能。バリューには使えない。
# 「not in」で使われていないか確認可能。
# bill = {"Bill Gates":"charitable"}
# print("Bill Gates" in bill)
# print("Bill Doors" not in bill)

# キーバリューペアを辞書から削除するには「del」キーワードを使用。
# books = {"Dracula":"Stocker", "1984":"Orwell", "The Trial":"Kafka"}
# print(books)
# del books["The Trial"]
# print(books)

# 辞書を使ったプログラムの例
# songs = {"1":"fun", "2":"blue", "3":"me", "4":"floor", "5":"live"}
# n = input("数字を入力してください：")
# if n in songs:
#   song = songs[n]
#   print(song)
# else:
#   print("見つかりません。")


# # コンテナの中のコンテナ
# lists = []
# rap = ["1", "2", "3", "4"]
# rock = ["5", "6", "7"]
# djs = ["8", "9"]

# lists.append(rap)
# lists.append(rock)
# lists.append(djs)

# print(lists)

# # コンテナの中のコンテナにもインデックスを使ってアクセスできる
# print(lists[0])
# # 追加もできる
# rap.append("aaa")
# print(lists[0])


# リストの要素にタプル、辞書を持たせることも可能。
# locations = []
# la =(34.0522, 188.2437)
# chicago = (41.8781, 87.6298)
# locations.append(la)
# locations.append(chicago)
# print(locations)

# eights = ["1", "2"]
# nines = ["3", "4", "5"]
# authors =(eights, nines)
# print(authors)

# bday ={"1":"one", "2":"two"}
# my_list =[bday]
# print(my_list)
# my_tuple = (bday,)
# print(my_tuple)

# 辞書のバリューとしてリスト、タプル、辞書を格納可能。
# ny={"座標":(40.4, 74.7),
#     "セレブ":["1", "2", "3"],
#     "事実":{"州":"ニューヨーク", "国":"アメリカ"}
#     }
# print(ny)

# チャレンジ
# １、好きなミュージシャンのリストを作成
# my_favmusi = ["straightener", "acidman", "aimer", "niziu"]
# my_favplace =[("home", 30, 40), ("hanazonokeikkoku", 21, 20)]
# my_feature ={"height":173, "favcolor":"black", "favauthor":"tachibanaakira"}
# feature = input("feature?:")
# print(my_feature[feature])
# my_favmusi = {"straightener":["play the star guitar", "sad and beautiful world"]
#               "acidman":["world symphony", "最後の景色"]
#               "aimer":["one", "reiam"]
#               "niziu":["make you happy", "step and a step"]}




