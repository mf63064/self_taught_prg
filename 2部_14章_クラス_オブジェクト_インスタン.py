# オブジェクト、インスタンス、クラスの関係。わからなくなったらこれを思い出す。
#   全てのオブジェクトはクラスのインスタンス。
#   クラス作られるオブジェクトをインスタンスと言う。
#   本書の文脈ではオブジェクトといったらインスタンスのことを指す。

# クラス変数vsインスタンス変数
#   クラスはtypeクラスのオブジェクト。typeクラスのインスタンス
#   オブジェクトとしてのクラスを「クラスオブジェクト」と言う。紛らわしいので。
#   クラスを作るクラスのことを「メタクラス」と言う。

# インスタンス変数
#   以下のコードではwidthとlenがインスタンス変数
# class Rectangle():
#   def __init__(self, w, l):
#     self.width = w ##widthがインスタンス変数
#     self.len = l ##lenがインスタンス変数
#   def print_size(self):
#     print("{} by {}".format(self.width, self.len))
# my_rectangle = Rectangle(20, 40)
# my_rectangle.print_size()

# クラス変数
#   クラス変数はクラスオブジェクト、インスタンスオブジェクトから参照できる。
#   クラス変数へのアクセスはインスタンス変数と同じな記載でアクセスできる。
#   クラス変数のメリット：グローバル変数に頼らずに済む
# 以下のコードではrecsがクラス変数
# class Rectangle():
#   recs = []  ##クラス変数は__init__の外で定義する
#   def __init__(self, w, l): ##__init__はインスタンスを作成した時のみ呼び出される
#     self.width = w
#     self.len = l
#     self.recs.append((self.width, self.len)) ##内側のかっこはタプルの意味。
#   def print_size(self):
#     print("{} by {}".format(self.width, self.len))
# r1 = Rectangle(10, 22)
# r2 = Rectangle(37, 41)
# r3 = Rectangle(59, 64)
# print(Rectangle.recs) ##クラス変数呼び出し方はクラス名.クラス変数名

# __init__の呼び出しタイミング
#   クラスオブジェクトを通してクラス変数にアクセスできるが、__init__は呼び出されない。
#   インスタンスを作成したときに初めて呼ばれる。

# 特殊メソッド
#   pythonの全てのクラスはobjectクラスを継承している。
#   そのため継承したメソッドが使用可能。
# 例コード
# class Lion():
#   def __init__(self, name):
#     self.name = name
# lion = Lion("fujita")
# print(lion)

# Lionのオブジェクト(=インスタンス)をprint関数に渡すとpythonはobjectクラスから継承した「__repr__」メソッドを呼び、reprが返した値を出力する。
# その証拠に「__repr__」をオーバーライドすると出力が変わる

# class Lion():
#   def __init__(self, name):
#     self.name = name
#   def __repr__(self):
#     return self.name
# lion = Lion("fujita")
# print(lion)

# 自動で__repr__を継承していることが確認できた。

# 演算子でも同様。
#   2+1の場合。
#     演算子の対象となる２と１は特殊メソッド__add__を持っている。
#     pythonは足し算を実施するために__add__を呼ぶ。
# その証拠に「__add__」を絶対値出力にオーバーライドしてみよう。
# class AlwaysPositive():
#   def __init__(self, number):#クラス内の他の関数でも適用される。
#     self.n = number
#   def __add__(self, other): #self:x other:yで受け取っていると覚えてしまうか。
#     return abs(self.n + other.n)#例えばこれ
# x = AlwaysPositive(-50)
# y = AlwaysPositive(2)
# print(x + y)
# __add__メソッドをオーバーライドしたことにより−48ではなく48が出力される。

# is
#   isは前後のオブジェクトが同一のオブジェクトかどうかをTrue Falseで返す
# 例コード
# class Person():
#   def __init__(self):
#     self.name = "bob"
# bob = Person()
# same_bob = bob
# print(bob is same_bob)
# another_bob = Person()
# print(bob is another_bob)

#   isはある変数がNoneかどうかを調べる時にも使える。
# 例コード
# x = 10
# if x is None:
#   print("xはNone :( ")
# else:
#   print("xはNoneじゃない")

# x = None
# if x is None:
#   print("xはNone :( ")
# else:
  # print("xはNoneじゃない")  

# チャレンジ1
# class Square():
#   square_list = []
#   def __init__(self, name):
#     self.name = name
#     self.square_list.append(self.name)
# a = Square("yeah!")
# b = Square("bean!")
# print(Square.square_list)

# チャレンジ2
# class Square():
#   def __init__(self,s):
#     self.side = s
#   def __repr__(self):
#     return("{} by {} by {} by {}".format(self.side,self.side,self.side,self.side))
# a = Square(29)
# print(a)

# チャレンジ3
# def j(a, b):
#   if a is b:
#     print("True!!")
#   else:
#     print("False!!")
# j(1, 2)


