def change(n):
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += n // coin
        n %= coin

    return count


# 사용 예시
n = 1260
print(n, '일 때 결과 ->', change(n))
