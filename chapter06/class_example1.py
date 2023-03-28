# クラスを理解するためのプログラム

class  sample:
    def __init__(self,ini): #　コンストラクタ（classを実体化した際に呼ばれる処理、クラス変数を初期化したり、最初だけ行いたい処理）
        self.var_a = ini
        self.var_b = ini

    var_a = 0   # クラス変数（クラス自体が保持する変数）
    var_b = 0
    def test(self, a, b):   # メソッド（クラスが固有に持つ関数）
        return(a + b)

new_class = sample(4)
print(new_class.var_a)
print(new_class.var_b)
print(new_class.test(2,3))