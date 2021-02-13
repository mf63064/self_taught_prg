# カプセル化
#   カプセル化は２つの概念で成り立つ
#     １、オブジェクトによって複数の変数(状態を保持する)と
#           メソッド(状態を変更したり状態を使用して計算する) をまとめること
# 例で説明
# class Rectangle:
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
#   def area(self):
#     return self.width * self.len
# オブジェクトによって複数の変数(状態を保持する):width、len
# メソッド(状態を変更したり状態を使用して計算する):area

#     ２、データをクラス内に隠蔽して外から見えないようにすること
#       クラスの外側にある利用がわのコードからデータを直接操作するのではなくメソッドで操作させる。
#       クラスの外側からオブジェクトを利用するコードを「client」と言う。

# 下記コードでインスタンス変数を変更するには２つの方法がある
# class Data:
#   def __init__(self):
#     self.nums = [1,2,3,4,5]

#   def change_data(self, index, n):
#     self.nums[index] = n
# # １つ目
# one = Data()
# one.nums[0] = 100
# print(one.nums)
# # ２つ目
# two = Data()
# two.change_data(1,99)
# print(two.nums)
# どちらの方法でもできるがもしnumsがタプルだと要素変更不可なのでエラーが出る
# よってクラスの外から使って欲しくない(private)コードと使っても良いコード(public)が必要。
# コード修正時もprivateなら修正によるエラーの心配がない。privateはclientに使われないルールだから。

# pythonではclientにアクセスして欲しくないメソッドには、名前の前に_をつけるルール。
# 例コード
# class PublicPrivateExample:
#   def __init__(self):
#     self.public = "safe"
#     self._unsafe = "unsafe"

#   def public_method(self):
#     # clientが使っても良い
#     pass #pass文は文が必須な構文で何もしない時に使う。とりあえず設計とか

#   def _unsafe_method(self):
#     #clientが使うべきじゃない
#     pass

# 抽象化
#   インスタンスで表現される内容は必要なことだけと言うこと。
#     オブジェクト：りんご  インスタンス変数：色  りんごは他の特徴も持っているが色のみをインスタンス変数とするとか。

# ポリモーフィズム
#   同じインターフェースでありながらデータ型に合わせて異なる動作をする機能のこと
#   インターフェースとは関数やメソッドのこと。
# ポリモーフィズムの例
# print("hello, world")
# print(200)
# print(200.1)
# print関数は文字列、整数、浮動小数点数のどれでも同じインターフェース(使い方)で動作する。
# print_string,print_intなどは必要ない。

# ポリモーフィズムの例
# print(type("hello world"))
# print(type(2))
# print(type(2.4))

# ポリモーフィズムなしのコード
# shapes = [trl, spl, crl]
# for a_shape in shapes:
#   if isinstance(a_shape, Triangle):
#     a_shape.draw_triangle()
#   if isinstance(a_shape, Square):
#       a_shape.draw_Square()
#   if isinstance(a_shape, Circle):
#       a_shape.draw_circle()
# 毎回データ型を確認しなければならない

# ポリモーフィズムありのコード
# shapes = [trl, spl, crl]
# for a_shapes in shapes:
#   a_shape.draw()
# これだけでおk

# 継承
# 親クラスから子クラスへメソッドや変数が引き継がれること
# class Shape:
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
#   def print_size(self):
#     print("{} by {}".format(self.width, self.len))

# #shapeクラスを継承 
# class Square(Shape):
#   pass

# my_square = Square(20, 25)
# my_square.print_size()

# class Shape:
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
#   def print_size(self):
#     print("{} by {}".format(self.width, self.len))

# class Square(Shape):
#   def area(self):
#     return self.len * self.width

# a_square = Square(20, 25)
# print(a_square.area())

# メソッドオーバーライド
#  子クラスで親クラスのメソッドを上書きすること
# class Shape:
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
#   def print_size(self):
#     print("{} by {}".format(self.width, self.len))

# class Square(Shape):
#   def area(self):
#     return self.len * self.width
#   def print_size(self):#親クラスのprint_sizeメソッドを上書き
#     print("I am {} by {}".format(self.width, self.len))
# a_square = Square(20,20)
# a_square.print_size()

# コンポジション
#   別のクラスのオブジェクトを変数として持たせる。
# class Dog:
#   def __init__(self, name, breed, owner):
#     self.name = name
#     self.breed = breed
#     self.owner = owner
# class Person:
#   def __init__(self, name):
#     self.name = name
# # Dogオブジェクト作成時に犬の飼い主としてPersonオブジェクトを渡す
# mick = Person("MIck Jagger")
# stan = Dog("Stanly", "Bulldog",mick)#mickを変数として渡す
# print(stan.owner.name)#.属性を２回連続で使用。
# print(stan.owner)#Mick jaggerではなくオブジェクトのクラスとpcもメモリの位置が表示される

# チャレンジ1
# class Rectangle:
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
#   def peri(self):
#     return 2 * self.width + 2 * self.len

# class Square:
#   def __init__(self, s):
#     self.side = s
#   def peri(self):
#     return 4 * self.side

# a = Rectangle(34, 56)
# b = Square(99)
# print(a.peri())
# print(b.peri())

# チャレンジ2
# class Rectangle:
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
#   def peri(self):
#     return 2 * self.width + 2 * self.len

# class Square:
#   def __init__(self, s):
#     self.side = s
#   def peri(self):
#     return 4 * self.side
#   def change_size(self, c):
#     self.side += c

# a = Rectangle(34, 56)
# b = Square(99)
# b.change_size(-9)
# print(a.peri())
# print(b.peri())

# チャレンジ3
# class Shape():
#   def what_am_I(self):
#     return "Iam a shape!"

# class Rectangle(Shape):
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
#   def peri(self):
#     return 2 * self.width + 2 * self.len

# class Square(Shape):
#   def __init__(self, s):
#     self.side = s
#   def peri(self):
#     return 4 * self.side
#   def change_size(self, c):
#     self.side += c

# a = Rectangle(34, 56)
# b = Square(99)
# b.change_size(-9)
# print(a.peri())
# print(b.peri())
# print(a.what_am_I())
# print(b.what_am_I())

# チャレンジ4
# class Horse():
#   def __init__(self, n, o):
#     self.owner = o
#     self.name = n
# class Rider():
#   def __init__(self, n):
#     self.name = n
# f = Rider("fujita")
# t = Horse("tachie", f)
# print(t.owner.name)