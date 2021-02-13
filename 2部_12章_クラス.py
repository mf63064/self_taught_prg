# プログラミングパラダイム：プログラミンの手法・スタイルのこと。
# オブジェクト指向プログラミング、手続き型プログラミング、関数型プログラミングがある
# 違いは状態(ステート)の持ち方。
# 状態(ステート)：プログラムが動いている時の変数の値。
# グローバルステートはプログラム実行中のグローバル変数の値のこと。
# 1章は手続き型プログラミングのパラダイム
# 手続き型は連続した手続きをこなし、途中途中でプログラムのステートを変え、少しずつ答えに近づく。
# x = 2
# y = 4
# z = 8
# xyz = x + y + z + z
# print(xyz)
# という感じ

# 手続き型プログラミングは小さいプログラムを書くには良い手法。
# 状態を全てグローバル変数に持たせているため、プログラムが大きくなると問題が出る。
# どこで何を参照しているのか、書き換えているのかわからなくなる。
# 手続き型はコードがグローバル変数の状態を変えるという副作用の上に成り立っている。
# それがオブジェクト指向プログラミング、関数型プログラミングの登場するきっかけとなった。


# 関数型プログラミングはグローバルステートを排除することで手続き型プログラミングの問題を解決した。
# 手続き型
# a = 0
# def increment():
#     global a
    # a += 1
# グローバルステートがある

# 関数型
# def increament(a):
#     return a + 1
# グローバルステートがない

# 関数型の利点：グローバルステートがないのでそれが原因のエラーを排除できる。
# 関数型の欠点：グローバルステートを持たせた方が解決しやすい問題を扱いにくい。

# オブジェクト指向プログラミング
# これもパラダイムもグローバルステートを排除する。
# 関数型との違いは関数に引数を持たせる(関数に状態を持たせる)のではなく、オブジェクトに状態を持たせる。
# クラスは表現したいオブジェクトを定義・分類するプログラミングの仕組み。
# クラスの説明例
# バッグ：クラス
# バッグの中のオレンジ：オブジェクトかつインスタンス
# オレンジの色、重さ、などの共通情報：属性
# クラスの中のオブジェクトのデータ型はオレンジとなる

# 数値123というオブジェクトはintクラスのインスタンス。
# 同様に”abc”という文字列オブジェクトはstrクラスのインスタンス。
# pythonでは全てのオブジェクトは何らかのクラスのインスタンス。
# リテラル：数値や文字のようにプログラミング言語で書き方が用意されているもの


# クラス
# 書き方
# class クラス名:
#     スイート
# ルール
# 常に頭文字は大文字。複数の単語の場合も同様。アンダースコアは使わない。LikeThisのように。
# スイート部分には単純文、メソッドという複合分を書く。
# メソッド：関数に似ているが、そのクラスの内部で定義し、そのクラスで生成したオブジェクトのみ使用可能。_でつなぐ。
# メソッドと関数の違い：1,クラスのスイート部分に定義する。2,引数を少なくとも１つ定義する必要がある。selfを使用。
# こんな感じ
# class Orange:
#   def __init__(self):
#     print("Created!")

# def __init__(self, *, *)はインスタンス変数の定義が目的。これがないとクラス内のインスタンス変数であることにならない。

# self変数：インスタンス変数の定義に使用。
# インスタンス変数：そのオブジェクトに属する変数のこと。
# インスタンス変数の書き方
# self.変数名 = 値
# インスタンス変数は__init__というメソッドの中で定義。
# 書き方の例
# class Orange:
#     def __init__(self, w, c):
#         self.weight = w
#         self.color = c
#         print("Created!")
# オブジェクト（インスタンス）が何もないから実行されない。

#オブジェクトの呼び出し方(インスタンス化)
# クラス名(引数)
# class Orange:
#   def __init__(self, w, c):
#       self.weight = w
#       self.color = c
#       print("Created!")
# or1 = Orange(10, "dark orange")
# print(or1)        
# 出力される<__main__.Orange object at 0x7ff4ed493d90>はOrangeクラスのオブジェクトであること、pcのメモリーの位置を表している。

# インスタンス変数の取得の仕方
# class Orange:
#   def __init__(self, w, c):
#     self.weight = w
#     self.color = c
#     print("Created!")
# or1 = Orange(10, "dark orange")
# print(or1.weight)
# print(or1.color)

# インスタンス変数の値を変更する書き方
# オブジェクト名.インスタンス変数名 = 新しい値
# class Orange:
#   def __init__(self, w, c):
#     self.weight = w
#     self.color = c
#     print("Created!")
# or1 = Orange(10, "dark orange")
# or1.weght = 100
# or1.color = "light orange"
# print(or1.color)
# print(or1.weight)

# 複数のorangeオブジェクトを作る
# class Orange:
#   def __init__(self, w, c):
#     self.wight = w
#     self.clolr = c
#     print("Created!")
# or1 = Orange(10,"light orange")
# or2 = Orange(8,"dark orange")
# or1 = Orange(23,"yellow")

# 腐る性質を追加
# class Orange:
#   def __init__(self, w, c):
#     self.weight = w
#     self.color = c
#     # self.mold = 0
#     print("Created!")

#   def rot(self,days,temp):
#     self.mold = days * temp

# orange = Orange(200,"dark")
# # print(orange.mold)
# orange.rot(10,37)
# print(orange.mold)

# class Rectangle:
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
# #インスタンス変数の定義
  
#   def area(self):
#     return self.width * self.len
#   #クラス内で使えるメソッドの定義

#   def change_size(self, w, l):
#     self.width = w
#     self.len = l
# #クラス内で使えるメソッドの定義

# rectangle = Rectangle(10, 20)
# print(rectangle.area())
# rectangle.change_size(333,99999)
# print(rectangle.area())

# チャレンジ1
# class Apple:
#   def __init__(self, c, s, w, t):
#     self.color = c
#     self.size = s
#     self.weight = w
#     self.taste = t
# ap = Apple("red", 5, 300, "good")
# print(ap.taste)

# チャレンジ2
# class Circle:
#   def __init__(self, r):
#     self.radius = r
  
#   def area(self):
#     return self.radius ** 2 * 3.14

# c = Circle(999)
# print(c.area()) 

# チャレンジ3
# class Triangle:
#   def __init__(self, b, h):
#     self.bottom = b
#     self.height = h
  
#   def area(self):
#     return self.bottom * self.height / 2

# t = Triangle(987, 789)
# print(t.area())


# チャレンジ4
# class Hexagon:
#   def __init__(self,l):
#     self.one_side = l
  
#   def peri(self):
#     return self.one_side * 6

# h = Hexagon(956)
# print(h.peri())









