def find_max_change(coins, change):
	for coin in reversed(coins_list):
		if coin == change:
			return str(coin)
		elif coin < change:
			break
	return str(coin)+','+find_max_change(coins, change - coin)


coins_list = [1, 5, 10, 25]
print find_max_change(coins_list, 90)

