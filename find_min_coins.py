def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
  
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    used_coins = {i: {} for i in range(amount + 1)}
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = used_coins[i - coin].copy()
                used_coins[i][coin] = used_coins[i].get(coin, 0) + 1

    return used_coins[amount] if dp[amount] != float('inf') else {}


amount = int(input("Введіть суму для видачі решти: "))
print("Динамічне програмування:", find_min_coins(amount))
