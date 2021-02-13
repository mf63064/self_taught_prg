# モジュール：分割したコードを書いておくファイルのこと
# pythonではモジュールから別のモジュールを使うことができる
# 組込モジュール：python本体に組み込まれているモジュール
# pythonの組込みモジュールの一覧
# http://docs.python.org/ja/3/py-modindex.html

# 書き方は２種類
# from random import randint
# print(randint(9,9999999999))
# か
# import random
# print(random.randint(99,999999999999))


# # mathモジュール
# import math
# # pow 組込関数以下は２の３乗の意味。
# print(math.pow(2,3))

# randomモジュール
# import random
# # randint 組込関数2つの整数の範囲でランダムに整数を生成する
# print(random.randint(99,999999999999))
# この書き方でもok
# from random import randint
# print(randint(9,9999999999))


# statisticsモジュール
# import statistics
# # 平均mean中央値median最頻値modeを返してくれる。
# nums = [1,5,33,12,46,33,2]
# print(statistics.mean(nums))
# print(statistics.median(nums))
# print(statistics.mode(nums))

# pythonのキーワードかどうかを確認する
# import keyword
# print(keyword.iskeyword("for"))
# print(keyword.iskeyword("football"))

# モジュールを作成してインポートする。同じフォルダ内にないとだめ。
# import hello as h
# h.print_hello()

# モジュールをインポートすると中のコードは全て実行される。
# import module1
# インポートされるファイルを以下のように書き換えるとインポートしても実行されない。
# 作成中などでまだ実行されたくない時に便利。
# if __name__ == "__main__":
#   print("hello")

# チャレンジ
# statisticsの別の関数を読んでみよう
# import statistics as sta
# a = [1,2,3,4,5,6,7,8,9,1111111]
# print(sta.stdev(a))

# cubedというモジュールを作成し関数をよぶ。
# import cubed as cb
# cb.cube(2)