# 戦争カードゲームを作る
# カードのクラスを作成
class Card():
  suits = ["spades", "hearts", "diamonds", "clubs"]
  values = [None, None,
            "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "Jack", "Queen", "King", "Ace"]
  def __init__(self, v, s):
    """スート(マーク)も値も整数値です"""
    self.value = v
    self.suit = s
  def __lt__(self, c2):#<を再定義
    if self.value < c2.value:#オブジェクトのvalueインスタンス同士を比較
      return True
    if self.value == c2.value:#valueが等しい場合はスートを比較
      if self.suit < c2.suit:
        return True
      else:
        return False
    return False
  def __gt__(self, c2):#>を再定義
    if self.value > c2.value:#オブジェクトのvalueインスタンス同士を比較
      return True
    if self.value == c2.value:#valueが等しい場合はスートを比較
      if self.suit > c2.suit:
        return True
      else:
        return False
    return False
  def __repr__(self):#__repr__を再定義
    v = self.values[self.value] + " of " \
        + self.suits[self.suit]
    return v
# card1 = Card(10, 2)
# card2 = Card(11, 3)
# print(card1 > card2)
# print(card1)


# Deckクラスの作成
# from random import shuffle
import random
class Deck():
  def __init__(self):#初期化の時点でinit内のことを全て実行。
    self.cards = []#インスタンスとしてカードの種類を持たせる
    for i in range(2, 15):#2からaceまでを繰り返す。
      for j in range(4):#0から3までを繰り返す。スペードハートダイアモンドクラブ。
        self.cards.append(Card(i,j))#ここでCardクラスの定義を使用。cardsインスタンスに追加
    # shuffle(self.cards)
    random.shuffle(self.cards)
  def rm_card(self):
    if len(self.cards) ==0:
      return
    return self.cards.pop()

# deck = Deck()
# for card in deck.cards:
#   print(card)

# Playerクラスの作成
class Player():
  def __init__(self, name):
    self.wins = 0
    self.card = None
    self.name = name


# Gameクラスの作成
class Game():
  def __init__(self):
    name1 = input("プレーヤー１の名前")
    name2 = input("プレーヤー２の名前")
    self.deck = Deck()
    self.p1 =Player(name1)#ここでPlayerクラスのインスタンスが使用可能になる
    self.p2 =Player(name2)#ここでPlayerクラスのインスタンスが使用可能になる
  def wins(self, winner):
    w = "このラウンドは{}が勝ちました。"
    w = w.format(winner)
    print(w)
  def draw(self, p1n, p1c, p2n, p2c):
    d = "{} は {}、 {} は {} を引きました。"
    d = d.format(p1n, p1c, p2n, p2c)
    print(d)
  def play_game(self):
    cards = self.deck.cards
    print("戦争を始めます！！")
    while len(cards) >= 2:
      m = "qで終了、それ以外のキーでPlay:"
      response = input(m)
      if response == "q":
        break
      p1c = self.deck.rm_card()
      p2c = self.deck.rm_card()
      p1n = self.p1.name #74,75行目でPlayerクラスのインスタンス.nameが使用可能になっている。
      p2n = self.p2.name #74,75行目でPlayerクラスのインスタンス.nameが使用可能になっている。
      self.draw(p1n, p1c, p2n, p2c)#drawメソッドの実行。
      if p1c > p2c:
        self.p1.wins += 1
        self.wins(self.p1.name) #winsメソッドにself.p1.nameを代入している。
      else:
        self.p2.wins += 1
        self.wins(self.p2.name) #winsメソッドにself.p2.nameを代入している。
    win = self.winner(self.p1, self.p2)
  def winner(self, p1, p2):
    if p1.wins > p2.wins:
      return p1.name 
    if p1.wins < p2.wins:
      return p2.name
    return "引き分け"

game = Game()
game.play_game()
