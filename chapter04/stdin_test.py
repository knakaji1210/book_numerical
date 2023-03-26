import sys

lines = sys.stdin.readlines()
print(lines)

"""
% python3 stdin_test.py < initlife.txtとやると
['0\n', '0\n', '0\n', '0\n', '000000000111\n', '000000000101\n', '000000000101']
と返される
"""

for line in lines:
    line = line.rstrip()
    print(line)

"""
これをやると以下が出力される
0
0
0
0
000000000111
000000000101
000000000101

文字列.rstrip(除去する文字)
文字列の右側から「除去する文字」に該当する文字が削除される
引数を省略した場合にはスペースが削除される
"""

for no, line in enumerate(lines):
    print("No: {0}".format(no))
    line = line.rstrip()
    print(line)

"""
これをやると以下が出力される
No: 0
0
No: 1
0
No: 2
0
No: 3
0
No: 4
000000000111
No: 5
000000000101
No: 6
000000000101
"""