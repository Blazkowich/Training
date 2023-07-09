def change(money, coins):
    coins.sort(reverse=True)
    num_coins = 0
    i = 0
    while money > 0 and i < len(coins):
        if coins[i] <= money:
            num_coins += money // coins[i]
            money %= coins[i]
        i += 1
    if money > 0:
        return -1
    return num_coins
    
print(change(77, [10,25,5,1])
    
