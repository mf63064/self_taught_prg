# 正規表現
#   連続した文字列の検索パターンの定義
#   検索ワードと思って良い気がする。
#   データの中から複雑なパターンと一致するものを探すのに役立つ。
#   例えばファイル内の全ての数値を取り出すのに正規表現を使えます。
#$ ptyhon3 -c"import this" #python3 に-cフラグを立て、引数"import this”を渡す
# 詩が表示される
# このような隠されたメッセージはイースターエッグと呼ばれる。

# grepコマンド：シンプルな一致を出力
# grepで一致した文字列を赤い色で示すようにする
# export GREP_OPTIONS='--color=always'
# ターミナルを終了しても変更を続ける。
# .bash_profileに以下を記載。
# GREP_OPTIONS='--color=always'だめだった。。。。

# 検索したいファイルがあるディレクトリで以下を実施
# grep Beautiful zen.txt  #grep 正規行限 検索したいファイル名
# 「Beautiful」が含まれる1行が表示される。ここの「Beautiful」が正規表現。
# 大文字小文字を無視して検索する
# grep -i beautiful zen.txt
# 一致した単語だけを出力
# grep -o Beau zen.txt

# 正規表現をpythonプログラムで使うには標準ライブラリの「re(regular expression:正規表現)」を使う
#   reモジュールにはfindall関数がある。
#     findall:正規表現パターンと検索対象テキストを渡すと一致した全ての部分をリストで返す。
# import re
# l = "Beautiful is better than ugly"
# matches = re.findall("Beauti", l)
# print(matches)
# 大文字小文字を無視する:re.IGNORECASEを追加する
# import re
# l = "Beautiful is better than ugly"
# matches = re.findall("beauti", l, re.IGNORECASE)
# print(matches)

# 前方一致と後方一致
# キャレット記号 ^ を使うと先頭に一致する正規表現パターンを作れる
# grep ^If zen.txt

# . はどんな文字でも一致する
#   例：thの後の一文字はわからない時は「th.」で検索する
# grep th. zen.txt

# $:行の終端に一致するパターンを作成できる。
# grep idea.$ zen.txt
# 終端にidea.が含まれる行が帰ってくる。


# pythonで^を使った例
# 複数行のテキストを複数行として扱う：re.MULTILINEフラグをfindallに渡す。
# 書き方：re.findall("^If", zen, re.MULTILINE)
import re
zen = """Although never is 
often better than 
*right* now.
If the implementation 
is hard to explain, 
it's a bad idea.
If the implementation 
is easy to explain, 
it may be a good 
idea.Namespaces 
are one honking 
great idea -- let's 
do more of those!"""

# m = re.findall("^If", zen, re.MULTILINE)
# print(m)
# Ifが先頭の単語が帰ってくる。つまり

# 複数文字との一致
# echo Two too. | grep -i t[ow]o
# ここでの正規表現は「tで始まり、その後にoかwがきて、次にo」がくること。
# []で文字を囲むとorの意味になると言うこと
# echo で出力された文字列がgrepに渡されるため、grepの引数にファイルパスを渡す必要はない。
# pythonで書いてみる
# import re
# string = "Two too"
# m = re.findall("t[ow]o", string, re.IGNORECASE)
# print(m)

# 数値検索
# echo 123 hi 34 hello. | grep [[:digit:]]
# 数値を含む文章が帰ってくる
# pythonで書いてみる
# \dを使用する。
# import re
# line = "123 hi 34 hello."
# m = re.findall("\d", line, re.IGNORECASE)
# print(m)

# 繰り返し
# echo two twoo not too. | grep -o two*
# ここでの正規表現は「twの後にoが０回以上続く文字列」

# 「.」と「*」を使うとなんでもokと言う意味になる
# echo __hello__ | grep -o __.*__
# ここでは__と__で囲まれたの文字列を検索す流という意味

# *は一番長い文字列を検索する。*は貪欲
# echo __hi__bye__hi__there | grep -o __.*__
# __hi__bye__hi__が返ってくる

# 一番短い文字列を検索する（pythonのみ）*を非貪欲にする。
# import re
# t = ":__one__ __two__ __three__"
# found = re.findall("__.*?__", t)
# for match in found:
#   print(match)

# 非貪欲な正規表現を使ってMad Libsゲームを作成。
#   いつくかの単語が抜けている文章を表示し、プレーヤーに抜けている単語を入力てもらうものです。
import re
text = """麒麟は大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ の中で一番背の高い動物ですが、科学者たちはそのような長い __体の一部__ をどうやって獲得したのか説明できません。
キリンの身長は __数値__ __単位__ 近くあり、その高さのほとんどは脚と __体の一部__ によるものです。"""

def mad_libs(mls):
  """
  :param mls:文字列で、ユーザーに入力してもらいたい単語(＝ヒント)の部分は後を２つのアンダーアスコアで挟んでください。
  ヒントの単語にはアンダースコアを含めないでください。__hint_hint__はだめです。__hint__はokです。
  """
#   hints = re.findall("__.*?__", mls)
#   if hints is not None:
#     for word in hints:
#       q = "{}を入力:".format(word)
#       new = input(q)
#       mls = mls.replace(word, new)
#     print("\n")#改行の意味
#     mls = mls.replace("\n", "")
#     print(mls)
#   else:
#     print("引数mlsが無効です。")

# mad_libs(text)

# str.replce(old, new[, count])
# 元の文字列をコピーし、現れる部分文字列old全てをnewに置換して返します。
# オプション引数countが与えられている場合、先頭からcount個のoldだけを置換します。
 
# エスケープ
#   特別な文字をエスケープして本来の文字に一致させたい場合、その文字の前に\をつける。
# echo I love $ | grep \$
# ドル記号は文字列の終端に一致の意味だが、＼によりドル記号そのものの意味になる
# pythonで書いてみる
# import re
# line = "i love $"
# m = re.findall("\$", line, re.IGNORECASE)
# print(m)


# チャレンジ
# grepを使ってthe zen of pythonの文中にあるDutchという単語に一致する正規表現をかこう。
# grep Dutch zen.txt

# grepを使って文字列"arizona 479, 501, 870, california 209, 213, 650."にある数字部分全てに一致する正規表現をかこう。
# echo arizona 479, 501, 870, california 209, 213, 650. | grep [[:digit:]]

# pythonで何かの文字の後に「o」が２回登場する単語に一致する正規表現を作成。
# "the ghost tha says boo haunts the loo"のboo、looに一致するか試す。
# import re
# sntnc = "the ghost tha says boo haunts the loo"
# regex = re.findall(".oo", sntnc)
# print(regex)
