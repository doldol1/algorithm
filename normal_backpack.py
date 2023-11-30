# # n, k= map(int,input().split(' '))

# # weight=list()
# # value=list()

# # for i in range(n):
# #     w, v=map(int,input().split(' '))
# #     weight.append(w)
# #     value.append(v)

# #######preset#######
# n=4 
# k=7

# weight=[6, 4, 3, 5]
# value=[13, 8, 6, 12]

# #####################

# print(n, k)

# for i in range(n):
#     print(weight[i], value[i])


# eff=list()
# for i in range(n):
#     eff.append


def knapsack(N, K, weights, values):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, K + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[N][K]

# 입력 처리
N, K = map(int, input().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# 결과 출력
result = knapsack(N, K, weights, values)
print(result)