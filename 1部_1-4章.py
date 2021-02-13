# for i in range(100):
#   print('hello,world')


# import  math
# l=4
# w=10
# d=math.sqrt(1**2 + w**2)
# よくわからんが実行できなかった

# 異なる３つの文字列を出力しよう
# print('a', 'b', 'c')
# # 変数が１０未満だったらメッセージ、１０以上だったら、別のメッセージを出力しよう
# v = 22
# if v<10:
#   print('ng')
# else:
#   print('ok')

# 変数が１０以下、１０より大きく２５以下、２５より大きかったらでそれぞれメッセージを出力
# v =14
# if v<= 10:
#   print('dame')
# elif v>10 and v<=25:
#   print('soso...')
# else:
#   print('ok')

# 余りを出力
# print(10%3)




# 関数
# def f(x):
#   return x+1
# z = f(6)
# if z==5:
#   print('z is 5')
# else:
#     print('z is not 5')




# len/str/int/float関数
#   オブジェクトの長さを返す関数
# print(len("Monty"))
# print(str(100.314))
# print(float(100.314))
# print(int(100.314))

# input関数
# age = input("Enter your age:")
# int_age = int(age)
# if int_age < 21:
#   print("You are young!")
# else:
#   print("Wow You are old!!")




# 関数を利用すると繰り返し使えて便利
# def even_odd(x):
#   if x % 2 == 0:
#     print("偶数")
#   else:
#       print("奇数")
# even_odd(59)
# even_odd(120)

# def even_odd():
#   n = int(input('type a number:'))
#   if n % 2 == 0:
#     print("偶数")
#   else:
#       print("奇数")
# even_odd()
# even_odd()




# オプション引数/必須引数
#   定義の時に引数に値を渡すとそれがデフォルト設定になる。この場合２がオプション引数。
# def f(x=2):
#   return x ** x
# print(f())
# print(f(3))




#   オプション引数/必須引数両方持つ関数も設定できる
# def add_it(x,y=10):
#   return x + y
# result = add_it(21)
# print(result)




# グローバル変数/ローカル変数/スコープ
# スコープ：変数を読み書きできる範囲のこと
# グローバル変数：関数やクラスの外で定義した変数。その変数はグローバルスコープに定義されどこからでも読書きできる変数
# ローカル変数：関数やクラス内で定義した変数。その変数はローカルスコープに定義されその中でのみ読書きができる。
# グローバル変数
# x = 1
# y = 2
# z = 3
# def f():
#   print(x)
#   print(y)
#   print(z)
# f()

# ローカル変数は外から読書きができない
# def f():
#   x = 1
#   y = 2
#   z = 3
# print(x)
# print(y)
# print(z)

# ローカル変数をその中で使えば問題ない
# def f():
#   x = 1
#   y = 2
#   z = 3
#   print(x)
#   print(y)
#   print(z)
# f()

# 定義されていない関数をしようするとエラーになる
# if x >= 100:
#   print("x is >= 100")

# global を使ってスコープをまたいで読書きする
# x = 100
# def f():
#   global x
#   x += 1
#   print(x)
# f()
# プログラムが大きくなるとこのスコープまたぎによるエラーや誤参照が起きやすくなる




# 例外処理 エラーが出た時の表示方法を定義する
#   下の構文はユーザーにbに０を入力されるとエラーになる。
# a = input("type a number:")
# b = input("type another:")
# a = int(a)
# b = int(b)
# print(a/b)

# try except 処理で０入力時の対応をする
# a = input("type a number:")
# b = input("type another:")
# a = int(a)
# b = int(b)
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("b cannot be zero")

# 文字列を入力された時の対応をする
# try:
#     a = input("type a number:")
#     b = input("type another:")
#     a = int(a)
#     b = int(b)
#     print(a / b)
# except (ZeroDivisionError,ValueError):
#     print("Invalid input.")

# try節内で使用した変数をexcept節で使用すると別の例外が発生する
# try:
#     10 / 0
#     c = "I will never get defined."
# except ZeroDivisionError:
#     print(ConnectionResetError)

# ドキュメンテーション文字列
# 関数の引数についての説明を書くこと"""と”””で囲む
# docstring:関数の目的、必要な引数の種類についての説明をかく
# def add(x, y):
#   """
#   return x + y.
#   :param x: int.
#   :param y: int.
#   :return: int sum of x and y.
#   """
#   return x + y

# データをのちに使う場合のみ変数に格納する。それ以外は変数に代入しない。
# 以下はだめな例
# x = 100
# print(x)
# それならこうしてください。
# print(100)

# チャレンジ
# １、数字を入力値として受け取り、その値を２乗して返す関数を作成
# x = input("number?:")
# def f(x):
#     x = int(x)
#     x **=x
#     print(x)
# f(x)
# ２、文字列を引数とし、その文字列を出力する関数を作成
# def sen(x):
#     x = str(x)
#     print(x)
# sen("fun!")

# ３、３つの必須引数と２つのオプション引数がある関数を作成
# def f(x, y, z, a=21, b=33, c=35):
#     return a * x**2 + b * y + c * z
# i = f(1,2,3,4,5,6)
# print(i)

# ４、２つの関数からなるプログラムを書いてみよう。
# 関数①整数を引数として受け取り２で割った値を返す
# 関数②整数を引数として受け取り４をかけた値を返す
# 関数①呼び、戻り値を変数に代入し、関数②の引数として渡そう。
# def f1(x):
#         return x / 2
# def f2(x):
#         return x * 4
# a = f1(12)
# b = f2(a)
# print(b)

# ５、文字列をfloat型に変換して返す関数を作成。起こり得る例外をキャッチする例外処理を作成。
a = input("number?:")
def f(x):
    """
    f makes x float.
    :param x: int.
    """

        x = float(x)
        return x
try:     
    b = f(a)
    print(b)
except (ZeroDivisionError,ValueError):
    print("Invalid input.")

# ６、上のプログラムにdocstringを追加 