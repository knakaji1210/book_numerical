"""
https://qiita.com/kzy83/items/64be4f5f1eaf08917f24
"""

N = 3  # 荷物の数
W = 10  # ナップサックの許容量
w = [9, 6, 4] # 荷物それぞれの重さの配列
v = [15, 10, 6] # 荷物それぞれの価値の配列

# 次使用する配列に今回の結果を残すので+1している
dp = [[0]*(W+1) for i in range(N+1)] # DPの配列作成

for i in range(N):
    for j in range(W+1):
        if j < w[i]: # この時点では許容量を超えていないので選択しない
            dp[i+1][j] = dp[i][j] # ただ選択はしていないが、今回の情報をそのままi+1の方へ移す
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])

print(dp[N][W])